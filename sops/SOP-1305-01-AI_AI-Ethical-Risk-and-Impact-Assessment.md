**SOP-1305-01-AI\_AI-Ethical-Risk-and-Impact-Assessment**

**![][image1]**  
**Title**: AI Ethical Risk & Impact Assessment  
**Effective Date**: (Date of Effect)  
**Previous Version**: None  
**Reason for Update**: New SOP  
**Owner**: AI Governance Office (AIGO)  
**Approved By**: (Name/Title/Signature/Date)  
---

**1\. Purpose**  
This SOP describes the structured approach for conducting Ethical Risk & Impact Assessments (ERIA) for AI systems across their lifecycle. It ensures that ethical considerations, potential societal impacts, and regulatory requirements are integrated into the AI System Development Life Cycle (AI-SDLC), overseen by the AI-IRB (Institutional Review Board).  
---

**2\. Scope**  
This procedure applies to all AI initiatives within the organization that require an ethical risk assessment, specifically any AI project proposed, in development, undergoing modifications, or operating in production. It covers:

* Identification of potential ethical, social, and legal risks.  
* Impact analysis on stakeholders, including vulnerable populations.  
* Documentation and approval of risk mitigation measures.

---

**3\. Applicability**  
All staff members—particularly AI Development, Data Scientists, Project Managers, and the AI Governance Office—must comply with this SOP whenever an AI solution is introduced, updated, or repurposed. The AI-IRB must be consulted if deemed necessary by scope or policy.  
---

**4\. Definitions**

| Term | Definition |
| ----- | ----- |
| **AI-IRB** | The institutional review board that governs and ensures ethical compliance for AI-related projects. |
| **AI Governance Office (AIGO)** | Central body responsible for AI oversight, ensuring adherence to policies, ethics, and regulations. |
| **ERIA** | Ethical Risk & Impact Assessment, a structured process for evaluating potential ethical and societal risks. |
| **Stakeholder** | Any entity (individual, group, organization) affected or potentially impacted by the AI system. |
| **Risk Mitigation Strategy** | Defined approach to reduce or eliminate identified risks. |

---

**5\. Responsibilities**

* **AI Governance Office (AIGO)**  
  * Facilitates, reviews, and approves the ethical risk assessment process.  
  * Coordinates communications among all stakeholders and the AI-IRB.  
* **Project Manager**  
  * Ensures the ERIA is initiated early in the project lifecycle and integrated into the project plan.  
* **Data Scientist/Engineer**  
  * Supplies technical details for risk identification.  
  * Provides data usage specifics, including source reliability and data privacy considerations.  
* **Risk Management**  
  * Assesses identified ethical risks, proposes or validates mitigation strategies, and monitors risk evolution.  
* **Quality Assurance**  
  * Reviews ERIA documentation, checks compliance with relevant standards, and verifies the effectiveness of mitigation steps.  
* **AI-IRB**  
  * Provides final ethical oversight and approval based on ERIA findings.

---

**6\. Procedure Activities**  
**6.1 Initiation of Ethical Risk & Impact Assessment**

1. **Trigger**: The Project Manager (PM) triggers an ERIA once an AI project or significant update is proposed.  
2. **Request**: The PM notifies the AI Governance Office (AIGO) and Risk Management of the need for an ERIA, providing project scope, data usage, and intended outcomes.

**6.2 Conduct Preliminary Risk Identification**

1. **Gather Information**: Data Scientist/Engineer compiles system design specs, data sources, model architecture, and any user/stakeholder data.  
2. **Identify Stakeholders**: PM and AIGO identify all impacted stakeholders (end-users, clients, broader society).  
3. **Risk Brainstorm**: AIGO, Data Scientist, and Risk Management lead a structured brainstorming session to identify potential ethical hazards, biases, and data privacy issues.

**6.3 Risk Classification & Documentation**

1. **Classify Risks**: Each risk item is assigned a severity level (Low, Medium, High, Critical) based on potential harm.  
2. **Ownership**: PM assigns a risk owner (Data Scientist, Developer, or Operations) for each risk.  
3. **Draft ERIA Document**: AIGO compiles all discovered risks, assumptions, potential mitigations, and references relevant SOPs (e.g., SOP-1301-01-AI for bias).

**6.4 Propose Mitigation Strategies**

1. **Mitigation Plans**: Risk owners propose actionable steps (technical or procedural) to reduce or eliminate ethical concerns.  
2. **Review**: Risk Management reviews these strategies for feasibility and completeness.  
3. **Update ERIA**: The documented plan is revised to include accepted mitigations and an implementation timeline.

**6.5 Evaluation and Approval**

1. **Internal Validation**: Quality Assurance evaluates the completeness of the ERIA, ensuring it addresses relevant compliance and regulatory guidelines.  
2. **Submission to AI-IRB**: AIGO sends the final ERIA to the AI-IRB for ethical oversight and sign-off.  
3. **IRB Decision**: AI-IRB either approves, requests clarification, or rejects the ERIA.  
   * If clarification is needed, the ERIA is updated, and the process repeats.  
   * If rejected, the project must undergo significant revision.

**6.6 Monitoring & Reassessment**

1. **Implementation**: Upon IRB approval, the project proceeds with implementing the mitigation strategies.  
2. **Periodic Review**: Risk owners and AIGO monitor metrics indicating ethical or societal impact.  
3. **Trigger Reassessment**: If new data sources or model changes occur, or if a risk threshold is exceeded, a new or updated ERIA is mandatory.

**6.7 Records and Reporting**

1. **Record Maintenance**: The PM ensures the final ERIA document is stored in the project repository.  
2. **Reporting**: AIGO regularly reports on the status of ethical risks and mitigation effectiveness to senior leadership, the AI-IRB, and any relevant regulators.  
3. **Lessons Learned**: At project closure or major milestone, a “lessons learned” summary is compiled and integrated into future risk frameworks.

---

**7\. Forms**

* **Ethical Risk & Impact Assessment Template**  
* **Risk Mitigation Planning Form**  
* **AI-IRB Submission Form**

---

**8\. Records Management**  
All ERIA-related documents (electronic or hard-copy) are controlled under SOP-2002-01 for Quality Records. The PM or delegate must maintain accurate, accessible records for audit or compliance reviews.  
---

**9\. References**

* **SOP-1300-01-AI: AI-IRB Governance & Oversight**  
* **SOP-1301-01-AI: AI Bias & Fairness Evaluation**  
* **SOP-1302-01-AI: AI Explainability & Model Transparency**  
* **SOP-1303-01-AI: AI Data Protection & Privacy**  
* **ISO 31000: Risk Management – Guidelines**  
* **IEEE 7000 Series – Ethics in AI**

---

**10\. Revision History**

| Version | Date | Summary of Changes | Author/Change Owner |
| ----- | ----- | ----- | ----- |
| 1.0 | (EffectiveDate) | Initial release of SOP-1305-01-AI | AI Governance Office |

---

**SOP-1305-01-AI: AI Ethical Risk & Impact Assessment**

@startuml  
participant "Project Manager" as PM  
participant "Data Scientist" as DS  
participant "Risk Management" as RM  
participant "AI Governance Office" as AIGO  
participant "Quality Assurance" as QA  
participant "AI-IRB" as IRB

PM \-\> PM: Recognize new AI project requires ERIA  
PM \-\> DS: Request project scope & technical details  
DS \--\> PM: Provide design specs, data usage, model summary

PM \-\> AIGO: Initiate Ethical Risk & Impact Assessment  
AIGO \-\> DS: Request expanded technical clarifications  
DS \--\> AIGO: Submit data sources & architecture details

AIGO \-\> RM: Begin risk identification brainstorm  
RM \-\> RM: Compile potential ethical or data privacy hazards  
RM \-\> PM: Provide initial risk classification (Low/Med/High/Critical)

PM \-\> AIGO: Draft ERIA document with identified risks  
AIGO \-\> RM: Request recommended mitigation strategies  
RM \--\> AIGO: Provide actionable steps for risk mitigation

AIGO \-\> QA: Submit ERIA for internal validation  
QA \-\> QA: Validate completeness and regulatory compliance  
QA \--\> AIGO: Validation complete

AIGO \-\> IRB: Submit final ERIA for oversight  
alt IRB requests clarification  
  IRB \-\> AIGO: Clarifications needed  
  AIGO \-\> PM: Update ERIA with clarifications  
  PM \-\> IRB: Resubmit revised ERIA  
else IRB rejects ERIA  
  IRB \-\> PM: Rejection, substantial revision required  
end

alt IRB approves  
  IRB \-\> PM: ERIA approved  
  PM \-\> AIGO: Proceed with implementing mitigation plan  
  AIGO \-\> RM: Begin continuous monitoring and reassessment  
else no further action  
end

@enduml

**Short textual explanation**:  
This sequence diagram illustrates how a project manager initiates an Ethical Risk & Impact Assessment for a new AI project, coordinates with data scientists for technical details, and collaborates with risk management to identify and classify ethical risks. The AI Governance Office compiles a comprehensive ERIA document, which quality assurance validates. Finally, the AI-IRB reviews, possibly requests clarifications, and either rejects or approves. If approved, mitigation strategies are implemented and continuously monitored.

[image1]: ../diagrams/SOP-1305-01-AI.PNG