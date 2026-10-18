import base64
def b(n): return "data:image/png;base64,"+base64.b64encode(open(n,'rb').read()).decode()
A={'fig1':"Four rows of blue blocks stacked as a staircase, with 1, 2, 3 and 4 blocks. Text: 1 + 2 + 3 + 4 = ? How many squares?",
'fig2':"The same staircase inside a 4 by 4 square. The missing blocks are outlined in red. Text: 4 x 4 = 16 squares, the red ones are not there.",
'fig3':"The blue staircase and an upside-down orange copy fit together into a rectangle 4 blocks tall and 5 wide.",
'fig5':"Five rows: a blue staircase and an orange copy fit into a rectangle 5 tall and 6 wide. Every row has 6 blocks, for example row 3 has 3 blue and 3 orange.",
'fig4':"Text summary: n rows and n + 1 columns. Row k has k + (n + 1 - k) = n + 1 blocks. Two copies of the sum equal n times n + 1, so the sum is n(n + 1)/2. Check for n = 4: 4 x 5 / 2 = 10."}
def img(k,cap): return f'<figure><img src="{b(k+".png")}" alt="{A[k]}"><figcaption>{cap}</figcaption></figure>'
html=f'''<!doctype html><html lang="en"><head><meta charset="utf-8"><meta name="viewport" content="width=device-width, initial-scale=1"><title>Adding 1 up to n by building a rectangle</title><style>
body{{background:#f4f1ea;margin:0;font-family:Georgia,serif;color:#222}}
.hero{{background:#111;color:#fff;padding:28px 0 22px}}
.col{{max-width:720px;margin:0 auto;padding:0 18px}}
h1{{margin:0 0 8px;font-size:clamp(26px,6vw,34px);line-height:1.15}} .tag{{color:#bbb;font-size:17px}} .meta{{color:#aaa;font-size:14px;margin-top:10px}}
p,li{{font-size:19px;line-height:1.6}} figure{{margin:22px 0 22px}} img{{width:100%;height:auto;display:block}} figcaption{{font-size:15px;color:#555;margin-top:6px}}
.ex{{border:2px solid #cfc9bb;border-radius:10px;padding:14px 16px;background:#fff;margin:22px 0}}
label{{display:block;font-weight:bold;margin-bottom:6px}} .pad{{width:100%;height:80px;border:1px solid #888;border-radius:6px;font-family:inherit;font-size:17px;box-sizing:border-box}}
details summary{{display:inline-block;background:#cfe3f5;border-radius:6px;padding:8px 18px;cursor:pointer;margin-top:10px;font-size:17px}}
.ans{{background:#e7e7e7;border-radius:10px;padding:4px 16px;margin-top:10px}}
.eq{{text-align:center;font-size:26px;margin:18px 0}} .n{{background:#fff4d6;border-left:4px solid #e0b030;padding:6px 14px;font-size:16px;margin:12px 0}}
.warn{{background:#fde9e4;border-left:4px solid #d9534f;padding:8px 14px;font-size:15px;margin:16px 0}}
</style></head><body>
<header class=hero><div class=col><h1>Adding 1 up to n by building a rectangle</h1><div class=tag>A staircase of blocks, and the picture that counts them.</div><div class=meta>Original sample note for the notes skill. Text and figures are original.</div></div></header>
<main class=col>
<div class=warn role=note>Test sample. Style rules came from a partial review: 196 channel uploads have no frame review, 26 channel items have no local transcript, no audio was inspected, and only a subset of lesson pages was deep-viewed.</div>
<p>Here is a staircase of blocks. It is one block wide at the top and four at the bottom.</p>
{img('fig1','Four rows of blocks: 1, 2, 3 and 4.')}
<p>How many blocks are there? You could count them one by one, and for four rows that works fine. But if the staircase had a hundred rows, counting would be a chore, and you would want a way that does not care about the number. So the question is really: is there a way to see the total at a glance?</p>
<p>A first thought: the staircase sits inside a 4 by 4 square, and a square is easy to count.</p>
{img('fig2','The square counts 16 blocks. The red ones are not part of the staircase.')}
<p>That gives 16, which is too many. The red blocks are the ones we should not have counted. Notice how they are shaped: they are also a staircase, one block short at every level. That hints that the empty space is not useless.</p>
<section class=ex aria-labelledby=q1><label id=q1 for=pad1>Pause and ponder. The red space is a staircase too. What happens if you place a second staircase, upside down, against the first? What shape do you get?</label>
<textarea id=pad1 class=pad placeholder="Use this box as a notepad."></textarea>
<details open><summary>Reveal</summary><div class=ans>
<p>Take a copy of the blue staircase and turn it upside down. In every row the blue staircase has some blocks, and the copy has exactly the missing ones. In the top row the blue has 1 and the copy has 4. In the next the blue has 2 and the copy has 3, and so on. Every row has 5 blocks in total.</p>
{img('fig3','Blue staircase plus its upside-down copy: a rectangle, 4 tall and 5 wide.')}
</div></details></section>
<p>So two staircases make a rectangle that is 4 blocks tall and 5 blocks wide. A rectangle is easy to count: 4 rows of 5 is 20 blocks.</p>
<div class=eq>4 × 5 = 20</div>
<p>Those 20 blocks are made of two identical staircases. Identical means they have the same count. If two equal amounts add up to 20, each is half of 20.</p>
<div class=eq>20 ÷ 2 = 10</div>
<p>So 1 + 2 + 3 + 4 = 10. You can check by counting the blocks one at a time: 1, 3, 6, 10.</p>
<h2 style="font-size:24px">Nothing special about 4</h2>
<p>Try five rows before trusting the pattern. The same fit works, and every row now adds up to 6 blocks.</p>
{img('fig5','Five rows: row k holds k blue blocks and 6 − k orange ones, so each row has 6.')}
<p>In general, with n rows, row k of the first staircase has k blocks, and row k of the copy has n + 1 − k. Their sum is k + (n + 1 − k) = n + 1 in every row, whatever k is. So the rectangle is n tall and n + 1 wide, and two copies of the sum fill it: 2 × (1 + 2 + … + n) = n × (n + 1).</p>
{img('fig4','The general statement, with the n = 4 case as a check.')}
<div class=n><b>Prerequisites:</b> multiplying whole numbers, and the idea that two equal parts of a total are each half of it.</div>
<div class=n><b>Caveat:</b> the row-by-row argument is the whole proof, since it does not depend on n. It is shown here in words and symbols, not formally.</div>
</main></body></html>'''
open('note.html','w').write(html)
