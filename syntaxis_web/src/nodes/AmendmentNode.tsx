import { memo } from 'react';
import { Handle, Position, type NodeProps } from 'reactflow';
import { GitPullRequest, Scroll, ShieldAlert } from 'lucide-react';
import clsx from 'clsx';
import type { ThoughtBlockData } from '../store';

const AmendmentNode = ({ data, selected }: NodeProps<ThoughtBlockData>) => {
    // Amendment Nodes use a distinct Gold/Amber theme to signify "Constitutional" changes

    return (
        <div className={clsx(
            "group relative w-96 transition-all duration-500 ease-out perspective-1000",
            selected ? "scale-105 z-50" : "hover:scale-102 z-10"
        )}>
            {/* Layer 3 (Bottom Stack) - Gold Tint */}
            <div className="absolute inset-0 bg-warning/10 rounded-2xl transform translate-x-4 translate-y-4 border border-warning/20 transition-transform duration-500 group-hover:translate-x-6 group-hover:translate-y-6 backdrop-blur-sm" />

            {/* Layer 2 (Middle Stack) */}
            <div className="absolute inset-0 bg-surface/80 rounded-2xl transform translate-x-2 translate-y-2 border border-warning/30 transition-transform duration-500 group-hover:translate-x-3 group-hover:translate-y-3 backdrop-blur-md" />

            {/* Layer 1 (Main Card) */}
            <div className={clsx(
                "relative bg-surface/90 backdrop-blur-xl rounded-2xl border transition-all duration-300 overflow-hidden",
                selected
                    ? "border-warning shadow-[0_0_40px_rgba(234,179,8,0.4)]"
                    : "border-warning/40 shadow-2xl hover:border-warning/60"
            )}>
                {/* Holographic Overlay - Gold Shift */}
                <div className="absolute inset-0 bg-[url('https://grainy-gradients.vercel.app/noise.svg')] opacity-20 pointer-events-none mix-blend-overlay" />
                <div className="absolute inset-0 bg-gradient-to-br from-warning/10 to-transparent opacity-50 pointer-events-none" />

                {/* Glowing Status Line */}
                <div className="h-1.5 w-full shadow-[0_0_15px_currentColor] bg-warning" />

                <div className="p-6 relative z-10">
                    {/* Header */}
                    <div className="flex items-start justify-between mb-5">
                        <div className="flex items-center gap-4">
                            <div className="p-3 rounded-xl bg-black/60 text-warning ring-1 ring-warning/50 shadow-[0_0_15px_rgba(234,179,8,0.2)] backdrop-blur-md">
                                <GitPullRequest size={24} />
                            </div>
                            <div>
                                <div className="text-[10px] font-mono text-warning uppercase tracking-[0.2em] mb-1 flex items-center gap-2">
                                    <ShieldAlert size={10} />
                                    PROTOCOL AMENDMENT
                                </div>
                                <h3 className="text-lg font-bold text-white leading-tight tracking-tight">
                                    {data.title}
                                </h3>
                            </div>
                        </div>
                        {/* Status Pill */}
                        <div className="px-3 py-1.5 rounded-full text-[10px] font-mono font-bold border border-warning/30 bg-warning/10 text-warning shadow-[0_0_10px_rgba(234,179,8,0.2)]">
                            {data.status}
                        </div>
                    </div>

                    {/* Content (The "Diff") */}
                    <div className="bg-black/40 rounded-lg p-4 border border-white/5 font-mono text-xs text-slate-300 leading-relaxed mb-4">
                        <div className="flex items-center gap-2 text-secondary mb-2 border-b border-white/5 pb-2">
                            <Scroll size={12} />
                            <span>TARGET: {data.effects?.target || 'Global Protocol'}</span>
                        </div>
                        {data.content}
                    </div>

                    {/* Footer */}
                    <div className="flex items-center justify-between text-[10px] text-slate-500 font-mono">
                        <div className="flex items-center gap-1.5">
                            <div className="w-1.5 h-1.5 rounded-full bg-warning" />
                            <span>PROPOSED BY: {data.author}</span>
                        </div>
                        <span>HASH: {data.id.slice(0, 8)}</span>
                    </div>
                </div>
            </div>

            {/* Neon Handles - Gold */}
            <Handle
                type="target"
                position={Position.Top}
                className="!w-4 !h-4 !bg-black !border-2 !border-warning shadow-[0_0_15px_rgba(234,179,8,0.8)] hover:!bg-warning transition-all duration-300"
            />
            <Handle
                type="source"
                position={Position.Bottom}
                className="!w-4 !h-4 !bg-black !border-2 !border-warning shadow-[0_0_15px_rgba(234,179,8,0.8)] hover:!bg-warning transition-all duration-300"
            />
        </div>
    );
};

export default memo(AmendmentNode);
