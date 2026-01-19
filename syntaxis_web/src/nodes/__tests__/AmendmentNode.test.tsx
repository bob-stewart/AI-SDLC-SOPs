import { render, screen } from '@testing-library/react';
import { describe, it, expect } from 'vitest';
import AmendmentNode from '../AmendmentNode';
import { ReactFlowProvider } from 'reactflow';

describe('AmendmentNode', () => {
    const mockData = {
        id: 'test-1',
        type: 'AMENDMENT' as const,
        title: 'Test Amendment',
        content: 'This is a test amendment.',
        author: 'Tester',
        timestamp: Date.now(),
        status: 'DRAFT' as const,
        effects: { risk: 0, fairness: 0, novelty: 0, privacy: 0, target: 'Test Protocol' },
    };

    it('renders the amendment title and content', () => {
        render(
            <ReactFlowProvider>
                <AmendmentNode
                    id="1"
                    data={mockData}
                    selected={false}
                    type="amendmentNode"
                    zIndex={1}
                    isConnectable={true}
                    xPos={0}
                    yPos={0}
                    dragging={false}
                />
            </ReactFlowProvider>
        );

        expect(screen.getByText('Test Amendment')).toBeInTheDocument();
        expect(screen.getByText('This is a test amendment.')).toBeInTheDocument();
        expect(screen.getByText('PROTOCOL AMENDMENT')).toBeInTheDocument();
    });

    it('displays the target protocol', () => {
        render(
            <ReactFlowProvider>
                <AmendmentNode
                    id="1"
                    data={mockData}
                    selected={false}
                    type="amendmentNode"
                    zIndex={1}
                    isConnectable={true}
                    xPos={0}
                    yPos={0}
                    dragging={false}
                />
            </ReactFlowProvider>
        );

        expect(screen.getByText('TARGET: Test Protocol')).toBeInTheDocument();
    });
});
