"""Build Editorial Manager-friendly submission archives from the current manuscript."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import json


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
FILES = [
    "numbers.tex", "review_numbers.tex", "references.bib",
    "elsarticle.cls", "elsarticle-num.bst", "main_table_revision.tex",
    "matched_table.tex", "recent_matched_table.tex", "informed_table.tex",
    "prior_diagnostic_table.tex", "task_area_table.tex", "attacks.pdf",
    "tradeoff.pdf", "recent_tradeoff.pdf", "calibration.pdf",
    "sensitivity.pdf", "recent_commute_zoom.pdf",
    "figures/system_architecture.png", "figures/bsp_workflow.png",
    "SOURCE_README.md",
]
IMAGEGEN = ["prompts.json", "architecture_edit_prompt.txt", "manifest.json"]


def main() -> None:
    """Create a flat LaTeX source archive plus a separate AI-provenance archive."""
    manuscript_output = PAPER / "manuscript_source.zip"
    provenance_output = PAPER / "ai_provenance.zip"

    main_text = (PAPER / "main.tex").read_text(encoding="utf-8")
    main_text = main_text.replace(
        "{figures/system_architecture.png}", "{system_architecture.png}"
    ).replace(
        "{figures/bsp_workflow.png}", "{bsp_workflow.png}"
    )

    archived = ["main.tex"]
    with ZipFile(manuscript_output, "w", ZIP_DEFLATED) as archive:
        archive.writestr("main.tex", main_text)
        for name in FILES:
            arcname = Path(name).name
            archive.write(PAPER / name, arcname)
            archived.append(arcname)

    with ZipFile(provenance_output, "w", ZIP_DEFLATED) as archive:
        for name in IMAGEGEN:
            archive.write(ROOT / "research" / "imagegen" / name, name)

    (ROOT / "research" / "source_bundle_files.json").write_text(
        json.dumps(
            {
                "manuscript_source.zip": archived,
                "ai_provenance.zip": IMAGEGEN,
            },
            indent=2,
        )
        + "\n",
        encoding="utf-8",
    )
    print(manuscript_output)
    print(provenance_output)


if __name__ == "__main__":
    main()
