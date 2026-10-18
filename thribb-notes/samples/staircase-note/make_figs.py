# Original figures for the sample note. Portrait-friendly: 480 px wide, labels >= 28 px so they stay readable at 390 px page width.
import cairosvg
B,O,R,Y="#58C4DD","#FF8C42","#FC6255","#FFD84D"
W=480
def sq(x,y,c,s=48,fo=.6): return f'<rect x="{x}" y="{y}" width="{s}" height="{s}" fill="{c}" fill-opacity="{fo}" stroke="{c}" stroke-width="2"/>'
def svg(body,h): return f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{h}" viewBox="0 0 {W} {h}"><rect width="{W}" height="{h}" fill="#000"/><style>text{{font-family:Georgia,serif;fill:#fff;font-size:28px}}</style>{body}</svg>'
def save(n,body,h):
    s=svg(body,h); open(n+'.svg','w').write(s); cairosvg.svg2png(bytestring=s.encode(),write_to=n+'.png')
def T(x,y,t,c="#fff",anchor="middle"): return f'<text x="{x}" y="{y}" text-anchor="{anchor}" style="fill:{c}">{t}</text>'
def stairs(x0,y0,n,c=B,s=48): return "".join(sq(x0+j*s,y0+i*s,c,s) for i in range(n) for j in range(i+1))
def comp(x0,y0,n,m,c,s=48,fo=.6): return "".join(sq(x0+j*s,y0+i*s,c,s,fo) for i in range(n) for j in range(i+1,m))
# fig1: 4 rows (190 wide) centered
x=(W-4*48)//2
save('fig1',stairs(x,30,4)+T(W/2,290,"1 + 2 + 3 + 4 = ?",Y)+T(W/2,335,"How many squares?"),370)
save('fig2',stairs(x,30,4)+comp(x,30,4,4,R,fo=.15)+T(W/2,290,"4 x 4 = 16 squares",R)+T(W/2,335,"The red ones are not there"),370)
x5=(W-5*48)//2
save('fig3',stairs(x5,30,4)+comp(x5,30,4,5,O)+T(W/2,290,"4 tall, 5 wide",Y)+T(W/2,335,"blue + upside-down copy"),370)
# fig5: n=5, 6 wide
x6=(W-6*48)//2
lab=T(W/2,350,"every row has 6 blocks",Y)+T(W/2,392,"row 3: 3 blue + 3 orange",O)
save('fig5',stairs(x6,30,5)+comp(x6,30,5,6,O)+lab,420)
save('fig4',T(W/2,70,"n rows, n + 1 columns",Y)+T(W/2,130,"row k: k + (n + 1 - k) = n + 1")+T(W/2,190,"2 x (1 + 2 + ... + n) = n (n + 1)")+T(W/2,250,"1 + 2 + ... + n = n (n + 1) / 2",Y)+T(W/2,310,"check n = 4: 4 x 5 / 2 = 10",B),360)
