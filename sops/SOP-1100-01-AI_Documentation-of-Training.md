**SOP-1100-01-AI**\_Documentation-of-Training

**Title**:Documentation of Training

![][image1]

**Effective Date**: *\[Insert Effective Date\]*  
**Previous Version**: None  
**Reason for Update**: New SOP  
**Owner**: Human Resources / AI-Training Oversight  
**Location**: \[Insert Repository or Reference\]  
**Signature/Date**: *\[Signature block\]*

---

## **1\. Objective**

This Standard Operating Procedure (SOP) defines the process for creating and maintaining documentation of job-related training for personnel participating in the AI-SDLC (Artificial Intelligence Systems Development Life Cycle), including mandatory AI-IRB compliance requirements as applicable. This procedure ensures that all training records are properly maintained and accessible for audit, regulatory, or operational needs.

---

## **2\. Scope**

This SOP applies to all internal and external training programs that pertain to AI-SDLC activities, especially those subject to AI-IRB regulations. It also includes project-specific training, both client-facing and internally required, that is relevant to the design, development, testing, deployment, or maintenance of AI-driven or AI-related systems at the organization.

---

## **3\. Definitions**

| Term/Abbreviation | Definition |
| ----- | ----- |
| AI-SDLC | The Systems Development Life Cycle adapted for AI-driven solutions, with AI-IRB oversight where required. |
| AI-IRB | The AI Institutional Review Board ensuring ethical and regulatory compliance for AI projects. |
| Trainer | The individual(s) delivering training (internal or external). |
| Training Coordinator | The person (often in HR or departmental lead) who organizes and tracks training events and records. |
| Project-Specific Training | Training tied to a defined feature, project, or protocol within the AI-SDLC. |
| External Training | Training provided by outside entities (seminars, conferences, vendor training, etc.). |
| Internal Training | Organized in-house training sessions, workshops, or courses on SOPs, AI frameworks, or tools. |

---

## **4\. Roles and Responsibilities**

| Role | Responsibility |
| ----- | ----- |
| Human Resources | Maintains overall training records, ensures data integrity, and grants authorized access to records. |
| Training Coordinator | Oversees scheduling, communications, and logistics for training, and ensures documentation is submitted to HR. |
| Line/Department Managers | Approve attendance at training, verify alignment with job needs, and forward approvals to HR. |
| Employees / Contract Staff | Request training approval, attend training, submit evidence or certifications of completion to HR. |
| Trainer | Develop and deliver training content, provide attendance records and materials to the Training Coordinator. |
| AI-IRB Liaison | Validates that AI-related training meets regulatory and ethical guidelines, especially for sensitive AI modules. |

---

## **5\. Procedure Activities**

### **5.1 Maintenance of Employee Training Records**

1. Human Resources maintains a secure record of training for each employee participating in the AI-SDLC. These records shall document:  
   * Employee name  
   * Date(s) of training  
   * Training content or course title  
   * Training provider / sponsor  
   * Duration and final status (completed, partially completed, canceled)  
   * AI-IRB compliance notes, if applicable  
2. Access Control: Only authorized personnel (managers, HR staff, AI-IRB Liaison if needed) can view or request training records.  
3. Reporting: HR is responsible for generating ad-hoc or scheduled reports on training status or compliance levels (e.g., AI-IRB compliance).  
4. Retention: Retain all training records per organizational retention policy (e.g., 3–5 years) or as mandated by relevant regulations.

### **5.2 Documentation of Internal Training**

1. Training Coordinator organizes the internal session (classroom, web-based, or self-paced modules).  
2. Trainer delivers the course, ensures a sign-in sheet or attendance log is completed.  
3. Course Feedback: A standard training evaluation form (e.g., quiz, feedback form) is provided at the end.  
4. Submission to HR: The Trainer or Training Coordinator forwards the completed attendance logs and materials to HR for entry into the training database.  
5. Evaluation: HR may facilitate post-training evaluations to assess effectiveness and compliance with AI-IRB ethical standards.

### **5.3 Documentation of External Training**

1. Employee requests permission to attend external training (seminar, conference).  
2. Manager reviews relevance and approves.  
3. AI-IRB Liaison reviews if training is mandated for handling sensitive AI datasets or meets certain ethical/regulatory standards.  
4. HR logs the approval and final attendance upon completion.  
5. Employee submits proof of completion (certificate or email confirmation).  
6. HR files these external training records in the employee’s file.

### **5.4 Project-Specific Training Documentation**

1. Project Manager identifies required training at project initiation or design.  
2. Trainer or SME (Subject Matter Expert) leads sessions on project protocols, data handling, AI model interpretability, or any relevant SOP.  
3. Attendance Documentation: Participant list, date, and summary of content.  
4. Filing: The Project Manager (or designee) ensures that the session record is placed into the project’s central file or e-record system, with cross-reference in the main training database if it is job-related training.  
5. AI-IRB Check: If the project is AI-IRB governed, the IRB Liaison verifies that participants have completed mandated training.

### **5.5 Post-Implementation and Audits**

1. HR or designated auditor may conduct periodic or triggered audits of training records for completeness and compliance.  
2. Non-Compliance: Any discovered gaps are remediated by scheduling additional training or by updating the records.  
3. Continuous Improvement: Lessons learned from audits feed into revised training modules or updates to this SOP.

---

## **6\. Metrics**

1. Training Completion Rate: Percentage of staff who completed required training vs. total staff assigned.  
2. Timeliness: Average time between assignment of training and completion.  
3. AI-IRB Training Compliance: Number of staff needing specialized AI-IRB training vs. number who have completed it.  
4. Audit Findings: Number of deviations or missing records found during internal or external audits.

---

## **7\. Forms**

* Training Attendance Log: Standard sign-in or e-sign form capturing name, date, time, course name, trainer signature.  
* External Training Request Form: Document used by employees to request external training.  
* Training Evaluation / Quiz: (Optional) Collects feedback and verifies comprehension.

---

## **8\. Exemptions**

* New Hire Orientation outside the AI-SDLC scope is not covered by this SOP.  
* Non-AI or non-SDLC training that does not impact regulatory or SOP compliance is excluded (e.g., social events training, general corporate policy sessions).

---

## **9\. Tools/Software/Technology Used**

* Training Database: Central repository for staff training records.  
* LMS (Learning Management System): If applicable, used to assign, track, and store e-learning data.  
* Document Management System: Where final forms, logs, approvals, and evaluations are archived.

---

## **10\. Document Governance**

* Review Cycle: At least annually or as regulatory changes occur.  
* Approvals: Owner (HR) coordinates updates, obtains sign-off from QA, AI-IRB Liaison if relevant, and Senior Management as needed.

---

## **Revision History**

| Version | Date | Description | Approved By |
| ----- | ----- | ----- | ----- |
| 01.000 | *\[Date\]* | Initial issue of SOP-1100-01 Documentation of Training | *\[Name/Title\]* |

---

END OF SOP-1100-01

@startuml  
title SOP-1100-01 Documentation of Training

' Define participants  
participant "Employee" as E  
participant "LineManager" as M  
participant "TrainingCoordinator" as TC  
participant "Trainer" as TR  
participant "Human Resources" as HR  
participant "AI-IRB Liaison" as IRB

' 1\. Employee requests training (internal or external)  
E \-\> M: Submit Training Request

' 2\. Manager reviews request  
M \-\> M: Evaluate relevance, job needs  
alt Approved  
  M \-\> E: Notify approval  
  E \-\> IRB: (If AI-IRB regulated) Check AI-IRB compliance needs  
  IRB \-\> E: Provide compliance input  
else Denied  
  M \-\> E: Notify denial  
end

' 3\. If Approved, proceed with training logistics  
E \-\> TC: Confirm training details (schedule, mode)  
TC \-\> TR: Arrange training content/schedule

' 4\. Conduct training session  
TR \-\> E: Deliver training session  
note over TR,E  
  Could be internal or external  
  with formal sign-in or e-attendance  
end note  
E \-\> TR: Participate/complete training  
TR \-\> TC: Provide attendance record

' 5\. Documentation  
TC \-\> HR: Forward attendance logs, course info  
HR \-\> HR: Update training database  
HR \-\> E: Confirm record of completion

' 6\. External training scenario  
alt External training  
  E \-\> M: Request to attend external course  
  M \-\> M: Approve based on budget/relevance  
  alt Approved  
    M \-\> E: Approval to attend  
    E \-\> IRB: (If AI-IRB related) Verify external course meets ethics  
    IRB \-\> E: Confirm compliance or additional steps  
    E \-\> HR: Submit proof of completion  
    HR \-\> HR: Update training record  
  else Denied  
    M \-\> E: Communicate denial  
  end  
else No external training  
  note over M,E  
    Skip this branch if purely internal  
  end note  
end

' 7\. Project-specific training  
TC \-\> TR: Coordinate project-specific session  
TR \-\> E: Conduct specialized training  
E \-\> TC: Confirm attendance  
TC \-\> HR: Log session in project’s central files  
HR \-\> IRB: Cross-check AI-IRB compliance if required

' 8\. Audit & Continuous Improvement  
HR \-\> HR: Periodic record audits  
alt Gaps found  
  HR \-\> E: Request missing info  
  E \-\> HR: Provide or retake training  
else No gaps  
  note over HR  
    Records complete  
  end note  
end

@enduml

**Short textual explanation:** This sequence diagram shows how employees request and attend training (both internal and external), how managers and HR handle approvals and records, and how AI-IRB Liaison may verify compliance for AI-related training. It ends with auditing the training records for completeness and remediating any gaps.

[image1]: ../diagrams/SOP-1100-01-AI.PNG