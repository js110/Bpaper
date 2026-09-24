"""Build the standalone LaTeX source archive from the current manuscript."""

from pathlib import Path
from zipfile import ZIP_DEFLATED, ZipFile
import json


ROOT = Path(__file__).resolve().parents[1]
PAPER = ROOT / "paper"
FILES = [
    "main.tex", "numbers.tex", "review_numbers.tex", "references.bib",
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
    output = PAPER / "manuscript_source.zip"
    with ZipFile(output, "w", ZIP_DEFLATED) as archive:
        for name in FILES:
            archive.write(PAPER / name, name)
        for name in IMAGEGEN:
            archive.write(ROOT / "research" / "imagegen" / name, f"imagegen/{name}")
    (ROOT / "research" / "source_bundle_files.json").write_text(
        json.dumps(FILES + [f"imagegen/{name}" for name in IMAGEGEN], indent=2)
        + "\n",
        encoding="utf-8",
    )
    print(output)


if __name__ == "__main__":
    main()
