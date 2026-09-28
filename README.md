# Latinviva Skills

Practise Latin in your own AI tool through short conversations, grammar explanations and vocabulary review.

This repository contains learning skills, bundled references, and usage and validation documentation. Website, App and business backend source code are maintained separately.

**Status: all three skills are drafts. There are no formal releases yet; compatibility with host tools and teaching behaviour still need validation.**

## Skills

| Skill | Purpose | Entry point |
| --- | --- | --- |
| latin-conversation | Practise short dialogues with optional hints and focused corrections | [Skill instructions](skills/latin-conversation/SKILL.md) |
| latin-grammar | Understand forms, syntax and translations; explore ambiguity and practise a specific point | [Skill instructions](skills/latin-grammar/SKILL.md) |
| latin-vocabulary | Practise a defined word set while tracking independent recall, hints and revealed answers separately | [Skill instructions](skills/latin-vocabulary/SKILL.md) |

## Usage

Each `skills/<name>/` directory is a self-contained package. Import the whole directory, including `references/`, into the skill location supported by your AI tool. Follow that tool's current installation documentation; no unverified universal install command is provided here.

Try one of these requests:

- Conversation: “I am a complete beginner. Help me practise one Latin greeting with English hints.”
- Grammar: “Does puellae always mean girls? Explain the possible readings.”
- Vocabulary: “Ask five questions from the bundled word list, one at a time. Track answers reached with hints separately.”

`agents/openai.yaml` provides optional display metadata for a specific host tool; it is not proof of compatibility. The teaching workflow lives in `SKILL.md`. See the [behaviour evaluation scenarios](docs/skill-evaluation.md) for validation criteria.

Repository documentation, skill instructions, metadata and contribution text are maintained in English. Latin examples retain their original language. During practice, skills follow the learner's requested explanation language.

## Models and costs

Your AI tool reads the skill instructions and local references. Model calls use your own subscription or API allowance. The skills require no Latinviva account and do not call company model APIs, Dify, speech services or backend services. There is no company-funded model fallback.

The skills include no usage telemetry, do not upload learning records and do not access your App history. Local notes outside the current conversation are saved only when you request them. Downloading skill files does not make model usage free.

## Content and licensing

The references are small original teaching drafts, not exports of the App's private question bank or Dify prompts. Sentences are constructed teaching examples, not ancient quotations, certified assessments or records of real host-tool tests.

Licences for code and teaching materials have not yet been selected. Access to these files does not itself grant an open-source licence. Licensing and compatibility documentation must be completed before a formal release; see the [release checklist](docs/release-checklist.md).

## Local validation

Requires Python 3.9 or newer. No third-party packages, model calls or network access are needed:

```bash
python3 scripts/validate.py
```

Checks skill directories, frontmatter, bundled references, the catalog and documentation links. Passing structural checks does not establish that model behaviour has been validated.
