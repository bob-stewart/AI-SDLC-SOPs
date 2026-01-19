**SOP-1101-01-AI\_Training-and-Documentation**

![][image1]  
**Title: Training and Documentation**

| Effective Date | Supersedes Date | Reason for Update | Owner |
| ----- | ----- | ----- | ----- |
| *YYYY-MM-DD* | *N/A (New)* | New AI-SDLC SOP | *Training Department / AI-IRB Liaison* |

---

## **1\. Purpose and Scope**

This SOP describes the method for identifying, analyzing, and preparing training and documentation materials necessary for effective deployment of AI-related enhancements or products to both internal functional units and external end-users under the AI-SDLC. Additionally, it outlines roles and responsibilities to ensure smooth knowledge transfer for AI-based or standard systems.

Scope:

* Covers all training (internal or external) required by the AI-SDLC, including product documentation, user manuals, and release notes.  
* Encompasses the steps from requirements definition of training materials to the execution of training (including FOA, pilot sessions, and final user classes).  
* Applies to internal staff (e.g., developers, testers, operations) and external clients or partners who receive training on AI products or features.  
* Excludes new-hire onboarding training (handled by HR) except where AI compliance is mandatory.  
* Incorporates possible AI-IRB or ethics regulatory oversight for AI-based solutions.

---

## **2\. Definitions**

* AI-IRB: An internal or external review board that oversees ethical and compliance aspects of AI solutions.  
* Training Needs Document (TND): A summary of training scope, audience, topics, format, and timeline.  
* Pre-Needs Assessment Form (PNAF): A client-facing form capturing specific training expectations, environment constraints, and sign-offs.  
* FOA (First Office Application) Training Pilot: The initial training event for a new or major updated AI solution, typically executed in a limited environment or with a select audience.  
* Training Pilot: An internal or smaller-scale test run of the final or near-final training plan and materials.  
* Post-Deployment Training: Training provided after system or AI model goes live to ensure adoption and correct usage.

---

## **3\. Roles and Responsibilities**

| Role | Responsibility |
| ----- | ----- |
| Training (Trainer/Group) | Delivers training to internal or external personnel; ensures training content is accurate and current. |
| Technical Support | Defines initial training & documentation requirements; reviews produced materials; trains end-users. |
| Product Group | Works with Technical Support to gather training needs; ensures SOW identifies all required training. |
| Development Group | Produces or updates technical documents as per AI-SDLC scope; collaborates with QA on documentation. |
| Quality Assurance (QA) | Reviews, accepts/rejects documentation for completeness & accuracy; ensures it meets acceptance criteria. |
| AI-IRB Liaison | Ensures training meets AI ethical/compliance guidelines; reviews training content if mandated. |
| Operations | May assist in environment setup for training sessions or staging environment usage. |
| Client/External User | Receives training; completes Pre-Needs Assessment Form (as relevant); provides feedback. |

---

## **4\. Procedure Activities**

### **4.1 Identify Training Requirements (Gate 6 of AI-SDLC)**

1. Technical Support & Product Group review the Scope of Work (SOW) from the Requirements Phase.  
2. These groups create or update a Training Needs Document (TND) that:  
   * Lists functionality requiring training (including any specialized AI functionality).  
   * Identifies trainers (internal or external).  
   * Defines audiences (internal Dev, QA, Ops, external clients, etc.).  
   * Notes whether FOA or pilot sessions are required.

### **4.2 Pre-Needs Assessment Form (PNAF)**

1. For external training, Technical Support and Product Group co-author the PNAF.  
2. PNAF is sent to the Client for acceptance and sign-off of training scope, timeline, environment constraints, and compliance with AI-IRB if relevant.  
3. AI-IRB Liaison verifies compliance details if the system or training includes regulated AI features.

### **4.3 Documentation Creation and Review**

1. Once the Detailed Plan is complete (Gate 5 of AI-SDLC), the Development Group prepares all training documents:  
   * User guides  
   * Interface changes  
   * Feature descriptions  
   * Known issues (applicable to system or AI model limitations)  
2. Technical Support, Product Group, QA, AI-IRB Liaison (if mandated) review these documents.  
3. QA has final accept/reject authority. Rejections lead to rework until acceptance criteria are met.

### **4.4 FOA (First Office Application) Training Pilot (If applicable)**

1. For selected AI-based releases requiring FOA, Technical Support or Product Group conducts the first pilot training using the newly produced materials.  
2. The pilot runs in a staging environment or a similarly controlled environment.  
3. Trainees evaluate effectiveness. If documentation or training is lacking, it returns to Development or Technical Support for improvement.

### **4.5 General Training Pilot**

1. Technical Support trains end-users (non-technical) while Development trains technical or engineering staff if needed.  
2. The pilot is tested in an environment that simulates final usage.  
3. Feedback is collected to measure training success using the Training Evaluation Form (SOP-1100 reference).  
4. If training or documentation is not meeting needs, additional sessions or revised materials are provided.

### **4.6 Customer Training Classes**

1. After acceptance of the training pilot(s), Technical Support hosts training classes before deployment or during controlled rollout.  
2. Attendees fill out post-training Evaluation Forms.  
3. If training is insufficient, more sessions are scheduled or materials updated.  
4. Four weeks post-deployment, the Evaluation Form is recirculated to measure training retention and to gather final feedback.

### **4.7 Post-Implementation**

1. Technical Support monitors user support calls to identify any training shortfalls.  
2. QA or AI-IRB Liaison can trigger follow-up training if AI compliance or usage anomalies are observed.  
3. Lessons Learned feed into future training cycles.

---

## **5\. Forms**

* Training Needs Document (TND)  
* Pre-Needs Assessment Form (PNAF)  
* Training Evaluation Form (see [SOP-1100](https://markdownlivepreview.com/#) for example)  
* AI-IRB Compliance Checklist (if applicable)

---

## **6\. Tools/Software/Technology**

* Content Management System (CMS) for hosting training docs  
* LMS (Learning Management System) for scheduling/tracking training  
* Issue Tracking (SQA Manager/JIRA/ServiceNow) for capturing training content bugs  
* AI-IRB Portal for regulated approvals (if mandated)

---

## **7\. Exceptions**

* New-Hire or general HR orientation not covered (separate procedure).  
* If no external client is involved, skip the PNAF.  
* If AI solution is minor or partial, the AI-IRB liaison step can be minimal or N/A.

---

## **8\. Revision History**

| Version | Date | Revised By | Changes |
| ----- | ----- | ----- | ----- |
| 1.0 | *YYYY-MM-DD* | *Training Department* | Initial AI-SDLC aligned SOP creation |
| 1.1 | *YYYY-MM-DD* | *AI-IRB Liaison* | Added AI compliance checks for regulated training |

---

End of SOP-1101-01-AI

@startuml  
title "SOP-1101-01-AI: Training and Documentation Sequence"

participant "Technical Support" as TS  
participant "Product Group" as PG  
participant "AI-IRB Liaison" as AIIRB  
participant "Development" as DEV  
participant "Quality Assurance" as QA  
participant "Operations" as OPS  
participant "Client/External User" as CLIENT

TS \-\> PG: Review SOW and define initial training needs  
PG \-\> TS: Draft or update Training Needs Document (TND)

alt AI-IRB needed  
  PG \-\> AIIRB: Submit training approach for AI compliance check  
  AIIRB \-\> PG: Approve or request changes  
end

alt External Training Required  
  TS \-\> CLIENT: Send Pre-Needs Assessment Form (PNAF)  
  CLIENT \-\> TS: Return signed PNAF (or request changes)  
end

DEV \-\> TS: Provide draft training documentation (user guides, known issues, etc.)  
TS \-\> QA: Forward documentation for QA review  
QA \-\> QA: Review doc completeness and correctness  
alt Documentation Rework Needed  
  QA \-\> DEV: Request revisions  
  DEV \-\> QA: Resubmit corrected documentation  
end  
QA \-\> TS: Documentation Accepted

alt FOA Training Pilot  
  TS \-\> PG: Coordinate FOA pilot training  
  TS \-\> OPS: Request staging environment readiness  
  OPS \-\> TS: Confirm environment set up  
  TS \-\> TS: Conduct FOA training pilot  
  TS \-\> PG: Gather FOA pilot feedback  
  alt FOA training insufficient  
    TS \-\> DEV: Request doc or content fix  
    DEV \-\> TS: Provide updated materials  
  end  
end

TS \-\> TS: Schedule Training Pilot (general)  
TS \-\> TS: Deliver pilot training to internal and/or external staff  
TS \-\> PG: Collect pilot feedback  
alt Pilot feedback insufficient  
  TS \-\> DEV: Additional revision or re-training  
end

TS \-\> CLIENT: Conduct final customer training classes  
CLIENT \-\> TS: Provide training evaluation  
alt Additional training needed  
  TS \-\> DEV: Adjust materials, repeat session(s)  
end

note over TS,PG,QA,OPS: Post-release, observe calls and usage to verify training success  
@enduml

**Short textual explanation:** This sequence diagram illustrates the entire training and documentation workflow for **SOP-1101-01**. After **Technical Support** and **Product Group** define the **Training Needs Document**, possible **AI-IRB** approvals and **Pre-Needs Assessments** occur. **Development** provides draft documentation, which **Quality Assurance** reviews for completeness. If needed, rework cycles take place. Then a **FOA Training Pilot** or a **General Training Pilot** might be conducted. Finally, customer training classes happen, with participant evaluations and any necessary follow-up training actions.

[image1]: ../diagrams/SOP-1101-01-AI.PNG