import { create } from 'zustand';
import {
    type Connection,
    type Edge,
    type EdgeChange,
    type Node,
    type NodeChange,
    addEdge,
    type OnNodesChange,
    type OnEdgesChange,
    type OnConnect,
    applyNodeChanges,
    applyEdgeChanges,
} from 'reactflow';
import { aegisApi, type ReductionResult } from './api/aegis';

export type BlockType = 'QUESTION' | 'CLAIM' | 'EVIDENCE' | 'PROTOCOL' | 'RISK' | 'DECISION' | 'AMENDMENT';
export type BlockStatus = 'DRAFT' | 'PROPOSED' | 'APPROVED' | 'REJECTED' | 'DEFERRED';

export interface EffectVector {
    risk: number;
    fairness: number;
    novelty: number;
    privacy: number;
    target?: string; // For Amendments
}

export interface ThoughtBlockData {
    id: string;
    title: string;
    type: BlockType;
    content: string;
    status: BlockStatus;
    effects: EffectVector;
    author: string;
    timestamp: number;
    reductionResult?: ReductionResult;
}

export type ThoughtNode = Node<ThoughtBlockData>;

interface RFState {
    nodes: ThoughtNode[];
    edges: Edge[];
    selectedNodeId: string | null;
    systemStatus: string;
    ledgerHeight: number;

    onNodesChange: OnNodesChange;
    onEdgesChange: OnEdgesChange;
    onConnect: OnConnect;

    addNode: (node: ThoughtNode) => void;
    updateNodeStatus: (id: string, status: BlockStatus) => void;
    selectNode: (id: string | null) => void;

    // Async Actions
    checkSystemStatus: () => Promise<void>;
    submitGraph: () => Promise<void>;
}

const useStore = create<RFState>((set, get) => ({
    nodes: [
        {
            id: '1',
            type: 'thoughtNode',
            position: { x: 250, y: 100 },
            data: {
                id: '1',
                type: 'QUESTION',
                title: 'Deploy Model M2?',
                content: 'Should we deploy the new M2 model to production given the current risk profile?',
                author: 'System',
                timestamp: Date.now(),
                status: 'PROPOSED',
                effects: { risk: 0.1, fairness: 0.5, novelty: 0.5, privacy: 0.1 },
            },
        },
        {
            id: '2',
            type: 'thoughtNode',
            position: { x: 100, y: 400 },
            data: {
                id: '2',
                type: 'RISK',
                title: 'Bias Detected',
                content: 'Analysis shows a 12% variance in demographic performance.',
                author: 'Sentinel',
                timestamp: Date.now(),
                status: 'PROPOSED',
                effects: { risk: 0.8, fairness: 0.2, novelty: 0.1, privacy: 0.1 },
            },
        },
        {
            id: '3',
            type: 'thoughtNode',
            position: { x: 400, y: 400 },
            data: {
                id: '3',
                type: 'EVIDENCE',
                title: 'Performance +15%',
                content: 'Overall accuracy has improved by 15% compared to M1.',
                author: 'Benchmark',
                timestamp: Date.now(),
                status: 'PROPOSED',
                effects: { risk: 0.1, fairness: 0.6, novelty: 0.8, privacy: 0.1 },
            },
        },
        {
            id: '4',
            type: 'amendmentNode',
            position: { x: 250, y: 700 },
            data: {
                id: '4',
                type: 'AMENDMENT',
                title: 'Protocol Update v1.1',
                content: 'Proposed change to risk threshold: Lower max risk from 0.8 to 0.5.',
                author: 'Governance',
                timestamp: Date.now(),
                status: 'DRAFT',
                effects: { risk: 0.0, fairness: 0.0, novelty: 0.0, privacy: 0.0, target: 'Risk Protocol' },
            },
        },
    ],
    edges: [
        { id: 'e1-2', source: '1', target: '2', type: 'pulse', animated: true },
        { id: 'e1-3', source: '1', target: '3', type: 'pulse', animated: true },
        { id: 'e2-4', source: '2', target: '4', type: 'pulse', animated: true },
    ],
    selectedNodeId: null,
    systemStatus: 'OFFLINE',
    ledgerHeight: 0,

    onNodesChange: (changes: NodeChange[]) => {
        set({
            nodes: applyNodeChanges(changes, get().nodes),
        });
    },
    onEdgesChange: (changes: EdgeChange[]) => {
        set({
            edges: applyEdgeChanges(changes, get().edges),
        });
    },
    onConnect: (connection: Connection) => {
        set({
            edges: addEdge(connection, get().edges),
        });
    },
    addNode: (node: ThoughtNode) => {
        set({
            nodes: [...get().nodes, node],
        });
    },
    updateNodeStatus: (id: string, status: BlockStatus) => {
        set({
            nodes: get().nodes.map((node: ThoughtNode) => {
                if (node.id === id) {
                    return {
                        ...node,
                        data: {
                            ...node.data,
                            status,
                        },
                    };
                }
                return node;
            }),
        });
    },
    selectNode: (id: string | null) => {
        set({ selectedNodeId: id });
    },

    checkSystemStatus: async () => {
        try {
            const status = await aegisApi.getStatus();
            set({ systemStatus: status.status, ledgerHeight: status.ledger_height });
        } catch (e) {
            set({ systemStatus: 'OFFLINE' });
        }
    },

    submitGraph: async () => {
        const { nodes, edges } = get();
        // Convert React Flow graph to AEGIS Governance Graph format
        const governanceGraph = {
            nodes: nodes.map(n => ({
                id: n.id,
                type: n.data.type === 'QUESTION' ? 'PROPOSAL' : n.data.type, // Map QUESTION to PROPOSAL
                title: n.data.title,
                content: n.data.content,
                author_id: "did:aegis:user",
                effects: n.data.effects
            })),
            edges: edges.map(e => ({
                source: e.source,
                target: e.target,
                relation: "SUPPORTS",
                weight: 1.0
            }))
        };

        try {
            const result = await aegisApi.submitProposal(governanceGraph);

            // Update the Proposal Node with the result
            // Find the root node (Question/Proposal)
            const proposalNode = nodes.find(n => n.data.type === 'QUESTION' || n.data.type === 'PROTOCOL');

            if (proposalNode) {
                set({
                    nodes: nodes.map(n =>
                        n.id === proposalNode.id
                            ? {
                                ...n,
                                data: {
                                    ...n.data,
                                    status: result.decision,
                                    reductionResult: result
                                }
                            }
                            : n
                    )
                });
            }
        } catch (e) {
            console.error("Submission failed", e);
        }
    },
}));

export default useStore;
