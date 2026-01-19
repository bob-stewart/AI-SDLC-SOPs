# **SOP-1000-01-AI\_AI-Integrated-Program-and-Project-Management**

![][image1]  
SOP ID: 1000-01-AI  
Title: AI-Integrated Program and Project Management (*AI-SDLC*)  
Version: 1.0  
Effective Date: 2025-01-28  
Previous Version: None  
Reason for Update: Initial AI-Integrated SOP incorporating AI-IRB regulatory requirements.  
Owner: Chief Technology Officer (CTO) and AI Program Management Office (AI-PMO)

---

[🏠 AI Mind Matrix](../AI_Mind_Matrix.md) | [⚖️ AI Governance Gaps](../AI_Governance_Gaps.md) | [📋 SOP Index](./SOP-LIST-01-AI_AI-IRB-Governed-AI-SDLC.md)

---

---

## **1\. Objective**

This SOP defines the *Program and Project Management* framework for AI-Integrated Systems Development Life Cycle (AI-SDLC) at Horizon. It includes processes for engaging the AI Institutional Review Board (AI-IRB) when a project involves regulated AI components or high-risk AI features. The objective is to ensure:

1. Compliance with relevant AI governance, ethical guidelines, and regulatory standards (including AI-IRB).  
2. Efficiency in delivering AI-enabled products or services, balancing scope, cost, and schedule constraints.  
3. Quality in design, documentation, and rollout of new or enhanced functionalities that incorporate AI or ML (machine learning) modules.  
4. Traceability from initial business need through final deployment and post-implementation review.

---

## **2\. Scope**

This SOP covers all AI-related program and project management activities under the AI-SDLC umbrella, including:

* Initiation: AI concept approval, preliminary AI risk analysis, scoping.  
* Planning: Resource estimation, risk planning, integration with AI-IRB gating if needed.  
* Execution & Monitoring: Development, QA oversight, schedule control, risk management, AI-IRB review(s).  
* Close-out: Transition to production (or controlled rollout), sign-off, post-implementation reviews.

It applies to all Horizon teams: Product Development, AI-PMO, Engineering (Development, QA, Ops), Technical Support, and any external or contract resources.

---

## **3\. Definitions**

| Term | Definition |
| ----- | ----- |
| AI-IRB | *AI Institutional Review Board*, a governance body ensuring ethical and compliant oversight of AI modules, focusing on risk, bias, and regulatory compliance. |
| AI-SDLC | *AI-Integrated Systems Development Life Cycle*, a methodology that extends classical SDLC with specialized AI design, model governance, ethics, and monitoring controls. |
| Program | A collection of AI-related projects that share dependencies, resources, or strategic goals. |
| Project | A temporary endeavor to create or enhance AI-driven products/services with a defined scope, time, and cost constraints. |
| Gate (Business Gate) | A defined checkpoint in the AI-SDLC that requires specific deliverables to be approved before proceeding. Example: Gate 10 (Requirements Lock-Down), Gate 6 (Project Lock-Down), Gate 0 (General Availability). |
| **Authorized AI Agent** | An AI system or autonomous agent granted specific governance privileges, approved by the AI-IRB. |
| Deliverable | Any project output requiring formal review/approval (e.g., AI risk assessment, system design, code modules, test results, AI model performance metrics). |
| Performing Organization | Typically the Engineering Department (Development, QA, Ops, AI specialists). |
| Contracting Organization | Typically the Product/Technical Support groups or external clients who define requirements and accept deliverables. |

---

## **4\. Roles and Responsibilities**

| Role | Responsibilities |
| ----- | ----- |
| Senior Management | \- Establishes overall AI strategy and R\&D budget. \- Commissions new AI projects; appoints AI Project Sponsors. \- Provides final decisions for resource trade-offs. |
| AI-IRB | \- Evaluates high-risk AI designs/changes for ethical, legal, and regulatory compliance. \- Issues formal approval or requests rework for AI modules prior to release. |
| Project Sponsor | \- Champions the AI-related project from concept to closure. \- Escalates issues to Senior Management. \- Final authority on scope changes, cost, schedule trade-offs for the project. |
| AI-PMO | \- Oversees the consolidated portfolio of AI-centric projects. \- Tracks cross-project dependencies, resource conflicts. \- Issues periodic status to Senior Management; ensures common standards, policies, and reporting. |
| Product Manager | \- Defines the business requirements for AI features. \- Aligns AI solutions to strategic goals; consults with AI-IRB if risk classification is uncertain. \- Coordinates user acceptance criteria with QA & end-users. |
| Program Manager | \- Manages day-to-day tasks across multiple AI projects under a single program. \- Ensures gating deliverables are completed; organizes reviews with AI-IRB, QA, and other stakeholders. \- Coordinates risk management activities. |
| Project Manager | \- Single project focus: planning, scheduling, budget management. \- Coordinates tasks among development, QA, AI-IRB, and operations. \- Maintains project documentation, issue logs, change requests. |
| Development | \- Implements AI system features and code changes. \- Provides estimates, tracks actuals vs. estimates. \- Submits technical design docs and code to QA & AI-IRB as necessary. |
| Quality Assurance (QA) | \- Defines test strategies for AI systems (functionality, data bias, model performance, ethics compliance). \- Approves system readiness at each gate; logs defects. \- Coordinates with AI-IRB on measuring AI compliance. |
| Operations | \- Provides infrastructure for AI model deployment, environment provisioning, version control, site monitoring. \- Executes deployment steps in production. |
| Technical Support | \- Acts as service organization and possibly training group. \- Provides first-level support for AI product usage after deployment. |

---

## **5\. Procedure Activities**

Below are the *core* phases of AI-SDLC in the context of Program/Project Management.  
The management of AI projects includes **recursive self-improvement subroutines** and **Exochain Peer Reviews** to ensure alignment with AI-IRB governance.
Note: This SOP references major gates: G-12 → G-10 → G-6 → G-4 → G-2 → G-0.

### **5.1. Project Initiation (G-12 to G-10)**

1. AI Concept & Risk Preliminary Assessment:  
   * *Owner:* Project Sponsor, with AI-IRB consultation if the AI use case is classified as high risk.  
   * *Output:* Initial scope, risk classification, resource estimates.  
2. Define Business Requirements:  
   * *Owner:* Product Manager.  
   * *Output:* *Business Requirements Document (BRD)* capturing high-level AI functionality, success metrics, regulatory constraints.  
3. AI-IRB Consultation (as needed):  
   * *Trigger:* If the BRD indicates potential high-risk AI or personal data usage.  
   * *Outcome:* Possibly proceed with standard or expedited AI-IRB gating, or reduce scope.  
4. Gate 10: Requirements Lock-Down  
   * *Deliverables:* Final BRD, Project Resource Plan, AI Risk Statement.  
   * *Approval:* Governance, AI-IRB (if triggered).

### **5.2. Planning & Definition (G-10 to G-6)**

1. Refine Project Plan  
   * *Owner:* Project Manager, with input from AI-PMO, Development, QA, Ops.  
   * *Activities:* Detailed schedule, final budget, risk plan, and AI model governance approach.  
2. System Requirements  
   * *Owner:* Development & QA in close collaboration.  
   * *Key Components:* AI data pipeline design, user acceptance criteria, performance constraints.  
3. Quality Plan  
   * *Owner:* QA.  
   * *Activities:* Incorporates model validation strategy, bias detection procedures, specialized AI test cases.  
4. Gate 6: Project Lock-Down  
   * *Deliverables:* Project Plan, Final System Requirements, AI Quality Plan.  
   * *Approval:* Sponsor, AI-IRB, Program Manager.

### **5.3. Development & Validation (G-6 to G-4)**

1. Technical Design & Implementation  
   * *Owner:* Development.  
   * *Tasks:* Code AI modules, follow coding standards, integration with data sources, unit tests.  
2. Integration Testing & Model Tuning  
   * *Owner:* QA & Development.  
   * *Scope:* Check end-to-end workflows, data throughput, inference accuracy.  
   * *Defects:* Logged in SQA Manager; must fix or address.  
3. Gate 4: Begin Validation  
   * *Deliverables:* Completed integration test results, model performance metrics, updated documentation.  
   * *Approval:* QA, AI-IRB (for final pre-production clearance if major AI changes).

### **5.4. System Test & UAT (G-4 to G-2)**

1. System (QA) Testing  
   * *Owner:* QA.  
   * *Activities:* Functional, regression, stress, security checks, compliance with AI-IRB guidelines.  
   * *Outcome:* Sign-off if test coverage meets acceptance criteria.  
2. User Acceptance Test (UAT)  
   * *Owner:* Product Manager & End-Users.  
   * *Focus:* Confirm solution meets business needs, user interface usability, data correctness.  
3. Fix Defects  
   * *Owner:* Development, iteration with QA.  
   * *Tools:* SQA Manager for logging/tracking.  
4. Gate 2: Begin FOA / Beta  
   * *Deliverables:* UAT sign-off, final test coverage metrics, final readiness.

### **5.5. FOA/Beta & Deployment (G-2 to G-0)**

1. FOA/Beta  
   * *Owner:* Contracting Organization, with Dev & QA support.  
   * *Scope:* Early real-world usage, gather feedback, confirm model performance.  
2. Training & Documentation  
   * *Owner:* Technical Support.  
   * *Deliverables:* Final user manuals, training sessions for staff or clients.  
3. Deployment  
   * *Owner:* Operations.  
   * *Activities:* Production environment setup, final model push, version control, release notes.  
4. Gate 0: General Availability  
   * *Deliverables:* Production Release, sign-off from Sponsor, AI-IRB (if required).

### **5.6. Post Implementation Review**

1. Collect Post-Deployment Data  
   * *Owner:* QA & Product Manager.  
   * *Data Points:* AI model usage, performance metrics, error logs, user feedback.  
2. Lessons Learned  
   * *Owner:* Program Manager.  
   * *Method:* Conduct a formal post-implementation session, document improvement points, provide feedback to AI-SDLC process.  
3. Close-Out  
   * *Owner:* Project Manager.  
   * *Outcome:* Officially close project, archive documents, transition ongoing ops to Tech Support.

---

## **6\. Forms**

* (None introduced in this SOP)  
  * Refer to other AI-SDLC SOPs for forms such as *Change Request*, *Production Defect*, or *Release Planning* forms.

---

## **7\. Exemptions**

* If an AI-based project is low-risk (as determined by initial AI-IRB consultation), some gates or deliverables may be streamlined or waived, *provided that*\* the final documentation clearly states the justification.  
* Projects solely with classical software changes (no AI component) may not require AI-IRB gating.  
* For strictly internal R\&D or lab prototypes, standard gating may be replaced by a minimal gate approach if the Project Sponsor and AI-IRB confirm no external user or regulated data is involved.

---

## **8\. Tools/Software/Technology**

* SQA Manager: For defect tracking.  
* Project Management Software: (e.g., Jira, Microsoft Project, or Asana) for tasks, scheduling, resource planning.  
* Version Control: Git, ClearCase, or other, for code and documentation.  
* Collaboration: Confluence, Teams, or Slack, for knowledge sharing, updates.

---

## **9\. References**

* SOP 1005: *Release Planning*  
* SOP 1040: *Requirements Definition*  
* SOP 1041: *Detail Design*  
* SOP 1101: *Training and Documentation*  
* SOP 1200: *Development*  
* SOP 1210: *Quality Function*  
* SOP 1220: *Deployment*

---

## **10\. Revision History**

| Version | Date | Description | Approved By |
| ----- | ----- | ----- | ----- |
| 1.0 | 2025-01-28 | Initial AI-Integrated SOP w/ AI-IRB compliance references. | CTO, AI-PMO |

---

## **11\. Approvals**

| Name/Title | Signature | Date |
| ----- | ----- | ----- |
| *Chief Technology Officer* | *(digital or ink)* | 2025-01-28 |
| *AI-PMO Director* | *(digital or ink)* | 2025-01-28 |
| *Head of AI-IRB* | *(digital or ink)* | 2025-01-28 |

---

END OF SOP 1000-01-AI

Note: This SOP becomes effective upon the date of the final signature and must be used in conjunction with all relevant AI-SDLC procedures.

**Diagram Description:**

* The diagram shows each major role as a swim lane.  
* It walks through the AI-SDLC program/project management stages, from initiation (where Senior Management commissions an AI project) through requirements gathering, AI-IRB consultation if high-risk AI is identified, formal gates (G-10, G-6, G-4, G-2, G-0), development and testing stages, final deployment, and post-implementation review. Decision points (notably around AI-IRB if the project is high risk, and during UAT and test defect fixes) are shown with `if/else` paths. The final stage is the project close-out and post-implementation review.

@startuml  
skinparam sequenceParticipant underline false  
skinparam participantBorderColor \#000000  
skinparam participantBackgroundColor \#DDDDDD  
skinparam participantFontColor \#000000  
skinparam sequenceArrowColor \#000000  
skinparam sequenceBoxBackgroundColor \#EEEEEE

title AI-SDLC Program/Project Management Flow

actor "Senior Management" as SM  
participant "AI-IRB" as IRB  
participant "Project Sponsor" as PS  
participant "AI-PMO" as APMO  
participant "Product Manager" as ProdM  
participant "Program Manager" as PrgM  
participant "Project Manager" as PJM  
participant "Development" as Dev  
participant "Quality Assurance" as QA  
participant "Operations" as Ops  
participant "Tech Support" as TS

\== Project Initiation (G-12 to G-10) \==  
SM \-\> PS: Commission AI project, name Project Sponsor  
PS \-\> ProdM: Request preliminary business requirements  
ProdM \-\> PS: Provide business requirements draft  
PS \-\> IRB: if (High-Risk AI?) then consult AI-IRB  
activate IRB  
IRB \-\> PS: Provide guidance/approval or reduce scope  
deactivate IRB  
PS \-\> APMO: Summarize scope, cost, schedule  
APMO \-\> PJM: Provide resources/funding guidelines

\== Gate 10: Requirements Lock-Down \==  
PJM \-\> QA: Review final business requirements  
QA \-\> PJM: Approve or request changes  
SM \-\> PS: Final sign-off on scope  
PS \-\> PrgM: Confirm move to planning

\== Planning & Definition (G-10 to G-6) \==  
PJM \-\> Dev: Gather system requirements  
Dev \-\> QA: Share system requirements for feedback  
QA \-\> PJM: Provide quality plan input  
Ops \-\> PJM: Provide environment/infrastructure details  
PJM \-\> IRB: if (Revised AI scope) then IRB review  
IRB \-\> PJM: OK or rework  
PJM \-\> PS: Summarize final plan, schedule, cost

\== Gate 6: Project Lock-Down \==  
PS \-\> SM: Approve overall plan  
SM \-\> PS: Proceed with development

\== Development & Validation (G-6 to G-4) \==  
Dev \-\> Dev: Code & unit test AI modules  
Dev \-\> QA: Turn over to QA for integration test  
QA \-\> Dev: if (Defects) then fix  
note over Dev: Repeat until integration is stable  
end note

\== Gate 4: Begin Validation \==  
QA \-\> PS: Approve readiness for system test  
PS \-\> PrgM: Accept move to system test

\== System Test & UAT (G-4 to G-2) \==  
QA \-\> Dev: Perform system test  
QA \-\> Dev: Log defects, retest fixes  
Dev \-\> QA: Provide fixed builds  
note over QA: Once tests pass, or partial pass  
end note  
ProdM \-\> TS: Prepare user acceptance test plan  
TS \-\> ProdM: Execute UAT with end-users  
TS \-\> Dev: if (UAT defects) fix  
note over Dev: Cycle until UAT passes  
end note

\== Gate 2: Begin FOA/Beta \==  
ProdM \-\> TS: Deploy pilot version  
TS \-\> ProdM: Evaluate user feedback

\== FOA/Beta & Deployment (G-2 to G-0) \==  
Dev \-\> Ops: Provide final build  
Ops \-\> TS: if (Training needed) deliver training  
TS \-\> QA: Final checks  
QA \-\> PS: Confirm final readiness

\== Gate 0: General Availability \==  
PS \-\> SM: Approve production rollout  
Ops \-\> All: Deploy to production environment  
All \-\> PJM: Project close-out  
PJM \-\> QA: Initiate post-implementation review

\== Post Implementation \==  
QA \-\> APMO: Gather lessons learned, finalize  
APMO \-\> IRB: if (Ethics improvements) track for next cycle

@enduml

**Diagram Description:** The diagram shows each major role as a swim lane and walks through the AI-SDLC program/project management stages, from initiation (where Senior Management commissions an AI project) through requirements gathering, AI-IRB consultation if high-risk AI is identified, formal gates (G-10, G-6, G-4, G-2, G-0), development and testing stages, final deployment, and post-implementation review. Decision points (notably around AI-IRB if the project is high risk, and during UAT and test defect fixes) are shown with `if/else` paths. The final stage is the project close-out and post-implementation review.

[image1]: ../diagrams/SOP-1000-01-AI.PNG
