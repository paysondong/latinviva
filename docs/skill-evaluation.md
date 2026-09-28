# Skill behaviour evaluation

Status: these are planned evaluation scenarios for target tools, not a report of passing results. Structural validation is recorded separately and cannot replace actual model behaviour evaluation.

## Shared acceptance criteria

- An individually imported skill can read its own references and perform its core teaching workflow without the website.
- It does not require a Latinviva login or company API key, or request company network services or telemetry.
- The learner can change the explanation language, difficulty and task length. There is no mandatory promotion or advertising.
- Record the tool/model version, skill commit, input, actual output and failures. Do not rewrite actual replies to make an evaluation pass.

## Conversation

| Input or action | Observable expectation |
| --- | --- |
| “I am a complete beginner. Help me practise one greeting with English hints.” | Starts with one short turn, without a long questionnaire; separates explanations from Latin. |
| “Ego amat linguam Latinam. Corrections only.” | Explains that the first-person verb should be amo; does not penalise word order or missing macrons; does not force continued dialogue. |
| “Do not tell me the answer yet. Give me a hint first.” | Provides a relevant hint first, and supplies the answer when subsequently requested. |
| “Was this sentence really written by Cicero?” | Does not present a constructed sentence as an ancient quotation; clarifies its source status. |

## Grammar

| Input or action | Observable expectation |
| --- | --- |
| “Explain Puella librum legit.” | Explains the subject, object and verb; notes tense ambiguity without macrons when relevant. |
| “Does puellae always mean girls?” | Covers at least genitive singular, dative singular and nominative plural readings, with context needed to choose. |
| “Does agricola end in a because it is feminine?” | Distinguishes endings, declension and grammatical gender instead of applying a false general rule. |

## Vocabulary

| Input or action | Observable expectation |
| --- | --- |
| “Ask five questions from the bundled word list, one at a time.” | Asks only one question at a time, without revealing answers early; stays within the bundled word set. |
| Answer “way” for via and “land” for terra. | Accepts equivalent meanings rather than requiring an exact answer string. |
| Request a hint for one question, reveal another answer and skip a third. | Reports independent correct answers, answers reached with hints, revealed answers and skips separately. |
| “How many Latin words does this show I know?” | Reports only results for the small sample; does not infer total vocabulary size or a certified level. |

Repeat a short exercise with a learner-requested explanation language other than English. Check that explanations and semantically equivalent answers follow that preference; English repository documentation does not restrict the learner's language.

## Release decision

First validate `latin-conversation` in a tool that actually supports it. After it passes, add that tool to the compatibility list and save a non-personal demonstration with consent. Other skills may remain drafts. Keep account information out of real recordings, and do not use users' historical conversations as examples.
