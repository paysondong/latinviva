# Skills release checklist

This repository publishes skill packages and related documentation only. All three skills are currently drafts; committing files is not a formal release.

## Before release

- Each skill is self-contained: installing its directory alone preserves access to its references.
- Packages contain no company credentials, user data, private question banks or unauthorised materials.
- Core tasks use the learner's own AI, with no company service calls, background telemetry or company-funded fallback.
- `python3 scripts/validate.py` passes, and [behaviour evaluation](skill-evaluation.md) is completed in the target tool.
- Code and teaching-material licences, verified tools/models and known limitations are documented.
- Documentation, metadata, commit messages and release notes are in English; Latin teaching examples retain their original language.
- Catalog status, version and compatibility records are updated before the corresponding version is released. Drafts are not labelled as released.

## Release notes

Describe actual capabilities, fixes and limitations. Clearly distinguish constructed teaching examples from real execution records. Do not exaggerate outcomes or list untested tools as compatible.

A website may reference published skill information from this repository, but website source code and deployment configuration do not belong here.
