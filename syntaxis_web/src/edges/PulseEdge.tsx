import { BaseEdge, type EdgeProps, getSmoothStepPath } from 'reactflow';

const PulseEdge = ({
    id,
    sourceX,
    sourceY,
    targetX,
    targetY,
    sourcePosition,
    targetPosition,
    style = {},
    markerEnd,
}: EdgeProps) => {
    const [edgePath] = getSmoothStepPath({
        sourceX,
        sourceY,
        sourcePosition,
        targetX,
        targetY,
        targetPosition,
    });

    return (
        <>
            {/* Glow Layer */}
            <BaseEdge
                path={edgePath}
                style={{
                    ...style,
                    stroke: '#3b82f6',
                    strokeWidth: 4,
                    strokeOpacity: 0.1,
                    filter: 'blur(4px)'
                }}
            />

            {/* Base Line */}
            <BaseEdge
                path={edgePath}
                markerEnd={markerEnd}
                style={{
                    ...style,
                    stroke: '#1e293b',
                    strokeWidth: 2
                }}
            />

            {/* Animated Pulse Packet */}
            <circle r="2" fill="#fff">
                <animateMotion dur="1.5s" repeatCount="indefinite" path={edgePath}>
                    <mpath href={`#${id}`} />
                </animateMotion>
            </circle>

            {/* Trailing Energy Tail */}
            <path
                id={id}
                d={edgePath}
                fill="none"
                stroke="url(#pulseGradient)"
                strokeWidth="2"
                strokeDasharray="100 100"
                className="animate-pulse-flow"
                style={{
                    strokeLinecap: 'round',
                    animation: 'dashdraw 1.5s linear infinite',
                }}
            />

            <defs>
                <linearGradient id="pulseGradient" gradientUnits="userSpaceOnUse">
                    <stop offset="0%" stopColor="#3b82f6" stopOpacity="0" />
                    <stop offset="50%" stopColor="#60a5fa" stopOpacity="1" />
                    <stop offset="100%" stopColor="#93c5fd" stopOpacity="0" />
                </linearGradient>
            </defs>

            <style>
                {`
          @keyframes dashdraw {
            from { stroke-dashoffset: 200; }
            to { stroke-dashoffset: 0; }
          }
        `}
            </style>
        </>
    );
};

export default PulseEdge;
