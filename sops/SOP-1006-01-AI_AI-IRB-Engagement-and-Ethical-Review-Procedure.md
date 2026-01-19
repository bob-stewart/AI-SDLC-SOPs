**SOP-1006-01-AI\_**AI-IRB-Engagement-and-Ethical-Review-Procedure  
[Mind Matrix Home](../AI_Mind_Matrix.md) | [SOP Index](../SOP_Index.md)

**Title:** AI-IRB Engagement and Ethical Review Procedure

![][image1]

**Effective Date:** *{Effective Date}*  
**Previous Version:** None  
**Reason for Update:** New SOP (AI-SDLC Context)  
**Owner:** *{Role or Department Owning This SOP}*  
**Location:** *{Repository/Location Reference}*  
**Signature/Date:** *{Signatory and Date}*

---

## **1\. Purpose**

This Standard Operating Procedure (SOP) defines the process for engaging with an AI Institutional Review Board (AI-IRB) or equivalent ethical/regulatory oversight body when developing, testing, and deploying AI-related features or products. The AI-IRB Engagement and Ethical Review Procedure ensures that all AI system components comply with regulatory, ethical, and data-handling requirements before proceeding through each phase of the AI Systems Development Life Cycle (AI-SDLC).

## **2\. Scope**

* **Applies To:**  
  * All AI-related projects and enhancements within the organization that involve potential human, organizational, or data risk requiring IRB or ethics committee oversight.  
  * Any AI subsystem or third-party integration that processes or produces output relevant to personal, sensitive, or regulated data.  
* **Exclusions:**  
  * Projects not involving AI or advanced analytics.  
  * Minor updates to AI models that have previously been deemed non-material by AI-IRB (subject to local IRB guidelines).

## **3\. Definitions and Acronyms**

* **AI-IRB (Institutional Review Board for AI):** An oversight body responsible for ethical risk assessment and governance for AI-related systems or features.  
* **AI-SDLC (AI Systems Development Life Cycle):** The set of phases and activities that guide the development, testing, deployment, and maintenance of AI systems.  
* **Ethical Review Dossier:** A formal document detailing the AI system’s purpose, data usage, potential risks, intended benefits, and mitigation strategies.  
* **Risk Level Classification:** The process to categorize AI projects into risk tiers (e.g., Low, Medium, High) based on potential ethical, privacy, or safety impacts.
* **Authorized AI Agent:** AI entities or subroutines officially sanctioned by the AI-IRB to perform autonomous or semi-autonomous tasks within the scope of this procedure.

## **4\. Roles and Responsibilities**

Below is a summary of the key roles involved in this procedure:

| Role | Responsibility |
| ----- | ----- |
| **AI-IRB Liaison** | Acts as the primary point of contact between project teams and the AI-IRB. Manages scheduling, submissions, and clarifications. |
| **Project Sponsor** | Ensures overall compliance with business objectives; has final sign-off on budgets and resources for AI-IRB compliance. |
| **Project Manager** | Coordinates project activities; ensures IRB tasks and requirements are integrated into the project plan and timeline. |
| **Development Team** | Provides technical details, risk assessments, and addresses IRB-related feedback on design, code, or data usage. |
| **Quality Assurance (QA)** | Ensures that all IRB-imposed constraints are tested and verified; reviews AI system logs or test results for compliance gaps. |
| **Operations** | Implements environment or infrastructure updates driven by IRB concerns; ensures safe data handling and disposal. |
| **Legal/Compliance** | Advises on regulatory implications; reviews any changes needed in data or usage agreements. |

## **5\. Metrics**

To gauge the effectiveness of the AI-IRB Engagement and Ethical Review Procedure, the following metrics are tracked:

1. **IRB Submission Cycle Time:**  
   * *Definition:* Average time from initial IRB request to IRB approval or conditional acceptance.  
   * *Target:* ≤ 3 weeks for standard requests (longer if high-risk).  
2. **Conditional Approvals vs. Direct Approvals:**  
   * *Definition:* Ratio of IRB submissions that return with conditions or modifications required vs. direct approvals.  
   * *Target:* Continuous reduction of conditional approvals, aiming for \< 30% conditional rate.  
3. **Number of Revisions Requested by AI-IRB:**  
   * *Definition:* Average number of revision cycles required by the IRB.  
   * *Target:* Limit to 1–2 cycles on average, reflecting effective pre-submission clarity.  
4. **Compliance Incidents Post-Deployment:**  
   * *Definition:* Count of compliance or ethical complaints after general availability of an AI feature.  
   * *Target:* Zero serious non-compliance findings post-release.

## **6\. Procedure Activities**

### **6.1 Initiate AI-IRB Engagement**

1. **Project Manager** identifies AI aspects (use of personal data, new data sets, potential bias, and recursive self-improvement subroutines) that may require IRB oversight.  
2. **Project Manager** notifies the **AI-IRB Liaison**, providing a summary:  
   * Project scope, timeline, and risk classification (if known).  
   * Proposed approach or model type and data usage.  
3. **AI-IRB Liaison** advises on next steps: full IRB submission or preliminary consultation.

### **6.2 Prepare Ethical Review Dossier**

1. **Development Team** and **Project Manager** compile or update the Ethical Review Dossier, including:  
   * Data flow diagrams, model design details, potential biases, privacy considerations, and user impact.  
   * Proposed risk mitigation strategies.  
2. **QA** performs a preliminary quality check to ensure completeness of the dossier.  
3. **AI-IRB Liaison** schedules an IRB meeting or submission date.

### **6.3 Submit to AI-IRB**

1. **AI-IRB Liaison** formally submits the dossier and supporting docs.  
2. **AI-IRB** acknowledges receipt and provides an expected review timeframe.  
3. **Project Manager** updates the AI-SDLC plan to reflect IRB review milestones.

### **6.4 AI-IRB Review and Feedback**

1. **AI-IRB** examines project documentation, focusing on:  
   * Ethical risk classification (e.g., low, medium, high).  
   * Data usage, privacy, and security compliance.  
   * Potential bias or harm.  
   * Proposed model interpretability and oversight.  
2. **AI-IRB** issues one of the following:  
   * **Approved** (no further changes required).  
   * **Cond. Approved** (conditions to be addressed).  
   * **Rejected** (significant concerns or insufficient data).

### **6.5 Respond to AI-IRB Conditions or Rejections**

If **Cond. Approved** or **Rejected**:

1. **Project Manager** organizes a discussion with the **Development Team** and possibly **Legal/Compliance** to interpret IRB feedback.  
2. **Development Team** revises design or documents.  
3. **Quality Assurance** ensures updated design or documentation meets IRB conditions.  
4. **AI-IRB Liaison** resubmits updated materials or clarifications.

### **6.6 Final IRB Approval**

1. Once final approval is granted, **AI-IRB Liaison** notifies the entire project team.  
2. **Project Manager** logs IRB status in the project’s official records.  
3. Implementation or testing gates dependent on IRB approval are unlocked, allowing further phases to proceed.

### **6.7 Post-Approval Oversight**

1. **Project Manager** ensures any IRB-imposed limitations or monitoring duties are integrated into the project plan (e.g., ongoing bias checks).  
2. **Operations** implements any mandated technical controls (data retention or disposal schedules, access controls).  
3. **Quality Assurance** monitors compliance with IRB directives, escalates any potential compliance issues.

### **6.8 Post-Deployment Monitoring**

1. **Project Manager** organizes periodic reviews, as mandated by IRB, to confirm ongoing compliance.  
2. **AI-IRB Liaison** may request usage logs or updated performance/bias metrics for IRB’s continuing review, including **Exochain Peer Reviews** of agent-originated code.  
3. **Development Team** addresses new issues found in real-world use (e.g., emergent bias) with additional IRB consultations if needed.

### **6.9 Post Implementation Review**

After the system is fully deployed and stable:

1. **Project Manager** hosts a post-implementation review focusing on IRB processes, ethical compliance, and lessons learned.  
2. **Quality Assurance** compiles metrics (incident reports, additional user feedback).  
3. **AI-IRB Liaison** documents final summary for the IRB, including improvements for future AI projects.

## **7\. Forms**

* **Ethical Review Dossier Template** – used by Development Team and Project Manager to compile details for IRB submission.  
* **AI-IRB Submission Cover Form** – top-level summary for AI-IRB, referencing the Dossier.  
* **Post Implementation Review Checklist** – outlines final compliance check items.

## **8\. Exemptions**

* Rapid fixes that do not significantly alter data usage or risk profile may bypass a formal IRB re-submission if previously authorized by the IRB under known minor-change provisions.  
* Projects entirely outside AI scope with no user or data risk.

## **9\. Tools/Software/Technology Used**

* **Document Repository** (e.g., SharePoint, Confluence) for storing IRB forms and confirmations.  
* **Project Management Tool** (e.g., Jira, Azure DevOps) with IRB-specific issue types or tasks.  
* **Version Control** (e.g., Git) with a separate branch for IRB-stipulated changes.  
* **Automated Testing** frameworks that can incorporate IRB-driven constraints or data usage checks.

---

### **Revision History**

| Version | Date | Author | Change/Reason |
| ----- | ----- | ----- | ----- |
| 1.0 | *{Date}* | *{Name/Dept}* | Initial release. |
| 1.1 | *{Date}* | *{Name/Dept}* | *{Reason for update}* |

**END OF SOP-1006-01-AI**

@startuml  
title SOP-1006-01-AI: AI-IRB Engagement and Ethical Review Sequence

participant "Project Manager" as PM  
participant "AI-IRB Liaison" as LIAISON  
participant "AI-IRB" as IRB  
participant "Development Team" as DEV  
participant "Quality Assurance" as QA  
participant "Operations" as OPS  
participant "Legal/Compliance" as LEGAL

PM \-\> PM: Identify AI aspects needing IRB oversight  
PM \-\> LIAISON: Notify about potential AI-IRB review  
LIAISON \-\> LIAISON: Determine if full submission or consult  
note right  
  LIAISON advises next steps for formal IRB  
  submission or preliminary consultation  
end note

PM \-\> DEV: Collect technical/data details for Ethical Review Dossier  
PM \-\> QA: Request preliminary check of dossier completeness  
QA \-\> PM: Confirm dossier ready for submission

PM \-\> LIAISON: Submit final Ethical Review Dossier to IRB  
LIAISON \-\> IRB: Forward dossier and supporting docs

IRB \-\> IRB: Examine project doc & assess risk  
IRB \-\> LIAISON: Provide review outcome  
alt Approved  
  LIAISON \-\> PM: Notifies final IRB approval  
  PM \-\> QA: Mark IRB-based tasks complete  
else "Cond. Approved"  
  LIAISON \-\> PM: Shares IRB conditions  
  PM \-\> LEGAL: (If needed) Clarify conditions or regulatory constraints  
  PM \-\> DEV: Adjust design per conditions  
  DEV \-\> QA: Confirm updated design meets IRB demands  
  QA \-\> LIAISON: Resubmit for IRB sign-off  
  IRB \-\> LIAISON: Final approval  
  LIAISON \-\> PM: Notifies IRB approval  
else "Rejected"  
  LIAISON \-\> PM: Shares IRB rejection  
  PM \-\> DEV: Major revision or additional data  
  DEV \-\> QA: Validate reworked approach  
  QA \-\> LIAISON: Resubmit to IRB  
  IRB \-\> LIAISON: Final decision  
  LIAISON \-\> PM: If approved, proceed  
end

PM \-\> OPS: Implement IRB-mandated technical controls  
QA \-\> QA: Monitor compliance with IRB directives

PM \-\> DEV: Proceed with development/test gates (unlocked)  
PM \-\> PM: Plan post-approval oversight (scheduled checks)  
OPS \-\> PM: Provide logs or metrics for ongoing IRB reviews  
PM \-\> LIAISON: Provide updates to IRB, if required

PM \-\> PM: Conduct post-deployment review  
PM \-\> QA: Gather metrics on compliance/ethical usage  
PM \-\> LIAISON: Prepare final IRB summary and lessons learned

@enduml

**Short textual explanation:** This sequence diagram shows how an AI project team engages with an AI-IRB, from identifying the need for IRB review to preparing an Ethical Review Dossier, handling IRB feedback (approval, conditional, or rejection), implementing final requirements, and conducting post-deployment oversight.

[image1]: ../diagrams/SOP-1006-01-AI.PNG