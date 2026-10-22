# INSTALL

## Claude Code — global
Copy each skill directory into:

`~/.claude/skills/`

Example:

```bash
cp -r skills/yt-* ~/.claude/skills/
```

## Claude Code — project local

```bash
mkdir -p .claude/skills
cp -r skills/yt-* .claude/skills/
```

## No Claude Code
Paste the contents of the desired `SKILL.md` at the top of a Claude chat.

## First run

1. Fill `templates/channel_profile.md`
2. Run `/yt-showrunner`
3. Provide your channel URL/data
4. Let the skill decide MAKE / REVISE / KILL
