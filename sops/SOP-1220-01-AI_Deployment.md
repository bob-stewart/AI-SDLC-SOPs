**SOP-1220-01-AI\_Deployment**  
**Title:** **Deployment (AI-SDLC)**

![][image1]

| Effective Date | Previous Version | Reason for Update | Owner | Location | Signature/Date |
| ----- | ----- | ----- | ----- | ----- | ----- |
| *YYYY-MM-DD* | None | New SOP (AI-enabled) | Deployment Lead | *Repository* | *Sign/Date* |

---

## **1\. Objective**

This Standard Operating Procedure (SOP) defines the **planning and implementation requirements** for deploying AI-driven systems and enhancements into production as part of the **AI-SDLC** (Artificial Intelligence System Development Life Cycle). It ensures that releases meet **compliance** (including AI-IRB concerns), are fully tested, documented, and successfully transitioned to production/operations environments.

---

## **2\. Scope**

* Encompasses **all deployment stages** of an AI-based or AI-affecting system.  
* Covers steps taken from the end of development, QA acceptance, user acceptance, FOA/Beta through final production release.  
* Includes **post-deployment** tasks (e.g., validating deployment success, user training completion, capturing lessons learned).  
* Applies to **internal** (in-house) deployments and **external** (client-facing) AI system rollouts.

---

## **3\. Applicable To**

* **Development Team:** Responsible for final readiness of code and documentation.  
* **Quality Assurance (QA) Team:** Ensures readiness, final testing acceptance, and post-deployment validation activities.  
* **Operations/Configuration Management Team:** Manages the infrastructure for AI solution deployment, verifies environment readiness, executes final push to production, and monitors performance.  
* **Product/Project Manager (PM):** Oversees scheduling, communicates with sponsors, obtains approvals for rollout.  
* **Program Manager (PG):** Coordinates across multiple releases/programs, ensures resources and alignment with AI-IRB or regulatory requirements.  
* **Technical Support/Service Organization:** Provides end-user support/training, helps coordinate FOA or Beta site usage.  
* **AI-IRB Liaison:** Verifies that final solution meets all AI governance and compliance requirements prior to go-live.

---

## **4\. Sections**

1. **Definitions**  
2. **Roles and Responsibilities**  
3. **Metrics**  
4. **Deployment Procedure Activities**  
5. **Post-Deployment and Lessons Learned**  
6. **Forms**  
7. **References**

---

## **5\. Definitions**

* **FOA (First Office Application)**: First live deployment to a controlled environment/client, used to validate real-world performance of new AI features or solutions.  
* **Beta**: Limited release to a small group of users for final feedback prior to general availability.  
* **Deployment Plan**: A formal document outlining tasks, resources, and schedules for rolling out a system or feature into production.  
* **User Acceptance**: Formal process whereby end-users confirm the system meets requirements and is ready for production.

---

## **6\. Roles and Responsibilities**

| Role | Responsibility |
| ----- | ----- |
| **Development Lead** | Finalizes code, ensures release readiness, addresses any issues discovered during last-mile QA or user acceptance. |
| **QA Lead** | Validates system readiness, coordinates final acceptance testing, ensures that system is thoroughly tested and stable. |
| **Operations Manager** | Reviews and executes the deployment plan, sets up environments, performs the final “push,” and monitors post-release. |
| **Product/Project Mgr** | Communicates with stakeholders, obtains final approvals, orchestrates the release timeline, ensures full compliance. |
| **Program Manager** | Monitors overall resource usage, scheduling, cross-project dependencies, and coordinates with AI-IRB Liaison. |
| **Technical Support** | Schedules training, FOA/Beta support, coordinates user acceptance and go-live training, logs post-release issues. |
| **AI-IRB Liaison** | Confirms all AI-related compliance steps are completed before final push to production, addresses any regulatory steps. |

---

## **7\. Metrics**

1. **On-Time Deployment Rate:** Percentage of releases deployed within the planned time window.  
2. **Deployment Defects:** Number of post-deployment bugs discovered that are directly linked to the release process.  
3. **Customer Satisfaction:** Feedback from early-adopter or FOA/Beta sites on ease-of-use and correctness of AI functionality.  
4. **AI-IRB Compliance Pass Rate:** Number/percentage of deployment packages passing AI-IRB/regulatory checks without major findings.

---

## **8\. Deployment Procedure Activities**

### **8.1 Prepare Deployment Plan**

**Owner:** Performing Organization (Development, QA, Ops, PM)

1. **Gather Requirements:** Product Manager and Development team confirm final scope, cost, schedule, and approved changes.  
2. **Draft Plan:** Development lead (with QA, Ops) outlines tasks, roles, environment details, timing, rollback steps, acceptance criteria.  
3. **Review & Approve Plan:**  
   * Operations verifies feasibility,  
   * QA ensures testing coverage,  
   * AI-IRB Liaison checks for any unresolved compliance concerns.  
4. **Document Final Plan:** Store in project repository, share with all stakeholders.

### **8.2 Prepare Installation Procedure & Preliminary Documentation**

**Owner:** Development

1. **Create/Update Installation Procedure Document:** Summarize environment configuration, data migrations, scripts, AI model versions, etc.  
2. **Operations Review:** Validate feasibility, environment readiness, rollback method.  
3. **Preliminary Documentation:** Summaries for user guides, readme files, release notes.

### **8.3 FOA/Beta & Documentation Testing**

**Owner:** Product Development & Technical Support

1. **FOA/Beta Kickoff:** If FOA or Beta needed, coordinate with selected users/partners to verify real-world usage, gather feedback.  
2. **Documentation Review:** Ensure help files, user guides, or integrated AI model usage instructions are tested for clarity.  
3. **Accept/Reject:** If issues are discovered, route them to Development for fixes and QA retesting.

### **8.4 User Acceptance Testing (UAT)**

**Owner:** Contracting Organization, with QA & Dev assistance

1. **UAT Environment Preparation:** Operations sets up environment mirroring production.  
2. **Execute UAT:** End-users run AI features, confirm results.  
3. **Track Defects:** QA logs issues; Development addresses them.  
4. **Decision:** If pass, proceed. If fails, fix or re-plan.

### **8.5 Final Approval for Production**

**Owner:** Governance & Program Management

1. **Check AI-IRB**: AI-IRB Liaison confirms compliance sign-off.  
2. **All Stakeholders Sign-off**: Product Manager ensures all relevant parties (QA, Ops, IRB, Dev) approve.  
3. **Deployment “Go” Decision**: Program Manager authorizes final push.

### **8.6 Release to Production**

**Owner:** Operations, QA verifying

1. **Environment Prep:** Ops readies production environment, backups, final checks.  
2. **Push Execution:** Deploy the code, AI models, or configurations using scripts, tools as per plan.  
3. **Post-Deployment Verification:** QA and Dev confirm successful deployment, run smoke tests to ensure AI features are functioning.  
4. **Notify Stakeholders:** Product Manager announces successful go-live.

---

## **9\. Post-Deployment and Lessons Learned**

1. **Post-Implementation Review**: Held by QA with Dev, Ops, PM, and IRB Liaison. Summarize performance, issues, successes.  
2. **User Feedback**: Evaluate user satisfaction, especially regarding new AI functionalities.  
3. **Finalize Documentation**: Incorporate final changes, update operations or next release tasks.  
4. **Lessons Learned Log**: The “Attachment A” Lesson(s) Learned form is completed, capturing improvements for future deployment cycles.

---

## **10\. Forms**

* **Attachment A: Lessons Learned**  
  This form tracks continuous improvement from each release.

---

## **11\. References**

* SOP-1000-01-AI: Program/Project Management  
* SOP-1003-01-AI: Configuration Management  
* SOP-1010-01-AI: Site Monitoring and Problem Management  
* SOP-1101-01-AI: Training and Documentation  
* AI-IRB guidelines for compliance checks

---

**End of SOP-1220-01-AI**

@startuml  
title SOP-1220-01 Deployment (Sequence Diagram)

participant "Development Lead" as DEV  
participant "QA Lead" as QA  
participant "Operations Manager" as OPS  
participant "Product/Project Mgr" as PM  
participant "Program Manager" as PG  
participant "Technical Support" as TS  
participant "AI-IRB Liaison" as IRB

PM \-\> DEV: Request final scope and deliverables  
DEV \-\> PM: Provide final scope details  
PM \-\> PG: Communicate final scope/cost/schedule updates  
PG \-\> PM: Confirm resource alignment

PM \-\> DEV: "Draft Deployment Plan" request  
DEV \-\> QA: "Gather QA input for plan"  
DEV \-\> OPS: "Gather environment/deployment input"  
DEV \-\> IRB: "Check AI compliance readiness"  
alt If IRB has concerns  
    IRB \-\> DEV: "Adjust compliance steps"  
    DEV \-\> QA: "Incorporate compliance changes"  
else No major IRB concerns  
    note over IRB: No additional compliance changes needed  
end  
DEV \-\> PM: Submit Deployment Plan

PM \-\> OPS: "Review & Approve Deployment Plan"  
OPS \-\> PM: Confirm environment feasibility  
PM \-\> QA: "Validate Deployment Plan meets testing coverage"  
QA \-\> PM: Approve test coverage

PM \-\> IRB: "Sign-off on compliance readiness"  
IRB \-\> PM: "Compliance Approved"

PM \-\> DEV: "Prepare Installation Procedure & Preliminary Docs"  
DEV \-\> OPS: "Submit install procedure for review"  
OPS \-\> DEV: Provide feedback on procedure  
DEV \-\> QA: Provide preliminary user/product docs for review  
QA \-\> DEV: Documentation feedback

PM \-\> TS: "Coordinate FOA/Beta readiness"  
alt FOA/Beta needed  
    TS \-\> TS: "Kick off FOA/Beta with limited user group"  
    TS \-\> DEV: "Collect feedback on real-world usage"  
    DEV \-\> QA: "Fix issues from FOA/Beta if any"  
    QA \-\> DEV: Retest and confirm fixes  
else No FOA/Beta needed  
    note over TS: Proceed directly to final user acceptance  
end

PM \-\> OPS: "Prepare user acceptance environment"  
OPS \-\> TS: "Environment ready for UAT"  
TS \-\> TS: "Execute UAT with end-users"  
TS \-\> QA: "Report UAT defects"  
QA \-\> DEV: "Assign defects to fix"  
DEV \-\> QA: "Deliver fixes"  
QA \-\> TS: "Verify final UAT pass"

PM \-\> IRB: "Request final compliance sign-off"  
IRB \-\> PM: "Compliance sign-off Granted"  
PM \-\> PG: "All conditions met, request deployment 'Go'"

alt Final approval  
    PG \-\> PM: "Authorize final push to production"  
    PM \-\> OPS: "Initiate production release"  
    OPS \-\> DEV: "Deploy code, AI models, config to production"  
    OPS \-\> QA: "Perform smoke test in production"  
    QA \-\> OPS: "Production environment is stable"  
    PM \-\> TS: "Announce successful go-live"  
else Approval delayed  
    note over PM,PG: Reassess schedule or re-work items  
end

TS \-\> TS: "Provide ongoing support"  
PM \-\> QA: "Schedule Post-Implementation Review"  
QA \-\> DEV: "Collect lessons learned"  
DEV \-\> QA: "Submit improvement suggestions"  
QA \-\> IRB: "Confirm any additional compliance notes"  
QA \-\> PG: "Finalize Post-Implementation Review"  
@enduml

**Short textual explanation:**

1. **Project/Program Management** requests final scope updates from **Development** and aligns resources with the **Program Manager**.  
2. **Development** drafts the **Deployment Plan** with input from **QA**, **Operations**, and checks with **IRB** for AI compliance.  
3. **Operations** reviews the plan for feasibility. **QA** verifies test coverage. **IRB** grants compliance sign-off.  
4. If FOA/Beta is needed, **Technical Support** pilots it; issues are routed back to **Development** and **QA** for fixes.  
5. **User Acceptance Testing** is performed. Upon success, final compliance sign-off occurs.  
6. **Program Manager** authorizes final push. **Operations** deploys to production. **QA** performs final checks.  
7. Finally, a **Post-Implementation Review** is conducted, capturing lessons learned and additional improvements.

[image1]: ../diagrams/SOP-1220-01-AI.PNG