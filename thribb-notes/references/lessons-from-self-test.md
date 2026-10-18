# Lessons from building one illustrated article with this skill

Observed in one build (an article about this skill). No learner test.

- Quiz/exercise blocks must not split across pages in the PDF; keep the answer heading with its answer (break-inside: avoid on the block and the details element, break-after: avoid on summary). Check each page's last line for orphaned headings.
- A PDF has no interaction: drop Reveal buttons and notepads, print "Worked answer" and plain "Your notes ____" lines.
- Interactive HTML: Check disabled until a choice is made; changing the choice clears feedback; a wrong attempt must not show the solution; give feedback role=status aria-live=polite. Test the state transitions in a headless browser.
- Figures exported as PNG are not resolution independent; say so, and state the source width. Do not claim a text size at phone width unless measured.
- A "page anatomy" figure should be a miniature page with numbered parts, not a text list.
- Qualify claims about the technique ("in the rebuilt version", "before any letter n") and keep source counts exact (what was read as text vs viewed).
- Colors in formulas follow the same object-color mapping as the figures.
- Hosted pages: in one build the hosting component cropped figures to 3:2 (cover). Check how figures are cropped in the private preview at phone width before publishing; fix with a CSS override if needed. Observed once, not a general claim.
