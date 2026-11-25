"""Fix Human Sleep: Funniest Patch Note.

Writes one patch-note line about human sleep being fixed to
$MAKEFUN_OUTPUT_DIR/entry.txt. Pure stdlib, deterministic: the same
line, byte for byte, on every run.

The joke: your brain behaves like a browser. The moment you close
your eyes it opens a dozen tabs of unfinished thoughts, so sleep
never loads. The fix closes the tabs at bedtime — the patch-note
voice does the work, no setup outside the line itself.
"""

import os

# One line, under 160 characters, no title, no explanation.
LINE = (
    "Fixed a bug where closing your eyes opened twelve tabs of "
    "unfinished thoughts; tabs now close at bedtime."
)


def main() -> None:
    out_dir = os.environ["MAKEFUN_OUTPUT_DIR"]
    # The grader owns this directory: create it only if missing,
    # clear only its contents, never remove the directory itself.
    os.makedirs(out_dir, exist_ok=True)
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.unlink(path)
    line = LINE.strip()
    # Single line, under 160 characters: the competition's hard limits.
    assert "\n" not in line, "entry must be a single line"
    assert 0 < len(line) < 160, "entry must be 1-159 characters"
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(line)
    # Verify the artifact the judge will read is exactly the line,
    # byte for byte -- the grader scores /output/entry.txt, not stdout.
    with open(os.path.join(out_dir, "entry.txt"), "rb") as f:
        assert f.read() == line.encode("utf-8"), "written bytes mismatch"


if __name__ == "__main__":
    main()
