import useStore from '../store';
import { X, Activity, Play } from 'lucide-react';
import clsx from 'clsx';

const Inspector = () => {
    const selectedNodeId = useStore((state) => state.selectedNodeId);
    const nodes = useStore((state) => state.nodes);
    const selectNode = useStore((state) => state.selectNode);
    const submitGraph = useStore((state) => state.submitGraph);

    const selectedNode = nodes.find((n) => n.id === selectedNodeId);

    if (!selectedNode) return null;

    const { data } = selectedNode;

    const handleDeliberate = () => {
        submitGraph();
    };

    return (
        <div className="absolute top-20 right-8 w-80 glass rounded-xl p-6 shadow-2xl z-40 animate-in slide-in-from-right-10 fade-in duration-200">
            <div className="flex justify-between items-start mb-6">
                <div>
                    <div className="text-xs font-mono text-secondary mb-1 uppercase tracking-wider">{data.type}</div>
                    <h2 className="text-xl font-bold text-white leading-tight">{data.title}</h2>
                </div>
                <button onClick={() => selectNode(null)} className="text-secondary hover:text-white transition-colors">
                    <X size={20} />
                </button>
            </div>

            <div className="mb-6">
                <p className="text-sm text-slate-300 leading-relaxed">
                    {data.content}
                </p>
            </div>

            <div className="space-y-4 mb-6">
                <div className="flex items-center gap-2 text-xs font-mono text-secondary uppercase tracking-wider">
                    <Activity size={14} />
                    <span>Effect Vector</span>
                </div>

                <div className="space-y-3">
                    <div className="space-y-1">
                        <div className="flex justify-between text-xs">
                            <span className="text-slate-400">Risk</span>
                            <span className="text-white font-mono">{data.effects.risk.toFixed(2)}</span>
                        </div>
                        <div className="h-1.5 bg-surface rounded-full overflow-hidden">
                            <div
                                className="h-full bg-danger transition-all duration-500"
                                style={{ width: `${data.effects.risk * 100}%` }}
                            />
                        </div>
                    </div>

                    <div className="space-y-1">
                        <div className="flex justify-between text-xs">
                            <span className="text-slate-400">Fairness</span>
                            <span className="text-white font-mono">{data.effects.fairness.toFixed(2)}</span>
                        </div>
                        <div className="h-1.5 bg-surface rounded-full overflow-hidden">
                            <div
                                className="h-full bg-success transition-all duration-500"
                                style={{ width: `${data.effects.fairness * 100}%` }}
                            />
                        </div>
                    </div>
                </div>
            </div>

            <div className="pt-6 border-t border-white/10">
                <div className="flex justify-between items-center mb-4">
                    <span className="text-xs font-mono text-secondary">STATUS</span>
                    <span className={clsx(
                        'px-2 py-0.5 rounded-full text-xs font-bold border',
                        data.status === 'APPROVED' ? 'bg-success/20 text-success border-success/50' :
                            data.status === 'REJECTED' ? 'bg-danger/20 text-danger border-danger/50' :
                                'bg-surface text-primary border-white/10'
                    )}>
                        {data.status}
                    </span>
                </div>

                {data.status === 'DRAFT' && (
                    <button
                        onClick={handleDeliberate}
                        className="w-full group relative overflow-hidden bg-primary hover:bg-blue-600 text-white py-3 rounded-lg font-medium transition-all hover:shadow-lg hover:shadow-primary/25"
                    >
                        <div className="absolute inset-0 bg-white/20 translate-y-full group-hover:translate-y-0 transition-transform duration-300" />
                        <div className="relative flex items-center justify-center gap-2">
                            <Play size={18} className="fill-current" />
                            <span>INITIATE DELIBERATION</span>
                        </div>
                    </button>
                )}

                {data.reductionResult && (
                    <div className="mt-4 p-3 bg-surface rounded-lg border border-white/5">
                        <div className="text-xs font-mono text-secondary mb-2">REDUCTION TRACE</div>
                        <div className="text-xs text-slate-400 font-mono space-y-1 max-h-32 overflow-y-auto">
                            {data.reductionResult.trace.map((line, i) => (
                                <div key={i}>{line}</div>
                            ))}
                        </div>
                    </div>
                )}
            </div>
        </div>
    );
};

export default Inspector;
