# **SOP-1200-01-AI\_Development**

**![][image1]**

**Title:** Development  
**Document ID:** SOP-1200-01-AI  
**Effective Date:** (Date to be inserted)  
**Supersedes:** None  
**Owner:** Development Department  
**Approved By:** (Name/Signature/Date)

---

## **Objective**

This Standard Operating Procedure (SOP) defines the process, responsibilities, and controls for designing, implementing, and testing system components during the Development phase of the AI-SDLC. The Development phase ensures all business and technical requirements are satisfied and ready for subsequent Testing, Validation, and Deployment.

---

## **Scope**

* Applies to all AI-related software/product development activities, including prototypes, enhancements, patches, bug fixes, and major releases.  
* Covers code and associated documents from the time detail designs are approved to the point where a final, production-ready build is handed over to **Quality Assurance**.  
* Includes required compliance steps involving the **AI-IRB Liaison** if any changes or additions have regulatory or ethical implications.

---

## **Definitions**

| Term | Definition |
| ----- | ----- |
| **AI-IRB Liaison** | The individual or committee representative responsible for overseeing compliance with AI risk management, alignment with ethical/regulatory standards, etc. |
| **Implementation Unit (IU)** | A distinct chunk of functionality, code, or script that can be developed, tested, and integrated independently, e.g., a class or module. |
| **VOB** | Versioned Object Base. Central source control repository that maintains versioned code, documentation, and other development artifacts. |

---

## **Roles and Responsibilities**

| Role | Responsibility |
| ----- | ----- |
| **Project Manager** | Orchestrates project tasks, resource planning, timeline updates, and cross-team communication. |
| **Development Team Leader** | Oversees coding standards, assignment of Implementation Units (IUs), code review sessions, and ensures developer adherence to technical design. |
| **Developer** | Writes, integrates, and unit-tests code for assigned IUs, addresses assigned defects, and updates associated documentation in the VOB. |
| **Quality Assurance (QA)** | Reviews deliverables for compliance and completeness, performs acceptance of code prior to QA environment. Tests fixes for defects and ensures test coverage is achieved. |
| **Operations** | Prepares or reviews environment configurations, ensures successful builds for integration testing, and readies staging or production as needed. |
| **AI-IRB Liaison** | Conducts or coordinates AI risk assessment if new or changed AI-related functionality is introduced, providing sign-off or requiring additional compliance steps. |
| **Product Group** | Collaborates on design input, ensures final product meets business and user needs. |

---

## **References**

* **SOP-1040-01-AI** (Requirements Definition)  
* **SOP-1041-01-AI** (Detail Design)  
* **SOP-1210-01-AI** (Quality Function & Testing)  
* **SOP-1003-01-AI** (Configuration Management)  
* **AI-IRB** (Ethical and regulatory compliance guidelines for AI-enabled functionality)

---

## **Procedure Activities**

### **1\. Commence Development**

1. **Pre-Development Validation**  
   * Once **Detail Design** (SOP-1041-01-AI) is approved by QA and relevant stakeholders, the **Development Team Leader** allocates Implementation Units (IUs) to each **Developer**.  
   * If new AI functionalities are introduced, the **AI-IRB Liaison** must be notified for possible additional compliance steps.  
2. **Set Up VOB and Environment**  
   * **Operations** or **Configuration Management** sets up a VOB branch or similar structure for the new development.  
   * **Developers** ensure local dev environments match project specs.

### **2\. Coding and Documentation**

1. **Follow Approved Technical Design**  
   * **Developers** create or modify source code adhering to coding standards.  
   * Code changes must reference relevant requirements and design documents.  
   * If AI changes require updated data usage approach or model updates, the **AI-IRB Liaison** steps in for re-approval, if needed.  
2. **Unit Testing**  
   * **Developers** write and execute unit tests for each IU.  
   * If tests fail, code is revised and re-tested.  
   * If a showstopper or unforeseen AI compliance issue arises, the **Developer** escalates to the **Development Team Leader** or **AI-IRB Liaison**, as appropriate.

### **3\. Code Review / Peer Walk-Through**

1. **Walk-Through Preparations**  
   * **Development Team Leader** schedules code review sessions weekly or per milestone.  
   * Code authors and relevant peers (including QA if needed) attend.  
2. **Session Execution**  
   * The code author presents logic, functionality, any new AI modules.  
   * Attendees note findings, ensure coding style and design compliance.  
   * The **recording secretary** compiles any discovered defects or improvement requests.

### **4\. Build and Merge for Integration**

1. **Build IU Code**  
   * **Developers** produce compiled executables or scripts for the assigned IU.  
2. **Merge into VOB**  
   * With the Team Leader's approval, code merges into the shared integration branch.  
   * The **Developer** rechecks merges for conflicts, ensuring no overwritten changes.  
3. **Integration Smoke Test**  
   * The **Developer** performs a quick smoke test in the integration environment.  
   * Defects discovered are either resolved immediately or recorded for triage.

### **5\. QA Handover**

1. **Documentation Update**  
   * **Developer** updates IU documentation, verifying references to new or changed code.  
   * If AI models or code changes are included, relevant sections are documented in separate AI compliance notes.  
2. **Integration Sign-Off**  
   * **Quality Assurance** reviews integration test results.  
   * If results are acceptable, QA signals readiness for QA environment testing. Otherwise, code is returned for rework.

### **6\. Post-Development Review**

1. **Development Team Leader** organizes final check to confirm readiness for formal QA testing (SOP-1210-01-AI).  
2. **Project Manager** updates the project plan if there's scope or schedule deviation discovered.  
3. **AI-IRB Liaison** confirms final AI compliance sign-off if AI-related enhancements were introduced during development.

---

## **Acceptance Criteria**

* **All** Implementation Units pass unit tests with recorded results, including AI compliance steps if relevant.  
* Peer code reviews yield no critical design or compliance issues.  
* Integration smoke test passes with no critical or blocking issues.  
* Documentation is updated in the VOB or designated repository.

---

## **Records and Reports**

* **Unit Test** results stored in the VOB or test management tool.  
* **Peer Review** notes or logs compiled by the recording secretary.  
* **Integration** test logs, including smoke test results.  
* **AI-IRB** sign-off emails or forms if AI changes were introduced.

---

## **Change Management**

* Any major re-scoping or additional AI compliance requirements discovered mid-development must follow **SOP-1003-01-AI** (Configuration Management) or relevant gating procedures.

---

## **Attachments/Appendices**

None in this SOP version.

---

## **Revision History**

| Version | Date | Changes | Approved By |
| ----- | ----- | ----- | ----- |
| 1.0 | (insert date) | Initial Release | Development Dept. |

---

## **End of SOP**

@startuml  
title SOP-1200-01 Development Sequence Diagram

actor PM as "Project Manager"  
actor LDR as "DevTeamLeader"  
actor DEV as "Developer"  
actor QA as "Quality Assurance"  
actor OPS as "Operations"  
actor IRB as "AI-IRB Liaison"  
actor PG as "Product Group"

PM \-\> LDR: Provide Approved Detail Design  
note right  
  Commence Development   
  after final design sign-off  
end note

LDR \-\> LDR: Plan Implementation Units (IUs)  
LDR \-\> DEV: Assign IUs and Provide Code Standards

alt New AI Functionality Introduced?  
  LDR \-\> IRB: Notify AI-IRB for compliance check  
  IRB \-\> LDR: AI compliance guidance or approval  
else No AI Changes  
  LDR \-\> LDR: Proceed without IRB involvement  
end

OPS \-\> LDR: Confirm VOB branch & environment readiness  
LDR \-\> DEV: Confirm Dev environment setup

DEV \-\> DEV: Code Implementation (following design specs)  
DEV \-\> DEV: Execute Unit Tests  
alt Unit Tests Pass?  
  DEV \-\> LDR: Unit test success, ready for peer review  
else Unit Tests Fail  
  DEV \-\> DEV: Fix code and re-run unit tests  
  DEV \-\> LDR: Updated code with successful unit tests  
end

LDR \-\> LDR: Schedule Code Walk-Through  
LDR \-\> DEV: Present code in weekly walk-through  
LDR \-\> LDR: Document review findings

DEV \-\> DEV: Update code per walk-through findings  
DEV \-\> DEV: Build IU Code (executable)  
DEV \-\> LDR: Request Merge to Integration Branch

LDR \-\> LDR: Approve code merging  
DEV \-\> OPS: Merge to shared VOB branch  
DEV \-\> DEV: Perform integration smoke test

alt Smoke Test Pass?  
  DEV \-\> QA: Notify readiness for QA environment  
else Smoke Test Fail  
  DEV \-\> DEV: Fix integration issues  
  DEV \-\> LDR: Request additional check  
  DEV \-\> QA: Ready for QA after fix  
end

QA \-\> DEV: Review final integration build  
alt Accept or Return?  
  QA \-\> QA: If accepted, proceed  
  QA \-\> DEV: If not, rework needed  
end

DEV \-\> DEV: Update Documentation  
alt AI-IRB Impact Re-check?  
  DEV \-\> IRB: Provide final AI changes doc  
  IRB \-\> DEV: AI re-approval or no changes  
else No AI Re-check needed  
  note over DEV  
    Standard process continues  
  end note  
end

LDR \-\> PM: Final readiness for QA Testing  
PM \-\> LDR: Adjust schedule/resources if needed

@enduml

**Short textual explanation:**  
This sequence diagram shows the SOP-1200-01 Development process. The **Project Manager** hands off approved detail designs to the **DevTeamLeader**, who partitions tasks into Implementation Units. If new AI functionality is present, the **AI-IRB Liaison** reviews compliance aspects. **Developers** code, perform unit tests, and fix issues before merging to the integration branch. A smoke test checks basic integration readiness. After acceptance, **Quality Assurance** validates the final integration build. Documentation is updated, and any final AI re-check is done before the **DevTeamLeader** signals readiness for formal QA testing. The **Project Manager** may update schedules if needed.

[image1]: ../diagrams/SOP-1200-01-AI.PNG