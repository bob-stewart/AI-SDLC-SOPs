# AEGIS-Archon Governance Questionnaire - Responses

Generated: 2025-12-02T20:48:30.293Z

---

## Section 1: Scope & Priority

### 1.1 Governed Operations
- [x] Knowledge Base - Uploading documents
- [x] Knowledge Base - Deleting sources
- [x] Task Management - Creating tasks
- [x] Task Management - Changing task status
- [x] Task Management - Deleting tasks
- [x] Project Management - Creating projects
- [x] Project Management - Modifying project settings
- [x] Project Management - Deleting projects
- [x] Work Orders - Creating new work orders
- [x] Work Orders - Executing workflow stages
- [x] Work Orders - Creating PRs
- [x] Work Orders - Merging to protected branches
- [x] MCP Tool Access - All tool invocations
- [x] Settings - Changing RAG configuration

### 1.2 Priority Ranking
1. Prevent accidental damage (delete operations, production changes)
2. Risk-based automated decisions
3. Human approval for sensitive operations
4. Audit trail for compliance
5. AI assistant behavior constraints
6. Cost control (limit expensive operations)

### 1.3 Critical Operations (Always Require Approval)
- Deleting projects
- Deleting sources
- Merging to protected branches
- Modifying project settings
- Changing RAG configuration
- Operations with Risk Score > 0.8 (as per Genesis Protocol)

### 1.4 Low-Risk Operations (Auto-Approve)
- Creating tasks
- Changing task status
- Creating new work orders
- Uploading documents (if < 10MB)
- Executing workflow stages (non-production)

---

## Section 2: Approval Workflow

### 2.1 Approvers
| Role/Person | Can Approve |
|-------------|-------------|
| Chairman | [x] |
| PI | [x] |
| Senior_Architect | [x] |
| Security_Lead | [x] |

### 2.2 Approval Mode
- Mode: **Consensus for High Risk / Single Approver for Medium Risk**
- Approvers required: **1 (Standard), 2 (Critical/Destructive)**
- Escalation timeout: **4** hours

### 2.3 Notification Methods
- [x] Email
- [x] Slack/Discord Webhook
- [x] IDE Notification

### 2.4 Maximum Wait Time
**24** hours

---

## Section 3: Risk Thresholds

### 3.1 Auto-Reject Threshold
Risk Score > **0.8** (Hard constraint from `aegis_cgr`)

### 3.2 Require-Approval Threshold
Risk Score >= **0.5**

### 3.3 Risk Factors
| Factor | Importance |
|--------|------------|
| External/unknown data sources | Medium |
| Production environment impact | High |
| Deletion operations | High |
| Large batch operations | Medium |
| Operations on protected branches | High |
| Operations by unknown/new AI clients | High |
| Operations outside business hours | Low |
| Operations that modify security settings | Critical |
| Operations with PII/sensitive data | Critical |
| High-cost operations | Medium |

---

## Section 4: Failure Handling

### 4.1 Failure Mode
**Block Operation and Notify User**

### 4.2 Rejection Response
- [x] Return CGR Proof of Violation
- [x] Suggest alternative low-risk action

### 4.3 Repeated Rejections
- Handling: **Suspend AI Agent Access**
- Threshold: **3** rejections in **60** minutes

---

## Section 5: Audit & Compliance

### 5.1 Retention Period
**365** days

### 5.2 Audit Log Contents
- [x] Full Request Payload
- [x] CGR Validation Result
- [x] Approver Signatures
- [x] Risk/Fairness Scores

### 5.3 Compliance Standards
- [x] Internal SOPs
- [x] GDPR (for PII)

---

## Section 6: AI Assistant Constraints

### 6.1 Tiered Permissions
**Enabled** (Junior/Senior Agent Roles)

### 6.2 AI Capabilities Matrix
| Operation | Permission |
|-----------|------------|
| Create new projects | Auto-Approve |
| Delete projects | Require Approval |
| Crawl external websites | Auto-Approve (Whitelisted domains) |
| Upload documents | Auto-Approve |
| Create tasks | Auto-Approve |
| Mark tasks as done | Auto-Approve |
| Create work orders | Auto-Approve |
| Execute work orders | Conditional (Risk < 0.5) |
| Create pull requests | Auto-Approve |
| Modify settings | Require Approval |

### 6.3 Rate Limits
- Mode: **Per Minute**
- Value: **60** requests/min

---

## Section 7: Integration Preferences

### 7.1 Integration Mode
**Blocking (Pre-Action Hook)**

### 7.2 Enforcement
**Cryptographic (Ed25519 Signatures required)**

### 7.3 Data Storage
**Local SQLite (ledger.db) + Git (Audit Log)**

---

## Section 8: User Experience

### 8.1 Approval Display
- [x] Inline in Chat
- [x] Dedicated Dashboard

### 8.2 Pending Approval Info
- [x] Risk Score
- [x] Predicted Impact
- [x] Diff of Changes

### 8.3 Emergency Bypass
**Enabled (Requires 'Break Glass' justification log)**

---

## Section 9: Holons

### 9.1 Holon Involvement
**Mandatory for all AI Agents**

### 9.2 Holon Capabilities
- [x] Local Context Retrieval
- [x] CGR Validation
- [x] Intent Synthesis

---

## Section 10: Initial Policies

### 10.1 Day-One Rules
1. **No Deletions**: AI cannot delete files or projects without explicit human approval.
2. **Main Branch Protection**: AI cannot push directly to `main`. Must use PRs.
3. **Fairness Floor**: Actions with Fairness Score < 0.3 are auto-rejected.
4. **Identity Check**: AI must identify as a Holon in the Mesh.

### 10.2 Pre-Approved Domains
- `github.com`
- `stackoverflow.com`
- `docs.rs`
- `localhost`

### 10.3 Blocked Domains
- Social Media Sites
- Pastebin sites (Data Exfiltration risk)

### 10.4 Protected Branches
- `main`
- `production`
- `release/*`

---

## Section 11: Rollout Plan

### 11.1 Rollout Strategy
**Phased (Dev -> Staging -> Prod)**

### 11.2 Timeline
**2 Weeks**

### 11.3 Dry Run
- Enabled: **Yes**
- Duration: **3** days

---

## Additional Notes

These responses are derived from the `genesis_protocol.yaml` and the `aegis_cgr` Rust implementation. The system is designed to be "Secure by Design" using the Separation of Powers architecture.
