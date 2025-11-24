use wasm_bindgen::prelude::*;
use serde::{Deserialize, Serialize};

// --- Domain Models ---

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct EffectVector {
    pub risk: f64,
    pub fairness: f64,
    pub novelty: f64,
    pub privacy: f64,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct GovernanceNode {
    pub id: String,
    pub type_: String, // "PROPOSAL", "CLAIM", etc.
    pub title: String,
    pub content: String,
    pub effects: EffectVector,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct GovernanceGraph {
    pub nodes: Vec<GovernanceNode>,
    // Edges omitted for MVP reduction logic, but would be here
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct ReductionResult {
    pub decision: String, // "APPROVED", "REJECTED", "DEFERRED"
    pub reason: String,
}

// --- The Iron Law (Reduction Engine) ---

#[wasm_bindgen]
pub fn evaluate_proposal(val: JsValue) -> JsValue {
    // 1. Deserialize JS Object to Rust Struct
    let graph: GovernanceGraph = serde_wasm_bindgen::from_value(val).unwrap();

    // 2. The Reduction Logic
    let result = reduce(&graph);

    // 3. Serialize Rust Struct back to JS Object
    serde_wasm_bindgen::to_value(&result).unwrap()
}

fn reduce(graph: &GovernanceGraph) -> ReductionResult {
    // The "Constitution" encoded in Rust
    
    // Rule 1: Empty Graph is Invalid
    if graph.nodes.is_empty() {
        return ReductionResult {
            decision: "REJECTED".to_string(),
            reason: "Graph is empty.".to_string(),
        };
    }

    // Rule 2: Risk Threshold
    // Find the PROPOSAL node (assuming first node for MVP)
    let proposal = &graph.nodes[0];
    
    if proposal.effects.risk > 0.8 {
        return ReductionResult {
            decision: "REJECTED".to_string(),
            reason: format!("Risk level {:.2} exceeds constitutional threshold of 0.8", proposal.effects.risk),
        };
    }

    // Rule 3: Fairness Floor
    if proposal.effects.fairness < 0.3 {
        return ReductionResult {
            decision: "REJECTED".to_string(),
            reason: format!("Fairness level {:.2} is below constitutional floor of 0.3", proposal.effects.fairness),
        };
    }

    // Default: Approve
    ReductionResult {
        decision: "APPROVED".to_string(),
        reason: "Proposal satisfies all constitutional invariants.".to_string(),
    }
}
