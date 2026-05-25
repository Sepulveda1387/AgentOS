# Video Research Ingestion Workflow

cadence: on demand
required_tools: yt-dlp or platform export, ffmpeg, optional transcription model, memory index

Use this workflow when a video should become searchable knowledge, implementation notes, a workflow, a skill, or a verified operating recommendation.

## Steps

1. **Identify the source.**
   - URL or local file.
   - Public, user-provided, or private.
   - Permission and access constraints.

2. **Create a working area.**
   - Use a temporary folder for downloads, captions, frames, and transcripts.
   - Keep large media out of git unless the user explicitly approves committing it.

3. **Collect transcript.**
   - Prefer official captions or user-provided transcript.
   - If captions are missing, use the cheapest adequate transcription path.
   - Preserve timestamps when available.

4. **Extract frames.**
   - Capture frames at topic changes, visible commands, UI transitions, slides, diagrams, and any timestamp cited in the transcript.
   - Avoid unnecessary frame volume.

5. **Analyze speech and visuals together.**
   - What was said.
   - What was shown.
   - What is implied.
   - What needs independent verification.

6. **Verify actionable claims.**
   - Commands: run `--help`, official docs, or dry-run where safe.
   - Product claims: official docs or primary sources.
   - Best practices: compare with current docs or trusted references.

7. **Write durable notes.**
   - Use `logs/video-research/` for dated research notes.
   - Use `projects/<project>/` when tied to an active project.
   - Use `vault/` for evergreen knowledge.

8. **Refresh memory.**
   - Run `python3 memory/scripts/register_assets.py`.
   - Run `python3 memory/scripts/index_markdown.py`.
   - Verify counts or registry entries before claiming completion.

## Output Checklist

- Source and access date recorded.
- Transcript summary included.
- Visual evidence table included when frames were reviewed.
- Claims separated from verification.
- Takeaways converted into actions, workflows, or skill suggestions.
- Raw media kept out of git unless approved.
