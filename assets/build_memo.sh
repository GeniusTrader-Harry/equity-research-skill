#!/usr/bin/env bash
# Build [TICKER]_pitch.docx + [TICKER]_pitch.pdf from [TICKER]_pitch.md
#
# Usage:
#   1. Copy this script into your project's working/ directory.
#   2. Copy memo_style.css next to it.
#   3. Set TICKER below (or pass as $1).
#   4. Run: bash build_memo.sh [TICKER]
#
# Requires:
#   - pandoc (md->docx + md->html5)              brew install pandoc
#   - weasyprint (html->pdf)                     pip install weasyprint
#   - pango (libpango binding for weasyprint)    brew install pango
#
# macOS note: weasyprint needs libpango via DYLD_LIBRARY_PATH for the brew-installed pango.

set -euo pipefail

TICKER="${1:-${TICKER:-}}"
if [ -z "$TICKER" ]; then
  echo "Usage: bash build_memo.sh [TICKER]   (or set TICKER env var)" >&2
  exit 1
fi

# Paths — assumes this script lives in working/ and deliverables/ is a sibling
HERE="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
PROJECT_ROOT="$(dirname "$HERE")"
SRC="$PROJECT_ROOT/deliverables/${TICKER}_pitch.md"
OUT_DOCX="$PROJECT_ROOT/deliverables/${TICKER}_pitch.docx"
OUT_PDF="$PROJECT_ROOT/deliverables/${TICKER}_pitch.pdf"
TMP_HTML="/tmp/${TICKER}_pitch.html"
CSS="$HERE/memo_style.css"

if [ ! -f "$SRC" ]; then
  echo "Source not found: $SRC" >&2
  exit 1
fi
if [ ! -f "$CSS" ]; then
  echo "CSS not found: $CSS (copy memo_style.css next to this script)" >&2
  exit 1
fi

echo "Building ${TICKER}_pitch.docx..."
pandoc "$SRC" \
  --standalone \
  -o "$OUT_DOCX"

echo "Building ${TICKER}_pitch.pdf (via pandoc HTML + weasyprint)..."
pandoc "$SRC" \
  --standalone \
  --css="$CSS" \
  -t html5 \
  -o "$TMP_HTML"

DYLD_LIBRARY_PATH=/usr/local/lib weasyprint "$TMP_HTML" "$OUT_PDF"

echo ""
echo "Done."
echo "  DOCX: $OUT_DOCX ($(wc -c < "$OUT_DOCX" | tr -d ' ') bytes)"
echo "  PDF:  $OUT_PDF  ($(wc -c < "$OUT_PDF" | tr -d ' ') bytes)"
