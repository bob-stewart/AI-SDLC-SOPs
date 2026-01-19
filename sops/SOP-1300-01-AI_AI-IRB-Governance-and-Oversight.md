**SOP-1300-01-AI\_**AI-IRB-Governance-and-Oversight  
**Title:** AI-IRB Governance & Oversight

**![][image1]**

**Effective Date:** (Date of Implementation)  
**Supersedes:** None (New SOP)  
**Reason for Update:** Initial Release  
**Owner/Document Control:** AI Governance Office

---

## **Objective**

The objective of this Standard Operating Procedure (SOP) is to define and document the governance structure and oversight responsibilities of the AI Institutional Review Board (AI-IRB) within the AI-SDLC framework. This SOP outlines the processes by which the AI-IRB evaluates, approves, and monitors AI projects to ensure compliance with ethical, regulatory, and organizational requirements.

---

## **Scope**

This SOP applies to all AI initiatives under the jurisdiction of the AI-IRB, including internal product development, external client engagements, research collaborations, and any other AI/ML-based or data-driven endeavors. It also governs the oversight and ethical review of AI models, tools, or algorithms developed or integrated into the production environment by the Performing Organization (Engineering), Contracting Organization (Product/Technical Support), or external partners.

---

## **Applicability**

All personnel and functional areas—Development, Quality Assurance, Operations, Product, Technical Support, AI Governance Office, and Senior Management—are required to adhere to this SOP when proposing or modifying AI-based projects that fall within the AI-IRB’s purview.

---

## **References**

* **SOP-1000-01-AI**: Program/Project Management  
* **SOP-1003-01-AI**: Configuration Management  
* **SOP-1101-01-AI**: Training and Documentation  
* **SOP-1301-01-AI**: AI Bias & Fairness Evaluation (Placeholder if not finalized)  
* **SOP-1305-01-AI**: AI Ethical Risk & Impact Assessment (Placeholder if not finalized)  
* Applicable data protection laws and regulations (e.g., GDPR, CCPA)  
* Applicable AI ethical guidelines (e.g., IEEE standards, EU AI Act proposals)

---

## **Roles and Responsibilities**

| Role | Responsibility |
| ----- | ----- |
| **AI-IRB Chair** | \- Convenes AI-IRB meetings \<br/\> \- Coordinates reviews, ensures conformance to policies \<br/\> \- Approves final decisions |
| **AI-IRB Members** | \- Expert panelists across technical, legal, ethical, operational domains \<br/\> \- Review project proposals, voice concerns, provide recommendations |
| **Project Sponsor** | \- Submits project proposal to AI-IRB \<br/\> \- Addresses feedback/revisions required \<br/\> \- Ensures resources for compliance |
| **AI Governance Office** | \- Maintains repository of AI-IRB decisions \<br/\> \- Tracks open items and follow-ups \<br/\> \- Communicates policy updates |
| **Engineering Dept.** | \- Implements required modifications from AI-IRB \<br/\> \- Submits technical artifacts, ensures compliance with recommendations |
| **Product/Tech Support** | \- Provides user and client perspective \<br/\> \- Coordinates training and user documentation with AI-IRB guidelines |
| **Operations** | \- Implements changes into production environments \<br/\> \- Maintains logs/evidence of compliance post-release |
| **Senior Management** | \- Confirms alignment of AI-IRB with strategic direction \<br/\> \- Resolves escalated issues or cross-organizational conflicts |

---

## **Procedure Activities**

1. **AI-IRB Setup and Membership**  
   * The AI Governance Office appoints the AI-IRB Chair in consultation with Senior Management.  
   * The Chair nominates AI-IRB Members with diverse expertise (ethical, technical, legal).  
   * AI-IRB membership is reviewed annually to maintain independence and diversity of opinions.  
2. **Project Proposal Submission**  
   * The Project Sponsor completes the **AI-IRB Project Proposal Form** describing project scope, objectives, data usage, ethical considerations, and potential impact.  
   * The Project Sponsor submits the form to the AI-IRB Chair at least two weeks before the next scheduled meeting.  
   * The AI-IRB Secretary (delegated by Chair or AI Governance Office) logs the proposal, assigns a reference number, and distributes it to AI-IRB Members.  
3. **Preliminary Screening**  
   * The AI-IRB Chair designates one or more primary reviewers based on subject matter expertise.  
   * Primary reviewers perform an initial analysis:  
     * Data privacy compliance (GDPR, CCPA, etc.)  
     * Risk classification (low, medium, high)  
     * Potential biases (training data, model approach)  
     * Ethical risk & impact assessment readiness (SOP-1305-01-AI if applicable)  
   * If the preliminary analysis reveals major gaps, the AI-IRB Chair requests clarifications from the Project Sponsor.  
4. **AI-IRB Meeting and Discussion**  
   * The AI-IRB convenes periodically or on-demand (for high-priority projects).  
   * The Project Sponsor presents the project proposal with relevant stakeholders (Engineering, Product, etc.).  
   * AI-IRB Members discuss potential concerns, ask clarifying questions, and highlight risk areas (e.g., bias, transparency, or safety).  
5. **Decision and Post-Meeting Actions**  
   * The AI-IRB Chair calls for a decision based on the panel’s discussion. Potential outcomes:  
     * **Approval** (with or without minor conditions)  
     * **Deferred** (requires additional info or rework)  
     * **Rejection** (project not viable within current constraints)  
   * The AI Governance Office documents the decision and any conditions.  
   * The Project Sponsor receives official AI-IRB feedback within two business days.  
6. **Tracking and Follow-up**  
   * The AI-IRB’s conditions (if any) must be addressed before the next milestone.  
   * The Engineering Dept. implements changes or mitigations.  
   * The Project Sponsor re-submits an updated proposal or relevant artifacts for final sign-off.  
   * The AI Governance Office updates the master AI-IRB Decision Registry, logs open items, and sets review timelines.  
7. **Deployment Clearance**  
   * Once the project is near completion in the AI-SDLC, the AI-IRB rechecks if all conditions are met.  
   * If satisfied, the AI-IRB issues a formal letter or email clearing the model/project for deployment.  
   * Operations, with QA oversight, then proceeds with final release steps (SOP-1220-01 Deployment).  
8. **Post-Implementation Review**  
   * The AI-IRB and the AI Governance Office schedule a post-implementation check (30–90 days post-launch).  
   * Observed metrics (model performance, real-world ethical or bias issues, user feedback) are compiled.  
   * Lessons learned feed back into future AI-IRB guidelines and best practices.  
9. **Annual Review / Ongoing Oversight**  
   * High-risk or critical AI systems require periodic re-review.  
   * The AI-IRB may request updated documentation or performance metrics to ensure ongoing compliance.  
   * Non-compliance or unaddressed concerns can trigger corrective actions or suspension of AI system usage.

---

## **Forms / Templates**

1. **AI-IRB Project Proposal Form**  
2. **AI-IRB Decision Registry**  
3. **Change Request / Mitigation Worksheet**

---

## **Metrics**

* **Review Cycle Time**: Number of days from proposal submission to AI-IRB final decision.  
* **Rework Rate**: Percentage of proposals requiring major re-submissions.  
* **Compliance Rate**: Percentage of approved AI projects that meet AI-IRB conditions by the next milestone.  
* **Post-Implementation Issues**: Number of ethical or compliance issues flagged within 90 days of launch.

---

## **Records and Archiving**

* All AI-IRB decisions and final approvals are stored in the AI Governance Office’s secure repository, referencing the project code.  
* Meeting minutes and any re-submissions are kept on file for auditing purposes for at least five years or in compliance with specific regulatory requirements.

---

## **Exemptions**

* Projects or research exempted by external regulatory or client constraints must still notify the AI-IRB.  
* Exemption decisions rest with the AI-IRB Chair, documented in writing.

---

## **Tools/Software/Technology Used**

* **AI-IRB Decision Registry**: Central repository or database tracking all decisions.  
* **AI Ethical Risk & Impact Assessment Tool** (SOP-1305-01-AI).  
* **Issue Tracking System** (e.g., JIRA or SQA Manager) for open items.

---

## **Change History**

| Version | Date | Description | Author/Change Owner |
| ----- | ----- | ----- | ----- |
| 1.0 | (EffectiveDate) | Initial Release | AI Governance Office |
| 1.1 | TBD | N/A | N/A |

---

## **Approval Signatures**

* **AI-IRB Chair:** *Signature/DateSignature / DateSignature/Date*  
* **CTO / Senior Management:** *Signature/DateSignature / DateSignature/Date*  
* **AI Governance Office Head:** *Signature/DateSignature / DateSignature/Date*

**End of SOP**

@startuml

' Define participants (Roles)  
participant "Project Sponsor" as PS  
participant "AI-IRB Chair" as CHAIR  
participant "AI-IRB Members" as MEMBERS  
participant "AI Governance Office" as GOV  
participant "Engineering Dept." as ENG  
participant "Product/Tech Support" as PTS  
participant "Operations" as OPS  
participant "Senior Management" as SM

' 1\. Project proposal submission  
PS \-\> CHAIR: Submits AI-IRB Project Proposal Form  
CHAIR \-\> MEMBERS: Distribute proposal for initial screening

alt Major gaps identified  
  CHAIR \-\> PS: Request clarifications/further info  
else Sufficient detail  
  MEMBERS \-\> MEMBERS: Perform preliminary analysis (data privacy, risk classification, etc.)  
end

' 2\. AI-IRB Meeting  
CHAIR \-\> CHAIR: Schedule AI-IRB meeting  
CHAIR \-\> PS: Invite Project Sponsor to present  
PS \-\> MEMBERS: Present project scope, objectives, data usage

' 3\. Deliberation  
MEMBERS \-\> CHAIR: Discuss concerns, recommendations  
CHAIR \-\> GOV: Record meeting minutes/decision notes

' 4\. Decision outcomes  
alt Approved  
  CHAIR \-\> PS: Notifies approval (with or without conditions)  
else Deferred  
  CHAIR \-\> PS: Notifies deferral; rework required  
else Rejected  
  CHAIR \-\> PS: Notifies rejection  
end

' 5\. Tracking conditions and follow-up  
PS \-\> ENG: Address AI-IRB conditions / implement changes  
ENG \-\> PS: Provide updated compliance or revised proposal  
PS \-\> CHAIR: Submit revised artifacts if needed

' 6\. Final sign-off  
CHAIR \-\> MEMBERS: Final review of revised submission  
MEMBERS \-\> CHAIR: Confirm readiness  
CHAIR \-\> GOV: Update Decision Registry

' 7\. Deployment clearance  
CHAIR \-\> OPS: Issue formal clearance for deployment (if all conditions met)  
OPS \-\> CHAIR: Confirms release scheduling  
CHAIR \-\> PTS: Coordinate end-user training, if needed

' 8\. Post-implementation  
GOV \-\> CHAIR: Schedule post-implementation check (\~30-90 days)  
CHAIR \-\> MEMBERS: Evaluate real-world metrics, performance  
alt Non-compliance detected  
  CHAIR \-\> SM: Escalate major concerns for executive resolution  
else All in compliance  
  note right  
    Project remains in good standing under AI-IRB oversight  
  end note  
end

@enduml

**Short textual explanation:**  
This sequence diagram illustrates how the AI-IRB Governance & Oversight process unfolds under SOP-1300-01-AI. The Project Sponsor submits a proposal to the AI-IRB Chair, who distributes it to members for initial screening. Following an AI-IRB meeting, members deliberate and issue a decision (approve, defer, or reject). If approved or deferred, the Engineering and Sponsor teams address required conditions, resubmit for final sign-off, and proceed to deployment clearance. A post-implementation review is scheduled to monitor compliance and address any non-compliance issues.

[image1]: ../diagrams/SOP-1300-01-AI.PNG