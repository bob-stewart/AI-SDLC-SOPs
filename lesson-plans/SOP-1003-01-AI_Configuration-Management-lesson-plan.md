# Lesson Plan Draft: Configuration Management

**SOP Reference:** SOP-1003-01-AI_Configuration-Management

## Objective

This SOP establishes a consistent, controlled, and repeatable method for configuring, updating, and managing development, QA, staging, and production environments for AI-related systems. It clarifies responsibilities, processes, and quality checks to ensure changes are systematically planned, tested, documented, and reviewed, including where AI-IRB considerations apply.

## Audience & Applicability

Applies to all configuration changes (software, hardware, environment parameters, etc.) within the AI Systems Development Life Cycle (AI-SDLC). It includes management of AI model versions, data pipelines, HPC infrastructure, cloud or on-prem deployments, and any other environment or component whose change could affect system performance, functionality, or compliance. It also covers the integration of AI-IRB reviews where changes pose potential ethical/compliance impact or risk to end-users.

## Key Definitions

- No key definitions provided.

## Key Roles

- **Configuration Manager**: Maintains the configuration management plan, tracks all changes, ensures CR documentation is complete, and updates the CI repository.
- **AI Development Lead**: Proposes model/data changes, ensures changes follow coding standards, and coordinates with the AI-IRB Liaison for high-risk modifications.
- **AI-IRB Liaison**: Determines if a proposed change triggers an AI-IRB review, coordinates the review process, communicates acceptance conditions.
- **QA Representative**: Reviews, tests, and validates changes before they are moved beyond QA environment.
- **Operations Team**: Implements changes in staging/production, maintains environment integrity, ensures correct rollback plan, and monitors post-deployment.
- **Project Manager**: Oversees scheduling, resources, risk management, and ensures synergy with all project deliverables; escalates complex CRs if needed.
- **Product Owner**: Approves significant changes, signs off on user impact statements, ensures alignment with business objectives.

