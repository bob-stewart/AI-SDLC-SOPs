# **SOP-1040-01-AI\_Requirements-Definition**

# **![][image1]**

# **Title: Requirements Definition**

**Version:** 1.0  
**Effective Date:** *2025-01-30*  
**Approved By:** Chief Technology Officer (CTO), AI IRB Chair  
**Scope:** Enterprise-Wide AI/ML Projects

---

**[Mind Matrix: Navigation](file:///Users/bobstewart/dev/AI-SDLC-SOPs/sops/SOP-1000-01-AI_Mind-Matrix-Governance-Navigation-Hub.md)**  

## **1\. Purpose**

This Standard Operating Procedure (SOP) defines the process for **Requirements Definition** within the AI Systems Development Life Cycle (AI-SDLC). It ensures that all business, regulatory, ethical, and technical requirements for AI-related projects are systematically identified, analyzed, documented, and approved, including integration with the **AI Institutional Review Board (AI-IRB)** as needed.

---

## **2\. Scope**

This SOP applies to all AI-focused software and system development projects at the organization that require formal requirements capture. It addresses:

* Elicitation, analysis, documentation, and validation of requirements  
* Alignment with AI IRB guidelines for ethical, compliance, and risk considerations  
* Traceability from concept to design, development, and validation

All departments—Product Development, Engineering, Quality Assurance, Operations, Technical Support, and the AI IRB—must follow this SOP for any AI-related project or feature release that goes through the AI-SDLC.

---

## **3\. Roles and Responsibilities**

| Role | Responsibilities |
| ----- | ----- |
| **AI Project Sponsor** | Champions the project, obtains funding, and ensures high-level alignment with AI/ethical guidelines. |
| **AI IRB Liaison** | Reviews potential AI ethics impacts, organizes IRB reviews, ensures compliance with AI IRB directives. |
| **Product Manager** | Leads the business vision, compiles user/business requirements, and coordinates with AI IRB Liaison. |
| **AI Business Analyst** | Elicits, documents, and validates all business and user requirements with an AI lens. |
| **AI Data Scientist** | Advises on feasibility, data requirements, and defines **Model Validation Metrics** (e.g. F1, AUC) for acceptance. |
| **Quality Assurance (QA)** | Reviews requirements for testability, ensures acceptance criteria are well-defined and trackable. |
| **AI Ethics/Compliance** | Monitors regulatory, ethical, privacy, and fairness aspects in the requirement definitions. |
| **Operations** | Contributes operational, infrastructure, and deployment constraints or requirements. |
| **Technical Support** | Communicates user needs, logs known constraints, and receives training for future user support. |
| **Program Manager** | Oversees schedule, budget, resources, ensures synergy among cross-functional teams. |
| **Development** | Provides input on technical constraints and ensures feasibility for system or platform requirements. |

---

## **4\. Definitions**

* **AI-IRB**: An internal board that reviews AI solutions for ethical compliance, data governance, and potential biases.  
* **SOW** (*Statement of Work*): A high-level document that sets out the project scope, deliverables, acceptance criteria, and timeline.  
* **Business Requirements**: High-level objectives describing what the organization or customers seek from the AI solution.  
* **System Requirements**: Detailed functional and technical specifications for building AI/ML solutions, including data ingestion, model training/inference, performance metrics, and compliance.  
* **Ethical/Regulatory Requirements**: Requirements derived from AI IRB guidelines, data privacy laws, fairness, interpretability, or other compliance standards.
* **Authorized AI Agent**: A validated AI system or subsystem identified within the Mind Matrix as having the authority to execute specific SDLC or operational tasks. |

---

## **5\. Procedure Activities**

Below is the end-to-end procedure for AI Requirements Definition:

### **5.1 Initiate Requirements Definition**

1. **Project Sponsor**: Communicates project concept to **AI IRB Liaison** and obtains initial approval to proceed with scoping.  
2. **Program Manager**: Sets up the initial project record in AI-SDLC tracking system.  
3. **Product Manager**, **AI Business Analyst**, and **Lead Data Scientist**: Begin high-level business requirements and **Hypothesis Definition** drafting.

### **5.2 AI IRB Preliminary Review**

1. **AI IRB Liaison**: Evaluates if the project needs immediate AI IRB attention (sensitive data, high-risk use case).  
2. If needed, the Liaison convenes an **AI IRB** quick check.  
   * **If accepted**: proceed.  
   * **If clarifications**: revise scope.

### **5.3 Requirements Elicitation**

1. **AI Business Analyst**: Conducts interviews and workshops with stakeholders (Product Dev, Data Scientist, Ethics, Ops).  
2. **Technical Support**: Provides user feedback, prior incidents or requests relevant to this new AI project.  
3. **AI Data Scientist**: Outlines technical feasibility, data needs, possible AI approaches, constraints.  
4. **AI Ethics/Compliance**: Identifies any data governance or interpretability mandates, including specific controls for **recursive self-improvement subroutines**.  
5. Collate results into a **Draft Requirements Document** (business & system requirements).

### **5.4 Analyze & Document Requirements**

1. **AI Business Analyst**: Structures user stories or use cases, includes acceptance criteria for AI functionality, risk analyses (bias, drift).  
2. **Product Manager**: Confirms alignment with business goals, updates potential release timeline in the SOW.  
3. **Operations**: Validates any infrastructure or deployment constraints.  
4. **AI IRB Liaison**: Ensures compliance concerns are integrated.

### **5.5 Requirement Validation**

1. **Quality Assurance**: Reviews requirements for testability, completeness, and clarity; ensures acceptance criteria are unambiguous.  
2. **AI Data Scientist**: Double-checks feasibility for ML tasks, data availability.  
3. **AI Ethics/Compliance**: Final check for fairness, privacy, or regulatory concerns.  
4. **Operations**: Confirms readiness or calls out missing operational details.  
5. Organize a formal **Requirements Review Meeting** with all roles. Document any changes or clarifications.

### **5.6 Approve System Requirements**

1. **Product Manager**: Presents final system requirements to **Project Sponsor** and **AI IRB Liaison** for sign-off.  
2. **Project Sponsor**: Provides final authorization, acknowledging resource and schedule implications.  
3. **AI IRB Liaison**: Grants final ethical/regulatory acceptance if needed, utilizing **Exochain Peer Reviews** to verify governance adherence.  
4. **Program Manager**: Marks requirements “Locked-Down.” Further changes proceed via formal change control (SOP-ChangeCtrl).

### **5.7 Requirements Baselining & Next Steps**

1. **AI Business Analyst**: Publishes the baselined **Requirements Document** in the repository.  
2. **Program Manager**: Informs relevant teams that development/design can proceed, referencing the approved requirements.  
3. **Quality Assurance**: Prepares test strategy (SOP-1210) referencing these requirements.  
4. **Operations**: Begins refining capacity or infrastructure planning (SOP-1002) if new demands are discovered.

---

## **6\. References**

* **SOP-1000-AI**: Program/Project Management for AI  
* **SOP-1002-AI**: AI Capacity Management  
* **SOP-1041-AI**: Detail Design Procedure  
* **AI IRB Guidelines**: Organizational standard for ethically reviewing AI solutions

---

## **7\. Document Control**

| SOP Version | Date | Description | Approved By |
| ----- | ----- | ----- | ----- |
| 1.0 | *2025-01-30* | Initial release (AI-specific). | CTO, AI IRB Chair |

**Supersedes:** None  
**Retention:** Maintain this SOP and all subsequent versions for minimum 5 years after decommission of the AI system.

---

### **Revision History**

| Version | Revision Date | Summary of Changes | Author/Editor |
| ----- | ----- | ----- | ----- |
| 1.0 | *2025-01-30* | Initial AI-SDLC version | AI Governance Team |

---

**End of SOP-1040-01-AI**

@startuml  
title SOP-1040-01-AI: Requirements Definition (Sequence Diagram)

participant "AI Project Sponsor" as SPONSOR  
participant "AI IRB Liaison" as IRB  
participant "Program Manager" as PRM  
participant "Product Manager" as PDM  
participant "AI Business Analyst" as BA  
participant "AI Data Scientist" as DS  
participant "AI Ethics/Compliance" as ETH  
participant "Operations" as OPS  
participant "Quality Assurance" as QA  
participant "Technical Support" as TS  
participant "Development" as DEV

' Step 1: Sponsor Initiates Concept  
SPONSOR \-\> IRB: Present new AI project concept  
alt IRB requests clarifications  
  IRB \-\> SPONSOR: Clarification needed  
  SPONSOR \-\> IRB: Provide clarifications  
  IRB \-\> SPONSOR: Preliminary acceptance  
else IRB approves  
  IRB \-\> SPONSOR: Preliminary acceptance  
end

' Step 2: Program Manager sets up project record  
SPONSOR \-\> PRM: Notify of IRB acceptance  
PRM \-\> PDM: Request business requirements drafting  
PDM \-\> BA: Begin high-level requirements  
BA \-\> TS: Gather known user constraints  
TS \-\> BA: Provide user feedback

' Step 3: AI IRB Preliminary Review  
BA \-\> IRB: Submit early risk/ethical info  
alt IRB concerns  
  IRB \-\> BA: Adjust scope or data approach  
else IRB no concerns  
  IRB \-\> BA: Proceed  
end

' Step 4: Requirements Elicitation  
BA \-\> DS: Confirm ML feasibility, data needs  
DS \-\> ETH: Flag any data privacy or fairness issues  
ETH \-\> BA: Provide compliance requirements  
OPS \-\> BA: Provide operational constraints  
BA \-\> BA: Draft Requirements Document

' Step 5: Analyze & Document  
BA \-\> QA: Request testability review  
QA \-\> BA: Review acceptance criteria  
BA \-\> PDM: Validate alignment with business goals  
PDM \-\> BA: Confirm timeline in SOW  
BA \-\> OPS: Confirm operational details

' Step 6: Requirements Validation  
QA \-\> DS: Check feasibility & data readiness  
DS \-\> QA: Acknowledge feasibility  
ETH \-\> BA: Check final ethics/regulatory compliance  
BA \-\> IRB: If big changes, re-check compliance  
OPS \-\> BA: Confirm final environment constraints  
BA \-\> BA: Prepare final version for sign-off

' Step 7: Approve System Requirements  
BA \-\> SPONSOR: Present final requirements  
SPONSOR \-\> IRB: Final ethical sign-off (if required)  
alt IRB sign-off needed  
  IRB \-\> SPONSOR: IRB approval  
end  
SPONSOR \-\> PRM: Approve & lock down scope  
PRM \-\> DEV: Communicate “Locked-Down” requirements

@enduml

**Short textual explanation:** This sequence diagram walks through the SOP-1040-01-AI requirements-definition process. It begins with the **AI Project Sponsor** presenting the new AI concept to the **AI IRB Liaison**, proceeds through the **Program Manager** setting up the project, and then details the roles (**Business Analyst**, **Data Scientist**, **Ethics**, **Operations**, **Quality Assurance**, etc.) collaborating on eliciting, analyzing, and validating requirements. Finally, the **Sponsor** and **AI IRB** give final sign-off on the “locked-down” requirements.

[image1]: ../diagrams/SOP-1040-01-AI.PNG