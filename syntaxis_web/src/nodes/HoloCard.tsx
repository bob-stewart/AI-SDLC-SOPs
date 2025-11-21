import { memo } from 'react';
import { Handle, Position, type NodeProps } from 'reactflow';
import { BrainCircuit, Shield, Zap, FileText, CircleHelp, TriangleAlert } from 'lucide-react';
import clsx from 'clsx';
import type { ThoughtBlockData } from '../store';

const HoloCard = ({ data, selected }: NodeProps<ThoughtBlockData>) => {
    const Icon = getIcon(data.type);
    const statusColor = getStatusColor(data.status);
    const glowColor = getGlowColor(data.status);

    return (
        <div className={clsx(
            "group relative w-80 transition-all duration-500 ease-out perspective-1000",
            selected ? "scale-105 z-50" : "hover:scale-102 z-10"
        )}>
            {/* Layer 3 (Bottom Stack) */}
            <div className="absolute inset-0 bg-surface/40 rounded-2xl transform translate-x-4 translate-y-4 border border-white/5 transition-transform duration-500 group-hover:translate-x-6 group-hover:translate-y-6 backdrop-blur-sm" />

            {/* Layer 2 (Middle Stack) */}
            <div className="absolute inset-0 bg-surface/60 rounded-2xl transform translate-x-2 translate-y-2 border border-white/10 transition-transform duration-500 group-hover:translate-x-3 group-hover:translate-y-3 backdrop-blur-md" />

            {/* Layer 1 (Main Card) */}
            <div className={clsx(
                "relative bg-surface/80 backdrop-blur-xl rounded-2xl border transition-all duration-300 overflow-hidden",
                selected
                    ? `border-${glowColor} shadow-[0_0_30px_rgba(var(--color-${glowColor}),0.3)]`
                    : "border-white/10 shadow-2xl hover:border-white/20"
            )}>
                {/* Holographic Overlay */}
                <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-10 pointer-events-none mix-blend-overlay" />
                <div className="absolute inset-0 bg-gradient-to-br from-white/5 to-transparent opacity-50 pointer-events-none" />

                {/* Glowing Status Line */}
                <div className={clsx("h-1 w-full shadow-[0_0_10px_currentColor]", statusColor)} />

                <div className="p-5 relative z-10">
                    {/* Header */}
                    <div className="flex items-start justify-between mb-4">
                        <div className="flex items-center gap-3">
                            <div className={clsx(
                                "p-2.5 rounded-xl bg-black/40 text-white ring-1 ring-white/10 shadow-inner backdrop-blur-md",
                                `shadow-${glowColor}/20`
                            )}>
                                <Icon size={20} className={clsx(`text-${glowColor}`)} />
                            </div>
                            <div>
                                <div className="text-[10px] font-mono text-secondary uppercase tracking-[0.2em] mb-1">
                                    {data.type}
                                </div>
                                <h3 className="text-sm font-bold text-white leading-tight max-w-[180px] tracking-tight">
                                    {data.title}
                                </h3>
                            </div>
                        </div>
                        {/* Status Pill */}
                        <div className={clsx(
                            "px-2.5 py-1 rounded-full text-[10px] font-mono font-bold border shadow-lg backdrop-blur-md",
                            data.status === 'APPROVED' ? "bg-success/10 text-success border-success/20 shadow-success/10" :
                                data.status === 'REJECTED' ? "bg-danger/10 text-danger border-danger/20 shadow-danger/10" :
                                    "bg-white/5 text-secondary border-white/10"
                        )}>
                            {data.status}
                        </div>
                    </div>

                    {/* Content */}
                    <div className="text-xs text-slate-300 leading-relaxed font-light border-t border-white/5 pt-4 min-h-[60px]">
                        {data.content}
                    </div>

                    {/* Footer */}
                    <div className="mt-4 flex items-center justify-between text-[10px] text-slate-500 font-mono">
                        <div className="flex items-center gap-1.5">
                            <div className="w-1.5 h-1.5 rounded-full bg-secondary/50" />
                            <span>{data.author}</span>
                        </div>
                        <span>{new Date(data.timestamp).toLocaleTimeString()}</span>
                    </div>
                </div>
            </div>

            {/* Neon Handles */}
            <Handle
                type="target"
                position={Position.Top}
                className={clsx(
                    "!w-3 !h-3 !bg-black !border-2 transition-all duration-300",
                    `!border-${glowColor} shadow-[0_0_15px_rgba(var(--color-${glowColor}),0.8)]`,
                    "hover:!w-4 hover:!h-4 hover:!bg-white"
                )}
            />
            <Handle
                type="source"
                position={Position.Bottom}
                className={clsx(
                    "!w-3 !h-3 !bg-black !border-2 transition-all duration-300",
                    `!border-${glowColor} shadow-[0_0_15px_rgba(var(--color-${glowColor}),0.8)]`,
                    "hover:!w-4 hover:!h-4 hover:!bg-white"
                )}
            />
        </div>
    );
};

// Helpers
const getIcon = (type: string) => {
    switch (type) {
        case 'QUESTION': return CircleHelp;
        case 'CLAIM': return Zap;
        case 'EVIDENCE': return FileText;
        case 'RISK': return TriangleAlert;
        case 'DECISION': return BrainCircuit;
        case 'PROTOCOL': return Shield;
        default: return BrainCircuit;
    }
};

const getStatusColor = (status: string) => {
    switch (status) {
        case 'APPROVED': return 'bg-success';
        case 'REJECTED': return 'bg-danger';
        case 'PROPOSED': return 'bg-accent';
        default: return 'bg-slate-500';
    }
};

const getGlowColor = (status: string) => {
    switch (status) {
        case 'APPROVED': return 'success';
        case 'REJECTED': return 'danger';
        case 'PROPOSED': return 'accent';
        default: return 'primary';
    }
};

export default memo(HoloCard);
