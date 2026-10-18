# Sample: "Two staircases make a rectangle" (ORIGINAL, written for this skill; script and storyboard; the 38 s silent test in samples/staircase-render is a shortened visual render of this idea, not a rendering of this long-form script)

Audience: someone who has seen 1+2+3+... and maybe a formula, never felt why it works. One idea: the sum 1+2+...+n is half a rectangle.
Palette: blue = the staircase we start with, orange = its upside-down copy, white = counts and labels, yellow = the unknown we are solving for.
Persistent frame: a grid canvas on the left; a running table of n and total on the right.

| SAY | SHOW | MOVE |
|---|---|---|
| Here is a staircase made of blocks. One block, then two, then three, then four. How many blocks in all? | Blue staircase, n=4, blocks pop in per step. Table row: n=4, total ? | concrete seed |
| You can count: ten. Fine. Now someone hands you a staircase with a hundred steps. Counting is not going to be fun. | Staircase zooms out to 100 steps; blocks become a blue slope. | stakes by scale |
| So the goal is a way to know the total without counting, and ideally a reason you can see. | One-line goal text, three-dot map pinned top: small case, a trick, the check. | goal and map |
| Small case first. Four steps. Total ten. Let's see what ten is made of. | Table row filled: 4, 10, new row dims old. | smallest case |
| Here is a tempting idea: the total is roughly the number of steps times the tallest step. Four times four, sixteen. Too big, of course. | Draw 4x4 square around staircase; extra empty cells shaded red; label wrong. | failed attempt, marked |
| But look how it is wrong. The empty part is also a staircase. | Empty cells recolored: a smaller staircase of three steps. | the failure motivates the fix |
| What if we stop fighting it and use that. Take a second copy of our staircase, flip it, and fit it against the first. | Orange copy rotates 180 degrees, slides in; blue + orange make a rectangle. | the idea, built |
| Pause here and guess: how wide and how tall is this rectangle, if we started with four steps? | Prediction options on screen: 4x4, 4x5, 5x5, 4x8. Hold. | prediction beat |
| Four tall, five wide. Twenty blocks, and each staircase is half. Ten. | Dimensions braced; 4 and 5 appear as labeled arrows; 20 / 2 = 10 in yellow. | reveal and check |
| Now the hundred-step version stops being scary. It is a hundred by a hundred and one, cut in half. | Zoom out; rectangle with just labels 100 and 101. Row in table: 100, 5050. | generalize from picture |
| Only now does the usual formula earn its place: steps, times steps plus one, over two. It is just a description of this rectangle. | Symbols n, n+1 appear colored as the rectangle's sides, then the formula assembles. | notation after picture |
| One honest caveat: this works because the two staircases fit exactly. It would not for steps of varying height, and I am not claiming otherwise. | Uneven staircase shown with gap, labeled "does not tile". | caveat |
| If you want to try something: what shape does the same flip-and-fit give for sums of odd numbers? | Odd-number staircase outline, no answer. | invitation |
| Takeaway: a sum can be half a rectangle. Next time a sum looks like a staircase, look for its twin. | Final frame: blue and orange rectangle, table complete. | close |

## Self-review (rubric)
- Motivation macro: weak-ok (stakes by scale only). Micro: strong (each step has a reason). Clarity: strong. Novelty: weak (a classic argument); memorability: ok (twin staircase).
- Checks: palette fixed; one persistent frame; failure marked; prediction beat present; caveat present; no borrowed text; no voice imitation; no paid service.
- The long-form script itself is unrendered. Only the short silent test in samples/staircase-render was rendered (see its README).
