---
name: video-research-ingestion
description: Auto-invoke when the user asks to learn from a video, training recording, tutorial, webinar, screen recording, social video, or video URL; extract instructions, transcript, frames, steps, best practices, or claims from video; compare what a speaker says with visible video evidence; or turn prerecorded training into notes, workflows, skills, or implementation guidance.
status: approved
---

# Video Research Ingestion

## Purpose

Turn videos into usable operating knowledge by combining transcript, representative frames, source metadata, and verification notes. Use this for training recordings, tutorials, product walkthroughs, webinars, and social clips where the system needs to understand both what was said and what was shown.

## When To Use

Use this skill when the user provides or references:

- A video URL, recording, reel, webinar, course module, screen recording, demo, or tutorial.
- A request to "watch," summarize, extract steps, identify best practices, validate claims, or make a workflow from a video.
- A training recording that should become documentation, SOPs, prompts, skills, or implementation tasks.
- A video where visual context matters, such as UI walkthroughs, diagrams, commands, slides, or code.

## When Not To Use

Do not use this skill for normal web pages, articles, PDFs, or audio-only files unless the user specifically wants video-style frame extraction or multimodal review. Use `markitdown`, `scrapling-research`, or ordinary research first when those are a better fit.

## Workflow

1. **Confirm source and permission.** Note whether the video is public, user-provided, or private. Do not bypass access controls or download restricted content without permission.
2. **Collect metadata.** Capture source URL or file path, title if available, creator, duration, publish date if known, and access date.
3. **Get transcript first.** Prefer official captions, platform captions, or local transcript files. If unavailable and the user approved transcription, use the cheapest adequate transcription model or local tool.
4. **Extract representative frames.** Capture frames around topic changes, command displays, UI changes, slide transitions, diagrams, or moments referenced in the transcript.
5. **Align speech and visuals.** Connect key transcript excerpts to timestamps and frame evidence. Note where visual evidence confirms, contradicts, or adds detail to the spoken instruction.
6. **Distill operational knowledge.** Convert the video into notes, steps, commands, best practices, risks, and possible reusable workflows or skills.
7. **Verify claims.** For tool commands, APIs, install steps, or current product claims, validate against official docs, local CLI help, command output, or primary sources.
8. **Store outputs.** Save durable notes under `vault/`, `projects/`, or `logs/video-research/` depending on the user's OS structure. Keep raw downloads or generated media out of git unless intentionally approved.
9. **Refresh memory.** Run memory registration and indexing after writing durable Markdown.

## Suggested Local Tooling

Prefer local and reversible tools:

```bash
yt-dlp --write-auto-subs --write-subs --sub-lang en --skip-download "<url>"
yt-dlp -f "bv*+ba/b" -o "video.%(ext)s" "<url>"
ffmpeg -i video.mp4 -vf fps=1/30 frames/frame-%04d.jpg
python3 memory/scripts/index_markdown.py
```

Use platform terms, copyright rules, and user permissions as constraints. If a site blocks download but the user can view it in an authenticated browser, prefer user-provided exports, screenshots, or manual notes over bypass attempts.

## Output Format

For research notes, use this structure:

```markdown
# Video Research Note

## Source
- URL or file:
- Title:
- Creator:
- Duration:
- Accessed:

## Purpose

## Transcript Summary

## Visual Evidence

| Timestamp | Frame / visual | What it shows | Why it matters |
|-----------|----------------|---------------|----------------|

## Instructions Or Claims

| Claim / instruction | Evidence | Verified? | Notes |
|---------------------|----------|-----------|-------|

## Actionable Takeaways

## Recommended Workflows Or Skills

## Open Questions
```

## Operating Rules

- Separate what the speaker said from what the video visibly shows.
- Do not treat video claims as true until verified.
- Use timestamps so the user can audit conclusions.
- Use the cheapest adequate transcription path and escalate only when quality is insufficient.
- Do not commit raw video, audio, or large frame folders unless explicitly approved.
- If the video contains sensitive training material, store only the minimum durable notes needed for future use.
