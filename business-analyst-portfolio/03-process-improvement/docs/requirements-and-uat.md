# Requirements and UAT — Request Intake Redesign

## AS-IS workflow
Requester emails shared inbox → coordinator manually categorizes → manager assigns → team resolves → requester follows up for status.

## TO-BE workflow (proposed)
Requester submits standardized form → automatic validation and category → SLA-based queue routing → visible status and alerts → resolution and feedback.

## Business requirements and traceability
| ID | Requirement | User story | Acceptance criterion | UAT test |
|---|---|---|---|---|
| BR-01 | Standardize intake | As a requester I want one form | Mandatory fields validated | UAT-01 |
| BR-02 | Route by category | As an operator I want assigned queues | Correct routing for all supported types | UAT-02 |
| BR-03 | Track SLA | As a manager I want due-date alerts | Alert triggers before threshold | UAT-03 |
| BR-04 | Audit status | As an auditor I need history | All state changes timestamped | UAT-04 |

## UAT scenarios
- UAT-01: Leave required field blank; form blocks submission with actionable error.
- UAT-02: Submit each category; verify the assigned queue matches routing rules.
- UAT-03: Simulate approaching SLA breach; verify alert and escalation.
- UAT-04: Change ticket status twice; verify full timestamped history.

## Assumptions and risks
- Benefits are modeled, not observed.
- Queue mapping requires stakeholder approval.
- Access controls and audit retention need security review.
- Pilot success criterion: measured median cycle-time reduction ≥15% without quality regression.
