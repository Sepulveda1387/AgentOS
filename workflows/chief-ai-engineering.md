# Chief AI Engineering Workflow

cadence: on demand
required_tools: memory index, installed skills, optional provider CLI/API

Use this workflow when a request needs deliberate AI model selection, prompt architecture, paid API guardrails, or model-specific quality control.

## Steps

1. **Classify the AI task.**
   - Text, code, research, image, audio, video, data, automation, or mixed modality.
   - Low, medium, or high risk.
   - One-off output or repeatable workflow.

2. **Load local context first.**
   - Search memory for prior model decisions.
   - Check installed skills and connection docs.
   - Read only the project or workflow files needed for the request.

3. **Define success.**
   - Output format.
   - Audience.
   - Quality bar.
   - Cost or credit constraints.
   - Deadline or latency needs.
   - Verification method.

4. **Route the model.**
   - Cheapest adequate model for easy-to-verify extraction or transformation.
   - Stronger reasoning model for ambiguous strategy, architecture, or high-stakes synthesis.
   - Modality-native model for images, audio, video, or media generation.
   - Deterministic CLI or parser where model judgment is unnecessary.

5. **Design the prompt.**
   - Preserve the user's original intent.
   - Include context, constraints, source material, output schema, and verification criteria.
   - Add negative instructions only when they prevent likely failure.

6. **Check paid-service gates.**
   - Credentials stay in `.env`.
   - Balance or credits are confirmed before production runs.
   - Small tests come before expensive generations.
   - External calls are only made when approved or clearly requested.

7. **Validate and record.**
   - Compare output to user intent and constraints.
   - Note model failures, cost risk, and fallback.
   - If the pattern will recur, propose a reference note, workflow, or skill draft.

## Deliverable

Return a concise recommendation:

- Recommended model or tool:
- Why it fits:
- Cheapest safe test:
- Prompt or workflow:
- Verification:
- Cost or credit risk:
- Fallback:
