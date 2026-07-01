#!/usr/bin/env python3
"""『プログラマーはなぜそう考えるのか』旗艦図版の生成（自作 SVG）。
ASSET_RULES に従い、再生成できるよう全図の定義をここに集約する。
出力: manuscript/assets/fig-*.svg
方針: 1図1主張／図中用語は本文と一致／色だけに依存しない（形・ラベル・矢印で区別）。
"""
import html, math, pathlib

ASSETS = pathlib.Path(__file__).resolve().parents[2] / "manuscript/assets"
ASSETS.mkdir(parents=True, exist_ok=True)

INK="#1f2933"; SUB="#52606d"; ACC="#3a6ea5"; DANGER="#b23a48"
NEUT="#eef1f5"; BLUE="#dce9f2"; WARM="#f4e9dc"; LINE="#b8c2cc"

def esc(s): return html.escape(str(s), quote=True)

def head(w,h,aria):
    return [f'<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 {w} {h}" '
            f'font-family="sans-serif" role="img" aria-label="{esc(aria)}">',
            '<defs>'
            f'<marker id="ar" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="{ACC}"/></marker>'
            f'<marker id="arr" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="{DANGER}"/></marker>'
            f'<marker id="arg" markerWidth="10" markerHeight="10" refX="7" refY="3" orient="auto"><path d="M0,0 L7,3 L0,6 Z" fill="{SUB}"/></marker>'
            '</defs>']

def rect(x,y,w,h,fill="#fff",stroke=LINE,rx=0,sw=1.2,dash=None):
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<rect x="{x}" y="{y}" width="{w}" height="{h}" rx="{rx}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"{d}/>'

def txt(x,y,s,size=16,fill=INK,anchor="start",weight="normal",mono=False):
    fam=' font-family="ui-monospace,monospace"' if mono else ''
    return f'<text x="{x}" y="{y}" text-anchor="{anchor}" font-size="{size}" font-weight="{weight}" fill="{fill}"{fam}>{esc(s)}</text>'

def ln(x1,y1,x2,y2,stroke=ACC,sw=2,marker=None,dash=None):
    m=f' marker-end="url(#{marker})"' if marker else ''
    d=f' stroke-dasharray="{dash}"' if dash else ''
    return f'<line x1="{x1}" y1="{y1}" x2="{x2}" y2="{y2}" stroke="{stroke}" stroke-width="{sw}"{m}{d}/>'

def circ(cx,cy,r,fill,stroke="none",sw=1):
    return f'<circle cx="{cx}" cy="{cy}" r="{r}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def poly(points,fill,stroke=LINE,sw=1.2):
    pts=" ".join(f"{x},{y}" for x,y in points)
    return f'<polygon points="{pts}" fill="{fill}" stroke="{stroke}" stroke-width="{sw}"/>'

def save(name,p):
    p.append('</svg>')
    (ASSETS/name).write_text("\n".join(p),encoding="utf-8")
    print("wrote",name)

# ---------------------------------------------------------------- fig-0-1
def fig_0_1():
    rows=[("1","複雑さに飲まれる","手を入れ続けられる"),
          ("2","半年後には読めない","読まれる"),
          ("3","先に固めると動けない","変えられる"),
          ("4","動くのに誰も触れない","触れ続けられる"),
          ("5","一人が抜けると触れない","一人に縛られない"),
          ("6","道具の中身を直せない","直し、見て、配る"),
          ("7","「正しい一つ」に縛られる","選び続ける"),
          ("8","言語が許すことしか考えられない","価値観で作り直す"),
          ("9","持ち主に縛られ、届かない","許可なく届ける")]
    W,top,rh=780,88,50; H=top+rh*len(rows)+24
    lx,lw,rx,rw=96,286,470,286; ax0,ax1=lx+lw+12,rx-12
    p=head(W,H,"九つの不自由が、対応する九つの自由に変わる本書の地図")
    p+=[txt(lx+lw/2,44,"不自由",22,INK,"middle","bold"),
        txt(rx+rw/2,44,"自由",22,ACC,"middle","bold"),
        txt((ax0+ax1)/2,44,"勝ち取る",13,SUB,"middle"),
        ln(40,60,W-40,60,"#cdd5df",1)]
    for i,(n,u,f) in enumerate(rows):
        y=top+i*rh; cy=y+rh/2
        p+=[circ(48,cy,15,ACC),txt(48,cy+5,n,15,"#fff","middle","bold"),
            rect(lx,y+6,lw,rh-12,NEUT,"#b8c2cc"),txt(lx+14,cy+6,u,17,INK),
            ln(ax0,cy,ax1-6,cy,ACC,2.5,"ar"),
            rect(rx,y+6,rw,rh-12,BLUE,ACC,rx=11),txt(rx+14,cy+6,f,17,ACC,weight="bold")]
    save("fig-0-1.svg",p)

# ---------------------------------------------------------------- fig-0-2
def fig_0_2():
    W,H=620,430; cx,cy,R=310,225,140
    nodes=["① 問題","② 最初の答え","③ 失敗","④ 議論","⑤ 改善","⑥ 文化"]
    p=head(W,H,"問題から文化までの六つの拍子が円環し、また次の問題へ戻る図")
    p+=[circ(cx,cy,58,"#fff",LINE,1),
        txt(cx,cy-6,"六つの拍子",17,SUB,"middle","bold"),
        txt(cx,cy+16,"何度も回る",13,SUB,"middle")]
    pos=[]
    for i in range(6):
        a=math.radians(-90+i*60); pos.append((cx+R*math.cos(a),cy+R*math.sin(a)))
    for i,(x,y) in enumerate(pos):
        p+=[rect(x-62,y-20,124,40,BLUE if i in(0,5) else NEUT,ACC if i in(0,5) else "#b8c2cc",rx=20),
            txt(x,y+6,nodes[i],15,INK,"middle","bold")]
    for i in range(6):
        x1,y1=pos[i]; x2,y2=pos[(i+1)%6]
        ang=math.atan2(y2-y1,x2-x1)
        sx,sy=x1+66*math.cos(ang),y1+26*math.sin(ang)
        ex,ey=x2-70*math.cos(ang),y2-30*math.sin(ang)
        p.append(ln(sx,sy,ex,ey,ACC,2,"ar"))
    save("fig-0-2.svg",p)

# ---------------------------------------------------------------- fig-1-1
def fig_1_1():
    W,H=720,430
    x0,x1,y0,y1=110,650,350,80
    ns=list(range(2,21)); rel=[n*(n-1)/2 for n in ns]; mx=190
    xm=lambda n:x0+(n-2)/18*(x1-x0); ym=lambda v:y0-v/mx*(y0-y1)
    p=head(W,H,"機能数が増えると、気を配る関係の数が直線を超えて急増することを示すグラフ")
    # axes
    p+=[ln(x0,y0,x1,y0,SUB,1.5),ln(x0,y0,x0,y1,SUB,1.5),
        txt(x1,y0+26,"機能の数 →",14,SUB,"end"),
        txt(x0-8,y1-8,"気を配る関係の数",14,SUB,"start")]
    # linear reference (faint)
    p+=[ln(xm(2),ym(2),xm(20),ym(20),LINE,2,dash="5 5"),
        txt(xm(11),ym(11)-10,"もし直線なら、20 どまり",12,SUB,"middle")]
    # curve
    pts=" ".join(f"{xm(n):.1f},{ym(v):.1f}" for n,v in zip(ns,rel))
    p.append(f'<polyline points="{pts}" fill="none" stroke="{ACC}" stroke-width="3"/>')
    for n in (2,10,20):
        v=n*(n-1)/2; p.append(circ(xm(n),ym(v),4.5,ACC))
        p.append(txt(xm(n),y0+22,str(n),13,SUB,"middle"))
    p+=[circ(xm(20),ym(190),6,ACC),
        txt(xm(20)-6,ym(190)-10,"20 の機能 → 190 の関係",13,ACC,"end","bold")]
    save("fig-1-1.svg",p)

# ---------------------------------------------------------------- fig-2-2
def fig_2_2():
    W,top,rh=720,76,74; rows=[
        ("f","まったく、わからない",1.0,NEUT,"#b8c2cc",INK),
        ("getUsers","半分だけ",0.55,NEUT,"#b8c2cc",INK),
        ("findDormantUsers","開く前に、わかる",0.12,BLUE,ACC,ACC)]
    H=top+rh*3+16
    p=head(W,H,"名前が語るほど、中身を読む必要が減ることを三段で示す図")
    p+=[txt(40,46,"名前とひとこと",16,INK,"start","bold"),
        txt(660,46,"中を読む必要",15,SUB,"end"),
        ln(40,56,W-40,56,"#cdd5df",1)]
    barx,barw=420,240
    for i,(code,note,frac,fill,st,cc) in enumerate(rows):
        y=top+i*rh; cy=y+rh/2
        p+=[rect(40,y+8,350,rh-16,fill,st,rx=8),
            txt(58,cy-4,code,19,cc,weight="bold",mono=True),
            txt(58,cy+20,note,12,SUB)]
        col=DANGER if frac>0.8 else (SUB if frac>0.4 else ACC)
        p+=[rect(barx,cy-11,barw,22,"#f0f2f5","#d5dbe2",rx=11),
            rect(barx,cy-11,max(18,barw*frac),22,col,"none",rx=11)]
    save("fig-2-2.svg",p)

# ---------------------------------------------------------------- fig-3-1
def fig_3_1():
    W,H=720,410; x0,x1,yb,yt=110,650,330,90
    def cost(t):
        c=((t-0.45)/0.5)**2; return min(1.0,c)
    xm=lambda t:x0+t*(x1-x0); ym=lambda c:yb-c*(yb-yt)
    p=head(W,H,"先に決めきる量が少なすぎても多すぎても痛手が増え、中間で最小になるU字の関係")
    p+=[ln(x0,yb,x1,yb,SUB,1.5),ln(x0,yb,x0,yt-4,SUB,1.5),
        txt(x1,yb+26,"事前に決める量 →",14,SUB,"end"),
        txt(x0-8,yt-10,"変化が来たときの痛手",14,SUB,"start")]
    ts=[i/40 for i in range(41)]
    pts=" ".join(f"{xm(t):.1f},{ym(cost(t)):.1f}" for t in ts)
    p.append(f'<polyline points="{pts}" fill="none" stroke="{ACC}" stroke-width="3"/>')
    # ends and sweet spot
    p+=[circ(xm(0),ym(cost(0)),5,DANGER),txt(xm(0)+8,ym(cost(0))-8,"決めなさすぎ＝迷子",13,DANGER),
        circ(xm(1),ym(cost(1)),5,DANGER),txt(xm(1)-8,ym(cost(1))-8,"決めすぎ＝動けない",13,DANGER,"end"),
        circ(xm(0.45),ym(0),6,ACC),txt(xm(0.45),ym(0)+26,"ちょうど＝手を入れられる形",13,ACC,"middle","bold")]
    save("fig-3-1.svg",p)

# ---------------------------------------------------------------- fig-4-1
def fig_4_1():
    W,H=760,300
    p=head(W,H,"同じ警告でも、1202は一度きりの本番、FAILは何度でもわざと鳴らす日常という対比")
    p+=[txt(W/2,42,"どちらも「ここが危ない」の合図",16,SUB,"middle","bold")]
    def panel(x,fill,st,head_,line,tag,hc):
        return [rect(x,70,330,192,fill,st,rx=10),
                txt(x+165,128,head_,34,hc,"middle","bold",mono=True),
                txt(x+165,176,line,17,INK,"middle"),
                rect(x+110,216,110,30,"#fff",st,rx=15),
                txt(x+165,236,tag,14,hc,"middle","bold")]
    p+=panel(40,NEUT,"#b8c2cc","1202","月の降下、一度きり","本番",DANGER)
    p+=panel(390,BLUE,ACC,"FAIL","毎日、わざと鳴らす","日常",ACC)
    save("fig-4-1.svg",p)

# ---------------------------------------------------------------- fig-5-1
def fig_5_1():
    W,H=760,340
    p=head(W,H,"知識が一人に集中した状態と、その人が抜けて誰も触れなくなる状態の前後比較")
    p+=[ln(W/2,60,W/2,300,"#cdd5df",1,dash="4 4"),
        txt(200,44,"強みに見える",16,SUB,"middle","bold"),
        txt(560,44,"抜けた瞬間、触れない",16,DANGER,"middle","bold")]
    # before
    pbox=(120,150)
    p+=[rect(60,148,150,54,BLUE,ACC,rx=8),txt(135,172,"決済コードを",14,ACC,"middle","bold"),
        txt(135,190,"一人が握る",14,ACC,"middle","bold")]
    for my in (105,170,235):
        p+=[circ(300,my,15,NEUT,"#b8c2cc"),ln(285,my,214,175,SUB,1.6,"arg")]
    # after
    p+=[rect(470,148,150,54,"#f0f2f5","#c7ccd3",rx=8),txt(545,178,"？ 誰も中を知らない",13,SUB,"middle")]
    p+=[ln(660,150,700,200,DANGER,3),ln(700,150,660,200,DANGER,3)]  # X over gone person area
    p.append(txt(680,140,"抜けた",12,DANGER,"middle","bold"))
    for my in (105,170,235):
        p+=[circ(430,my,15,NEUT,"#b8c2cc"),ln(445,my,520,175,"#c7ccd3",1.6,dash="4 4")]
    p.append(txt(545,270,"触れないコードの山",13,DANGER,"middle","bold"))
    save("fig-5-1.svg",p)

# ---------------------------------------------------------------- fig-6-1
def fig_6_1():
    W,H=640,430; cx,cy=320,215
    p=head(W,H,"フリーソフトウェアの四つの自由（使う・読んで学ぶ・直す・配る）を中心の周りに示す図")
    quad=[("使う",120,70),("読んで学ぶ",360,70),("直す",120,296),("配る",360,296)]
    for label,x,y in quad:
        p.append(ln(cx,cy,x+80,y+32,ACC,1.6))
    p+=[rect(cx-95,cy-34,190,68,BLUE,ACC,rx=10),
        txt(cx,cy-6,"自由な",18,ACC,"middle","bold"),
        txt(cx,cy+18,"ソフトウェア",18,ACC,"middle","bold")]
    for label,x,y in quad:
        p+=[rect(x,y,160,64,NEUT,"#b8c2cc",rx=10),
            txt(x+80,y+40,label,19,INK,"middle","bold")]
    save("fig-6-1.svg",p)

# ---------------------------------------------------------------- fig-7-1
def fig_7_1():
    W,H=720,380
    p=head(W,H,"勝者を語れるかで、閉じた問いと開いた問いに仕分ける分岐図")
    p+=[rect(290,34,140,44,NEUT,"#b8c2cc",rx=8),txt(360,62,"その論争",16,INK,"middle","bold"),
        ln(360,78,360,104,SUB,2,"arg")]
    dia=[(360,104),(470,158),(360,212),(250,158)]
    p+=[poly(dia,WARM,"#c9a26b",1.5),txt(360,154,"勝者を",15,INK,"middle","bold"),
        txt(360,174,"語れる？",15,INK,"middle","bold")]
    p+=[ln(250,158,150,158,SUB,2,"arg"),ln(150,158,150,250,SUB,2,"arg"),txt(200,148,"はい",12,SUB,"middle"),
        ln(470,158,570,158,SUB,2,"arg"),ln(570,158,570,250,SUB,2,"arg"),txt(520,148,"いいえ",12,SUB,"middle")]
    p+=[rect(30,252,240,100,NEUT,"#b8c2cc",rx=10),
        txt(150,292,"閉じた問い",18,INK,"middle","bold"),
        txt(150,324,"学ぶ（例：goto）",14,SUB,"middle")]
    p+=[rect(450,252,240,100,BLUE,ACC,rx=10),
        txt(570,292,"開いた問い",18,ACC,"middle","bold"),
        txt(570,324,"選ぶ（例：型・タブと空白）",14,SUB,"middle")]
    save("fig-7-1.svg",p)

# ---------------------------------------------------------------- fig-8-1
def fig_8_1():
    W,H=720,340
    p=head(W,H,"言語が簡単にする範囲が思考の範囲になり、難しいことは思いつかなくなる檻の図")
    p+=[rect(20,20,W-40,H-40,"#f0f2f5","#e2e6eb",rx=8)]
    p+=[txt(W/2,58,"言語の外 ＝ 難しいこと → 思いつかない",15,SUB,"middle","bold")]
    p+=[rect(160,100,400,170,BLUE,ACC,rx=16,dash="7 5")]
    p+=[txt(360,168,"簡単にすること",22,ACC,"middle","bold"),
        txt(360,206,"＝ 考えられる範囲",16,INK,"middle"),
        txt(360,246,"― 檻の中が、考えの範囲 ―",12,SUB,"middle")]
    save("fig-8-1.svg",p)

# ---------------------------------------------------------------- fig-9-1
def fig_9_1():
    W,H=760,360
    p=head(W,H,"重い標準は高い壁で少数しか参加できず、軽いWebは低い段差で誰でも参加できる対比")
    p+=[ln(W/2,50,W/2,320,"#cdd5df",1,dash="4 4"),
        txt(200,42,"重い標準",18,INK,"middle","bold"),
        txt(560,42,"軽い Web",18,ACC,"middle","bold")]
    base=300
    # heavy: tall wall, 2 people left, none right
    p+=[ln(70,base,360,base,SUB,1.5),
        rect(250,120,26,base-120,"#8a95a1","#6b7580"),
        txt(263,110,"高い壁",12,SUB,"middle")]
    for x in (110,150): p.append(circ(x,base-16,11,NEUT,"#b8c2cc"))
    p.append(txt(200,base+26,"少数だけが参加できる",13,SUB,"middle"))
    # light: low step, many people crossing
    p+=[ln(410,base,700,base,SUB,1.5),
        rect(548,base-30,26,30,BLUE,ACC),txt(561,base-40,"低い段差",12,ACC,"middle")]
    for x in (440,475,510,600,635,670): p.append(circ(x,base-16,11,BLUE,ACC))
    p.append(txt(560,base+26,"誰でも参加できる",13,ACC,"middle","bold"))
    save("fig-9-1.svg",p)

# ---------------------------------------------------------------- fig-e-1
def fig_e_1():
    W,H=720,230
    p=head(W,H,"閉じた問いはAIが再現でき、開いた問いを引き受ける担い手は未決であることを示す図")
    p+=[rect(40,60,300,120,NEUT,"#b8c2cc",rx=10),
        txt(190,108,"閉じた問い",18,INK,"middle","bold"),
        txt(190,146,"→ AI が再現できる",17,ACC,"middle","bold")]
    p+=[rect(380,60,300,120,BLUE,ACC,rx=10),
        txt(530,108,"開いた問い",18,ACC,"middle","bold"),
        txt(530,146,"→ 引き受けるのは、誰か？",16,DANGER,"middle","bold")]
    save("fig-e-1.svg",p)

# ================================================================ 第二波（補強）
def fig_1_2():
    W,H=560,330
    p=head(W,H,"外側の偶有的な複雑さは道具で減らせるが、中心の本質的な複雑さは消えない図")
    p+=[rect(50,60,460,240,NEUT,"#b8c2cc",rx=16),
        txt(280,94,"偶有的な複雑さ",16,SUB,"middle","bold"),
        txt(280,118,"＝ 道具で減らせる",13,SUB,"middle")]
    p+=[rect(180,155,200,120,BLUE,ACC,rx=14),
        txt(280,212,"本質的な複雑さ",16,ACC,"middle","bold"),
        txt(280,240,"＝ 消えない",14,INK,"middle")]
    save("fig-1-2.svg",p)

def fig_1_3():
    W,H=720,210
    p=head(W,H,"一つの仕事だけをする小さな道具を、パイプでつないで大きな仕事にする流れ")
    xs=[70,290,510]; labels=["道具 A","道具 B","道具 C"]
    for x,l in zip(xs,labels):
        p+=[rect(x,70,150,72,NEUT,"#b8c2cc",rx=10),
            txt(x+75,104,l,17,INK,"middle","bold"),
            txt(x+75,128,"一つの仕事",12,SUB,"middle")]
    for gx in (255,475): p.append(txt(gx,118,"│",36,ACC,"middle","bold"))
    p.append(txt(W/2,182,"つなぐと、大きな仕事になる",14,SUB,"middle"))
    save("fig-1-3.svg",p)

def fig_2_1():
    W,H=720,190; y=105
    p=head(W,H,"コードの一生で、書く回数は一度、読む回数は何度も続くことを示す帯")
    p+=[txt(60,46,"コードの一生",14,SUB,"start","bold"),ln(70,y,660,y,"#cdd5df",2)]
    p+=[circ(95,y,13,DANGER),txt(95,y-24,"書く",13,DANGER,"middle","bold"),txt(95,y+30,"一度",12,SUB,"middle")]
    for x in (210,280,350,420,490,560,630): p.append(circ(x,y,10,ACC))
    p+=[txt(420,y-24,"読む",13,ACC,"middle","bold"),txt(420,y+30,"何度も、ずっと",12,SUB,"middle")]
    save("fig-2-1.svg",p)

def fig_2_3():
    W,H=720,220
    p=head(W,H,"コードを直すと名前は追従し、コメントは取り残されて食い違うことの対比")
    p.append(txt(W/2,46,"コードを直したとき",16,SUB,"middle","bold"))
    p+=[rect(60,80,280,110,BLUE,ACC,rx=10),
        txt(200,126,"名前",19,ACC,"middle","bold"),
        txt(200,162,"○ 一緒に変わる",15,ACC,"middle","bold")]
    p+=[rect(380,80,280,110,NEUT,"#b8c2cc",rx=10),
        txt(520,126,"コメント",19,INK,"middle","bold"),
        txt(520,162,"× 取り残される",15,DANGER,"middle","bold")]
    save("fig-2-3.svg",p)

def fig_3_2():
    W,H=720,230
    p=head(W,H,"リファクタリングは外の動きを変えず内側だけ整え、作り直しはゼロから組み直す対比")
    p+=[rect(50,64,300,140,BLUE,ACC,rx=10),
        txt(200,102,"リファクタリング",18,ACC,"middle","bold"),
        txt(200,142,"外の動き：変えない",14,INK,"middle"),
        txt(200,174,"内側だけ整える",14,INK,"middle")]
    p+=[rect(370,64,300,140,NEUT,"#b8c2cc",rx=10),
        txt(520,102,"作り直し",18,INK,"middle","bold"),
        txt(520,142,"ゼロから組み直す",14,SUB,"middle"),
        txt(520,174,"動きも変わる・新バグ",14,DANGER,"middle")]
    save("fig-3-2.svg",p)

def fig_4_2():
    W,H=520,420; cx,cy,R=260,215,120
    nodes=["怖い","触らない","古びる","もっと怖い"]
    p=head(W,H,"怖いから触らず、触らないから古びて、さらに怖くなる悪循環の環")
    p.append(txt(cx,cy+6,"悪循環",16,DANGER,"middle","bold"))
    pos=[(cx+R*math.cos(math.radians(-90+i*90)),cy+R*math.sin(math.radians(-90+i*90))) for i in range(4)]
    for i,(x,y) in enumerate(pos):
        p+=[rect(x-60,y-22,120,44,"#f6e7e9","#c9727f" if i==3 else "#d8a2ab",rx=22),
            txt(x,y+6,nodes[i],15,DANGER if i==3 else INK,"middle","bold")]
    for i in range(4):
        x1,y1=pos[i]; x2,y2=pos[(i+1)%4]; a=math.atan2(y2-y1,x2-x1)
        p.append(ln(x1+64*math.cos(a),y1+26*math.sin(a),x2-68*math.cos(a),y2-30*math.sin(a),DANGER,2,"arr"))
    save("fig-4-2.svg",p)

def fig_4_3():
    W,H=720,230
    p=head(W,H,"変更のたびに検査が走り、通れば手を入れられ、壊せばその場で気づく安全網")
    p+=[rect(40,90,150,60,NEUT,"#b8c2cc",rx=10),txt(115,126,"変更",17,INK,"middle","bold"),
        ln(190,120,248,120,ACC,2,"ar"),
        rect(250,90,150,60,BLUE,ACC,rx=10),txt(325,126,"検査",17,ACC,"middle","bold")]
    p+=[ln(400,120,486,84,SUB,1.6,"arg"),ln(400,120,486,158,SUB,1.6,"arg"),
        txt(430,88,"通る",12,SUB,"middle"),txt(430,170,"壊れる",12,SUB,"middle")]
    p+=[rect(490,58,210,52,BLUE,ACC,rx=10),txt(595,90,"手を入れられる",15,ACC,"middle","bold"),
        rect(490,132,210,52,"#f6e7e9","#c9727f",rx=10),txt(595,164,"その場で気づく",15,DANGER,"middle","bold")]
    save("fig-4-3.svg",p)

def fig_5_2():
    W,H=760,180
    p=head(W,H,"変更を提案として差し出し、読んで意見をつけ、納得して取り込むまでの流れ")
    steps=["変更","提案","レビュー","取り込む"]; bw=150; gap=(W-80-bw*4)/3
    for i,s in enumerate(steps):
        bx=40+i*(bw+gap); on=i in(1,2)
        p+=[rect(bx,70,bw,60,BLUE if on else NEUT,ACC if on else "#b8c2cc",rx=10),
            txt(bx+bw/2,107,s,17,ACC if on else INK,"middle","bold")]
        if i<3: p.append(ln(bx+bw+4,100,bx+bw+gap-4,100,ACC,2,"ar"))
    save("fig-5-2.svg",p)

def fig_6_2():
    W,H=720,230
    p=head(W,H,"中身を閉じると直す力は作った会社に、中を開くと使う人にあることの対比")
    p+=[rect(50,64,300,140,NEUT,"#b8c2cc",rx=10),
        txt(200,100,"中を閉じて売る",17,INK,"middle","bold"),
        txt(200,144,"直す力",13,SUB,"middle"),
        txt(200,174,"＝ 作った会社",16,DANGER,"middle","bold")]
    p+=[rect(370,64,300,140,BLUE,ACC,rx=10),
        txt(520,100,"中を開く",17,ACC,"middle","bold"),
        txt(520,144,"直す力",13,SUB,"middle"),
        txt(520,174,"＝ 使う人",16,ACC,"middle","bold")]
    save("fig-6-2.svg",p)

def fig_6_3():
    W,H=720,210; y=115
    p=head(W,H,"ひとりの宣言から世界中の貢献が集まり、実用のソフトに組み上がる拡散の流れ")
    p+=[rect(30,85,120,60,BLUE,ACC,rx=10),txt(90,121,"宣言",17,ACC,"middle","bold"),txt(90,66,"ひとり",12,SUB,"middle")]
    for dx,dy in [(300,70),(355,100),(295,135),(365,150),(325,178),(285,102)]:
        p.append(circ(dx,dy,9,NEUT,"#b8c2cc"))
    p.append(txt(325,52,"世界中の貢献",12,SUB,"middle"))
    p+=[rect(560,85,130,60,BLUE,ACC,rx=10),txt(625,121,"実用へ",17,ACC,"middle","bold"),txt(625,66,"組み上がる",12,SUB,"middle")]
    p+=[ln(155,115,265,115,ACC,2,"ar"),ln(405,115,555,115,ACC,2,"ar")]
    save("fig-6-3.svg",p)

def fig_8_2():
    W,H=720,230
    p=head(W,H,"楽しさ・速さ・安全・素直さといった価値観ごとに言語があることを示す見本市")
    for label,x in [("楽しさ",55),("速さ",225),("安全",395),("素直さ",565)]:
        p+=[rect(x,75,120,95,NEUT,"#b8c2cc",rx=12),
            txt(x+60,116,label,17,INK,"middle","bold"),
            circ(x+60,146,11,BLUE,ACC)]
    p.append(txt(W/2,205,"大事にするものの数だけ、言語がある",14,SUB,"middle","bold"))
    save("fig-8-2.svg",p)

def fig_9_2():
    W,H=720,240
    p=head(W,H,"機械ごとに作り直し配布権も他人が握る世界と、URL 一つで全機械に届く世界の対比")
    p+=[rect(40,66,300,150,NEUT,"#b8c2cc",rx=10),
        txt(190,102,"作り直して配る",17,INK,"middle","bold"),
        txt(190,142,"OS ごとに作り直し",14,SUB,"middle"),
        txt(190,174,"配る鍵は、他人が握る",14,DANGER,"middle")]
    p+=[rect(380,66,300,150,BLUE,ACC,rx=10),
        txt(530,102,"URL 一つで届く",17,ACC,"middle","bold"),
        txt(530,142,"どの機械にも、そのまま",14,INK,"middle"),
        txt(530,174,"許可は、いらない",14,ACC,"middle","bold")]
    save("fig-9-2.svg",p)

for fn in [fig_0_1,fig_0_2,fig_1_1,fig_1_2,fig_1_3,fig_2_1,fig_2_2,fig_2_3,fig_3_1,fig_3_2,
           fig_4_1,fig_4_2,fig_4_3,fig_5_1,fig_5_2,fig_6_1,fig_6_2,fig_6_3,
           fig_7_1,fig_8_1,fig_8_2,fig_9_1,fig_9_2,fig_e_1]:
    fn()
print("done")
