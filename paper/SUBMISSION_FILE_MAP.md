# PMC Submission File Map

Target journal: **Pervasive and Mobile Computing**

Technical package status: **ready**  
Author declarations/approvals: **pending responsible-author confirmation**

## Files to upload

| Submission item | Repository file | Notes |
|---|---|---|
| Main manuscript PDF | `paper/main.pdf` | 27-page Elsevier review-layout manuscript |
| LaTeX source archive | `paper/PMC_submission_source.zip` | Flat one-level source; independently compiled and text-matched to `main.pdf` |
| Highlights | `paper/highlights.docx` | Five acronym-free bullets, each <=85 characters |
| Supplementary material | `paper/supplement.pdf` | 58-page complete technical record / extended evidence |
| Cover letter | `paper/COVER_LETTER_DRAFT.md` | Convert/paste after responsible-author review |
| Source manifest | `paper/PMC_submission_manifest.json` | Internal verification; normally not necessary to upload |

## Files not intended as journal submission files

Do **not** upload these as manuscript source unless the editor explicitly asks:
- `paper/full_research_record.tex`
- `paper/manuscript_source.zip`
- internal review/checklist files;
- raw experiment directories;
- third-party article full texts;
- the raw Microsoft GeoLife archive;
- GitHub Actions workflow files.

The reproducibility repository can remain linked separately.

## Final author-owned checks before pressing Submit

Complete `paper/AUTHOR_CONFIRMATION.md`. In particular:
1. confirm author spelling/order/affiliations/corresponding author;
2. confirm all authors approved the final manuscript;
3. supply competing-interests wording;
4. supply CRediT roles if required by the submission system;
5. confirm all grants and funder roles;
6. confirm any GeoLife secondary-data ethics/data-use wording required by the journal/institution;
7. handle any journal disclosure requirements the authors wish/need to complete;
8. decide whether the submitted code should receive a versioned GitHub release and/or immutable DOI.

## Verified technical facts

Final validation workflow: GitHub Actions run **36369413681**.

The workflow verified:
- all 28 automated tests pass;
- development manuscript compiles;
- flat Editorial Manager source compiles independently;
- development and flat PDFs both have 27 pages;
- extracted PDF text is identical between the two builds;
- supplementary technical material compiles to 58 pages;
- no final unresolved references;
- no final undefined control sequences;
- no final oversized floats;
- no final overfull boxes caught by the quality gate;
- the source archive contains no subfolders.

Repository status:
- `technical_ready = true`
- `submission_ready = false` only until author-owned confirmations are completed.
