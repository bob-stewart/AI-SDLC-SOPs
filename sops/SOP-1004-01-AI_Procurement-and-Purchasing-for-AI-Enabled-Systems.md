**SOP-1004-01-AI\_**Procurement-and-Purchasing-for-AI-Enabled-Systems  
**Title**: Procurement and Purchasing for AI-Enabled Systems

![][image1]

| Effective Date | *YYYY-MM-DD* |
| :---- | :---- |
| **Previous Version** | None |
| **Reason for Update** | New AI-SDLC SOP (AI-IRB integration) |
| **Owner** | Chief Technology Officer (CTO) |
| **Approvers** | AI-IRB Liaison, Head of Operations, Head of Compliance |

**Date of Approval:** (Fill in)

---

[🏠 AI Mind Matrix](../AI_Mind_Matrix.md) | [⚖️ AI Governance Gaps](../AI_Governance_Gaps.md) | [📋 SOP Index](./SOP-LIST-01-AI_AI-IRB-Governed-AI-SDLC.md)

---

## **1\. Objective**

The objective of this Standard Operating Procedure (SOP) is to document **an efficient and consistent** method for **procuring assets** needed to support AI-focused product development and/or business operations. This SOP places particular emphasis on **AI-related hardware, software licenses, data resources**, and **specialized tools** subject to AI-IRB or regulatory constraints.

It ensures that **compliance, ethical considerations, risk management,** and **AI-IRB conditions** are integrated into the procurement lifecycle from request initiation to asset deployment.

---

## **2\. Scope**

This SOP applies to **all staff and departments** within the AI-SDLC environment who are involved in **purchasing or leasing** assets (hardware, software, data sets, or third-party AI services) used in **AI product development**, QA, staging, or production.

**Exclusions**:

* Simple office supply orders.  
* Personal computing devices not used for AI or regulated data processing.  
* Non-technical contracts unrelated to the AI-SDLC or AI-IRB compliance.

---

## **3\. Definitions**

* **AI-IRB Liaison**: The individual ensuring that any procurement activity related to AI models, data, or tools meets ethical and regulatory guidelines specified by the AI-IRB.  
* **Requisitioner**: The person initiating a formal request for an asset.  
* **Requester**: Any SDLC staff or business unit who identifies the **need** for an AI-related or general resource purchase.  
* **Procurement Tracking Tool**: A software/database that tracks each purchase request from initiation to completion.  
* **Capital Equipment Justification**: Detailed rationale required for higher-cost or strategic assets (e.g., specialized AI hardware, large-scale GPU clusters).  
* **Approval Threshold**: Specific budgetary or regulatory limit requiring additional AI-IRB or CFO sign-off.  
* **Data Resource**: Any purchased or licensed dataset used for training or validating AI models, subject to AI-IRB data privacy and ethical usage constraints.
* **Authorized AI Agent**: An AI system or autonomous agent granted specific governance privileges, approved by the AI-IRB.

---

## **4\. Roles and Responsibilities**

| Role | Responsibilities |
| ----- | ----- |
| **Requester** | 1\. Identifies the need for an AI-related or standard asset. 2\. Completes Procurement Request Form (including any relevant AI or data constraints). |
| **Requisitioner** | 1\. Validates the request’s alignment with AI-IRB guidelines and technical requirements. 2\. Prepares the Purchase Order (PO). 3\. Tracks request lifecycle. |
| **AI-IRB Liaison** | 1\. Ensures that assets subject to AI-IRB approval meet documented ethical and compliance conditions. 2\. Advises Requisitioner on data usage or model licensing restrictions. |
| **Chief Financial Officer (CFO)** | 1\. Reviews and signs off on PO if it exceeds the Approval Threshold. 2\. Confirms budget availability and strategic alignment. |
| **CTO / Owner** | 1\. Oversees overall procurement policy for AI systems. 2\. Ensures synergy with broader AI-SDLC objectives. |
| **Office Manager** (back-up) | 1\. May place the order if the requisitioner is not available. 2\. Informs Requisitioner & Requester of delivery schedules. |
| **Asset Manager** | 1\. Updates asset-tracking database upon receipt. 2\. Manages warranties, licenses, compliance re-check for AI usage. |

---

## **5\. Metrics**

1. **Time-to-Purchase**  
   * **Definition**: The number of business days from the formal request date to the actual purchase order placement.  
   * **Goal**: Streamline the process without compromising AI-IRB or compliance checks.  
2. **AI-IRB Rework Count**  
   * **Definition**: The number of purchase requests that require re-submission to AI-IRB or legal due to missing or incorrect data usage documentation.  
   * **Goal**: Reduce rework by clarifying AI-IRB constraints early.  
3. **SLA Compliance**  
   * **Definition**: Rate of on-time deliveries meeting the expected AI project schedules.  
   * **Goal**: Maintain agile, timely procurement aligned with rapid AI iteration cycles.

---

## **6\. Procedure Activities**

All procurement activities incorporate **recursive self-improvement subroutines** and **Exochain Peer Reviews** to verify the provenance and compliance of assets under AI-IRB governance.

### **6.1 Identify Procurement Need**

1. **Trigger**:  
   * A new AI project, expansion of existing AI infrastructure, or data licensing requirement discovered.  
   * Requester consults the AI-IRB Liaison if unsure about potential IRB triggers.  
2. **Action**:  
   * **Requester** meets with the **Requisitioner** (and possibly **AI-IRB Liaison**) to detail the technical and ethical usage aspects.  
   * Potential vendor or product list is consulted (see Preferred Vendor/Product List).

### **6.2 Verify AI-IRB or Regulatory Constraints**

1. **Requisitioner** checks if the item meets **AI-IRB** conditions (e.g., large-scale HPC hardware for model training, biometric dataset licensing).  
2. If IRB sign-off is required, the **AI-IRB Liaison** obtains an IRB memo or approval letter ensuring the purchase aligns with ethical guidelines (data usage constraints, licensing terms).

### **6.3 Purchase Order Preparation**

1. **Requisitioner**:  
   * Prepares the **Purchase Order (PO)** using the Procurement Tracking Tool.  
   * For items above **USD $100,000** or any AI-critical item, completes a **Capital Equipment Justification** form.  
2. **CFO**:  
   * If cost is above the threshold, reviews and signs the PO within two business days.

### **6.4 Approvals and Ordering**

1. Once CFO (or delegated signatory) signs the PO, the **Requisitioner** forwards the PO to the **Office Manager** or, if specialized AI technical details are needed, **places the order** themselves.  
2. **Office Manager** or the **Requisitioner** informs the Requester about order status, estimated arrival, and any relevant compliance notes (AI licensing or data usage restrictions).

### **6.5 Receiving, Asset Management, and Payment**

1. **When Asset Arrives**:  
   * **Requisitioner** or **Office Manager** notifies the **Requester**.  
   * **Asset Manager** updates the **asset tracking database** with the relevant details (serial number, license keys, IRB conditions).  
2. **Payment Approval**:  
   * **Requisitioner** verifies correctness (packing slip, invoice) and signs off for Finance to **approve** payment.  
3. **AI Usage Tagging**:  
   * If the item is AI-specific (GPU cluster, specialized data set), the Asset Manager logs any IRB usage constraints (e.g., data usage end date, model recheck intervals).

### **6.6 AI-Specific Considerations**

1. **Data Usage**:  
   * If a purchased dataset is sensitive, a Data Privacy Impact Assessment (DPIA) must be attached.  
2. **Model/Tool**:  
   * Verify if ongoing license fees or monitoring obligations are needed.  
3. **Post-Purchase IRB**:  
   * For high-risk AI assets, the IRB Liaison may schedule a follow-up to ensure real usage aligns with declared purpose.

### **6.7 Procurement Tracking and Reporting**

1. **Key Events** to log in the procurement tracking tool:  
   * PO creation date, CFO approval date, vendor ordering date, asset delivery date, finance payment date.  
2. **Reports**:  
   * Time-lapse from request to order.  
   * IRB rework occurrences.  
   * On-time vs. delayed deliveries.

---

## **7\. Forms**

* **Purchase Order Form**  
* **Capital Equipment Justification Form** (for AI HPC hardware or major AI software licensing)  
* **Preferred Vendor/Product List** (AI tool vendors, data providers, etc.)

---

## **8\. Exemptions**

* **Small ad-hoc purchases** under $500 not involving regulated data or AI hardware are exempt from full CFO or IRB approval but still require minimal tracking.

---

## **9\. Tools / Software / Technology Used**

* **Procurement Tracking Tool**: Central database for all PO statuses, approvals, AI-IRB references.  
* **E-Mail** or **Slack**: Notification and updates.  
* **HR/Finance System**: For final payment sign-off.

---

## **Appendix A: AI-Specific Procurement Considerations**

1. **AI-IRB Submission**:  
   * Provide a brief justification of how the asset ties into your AI use case.  
   * Address any potential biases or data privacy concerns.  
2. **Regulatory**:  
   * If the asset is used for regulated industries (healthcare, finance), ensure separate legal disclaimers or compliance forms.  
3. **Annual IRB Reevaluation**:  
   * If the purchased item has continuing ethical usage implications, expect an annual or semi-annual reevaluation by the AI-IRB.

---

### **Document Revision History**

| Version | Date | Description | Approved By |
| ----- | ----- | ----- | ----- |
| 1.0 | *YYYY-MM-DD* | Initial AI-SDLC version (SOP 1004-01-AI). | CTO |

---

**END OF SOP 1004-01-AI**

@startuml

title "SOP-1004-01-AI\_Procurement-and-Purchasing-for-AI-Enabled-Systems-Sequence-Diagram"

actor "Requester" as REQ  
participant "Requisitioner" as RQN  
participant "AI-IRB Liaison" as IRB  
participant "CFO" as CFO  
participant "Office Manager" as MGR  
participant "Asset Manager" as ASM

REQ \-\> RQN: Submit procurement request (AI or standard asset need)  
note right  
  Requester identifies the need for a product/resource,  
  including AI or data usage info.  
end note

RQN \-\> IRB: Validate if AI-IRB approval is required  
alt AI-IRB Required  
  IRB \-\> RQN: Provide AI-IRB approval or constraints  
else No IRB needed  
  IRB \-\> RQN: IRB not required  
end

RQN \-\> RQN: Prepare Purchase Order (PO)\\nand/or Capital Justification

alt Cost Above Threshold  
  RQN \-\> CFO: Forward PO for CFO sign-off  
  alt CFO Approves  
    CFO \-\> RQN: PO signed  
  else CFO Denies  
    CFO \-\> RQN: PO denied, request revision  
    return PO revision or cancellation  
  end  
else Cost Below Threshold  
  RQN \-\> RQN: Sign internally\\n(no CFO step)  
end

RQN \-\> MGR: Provide final PO for order placement  
MGR \-\> REQ: Update on order status & delivery info  
note over MGR,REQ  
  Office Manager or Requisitioner  
  informs Requester about shipping details  
end note

\== Delivery Phase \==

MGR \-\> ASM: Asset arrives, hand off to Asset Manager  
ASM \-\> ASM: Update asset tracking database\\n(record license, IRB constraints)  
ASM \-\> RQN: Confirmation and invoice check  
RQN \-\> CFO: Payment sign-off (if needed)  
CFO \-\> ASM: Payment confirmed  
note over ASM  
  Asset is officially in inventory,  
  usage can begin after any final checks  
end note

@enduml

**Short textual explanation**:  
This sequence diagram illustrates the **end-to-end procurement flow** under SOP-1004-01-AI. The **Requester** triggers a purchase request, the **Requisitioner** determines if AI-IRB approval is needed and manages the Purchase Order. If the cost is above a threshold, the **CFO** signs off. The **Office Manager** or Requisitioner places the order, and once delivered, the **Asset Manager** updates the asset records and coordinates payment.  


[image1]: ../diagrams/SOP-1004-01-AI.PNG