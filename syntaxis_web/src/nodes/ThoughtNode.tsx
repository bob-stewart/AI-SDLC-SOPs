import { memo } from 'react';
import { Handle, Position, type NodeProps } from 'reactflow';
import type { ThoughtBlockData } from '../store';
import { HelpCircle, AlertCircle, FileText, ShieldAlert, CheckCircle, Gavel } from 'lucide-react';
import clsx from 'clsx';

const icons: Record<string, any> = {
    QUESTION: HelpCircle,
    CLAIM: AlertCircle,
    EVIDENCE: FileText,
    PROTOCOL: Gavel,
    RISK: ShieldAlert,
    DECISION: CheckCircle,
};

const statusColors: Record<string, string> = {
    DRAFT: 'border-secondary',
    PROPOSED: 'border-primary',
    APPROVED: 'border-success',
    REJECTED: 'border-danger',
};

const ThoughtNode = ({ data, selected }: NodeProps<ThoughtBlockData>) => {
    const Icon = icons[data.type] || FileText;

    return (
        <div
            className={clsx(
                'glass rounded-lg p-4 min-w-[200px] border-2 transition-all duration-200',
                statusColors[data.status],
                selected ? 'ring-2 ring-white shadow-lg scale-105' : 'hover:border-opacity-80'
            )}
        >
            <Handle type="target" position={Position.Top} className="!bg-secondary" />

            <div className="flex items-start gap-3">
                <div className={clsx(
                    'p-2 rounded-md',
                    data.status === 'APPROVED' ? 'bg-success/20 text-success' :
                        data.status === 'REJECTED' ? 'bg-danger/20 text-danger' :
                            'bg-surface text-primary'
                )}>
                    <Icon size={20} />
                </div>

                <div className="flex-1">
                    <div className="text-xs font-mono text-secondary mb-1">{data.type}</div>
                    <div className="font-medium text-sm text-slate-100 line-clamp-2">
                        {data.title}
                    </div>
                </div>
            </div>

            {data.status !== 'DRAFT' && (
                <div className="mt-3 flex items-center gap-2 text-xs font-mono">
                    <span className={clsx(
                        'px-2 py-0.5 rounded-full bg-surface border border-white/10',
                        data.status === 'APPROVED' ? 'text-success' :
                            data.status === 'REJECTED' ? 'text-danger' :
                                'text-primary'
                    )}>
                        {data.status}
                    </span>
                </div>
            )}

            <Handle type="source" position={Position.Bottom} className="!bg-secondary" />
        </div>
    );
};

export default memo(ThoughtNode);
