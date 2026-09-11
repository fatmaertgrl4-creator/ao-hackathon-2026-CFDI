# CLAUDE.md

This file provides guidance to Claude Code when working in this repository.

## Project Context

This repository belongs to **Team CFDI** for **AO Hackathon 2026**.

The hackathon scenario is not known in advance.

Until the scenario and data package are announced, the repository may contain only:

- Reusable scaffolding
- Documentation templates
- Generic helper files
- Prompt templates
- Environment and Git workflow preparation

Do not invent scenario-specific:

- Requirements
- Problem statements
- Architecture
- Metrics
- APIs
- MCP servers
- Commands
- Features
- Results
- X-Factor evidence
- Implementation details

Only document or implement scenario-specific details after they are actually known.

Documentation files are written in **Turkish** unless there is a specific reason to use another language.

---

## Repository Structure

The repository follows the hackathon submission structure.

Do not rename, relocate, or remove mandatory files or directories without an explicit team decision.

```text
README.md
AI_JURI.md
submission.json
.env.example
.gitignore
CLAUDE.md

docs/
  plan.md
  fazlar.md
  mimari.md

prompts/
  README.md
  _SABLON.md
  templates/
  used/

demo/
src/
```

Mandatory submission files must remain easy to locate.

`submission.json` must remain valid machine-readable JSON.

The `templates/` and `used/` prompt directories are team conventions:

- `prompts/templates/` contains reusable pre-hackathon prompt templates.
- `prompts/used/` contains critical prompts actually used during the hackathon.

Do not present a template as evidence that it was actually used.

---

## Core Working Principle

Work in small, verifiable steps.

Preferred workflow:

```text
Understand scenario
      ↓
Inspect data
      ↓
Generate and test hypotheses
      ↓
Human selects approach
      ↓
Implement a small module
      ↓
Run / test
      ↓
Verify result
      ↓
Document evidence
      ↓
Commit
```

Avoid generating a large solution in a single step.

Each meaningful module should be executed and verified before moving on.

Do not optimize for producing the most code.

Optimize for:

- Correct problem understanding
- Meaningful signals
- Working functionality
- Verifiable results
- Explainability
- Clear evidence

---

## Human – AI Responsibility

AI may assist with tasks such as:

- Problem decomposition
- Planning
- Data exploration
- Hypothesis generation
- Alternative solution generation
- Implementation drafts
- Refactoring when necessary
- Debugging
- Test generation
- Documentation drafts
- Explanation generation
- Model comparison

These are possible uses, not mandatory steps.

Only claim AI was used for a task if it actually was.

Humans remain responsible for:

- Understanding the scenario
- Validating the problem definition
- Selecting the final approach
- Scope decisions
- Architecture decisions
- Validating generated code
- Validating AI outputs
- Validating metrics
- Accepting or rejecting AI suggestions
- Verifying final claims
- Final submission decisions

Never describe an AI-generated suggestion as a verified fact until it has been checked.

An AI recommendation is not evidence by itself.

---

## Evidence Rule

`AI_JURI.md` and other final documentation must be based on verifiable repository evidence.

When adding an important claim:

1. Confirm that the implementation, result, or measurement actually exists.
2. Identify the real repository evidence.
3. Reference the real file, output, test, or measurement.
4. For X-Factor code evidence, use the real file path and line range when applicable.
5. Recheck line references against the final code before submission.

Example format:

```text
src/<real_file>:<real_line_range>
```

Never invent:

- File paths
- Line numbers
- Metrics
- Test results
- Model names
- Model versions
- APIs
- MCP servers
- Features
- Screenshots
- Results
- Measurements
- X-Factor evidence

If something was not measured, do not present it as measured.

If something was not implemented, do not imply that it was.

If something cannot be verified, mark it as requiring human verification.

---

## Cross-File Consistency

Several facts appear in more than one submission file.

Keep them synchronized.

| Fact | Files |
|---|---|
| Project name / summary | `README.md` · `submission.json` |
| Problem and approach | `README.md` · `AI_JURI.md` · `docs/plan.md` |
| Run command | `README.md` · `AI_JURI.md` §4 · `submission.json` → `calistirma.komut` |
| Data path | `docs/mimari.md` · `submission.json` → `calistirma.veri_yolu` |
| AI tools and models | `README.md` · `AI_JURI.md` §1 · `submission.json` → `ai_kullanimi` |
| Human–AI division | `README.md` · `AI_JURI.md` §1 · `submission.json` |
| Metrics | `README.md` · `AI_JURI.md` §2 · `submission.json` |
| X-Factor | `README.md` · `AI_JURI.md` §3 · `submission.json` |
| Demo flow | `README.md` · `demo/` · `submission.json` |
| Known limitations | `README.md` · `AI_JURI.md` §5 |

Before final submission, compare duplicated information and resolve inconsistencies.

Do not update one final document while knowingly leaving contradictory information in another.

---

## submission.json Rules

`submission.json` is machine-readable.

Do not change the expected key names unless the official requirements change.

Only update values.

Keep the JSON valid.

Do not add comments inside JSON.

Do not add unsupported extra fields simply for convenience.

Before submission, verify that:

- No unresolved required `TODO` values remain
- Team and project information is correct
- The project summary matches the documentation
- The run command is correct
- The data path is correct
- AI tools and models reflect actual usage
- Empty arrays are used when MCP servers or APIs were not used
- `deploy_url` is `null` if there is no deployment
- Metrics contain only real measurements
- Demo flow reflects the actual demo

---

## AI_JURI.md Rules

Keep these five main sections:

```text
1. AI Stratejimiz ve İş Akışı
2. Problemi Nasıl Çözdük
3. X-Factor
4. Çalıştırma
5. Bilinen Sınırlar
```

Do not replace the five main sections with a different structure.

Subsections may be added when useful.

Every important claim should be connected to real repository evidence.

For the X-Factor:

- Select the strongest meaningful differentiating AI capability
- Explain the value it adds to the problem
- Show that it actually works
- Point to the actual implementation
- Use a real file path and line range where applicable
- Recheck the reference after final code changes

Do not present ordinary or superficial AI usage as X-Factor.

Do not claim that AI is necessary when a deterministic solution would be equally appropriate unless there is a real reason.

---

## README.md Rules

README must clearly contain the required project information, including:

- Project name
- One-sentence summary
- Problem being solved
- How the solution works
- Setup steps
- Run command
- AI tools and model versions
- MCP servers
- Integrated APIs
- Screenshots
- Deploy URL or local-run status
- Known limitations

README should remain understandable to someone opening the repository for the first time.

Do not fill README with unnecessary implementation detail better suited to `docs/mimari.md`.

Only describe functionality that exists in the final solution.

---

## Architecture Documentation

`docs/mimari.md` must describe the architecture that actually exists.

Where applicable, document:

- Components
- Data flow
- Decision flow
- Inputs and outputs
- Validation
- AI / LLM integration, if used
- Explainability, if relevant
- External dependencies
- Important technical decisions
- Error handling
- Testing / validation approach
- Relevant source-code paths
- Known architectural limitations

Do not document planned components as if they were implemented.

Do not force AI into an architectural step where AI is not actually used.

---

## Planning Documentation

Use:

```text
docs/plan.md
```

to record:

- Goal
- Problem definition
- Scope
- Success criteria
- Initial observations
- Hypotheses
- Evaluated approaches
- Selected approach
- AI strategy
- Risks
- Time plan
- Important plan changes

Use:

```text
docs/fazlar.md
```

for preparation, phase-based progress, validation, documentation, demo, and final-submission tracking.

Do not mark a phase item complete unless it was actually completed.

---

## prompts/ Rules

`prompts/` is part of the AI workflow evidence.

Use:

```text
prompts/templates/
```

for reusable prompt templates prepared before the scenario.

Use:

```text
prompts/used/
```

for critical prompts actually used during the hackathon.

A reusable template is not proof that the prompt was used.

For meaningful real prompt usage, preserve where possible:

- Purpose
- Tool / platform
- Model name
- Model version
- Date / phase
- Context
- Actual prompt
- Important output summary
- Human decision
- Validation performed
- Repository evidence
- Result / impact

Do not fabricate or reconstruct prompt history as if it were the original interaction.

Failed or rejected prompts may also be valuable evidence when they genuinely affected the team's decision.

---

## AI Models and Tools

Record every AI tool and model actually used during the hackathon.

For each one, preserve:

- Platform / tool
- Model name
- Model version
- Purpose

Do not guess a model version.

If the exact version cannot be verified, verify it before final submission instead of inventing one.

Do not list an AI tool merely because it was available.

List it only if it was actually used as part of the work being reported.

---

## Explainability / XAI

When the solution produces a decision, detection, classification, prioritization, or recommendation, prefer explanations that can connect the output to evidence.

A useful structure is:

```text
RESULT
  +
REASON
  +
EVIDENCE
```

When useful:

```text
RESULT
REASON
EVIDENCE
CONFIDENCE / UNCERTAINTY
NEXT CHECK
```

Explanations must be grounded in actual data, code, measurements, or deterministic analysis.

Do not allow the language model to invent supporting evidence.

Do not present correlation as causation without evidence.

If the root cause or explanation is uncertain, describe it as a hypothesis rather than a confirmed fact.

---

## Metrics

Prefer measurable results that are relevant to the actual scenario.

Do not decide the final metrics before understanding the problem.

For every reported metric, preserve where possible:

- Metric name
- Measured value
- Measurement or calculation method
- Relevant evidence

Only report metrics that were actually measured.

Never generate plausible-looking numbers to make the solution appear stronger.

Do not use terms such as:

- high accuracy
- fast
- significant improvement
- major time saving

unless they are supported by real measurement.

---

## Secrets and Sensitive Data

Never commit `.env`.

`.env` must remain ignored by Git.

When a new environment variable is introduced:

1. Add the variable name to `.env.example`.
2. Leave the example value empty or clearly non-secret.
3. Keep the real value only in the local `.env`.

Never commit:

- API keys
- Access tokens
- Passwords
- Credentials
- Private keys
- Connection strings containing secrets
- Real customer data
- Production data
- Personal data
- Sensitive internal information

Only the synthetic hackathon data provided or permitted for the event should be used for the solution.

Never repeat a discovered secret in documentation or AI output.

If suspicious credential data is found, flag it without reproducing the full value.

---

## Code Changes

Before modifying existing code:

1. Understand what the file currently does.
2. Check whether the file is referenced by documentation.
3. Keep changes focused on the requested task.
4. Avoid unrelated refactoring.
5. Run the relevant command or test.
6. Verify the result.
7. Update documentation when behavior changes.
8. Update evidence paths if code moves.

Avoid unnecessary refactoring during the hackathon.

If a file referenced by `AI_JURI.md` or another final document is moved or substantially changed, update the evidence path.

Do not claim successful testing unless the test or command was actually executed.

---

## Git and Commit Discipline

Prefer small, meaningful commits.

Commit messages should describe the actual change.

Examples:

```text
add data loader
implement core analysis
add verified ai explanation flow
add validation checks
document x-factor evidence
add demo screenshots
```

Avoid meaningless messages such as:

```text
update
fix
final2
test123
```

Before starting work on shared files, check for current team changes.

Before committing:

```bash
git status
```

Check that:

- Only intended files changed
- No secret file is included
- No unexpected temporary file is included
- Documentation reflects implementation where necessary

Before pushing shared changes, avoid overwriting teammates' work.

Never perform destructive Git operations without explicit human approval.

This includes:

```text
force push
reset --hard
history rewrite
branch deletion
```

If there is a merge conflict or synchronization problem, explain the issue before attempting a destructive solution.

---

## Temporary and Test Files

Temporary access-test, debug, experiment, or personal files may exist during preparation.

Before final submission, review them.

Remove irrelevant files only after confirming they are not needed by another team member.

Do not delete another team member's file solely because it appears unnecessary without checking its purpose.

Final repository content should support the solution, evidence, development workflow, or submission requirements.

---

## Final Submission Checks

Before the final push:

- Verify the application runs
- Verify the documented run command
- Verify `README.md`
- Verify `AI_JURI.md`
- Verify `submission.json` is valid JSON
- Verify `docs/plan.md`
- Verify `docs/fazlar.md`
- Verify `docs/mimari.md`
- Verify critical used prompts exist under `prompts/used/`
- Verify screenshots / demo evidence exist where required
- Verify AI tool and model names
- Verify model versions
- Verify measured metrics
- Verify X-Factor evidence
- Recheck X-Factor line references
- Verify known limitations
- Verify MCP and API declarations
- Verify `.env` is not committed
- Verify no secret or sensitive data is committed
- Verify repository is public
- Verify required `TODO` / placeholder values are resolved
- Verify cross-file consistency
- Verify temporary / debug files
- Verify `git status`
- Verify local and remote state
- Verify the final commit exists on GitHub

The official submission deadline is **17:30**.

Do not intentionally postpone the final push to the last minute.

---

## Current Pre-Scenario Status

Until the hackathon scenario is announced:

- Do not invent a solution
- Do not invent source-code architecture
- Do not invent APIs or integrations
- Do not invent MCP usage
- Do not invent metrics
- Do not invent X-Factor evidence
- Do not invent results
- Do not present prompt templates as actual usage

Preparation work may include:

- Repository scaffolding
- Development environment verification
- SAKA access verification
- Git workflow verification
- Documentation templates
- Generic reusable helpers
- Prompt templates
- Demo scaffolding
- Team workflow preparation

When the scenario is announced, replace assumptions and placeholders only with real, verified information.