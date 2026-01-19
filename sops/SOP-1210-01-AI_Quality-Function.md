**SOP-1210-01-AI\_Quality-Function**

**![][image1]**

| SOP Title | Quality Function |
| :---- | :---- |
| **Effective Date** | (Date of Approval/Release) |
| **Previous Version** | None (New SOP) |
| **Reason for Update** | New SOP for AI-SDLC Quality Function |
| **Owner** | AI Quality Assurance Lead |
| **Location** | AI-SDLC Governance Repository |
| **Signature/Date** | \_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_\_ |

---

## **1\. Objective**

The objective of this Standard Operating Procedure (SOP) is to establish and describe the **Quality Function** within the AI Systems Development Life Cycle (AI-SDLC). It details how quality oversight is conducted on product and project deliverables, ensuring alignment with regulatory requirements, user needs, and AI-IRB guidelines. This includes the creation of the **Quality Plan**, the development of test strategies and plans, validation activities, and acceptance criteria that guarantee high-quality AI-based products and services.

---

## **2\. Scope**

This SOP applies to all AI-SDLC projects that require Quality Assurance (QA) oversight, from initial concept through post-deployment review. It addresses:

* **Planning and Strategy**: Creating the quality plan, test strategies, integration and system test plans.  
* **Oversight**: Verifying test preparation, environment readiness, test execution, and defect management.  
* **Validation**: Overseeing system acceptance, user acceptance, and performance testing for AI-based systems or components.  
* **Release**: Ensuring completion of QA sign-offs before any solution is deployed or enters the next AI-SDLC gate.

---

## **3\. Applicable To**

* **AI Quality Assurance** staff who provide independent reviews and verifications.  
* **AI Development Teams** requiring QA inputs and sign-offs.  
* **Operations Teams** that host environments for testing and production.  
* **Product/Project Managers** ensuring timely QA deliverables for AI-SDLC gates.  
* **AI-IRB Liaison** who must confirm compliance with responsible AI guidelines.

---

## **4\. Roles and Responsibilities**

| Role | Responsibility |
| ----- | ----- |
| **AI-QA Manager** | Oversees Quality Function, approves Test Strategies/Plans, coordinates QA resources, ensures compliance with AI-IRB. |
| **Quality Assurance Analyst** | Prepares quality plan, drafts test plans, performs inspections, manages defect logs, tracks testing progress. |
| **Development Team** | Provides technical design, code, and preliminary test results, fixes defects, addresses QA feedback. |
| **Operations** | Prepares test environments, ensures version control procedures, addresses environment issues discovered by QA. |
| **Product Manager** | Coordinates requirements with QA, ensures alignment with user needs, obtains resources for test execution. |
| **Program Manager** | Schedules overall AI-SDLC deliverables, ensures QA dependencies are addressed for each gate, communicates with sponsors |
| **AI-IRB Liaison** | Confirms that AI compliance guidelines are integrated into QA processes and are validated throughout. |

---

## **5\. Metrics**

1. **Cycle Time**  
   * Time from QA test plan creation to acceptance by the Program Manager.  
   * Time from QA discovering a defect to resolution by Development.  
2. **Defect Density**  
   * Ratio of reported defects vs. lines of code or story points.  
   * Ratio of critical defects discovered in System or Acceptance Test to total defects.  
3. **Test Coverage**  
   * Percentage of features, AI models, or requirements validated by QA.  
   * Number of AI compliance checks performed (if relevant).  
4. **Change Agents**  
   * QA staff or cross-functional members who identify process improvements or AI compliance risks.

---

## **6\. Procedure Activities**

Below is a high-level process flow describing how the Quality Function is implemented within the AI-SDLC:

### **6.1 Create Quality Plan**

1. **Initiate Quality Planning**  
   * The **AI-QA Manager** meets with the **Program Manager** and the **Development Team** to capture scope, schedule, and AI-IRB compliance requirements.  
   * The **AI-QA Manager** drafts a **Quality Plan** covering test objectives, responsibilities, milestones, acceptance criteria, and AI compliance checks.  
2. **Obtain Plan Review**  
   * **Quality Assurance Analyst** circulates the draft plan for input from **Product Manager**, **Development**, **Operations**, and **AI-IRB Liaison**.  
   * Revisions are made as necessary.  
3. **Plan Approval**  
   * The **AI-QA Manager** finalizes the plan, obtains sign-off from the **Program Manager** and any AI-IRB sign-offs if the project has potential AI compliance impact.

### **6.2 Develop Test Strategy, Integration, and System Test Plans**

1. **Test Strategy**  
   * **Quality Assurance Analyst** outlines the approach for verifying AI functionality, data integrity, edge cases, and potential biases.  
   * Includes environment configurations, test data strategy, risk analysis, and pass/fail criteria.  
2. **Integration and System Test Plans**  
   * Detailed test cases, data sets, sequences, and environment setups are specified.  
   * **AI-QA Manager** reviews and approves these plans in alignment with the **Quality Plan**.

### **6.3 Verify Test Preparation**

1. **Configuration Readiness**  
   * **Operations** sets up test environments (Development, Integration, System, Acceptance) per the **Configuration Management Plan**.  
   * **Quality Assurance Analyst** ensures all necessary AI test frameworks, logs, data sets, and compliance guidelines are in place.  
2. **Tooling & Data**  
   * Confirm that the required test tools (e.g., load test frameworks, AI model introspection tools) are installed and validated.  
   * Validate that test data sets meet privacy and bias checks as needed.

### **6.4 Perform Integration Test**

1. **Accept Unit Test Results**  
   * Development must show successful unit tests before QA integration tests start.  
   * If the AI feature changes are major, the **AI-IRB Liaison** may re-check compliance docs.  
2. **Execute Integration Test**  
   * **Quality Assurance Analyst** runs the integration test plan, logs any defects in the SQA Manager.  
   * If major issues are found, Development must fix them. The test is repeated until acceptance criteria are met.

### **6.5 Perform System (QA) Test**

1. **Execute System Test**  
   * The QA team performs system-wide tests, including functional, stress/load, regression, AI model performance tests, bias detection, etc.  
   * Each defect is tracked via SQA Manager. The QA team ensures compliance with the **Quality Plan**.  
2. **Complete Test and Turn Over Results**  
   * QA compiles test results, open/closed defects, coverage metrics, and AI compliance logs.  
   * This package is provided to the **Program Manager** for gating decisions.  
3. **Fix System Test Defects**  
   * Development addresses and corrects issues. Retesting occurs until the product meets acceptance thresholds.  
   * The **AI-QA Manager** signals readiness for user acceptance test.

### **6.6 Assist User Acceptance Test (UAT)**

1. **UAT Support**  
   * The QA team helps set up the environment, clarifies test instructions, ensures defect tracking is in place.  
   * UAT tests the user workflows, AI functionality from an end-user perspective, and any final compliance checks.  
2. **Fix UAT Defects**  
   * Development corrects any discovered issues.  
   * QA verifies fixes, updates logs, and readies final sign-off for deployment.

### **6.7 Post-Test Reviews & Sign-Off**

* QA leads a deliverable quality review after each major test cycle.  
* **AI-QA Manager** and **Program Manager** confirm that the defined acceptance criteria are satisfied or mitigate any open concerns.  
* If all conditions are met, QA approves the product for FOA/Beta or production release.

---

## **7\. Forms**

| Form | Purpose |
| ----- | ----- |
| **Test Plan** | Summarizes the scope, approach, resources, and schedule for the testing activities in each phase. |
| **Defect Log** | Central place to track, categorize, and prioritize defects discovered across the test cycles. |

---

## **8\. Exemptions**

* Minor content updates or purely cosmetic interface changes that do not affect AI logic or compliance may be exempt from full QA test cycles if the **AI-QA Manager** approves.

---

## **9\. Tools/Software/Technology Used**

* **SQA Manager** or any test management system for logging and tracking defects.  
* **Automated Testing Frameworks** (e.g., Selenium, JUnit, PyTest)  
* **AI Model Testing Tools** for fairness/bias detection.  
* **Load/Stress Tools** as relevant for system-level performance testing.

---

### **Revision History**

| Version | Date | Author | Changes |
| ----- | ----- | ----- | ----- |
| 1.0 | (Release Date) | AI-QA Manager | Initial AI-SDLC version |

---

**Signature of SOP Approval**  
*I hereby approve this SOP for immediate implementation.*  
**Name/Title:**  
**Signature/Date:**

@startuml

' Define participants (roles) as SHORTNAME  
participant "AI-QA Manager" as MQ  
participant "QA Analyst" as QA  
participant "Development Team" as DEV  
participant "Operations" as OPS  
participant "Product Manager" as PM  
participant "Program Manager" as PG  
participant "AI-IRB Liaison" as IRB

title SOP-1210-01 Quality Function Sequence

' 1\. Create Quality Plan  
MQ \-\> QA: Request draft of Quality Plan  
QA \-\> MQ: Provide draft Quality Plan  
MQ \-\> IRB: (Optional) Check AI compliance requirements  
alt Revisions needed?  
    IRB \-\> QA: Provide compliance feedback  
    QA \-\> MQ: Updated Quality Plan  
else No major revisions  
    QA \-\> MQ: Plan remains as is  
end  
MQ \-\> PG: Submit final Quality Plan for sign-off  
PG \-\> MQ: Approve Quality Plan

' 2\. Develop Test Strategy, Integration, System Test Plans  
QA \-\> QA: Draft Test Strategy, Integration & System Plans  
QA \-\> DEV: Request input (features, constraints)  
DEV \-\> QA: Provide technical details  
QA \-\> MQ: Submit Test Plans for review  
MQ \-\> PM: Gather feedback on user requirements  
alt Further changes needed?  
    PM \-\> QA: Provide feedback  
    QA \-\> MQ: Updated Test Plans  
else Test Plans approved  
    MQ \-\> QA: Test Plans accepted  
end

' 3\. Verify Test Preparation  
OPS \-\> QA: Confirm test environments readiness  
QA \-\> QA: Confirm test data & tools available  
QA \-\> MQ: All test prep verified

' 4\. Perform Integration Test  
QA \-\> DEV: Request unit test acceptance  
DEV \-\> QA: Provide unit test results  
alt Unit tests pass?  
    else  
    QA \-\> DEV: Defects found in unit results  
    DEV \-\> QA: Fix unit test issues  
    QA \-\> DEV: Re-verify until pass  
    end  
QA \-\> QA: Execute integration tests  
QA \-\> DEV: Log defects if found

' 5\. Perform System (QA) Test  
QA \-\> QA: Execute system test (functional, load, regression, AI checks)  
alt Defects discovered?  
    QA \-\> DEV: Defect details  
    DEV \-\> QA: Fix and retest  
else No critical defects  
end  
QA \-\> MQ: Provide final system test results  
MQ \-\> PG: Present readiness for user acceptance

' 6\. Assist User Acceptance Test (UAT)  
QA \-\> PM: Coordinate environment & test instructions  
PM \-\> OPS: Request environment for UAT  
OPS \-\> PM: Confirm UAT environment set up  
QA \-\> DEV: Wait on any UAT defect reports  
alt UAT defects?  
    PM \-\> QA: Defect logs  
    QA \-\> DEV: Forward defects  
    DEV \-\> QA: Fix & confirm  
else UAT pass  
end

' 7\. Post-Test Reviews & Sign-Off  
QA \-\> MQ: Summarize test cycles & open items  
MQ \-\> PG: Final acceptance discussion  
alt Outstanding issues?  
    PG \-\> MQ: Request mitigations  
    MQ \-\> DEV: Action to close issues  
    QA \-\> MQ: Re-check  
else  
    MQ \-\> PG: Everything satisfied  
end  
MQ \-\> IRB: Final AI compliance sign-off if applicable  
PG \-\> All: Authorize product readiness for next gate or deployment

@enduml

**Short textual explanation:**  
This sequence diagram shows how the **Quality Function** proceeds under **SOP-1210-01**. It begins with creating and finalizing the Quality Plan, then moves to test strategy/test plan development, verification of test preparations, and execution of integration/system testing. User Acceptance Testing is subsequently supported, and any defects are addressed. Finally, post-test reviews and sign-offs confirm readiness for deployment or the next AI-SDLC gate. The **AI-IRB Liaison** may be consulted at key points for compliance checks.

[image1]: ../diagrams/SOP-1210-01-AI.PNG