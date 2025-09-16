# Lesson Plan Draft: Incident Tracking

**SOP Reference:** SOP-1061-01-AI_Incident-Tracking

## Objective

This SOP describes the standardized method for **incident tracking** within the AI-SDLC environment to ensure all production incidents (defects) are reported, triaged, documented, and resolved efficiently.

## Audience & Applicability

Applies to all AI-related production incidents that occur post-deployment, including software malfunctions, data quality anomalies, or user-facing disruptions.

## Key Definitions

- **Incident**: Any unexpected behavior, defect, or anomaly in production systems requiring immediate action.
- **Incident Logging**: The process of recording details about the incident, such as date/time, severity, steps.
- **AI-IRB**: The internal/external AI Institutional Review Board ensuring compliance with ethical AI use.
- **Severity Level**: Classification of incident urgency (e.g. Emergency, High, Medium, Low) to set resolution priority.
- **Root-Cause**: The fundamental technical or procedural reason behind the incident.
- **SLA**: Service Level Agreement specifying commitments on incident response & resolution.
- **Production**: The environment or set of systems actively serving end-users or clients.

## Key Roles

- **Defect Reporter**: Identifies and reports an incident, providing essential info (symptoms, environment, steps to reproduce).
- **Technical Support**: Acts as the funnel for external client incidents; logs or rejects with explanation if incomplete; escalates for triage.
- **Quality Assurance**: Oversees the centralized tracking system (e.g., SQA Manager); validates severity, ensures thorough documentation.
- **AI-IRB Liaison**: Reviews incidents with ethical implications; ensures compliance with AI responsibility guidelines.
- **Development**: Investigates, fixes code or data issues, re-tests, and coordinates release of patches or emergency pushes.
- **Operations**: Confirms production environment readiness for patches; coordinates with QA to deploy fixes safely.
- **Project Manager**: Monitors incident resolution progress; communicates updates to stakeholders, ensures SLA adherence.

