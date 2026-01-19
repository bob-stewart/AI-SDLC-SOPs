# **SOP-1301-01-AI\_AI-Bias-and-Fairness-Evaluation**

**![][image1]**

**Effective Date:** (Insert Effective Date)  
**Previous Version:** None  
**Reason for Update:** New SOP for AI Bias & Fairness Evaluation  
**Owner:** Chief AI Officer (CAIO)  
**Location:** (Insert Controlled Document Repository Location)

---

## **Objective**

The purpose of this Standard Operating Procedure (SOP) is to establish a robust, standardized process for identifying, monitoring, and mitigating bias in AI systems developed or deployed within the organization. The SOP ensures that fairness considerations are consistently integrated into every phase of the AI Systems Development Life Cycle (AI-SDLC), thereby enhancing trust, compliance, and ethical alignment with regulatory requirements, including those mandated by the AI-IRB (Artificial Intelligence Institutional Review Board).

---

## **Scope**

* **Applies To:**  
  * All AI projects under the organization’s AI-SDLC framework.  
  * Any system or feature that leverages machine learning, deep learning, or advanced analytics.  
  * AI solutions developed, acquired, or integrated through third parties.  
* **Exclusions:**  
  * Traditional software solutions without ML/AI components, unless these systems significantly interact with AI modules.

---

## **Applicable To**

* **AI-IRB Chair & Members**: Provide governance oversight on bias/fairness protocols, review the Bias & Fairness Evaluation results.  
* **AI Governance Office**: Ensures compliance with organizational policies, coordinates bias/fairness audits, and maintains documentation.  
* **Project Sponsors / Product Owners**: Initiate and sponsor AI projects, accountable for ensuring bias mitigation is addressed in project scope.  
* **Data Scientists / ML Engineers**: Carry out the technical steps for bias detection, measurement, and mitigation.  
* **Quality Assurance (QA)**: Conduct independent bias checks, validate results, and ensure all methods align with quality standards.  
* **Operations / Deployment Team**: Incorporate final bias mitigation strategies into production systems.  
* **Technical Support**: Monitor customer feedback or reports indicating biased outcomes, feed into the bias re-evaluation loop.

---

## **References**

* **SOP-1300-01-AI**: AI-IRB Governance & Oversight  
* **SOP-1003-01-AI**: Configuration Management  
* **SOP-1210-01**: Quality Function  
* **Applicable Regulations**: General Data Protection Regulation (GDPR) Article 22 (Automated Decision-Making), Proposed EU AI Act guidelines on fairness, and relevant national data protection laws.

---

## **Definitions**

* **Bias**: Systematic, repeatable errors in an AI system that create unfair outcomes for certain groups or individuals.  
* **Fairness**: The principle ensuring an AI system's decisions or outputs do not discriminate against protected groups or minority populations.  
* **Protected Groups**: Classes or categories recognized by law or policy for protection (e.g., race, gender, ethnicity, religion).  
* **Mitigation**: Actions taken to reduce or eliminate unwanted bias, including data rebalancing, algorithmic approach changes, or post-processing corrections.

---

## **Section 1: Roles & Responsibilities**

| Role | Responsibility |
| ----- | ----- |
| AI-IRB Chair & Members | Review bias/fairness plans, verify compliance with policy and legal obligations, issue approval or corrective directions. |
| Project Sponsor/Product Owner | Ensure scope, timeline, and budget include bias & fairness tasks; respond to IRB feedback and incorporate changes. |
| Data Scientists / ML Engineers | Implement technical aspects of bias detection, fairness metrics, propose remediation solutions. |
| QA / Validation Team | Independently test for bias using established metrics and verifying the data scientists' results. |
| AI Governance Office | Maintain official documentation on bias/fairness evaluations, track compliance, liaise with IRB and Product Owners. |
| Operations / Deployment Team | Incorporate final bias remediation steps into production environment, coordinate logs/monitoring for bias detection. |
| Technical Support | Gather user feedback on potential unfair outcomes, funnel issues to QA or Data Scientists for re-check. |

---

## **Section 2: Procedure Activities**

### **2.1 Initiate Bias & Fairness Planning**

1. **Trigger**: Any new or updated AI project enters the AI-SDLC or is flagged by the AI-IRB for bias considerations.  
2. **Responsibility**: Project Sponsor ensures the Data Scientists & QA are informed about the need for a Bias & Fairness Evaluation.

### **2.2 Data Collection & Preliminary Analysis**

1. **Data Gathering**: Data Scientists gather relevant training, validation, and test data sets.  
2. **Identify Protected Attributes**: Determine which attributes or categories are considered protected or sensitive for the context.  
3. **Preliminary Exploration**: Conduct basic distribution checks, correlation analyses, and identify potential biases in sample distributions or feature sets.

### **2.3 Develop Bias & Fairness Evaluation Plan**

1. **Metric Selection**: Data Scientists propose fairness metrics (e.g., demographic parity, equalized odds, calibration).  
2. **Thresholds**: In collaboration with the AI Governance Office and QA, define acceptable metric thresholds or disclaimers if no single threshold is viable.  
3. **Review & Approval**: The AI Governance Office and QA review the plan. If approved, proceed; if not, revise as needed.

### **2.4 AI-IRB Oversight Check**

1. **Submission**: The AI Governance Office submits the Bias & Fairness Evaluation Plan to the AI-IRB Chair.  
2. **AI-IRB Review**: The IRB members examine the plan’s thoroughness and compliance.  
3. **Decision**: IRB issues feedback—approve, request changes, or reject.

### **2.5 Bias Detection & Analysis**

1. **Implementation**: Data Scientists run the designated fairness metrics on a test environment.  
2. **Result Compilation**: Summarize bias findings, highlight any deviations from accepted thresholds.  
3. **QA Verification**: QA re-checks calculations, confirms reproducibility.

### **2.6 Mitigation Strategies**

1. **Design Strategy**: If bias is detected, Data Scientists propose solutions (e.g., re-sampling data, altering algorithms, adjusting thresholds).  
2. **Implementation & Test**: Re-train or adjust the model with the new approach.  
3. **Re-evaluate**: Re-run fairness metrics to confirm bias reduction.

### **2.7 Formal Approvals & Documentation**

1. **Sign-Off**: AI Governance Office ensures final results and methods are documented.  
2. **IRB Re-check**: If major changes occurred, the IRB may require a second oversight check.  
3. **Deployment**: Once satisfied, the solution is cleared for final production deployment.

### **2.8 Post-Deployment Monitoring**

1. **Feedback Loop**: Operations and Technical Support gather complaints or anomaly reports.  
2. **Periodic Reevaluation**: Data Scientists schedule repeated fairness checks (quarterly, biannual) depending on guidelines.  
3. **Incident Tracking**: If new biases surface, open an incident and proceed with re-check or root-cause analysis.

### **2.9 Post-Implementation Review**

1. **Assessment**: Evaluate overall process, measure success in removing or reducing bias, propose improvements.  
2. **Lessons Learned**: Document best practices for future AI-SDLC iterations.  
3. **Closeout**: Archive the results in the knowledge repository.

---

## **Section 3: Metrics**

* **Percent of Use Cases Meeting Fairness Threshold**: The fraction of AI use cases that pass established fairness metrics.  
* **Number of Post-Deployment Bias Incidents**: How many new bias incidents or user complaints arise after production.  
* **Time to Mitigate**: Average turnaround time from detecting bias to implementing a fix.

---

## **Section 4: Deliverables and Records**

* **Bias & Fairness Evaluation Plan**  
* **Fairness Metrics Report**  
* **AI-IRB Review Outcome**  
* **Mitigation Implementation Log**  
* **Post-Deployment Monitoring Results**  
* **Lessons Learned Summary**

---

## **Section 5: Tools/Software/Technology Used**

* **Statistical Libraries**: e.g., Python’s `scikit-learn`, R, or specialized fairness libraries (AIF360, FairLearn).  
* **Data Pipeline**: Access control for protected attributes, HPC resources for model training.  
* **Ticketing System**: For tracking bias incidents in post-deployment.

---

## **Section 6: Forms**

1. **Bias & Fairness Evaluation Form**: Summarizes data scope, protected attributes, metrics chosen, thresholds, and final results.  
2. **IRB Submission Form**: Documents the submission details for the IRB’s review.  
3. **Incident Tracking Form**: For post-deployment bias or complaint escalation.

---

## **Section 7: Exemptions**

1. Solutions with no user data or no ability to create group/individual outcomes (purely generic/infrastructure) may not require the full bias protocol.  
2. Minimal-risk internal prototypes subject to a narrower form of evaluation if the IRB or Governance Office deems it.

---

## **Section 8: Revision History**

| Version | Date | Description | Approved By |
| ----- | ----- | ----- | ----- |
| 1.0 | (Date) | Initial release of SOP | (Name/Title) |

---

**End of SOP-1301-01-AI**

@startuml

title "SOP-1301-01-AI: AI Bias & Fairness Evaluation Sequence Diagram"

participant "Project Sponsor" as SP  
participant "Data Scientists" as DS  
participant "AI Governance Office" as AIGO  
participant "AI-IRB Chair" as AIIRB  
participant "Quality Assurance" as QA  
participant "Operations" as OPS  
participant "Technical Support" as TS

' 1\) Initiate Bias & Fairness Planning  
SP \-\> DS: Request Bias & Fairness Evaluation for new AI project

' 2\) Data Collection & Preliminary Analysis  
DS \-\> DS: Gather relevant data\\nIdentify protected attributes\\nPerform preliminary analysis

' 3\) Develop Bias & Fairness Evaluation Plan  
DS \-\> QA: Propose fairness metrics\\nDefine thresholds  
QA \-\> AIGO: Submit plan for internal review  
alt Plan Approved?  
  AIGO \-\> DS: Plan accepted  
else Plan Rejected  
  AIGO \-\> DS: Revise plan and resubmit  
end

' 4\) AI-IRB Oversight Check  
AIGO \-\> AIIRB: Provide plan for IRB oversight  
alt IRB Approves  
  AIIRB \-\> AIGO: Approve plan  
else IRB Requests Changes  
  AIIRB \-\> AIGO: Requires modifications  
  AIGO \-\> DS: Request plan adjustments  
  DS \-\> AIGO: Resubmit revised plan  
end

' 5\) Bias Detection & Analysis  
DS \-\> DS: Execute bias detection code\\nGenerate fairness metrics  
DS \-\> QA: Provide results for verification  
alt QA Accepts Results  
  QA \-\> DS: Data validated, proceed  
else QA Finds Issues  
  QA \-\> DS: Inconsistency found, re-check data  
  DS \-\> DS: Correct approach and retest  
end

' 6\) Mitigation Strategies  
DS \-\> DS: Propose bias mitigation (re-sampling, alt algorithms)  
DS \-\> DS: Implement mitigation & re-run tests  
DS \-\> QA: Submit updated metrics  
alt Resolved  
  QA \-\> DS: Bias within acceptable range  
else Still Biased  
  QA \-\> DS: Additional fixes required  
  DS \-\> DS: Further adjustments  
  DS \-\> QA: Re-test after iteration  
end

' 7\) Formal Approvals & Documentation  
AIGO \-\> SP: Confirm final results & sign-off  
alt IRB Re-check  
  AIIRB \-\> AIGO: Additional oversight required  
  AIGO \-\> DS: Provide updated documentation  
  DS \-\> AIIRB: Submit final metrics  
  AIIRB \-\> AIGO: IRB final approval  
else No IRB Re-check  
  AIGO \-\> DS: No further IRB action needed  
end

' 8\) Post-Deployment Monitoring  
OPS \-\> TS: Deploy model & monitor user feedback  
alt Bias Detected in Production  
  TS \-\> DS: Log bias incident  
  DS \-\> DS: Investigate & fix  
else No Issues  
  TS \-\> TS: Continue normal monitoring  
end

' 9\) Post-Implementation Review  
SP \-\> AIGO: Conduct Post-Implementation Review  
AIGO \-\> DS: Gather lessons learned, finalize documentation  
DS \-\> AIGO: Archive results\\nClose out process

@enduml

**Short textual explanation:** This diagram shows how bias and fairness considerations are integrated throughout the AI-SDLC. The **Project Sponsor** initiates bias planning. **Data Scientists** gather data and define a Bias & Fairness Plan, which is reviewed by **Quality Assurance** and the **AI Governance Office**, then approved by the **AI-IRB**. Bias detection, analysis, and mitigation steps occur prior to deployment. Finally, there is ongoing monitoring in production and a post-implementation review to capture lessons learned.  


[image1]: ../diagrams/SOP-1301-01-AI.PNG