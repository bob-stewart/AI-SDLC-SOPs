import { useEffect, useState } from 'react';
import init, { evaluate_proposal } from '../wasm/aegis_cgr/aegis_cgr';

export const CGRStatus = () => {
    const [status, setStatus] = useState<string>("Initializing Iron Core...");
    const [reason, setReason] = useState<string>("");

    useEffect(() => {
        const runWasm = async () => {
            await init();

            // Sample Proposal (High Risk)
            const graph = {
                nodes: [{
                    id: "1",
                    type_: "PROPOSAL",
                    title: "Dangerous Action",
                    content: "Delete all databases.",
                    effects: {
                        risk: 0.9, // Exceeds 0.8 threshold
                        fairness: 0.5,
                        novelty: 0.1,
                        privacy: 0.1
                    }
                }]
            };

            try {
                const result = evaluate_proposal(graph);
                setStatus(`Decision: ${result.decision}`);
                setReason(result.reason);
            } catch (e) {
                setStatus("Error executing CGR");
                console.error(e);
            }
        };

        runWasm();
    }, []);

    return (
        <div className="fixed bottom-4 right-4 p-4 bg-black/80 border border-amber-500/50 rounded-lg backdrop-blur-md text-xs font-mono z-50">
            <div className="text-amber-500 font-bold mb-1">IRON CORE (WASM)</div>
            <div className={status.includes("APPROVED") ? "text-green-400" : "text-red-400"}>
                {status}
            </div>
            <div className="text-gray-400 mt-1 max-w-[200px]">
                {reason}
            </div>
        </div>
    );
};
