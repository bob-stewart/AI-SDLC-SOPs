import { useEffect } from 'react';
import { Network, ShieldCheck } from 'lucide-react';
import useStore from '../store';

const ProtocolBar = () => {
    const systemStatus = useStore((state) => state.systemStatus);
    const ledgerHeight = useStore((state) => state.ledgerHeight);
    const checkSystemStatus = useStore((state) => state.checkSystemStatus);

    useEffect(() => {
        checkSystemStatus();
        const interval = setInterval(checkSystemStatus, 5000); // Poll every 5s
        return () => clearInterval(interval);
    }, [checkSystemStatus]);

    return (
        <div className="absolute top-0 left-0 w-full h-16 glass border-b border-white/10 z-50 flex items-center justify-between px-6">
            <div className="flex items-center gap-4">
                <div className="flex items-center gap-2 text-primary">
                    <Network size={24} />
                    <span className="font-bold text-lg tracking-tight">SYNTAXIS</span>
                </div>
                <div className="h-6 w-px bg-white/10" />
                <div className="flex items-center gap-2 text-xs font-mono text-secondary">
                    <span>PROTOCOL:</span>
                    <span className="text-white">GENESIS v1.0</span>
                </div>
            </div>

            <div className="flex items-center gap-4">
                <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-surface border border-white/5 text-xs font-mono text-secondary">
                    <div className={`w-2 h-2 rounded-full ${systemStatus === 'AEGIS ENGINE ONLINE' ? 'bg-success animate-pulse' : 'bg-danger'}`} />
                    {systemStatus}
                </div>
                <div className="flex items-center gap-2 px-3 py-1.5 rounded-full bg-surface border border-white/5 text-xs font-mono text-secondary">
                    <ShieldCheck size={14} />
                    <span>LEDGER HEIGHT: {ledgerHeight}</span>
                </div>
            </div>
        </div>
    );
};

export default ProtocolBar;
