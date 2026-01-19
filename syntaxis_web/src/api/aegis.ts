const BASE_URL = 'http://localhost:8000';

export interface AegisStatus {
    status: string;
    version: string;
    vm_state: any;
    ledger_height: number;
}

export interface ReductionResult {
    decision: 'APPROVED' | 'REJECTED' | 'DEFERRED';
    trace: string[];
    final_effects: any;
}

export const aegisApi = {
    async getStatus(): Promise<AegisStatus> {
        const res = await fetch(`${BASE_URL}/`);
        return res.json();
    },

    async triggerGenesis(trustees: string[], threshold: number) {
        const res = await fetch(`${BASE_URL}/genesis`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ trustees, threshold }),
        });
        return res.json();
    },

    async registerIdentity(alias: string, public_key: string) {
        const res = await fetch(`${BASE_URL}/identity/register`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify({ alias, public_key }),
        });
        return res.json();
    },

    async submitProposal(graph: any): Promise<ReductionResult> {
        const res = await fetch(`${BASE_URL}/proposal`, {
            method: 'POST',
            headers: { 'Content-Type': 'application/json' },
            body: JSON.stringify(graph),
        });
        if (!res.ok) throw new Error('Proposal submission failed');
        return res.json();
    },

    async getLedger() {
        const res = await fetch(`${BASE_URL}/ledger`);
        return res.json();
    }
};
