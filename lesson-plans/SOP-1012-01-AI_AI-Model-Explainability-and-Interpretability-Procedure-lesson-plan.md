# Lesson Plan Draft: AI Model Explainability and Interpretability Procedure

**SOP Reference:** SOP-1012-01-AI_AI-Model-Explainability-and-Interpretability-Procedure

## Objective

This Standard Operating Procedure (SOP) defines the methods and requirements by which the organization ensures **explainability and interpretability** of AI/ML models in production or under development. The procedure establishes guidelines to help internal stakeholders and external regulators understand and validate how AI models make decisions or predictions, while also ensuring compliance with ethical, legal, and AI-IRB (AI Institutional Review Board) requirements.

## Audience & Applicability

Applies to all AI/ML models developed, deployed, or maintained by the organization under the AI-SDLC process, whether they are for internal use or customer-facing. It includes.

## Key Definitions

- No key definitions provided.

## Key Roles

- **AI Dev Team**: Develops or integrates the AI model, including code for generating explainability and interpretability artifacts (e.g., feature importances, local explanations).
- **AI-IRB Liaison**: Reviews the proposed explainability approaches, verifying compliance with ethical, legal, and regulatory guidelines.
- **Product Management**: Ensures the product roadmap includes user-facing or client-facing explainability features when relevant.
- **Data Science Lead**: Oversees the interpretability framework selection, ensuring the correct approach (global vs. local explanations, LIME, SHAP, etc.) is used.
- **Quality Assurance (QA)**: Validates correctness of generated explanations, ensures no critical interpretability issues are found.
- **Operations**: Implements and monitors any production-level model explanation pipelines or scheduled tasks to maintain up-to-date explanation reports.
- **Legal/Compliance**: Verifies that the chosen explanation techniques meet regulatory requirements, particularly in sensitive or high-risk applications.
- **Technical Support**: Provides user or client documentation to help interpret outputs; addresses end-user inquiries on how the model arrived at certain results.
- **Senior Management**: Final decision authority and overall accountability for compliance; reviews escalations from AI-IRB or other stakeholders.

