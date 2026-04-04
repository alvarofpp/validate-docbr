# Review

Review the current changes following validate-docbr patterns.

---
description: Reviews current changes following project patterns.
allowed-tools: Read Grep Glob Bash
agent: reviewer
---

1. Run `git diff` to see unstaged changes
2. Run `git diff --cached` to see staged changes
3. If there are no changes, run
   `git log -1 --format="%H" | xargs git diff HEAD~1`
   to review the last commit

Analyze all changes found following the project review checklist.

$ARGUMENTS
