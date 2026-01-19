# **SOP-2002-01-AI\_Control-of-Quality-Records** 

# **![][image1]**

# **Control of Quality Records**

Effective Date: 2025-01-01  
Previous Version: None  
Reason for Update: New SOP  
Owner: Chief Quality Officer (CQO)  
Approved By: Chief Technology Officer (CTO)  
Signature/Date:  
*(Signatures on file)*

---

## **1\. Purpose**

This Standard Operating Procedure (SOP) defines the process for managing and controlling quality records throughout their lifecycle in the AI-SDLC (Artificial Intelligence System Development Life Cycle) environment. The goal is to ensure that all records—whether physical or electronic—are identifiable, retrievable, protected from damage or loss, and retained or disposed of in compliance with regulatory, contractual, and internal AI-IRB (AI Institutional Review Board) requirements.

## **2\. Scope**

This SOP applies to all AI-SDLC projects and associated quality records generated, received, maintained, archived, or disposed of by the Performing Organization (e.g., Engineering Department) and the Contracting Organization (e.g., Product and Technical Support). This includes records relating to:

* AI model design and implementation  
* Testing (unit, integration, system, and acceptance)  
* Regulatory and compliance documentation  
* Training, audits, and any other pertinent quality records  
* Communications with the AI-IRB, if relevant to AI compliance

## **3\. Definitions**

| Term | Definition |
| ----- | ----- |
| Quality Records | Documents or electronic records that provide objective evidence of activities performed or results achieved, e.g., test reports, AI model performance logs, design review minutes, AI-IRB approvals, etc. |
| AI-IRB | AI Institutional Review Board overseeing compliance and ethics for AI systems. |
| Record Retention Schedule | The documented policy or grid specifying the minimum retention period for each type of quality record. |
| Record Custodian | The individual or department responsible for maintaining and securing a given set of records. |

## **4\. Roles and Responsibilities**

### **4.1 Chief Quality Officer (CQO)**

* Ensures that this SOP meets regulatory and organizational requirements.  
* Approves final changes to the SOP.  
* Oversees training on quality records management.

### **4.2 Department Managers / Team Leads**

* Ensure that project teams are aware of and comply with record control procedures.  
* Assign a Record Custodian for each project or functional area.  
* Validate that records are accurately indexed, labeled, and stored.

### **4.3 Record Custodian**

* Maintains records in accordance with this SOP and the established retention schedule.  
* Ensures proper storage, handling, retrieval, and disposal of records.  
* Works with AI-IRB Liaison if record disposal or archival involves sensitive AI model data.

### **4.4 Project Team Members**

* Generate accurate and complete quality records.  
* Follow the labeling, filing, and maintenance guidelines for all relevant documents.  
* Promptly notify the Record Custodian of newly generated records requiring retention.

### **4.5 AI-IRB Liaison**

* Advises on AI-specific data requirements or constraints for quality records.  
* Reviews requests for record disposal to confirm no pending or future AI compliance implications.

### **4.6 QA Department**

* Periodically audits records to confirm compliance with retention, filing, and disposal processes.  
* Addresses any non-compliance by issuing Corrective Action/Preventive Action (CAPA) requests.

## **5\. Procedure**

### **5.1 Record Creation**

1. Identify Required Records  
   * During project planning and as part of each Gate Review, determine which deliverables qualify as quality records (e.g., design documents, test logs, AI compliance approvals).  
2. Use Approved Templates  
   * If templates exist for design, test, or compliance records, the team must use them to ensure consistency.

### **5.2 Record Labeling and Indexing**

1. Standard Naming Convention  
   * Each record shall have a unique identifier indicating the project name/code, document type, version, and date (e.g., AIProjectX\_TestPlan\_v1\_20250102).  
2. Physical Labeling  
   * For hard copies, attach a label or cover page with the identifier, date of creation, and classification level (e.g., Confidential, Restricted).  
3. Electronic Filing  
   * Store digital records in the designated repository (e.g., SharePoint, Git-based VOB) with the same naming scheme. Ensure folder structure aligns with the AI-SDLC phase and gating steps.

### **5.3 Access Control**

1. Authorized Access  
   * The Record Custodian assigns read/write permissions to staff based on the principle of least privilege.  
   * AI data specifically is restricted to AI-IRB-approved staff where relevant.  
2. Change Management  
   * For updates to records, track changes in an audit log or version control system.  
   * All changes require at least one reviewer’s approval (QA or Department Manager).

### **5.4 Record Review and Audit**

1. Internal QA Audit  
   * The QA department reviews selected records quarterly to confirm accurate labeling, completeness, and compliance with retention policies.  
2. AI-IRB Spot Checks  
   * For AI-related data sets or compliance records, the AI-IRB Liaison may conduct spot checks or request further documentation.

### **5.5 Record Retention and Archiving**

1. Retention Schedule  
   * The CQO or Record Custodian references the corporate Record Retention Schedule to determine how long each record type must be kept.  
   * The schedule is updated annually or as regulations change.  
2. Archival Protocol  
   * Physical records: store in secure, controlled-access archives.  
   * Electronic records: maintain in secure servers or cloud storage with regular backups.  
   * AI model logs must be stored with integrity checks to ensure no tampering.

### **5.6 Record Disposal**

1. Disposal Authorization  
   * Prior to destruction, the Record Custodian consults with QA, the respective Department Manager, and the AI-IRB Liaison (for AI-related records).  
2. Document Disposal  
   * For physical documents, use shredding or incineration.  
   * For electronic records, use secure deletion or cryptographic wiping.  
3. Disposal Log  
   * Record the date, type of document, volume/quantity, disposal method, and the authorization signature(s).

### **5.7 Post-Implementation Review**

1. Lessons Learned  
   * During or after each major release, gather feedback on the record management process.  
   * Identify areas to optimize (e.g., improved naming structures or simpler approval steps).  
2. Update SOP  
   * Incorporate any needed changes into this SOP or associated documents, subject to review and approval by the CQO and other stakeholders.

## **6\. Monitoring and Measurement**

* Quarterly QA Audits check compliance with labeling, archiving, and disposal guidelines.  
* Annual AI-IRB Compliance Review ensures no undue risk or potential non-compliance for AI data records.  
* Record Inventory Reconciliation performed semiannually by Record Custodians to ensure indexing is correct and up to date.

## **7\. Training**

* All staff members who create or handle quality records must receive training on this SOP.  
* Training records are themselves maintained per this SOP and SOP-1100-01 Documentation of Training.

## **8\. References**

* Corporate Record Retention Policy  
* AI-IRB Standards for Data Usage and Retention  
* SOP-1100-01 Documentation of Training  
* SOP-1051-01 Security Administration (for secure record access)

## **9\. Revision History**

| Version | Date | Author | Change Description |
| ----- | ----- | ----- | ----- |
| 1.0 | 2025-01-01 | CQO | Initial Release |

---

END OF SOP

@startuml  
title SOP-2002-01 Control of Quality Records

' Declare participants  
participant "Chief Quality Officer (CQO)" as CQO  
participant "Department Manager" as DeptM  
participant "Record Custodian" as RC  
participant "Project Team Member" as PTM  
participant "AI-IRB Liaison" as AIIRBL  
participant "QA Department" as QA

' 1\. Record Creation  
PTM \-\> DeptM: Inform manager about a newly generated quality record  
DeptM \-\> PTM: Provide guidelines on labeling\\nand indexing (templates, naming scheme)  
PTM \-\> RC: Submit newly created record\\nfor official indexing

' 2\. Record Labeling & Indexing  
RC \-\> RC: Assign unique ID\\n& store in designated repository  
RC \-\> QA: Notify QA of new record addition to system

' 3\. Record Review & Audit  
QA \-\> RC: Request sample for quarterly\\nrecord compliance audit  
RC \-\> QA: Provide requested records  
QA \-\> QA: Perform compliance check\\n(labeling, completeness, etc.)  
QA \-\> CQO: Submit audit findings or\\nrecommend CAPA if needed

' 4\. Retention & Archiving  
DeptM \-\> RC: Confirm retention schedule\\nfor record type  
RC \-\> RC: Archive record in secure storage\\n(physical/electronic) as required  
RC \-\> AIIRBL: Request any AI-specific restrictions\\non archiving (if relevant)

' 5\. Disposal Authorization  
alt Record disposal reached end-of-life  
    RC \-\> AIIRBL: Seek disposal authorization\\n(especially for AI-related data)  
    alt Disposal approved  
        AIIRBL \-\> RC: Approve record destruction  
        RC \-\> QA: Document disposal in\\nDisposal Log  
        note right: Record is securely deleted or shredded  
    else Disposal not approved  
        AIIRBL \-\> RC: Records must be\\nretained longer  
        note right: Retention extended  
    end  
else Not end-of-life  
    note over RC: No disposal needed\\nRecord remains archived  
end

' 6\. Post-Implementation or Release  
QA \-\> DeptM: Provide final compliance summary\\nfor improvements or updates  
CQO \-\> All: Issue any revised SOP or training if process improvements found

@enduml

**Short textual explanation:**  
This sequence diagram shows how quality records are created, labeled, reviewed, retained, and disposed of under SOP-2002-01. It begins with a project team member generating a record, proceeds through manager validation and custodian indexing, includes QA audits, and branches at disposal if retention ends or if the AI-IRB Liaison extends retention for AI-related data.

[image1]: ../diagrams/SOP-2002-01-AI.PNG