import React, { useCallback } from 'react';
import ReactFlow, {
  Background,
  Controls,
  MiniMap,
} from 'reactflow';
import 'reactflow/dist/style.css';
import useStore from './store';
// import ThoughtNode from './nodes/ThoughtNode';
import Composer from './components/Composer';
import { CGRStatus } from './components/CGRStatus';
import Inspector from './components/Inspector';
import ProtocolBar from './components/ProtocolBar';
import HoloCard from './nodes/HoloCard';
import AmendmentNode from './nodes/AmendmentNode';
import PulseEdge from './edges/PulseEdge';



function App() {
  const {
    nodes,
    edges,
    onNodesChange,
    onEdgesChange,
    onConnect,
    selectNode,
  } = useStore();

  const nodeTypes = React.useMemo(() => ({
    thoughtNode: HoloCard,
    amendmentNode: AmendmentNode,
  }), []);

  const edgeTypes = React.useMemo(() => ({
    pulse: PulseEdge,
  }), []);

  const onNodeClick = useCallback((_: React.MouseEvent, node: any) => {
    selectNode(node.id);
  }, [selectNode]);

  const onPaneClick = useCallback(() => {
    selectNode(null);
  }, [selectNode]);

  return (
    <div className="w-full h-screen bg-background text-white font-sans overflow-hidden relative">
      <ProtocolBar />

      <ReactFlow
        nodes={nodes}
        edges={edges}
        nodeTypes={nodeTypes}
        edgeTypes={edgeTypes}
        defaultEdgeOptions={{ type: 'pulse', animated: true }}
        onNodesChange={onNodesChange}
        onEdgesChange={onEdgesChange}
        onConnect={onConnect}
        onNodeClick={onNodeClick}
        onPaneClick={onPaneClick}
        fitView
        className="bg-background"
      >
        <Background color="#334155" gap={20} size={1} />
        <Controls className="!bg-surface !border-white/10 !fill-white" />
        <MiniMap
          className="!bg-surface !border-white/10"
          nodeColor={(n) => {
            if (n.data.status === 'APPROVED') return '#22c55e';
            if (n.data.status === 'REJECTED') return '#ef4444';
            return '#3b82f6';
          }}
        />
        <CGRStatus />
      </ReactFlow>

      <Composer />
      <Inspector />
    </div>
  );
}

export default App;
