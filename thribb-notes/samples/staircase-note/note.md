# Adding 1 through n by building a rectangle (original sample note)

The rendered version is note.html (figures are in the same folder). This markdown is a plain-text outline of the same note, with figure descriptions in place of images.

- Figure 1 (fig1.png): a staircase of blue blocks, 1, 2, 3 and 4 per row. Question: how many blocks?
- Figure 2 (fig2.png): the staircase inside a 4 by 4 square, missing blocks in red. 16 is too many.
- Exercise: what if a second, upside-down staircase is placed against the first? Reveal: row by row the two copies have 1+4, 2+3, 3+2, 4+1 = 5 blocks.
- Figure 3 (fig3.png): a rectangle 4 tall, 5 wide. 4 x 5 = 20, half is 10.
- Figure 5 (fig5.png): the same with 5 rows, every row 6 blocks.
- General: row k has k + (n + 1 - k) = n + 1 blocks, so 2 x (1 + ... + n) = n (n + 1) and the sum is n (n + 1) / 2. Check at n = 4: 10 (fig4.png).
- Limits: see the banner in note.html. Test sample only.
