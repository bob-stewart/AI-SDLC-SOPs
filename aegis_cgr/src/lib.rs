use wasm_bindgen::prelude::*;
use serde::{Deserialize, Serialize};
use std::collections::{HashSet, HashMap};

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
    pub type_: String, // "PROPOSAL", "CLAIM", "EVIDENCE", "VOTE", "POLICY"
    pub title: String,
    pub content: String,
    pub effects: EffectVector,
    pub author_id: Option<String>,
    pub signature: Option<String>,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct GovernanceEdge {
    pub source: String,
    pub target: String,
    pub relation: String, // "SUPPORTS", "OPPOSES", "DEPENDS_ON"
    pub weight: f64,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct GovernanceGraph {
    pub nodes: Vec<GovernanceNode>,
    pub edges: Vec<GovernanceEdge>,
}

#[derive(Serialize, Deserialize, Debug, Clone)]
pub struct ReductionResult {
    pub decision: String, // "APPROVED", "REJECTED", "DEFERRED"
    pub reason: String,
    pub violations: Vec<String>,
}

// --- The Iron Law (Reduction Engine) ---

#[wasm_bindgen]
pub fn evaluate_proposal(val: JsValue) -> JsValue {
    // 1. Deserialize JS Object to Rust Struct
    let graph: GovernanceGraph = match serde_wasm_bindgen::from_value(val) {
        Ok(g) => g,
        Err(e) => return serde_wasm_bindgen::to_value(&ReductionResult {
            decision: "REJECTED".to_string(),
            reason: format!("Invalid Graph Structure: {}", e),
            violations: vec![format!("Serialization Error: {}", e)],
        }).unwrap(),
    };

    // 2. The Reduction Logic
    let result = reduce(&graph);

    // 3. Serialize Rust Struct back to JS Object
    serde_wasm_bindgen::to_value(&result).unwrap()
}

fn reduce(graph: &GovernanceGraph) -> ReductionResult {
    let mut violations = Vec::new();

    // Rule 1: Empty Graph is Invalid
    if graph.nodes.is_empty() {
        return ReductionResult {
            decision: "REJECTED".to_string(),
            reason: "Graph is empty.".to_string(),
            violations: vec!["Graph must contain at least one node.".to_string()],
        };
    }

    // Rule 2: Cycle Detection (Infinite Loops in Logic)
    if has_cycle(graph) {
        violations.push("Cycle detected in governance graph. Logic must be acyclic.".to_string());
    }

    // Rule 3: Signature Verification (Stub)
    for node in &graph.nodes {
        if !verify_signature(node) {
            violations.push(format!("Invalid signature for node '{}'.", node.title));
        }
    }

    // Rule 4: Risk Threshold (The original rule)
    // Find the PROPOSAL node (assuming first node or explicit type)
    let proposal = graph.nodes.iter().find(|n| n.type_ == "PROPOSAL" || n.type_ == "AMENDMENT").unwrap_or(&graph.nodes[0]);
    
    if proposal.effects.risk > 0.8 {
        violations.push(format!("Risk level {:.2} exceeds constitutional threshold of 0.8", proposal.effects.risk));
    }

    // Rule 5: Fairness Floor
    if proposal.effects.fairness < 0.3 {
        violations.push(format!("Fairness level {:.2} is below constitutional floor of 0.3", proposal.effects.fairness));
    }

    if !violations.is_empty() {
        return ReductionResult {
            decision: "REJECTED".to_string(),
            reason: "Constitutional invariants violated.".to_string(),
            violations,
        };
    }

    // Default: Approve
    ReductionResult {
        decision: "APPROVED".to_string(),
        reason: "Proposal satisfies all constitutional invariants.".to_string(),
        violations: vec![],
    }
}

// --- Helper Functions ---

fn has_cycle(graph: &GovernanceGraph) -> bool {
    let mut adj: HashMap<&String, Vec<&String>> = HashMap::new();
    for edge in &graph.edges {
        adj.entry(&edge.source).or_default().push(&edge.target);
    }

    let mut visited = HashSet::new();
    let mut recursion_stack = HashSet::new();

    for node in &graph.nodes {
        if is_cyclic(&node.id, &adj, &mut visited, &mut recursion_stack) {
            return true;
        }
    }
    false
}

fn is_cyclic<'a>(
    node_id: &'a String,
    adj: &HashMap<&'a String, Vec<&'a String>>,
    visited: &mut HashSet<&'a String>,
    stack: &mut HashSet<&'a String>,
) -> bool {
    if stack.contains(node_id) {
        return true;
    }
    if visited.contains(node_id) {
        return false;
    }

    visited.insert(node_id);
    stack.insert(node_id);

    if let Some(neighbors) = adj.get(node_id) {
        for neighbor in neighbors {
            if is_cyclic(neighbor, adj, visited, stack) {
                return true;
            }
        }
    }

    stack.remove(node_id);
    false
}

fn verify_signature(node: &GovernanceNode) -> bool {
    // Stub: In a real system, we would check Ed25519 signatures.
    // For now, we just check if an author_id is present if it's a PROPOSAL.
    if node.type_ == "PROPOSAL" && node.author_id.is_none() {
        return false;
    }
    true
}
