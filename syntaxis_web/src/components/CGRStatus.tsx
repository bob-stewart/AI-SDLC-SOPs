import { useEffect } from 'react';
import useStore from '../store';

export const CGRStatus = () => {
    const { cgrStatus, cgrReason, cgrViolations, initWasm } = useStore();

    useEffect(() => {
        initWasm();
    }, [initWasm]);

    const isApproved = cgrStatus === "APPROVED";
    const isError = cgrStatus.includes("ERROR");

    return (
        <div className="fixed bottom-4 right-4 p-4 bg-black/80 border border-amber-500/50 rounded-lg backdrop-blur-md text-xs font-mono z-50 max-w-sm">
            <div className="text-amber-500 font-bold mb-1 flex justify-between items-center">
                <span>IRON CORE (WASM)</span>
                <span className="opacity-50">{new Date().toLocaleTimeString()}</span>
            </div>

            <div className={`text-lg font-bold ${isApproved ? "text-green-400" : isError ? "text-yellow-400" : "text-red-400"}`}>
                {cgrStatus}
            </div>

            <div className="text-gray-300 mt-1">
                {cgrReason}
            </div>

            {cgrViolations.length > 0 && (
                <div className="mt-2 pt-2 border-t border-white/10">
                    <div className="text-red-400 font-bold mb-1">VIOLATIONS:</div>
                    <ul className="list-disc list-inside text-red-300/80 space-y-1">
                        {cgrViolations.map((v, i) => (
                            <li key={i}>{v}</li>
                        ))}
                    </ul>
                </div>
            )}
        </div>
    );
};
