"""Build a standalone topology diagram, not an edit of the illustration."""
from pathlib import Path
from PIL import Image, ImageDraw, ImageFont
import numpy as np

OUT = Path(__file__).parent
# Tail -> rear arch -> front loop -> neck -> head, following the original large arcs.
curves = [
    [(1380,335),(1410,220),(1280,80),(1115,100)],
    [(1115,100),(905,135),(1300,330),(1100,375)],
    [(1100,375),(916,420),(774,253),(622,168)],
    [(622,168),(439,64),(336,157),(340,284)],
    [(340,284),(344,398),(453,415),(595,428)],
    [(595,428),(780,445),(795,610),(580,574)],
    [(580,574),(365,539),(311,315),(172,381)],
    [(172,381),(24,451),(126,616),(298,552)],
    [(298,552),(556,456),(689,269),(893,305)],
    [(893,305),(1108,339),(1100,475),(1180,625)],
]
pts=[]
for curve in curves:
    p=np.array(curve,dtype=float)
    for t in np.linspace(0,1,100,endpoint=False):
        pts.append((1-t)**3*p[0]+3*(1-t)**2*t*p[1]+3*(1-t)*t*t*p[2]+t**3*p[3])
pts=np.array(pts+[np.array(curves[-1][-1])])
arc=np.r_[0,np.cumsum(np.linalg.norm(np.diff(pts,axis=0),axis=1))]
radii=np.interp(arc/arc[-1],[0,.07,.2,.8,1],[2,28,65,69,46])
crossings=[]
def cross(a,b): return a[0]*b[1]-a[1]*b[0]
for i in range(len(pts)-1):
    a,b=pts[i:i+2]; r=b-a
    for j in range(i+30,len(pts)-1):
        c,d=pts[j:j+2]; s=d-c; den=cross(r,s)
        if abs(den)<1e-7: continue
        u=cross(c-a,s)/den; v=cross(c-a,r)/den
        if 0<=u<1 and 0<=v<1:
            crossings.append((i,j,a+u*r))

im=Image.new('RGB',(1536,1024),'#fffaf0'); draw=ImageDraw.Draw(im)
def colour(k):
    return '#3873a6' if k<200 else '#7770ab' if k<500 else '#b88621' if k<800 else '#b84b36'
# A centreline only: one continuous spline, with short gaps at the four underpasses.
for k in range(len(pts)-1):
    draw.line([tuple(pts[k]),tuple(pts[k+1])],fill=colour(k),width=14)
for i,j,p in crossings:
    owner=i if i>600 else j  # Original front loop passes above the neck at the low-left crossing.
    ids=np.flatnonzero(abs(arc-arc[owner])<45)
    line=[tuple(pts[k]) for k in ids]
    draw.line(line,fill='#fffaf0',width=34)
    draw.line(line,fill=colour(owner),width=14)
font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',28)
for num,k in enumerate([990,850,740,560,425,350,270,150,0],1):
    x,y=pts[k]
    draw.ellipse((x-18,y-18,x+18,y+18),fill='#fffaf0',outline='#25323a',width=2)
    draw.text((x,y),str(num),fill='#25323a',font=font,anchor='mm')
draw.text((60,785),'ONE CONTINUOUS BODY: 1 HEAD -> 9 TAIL',fill='#25323a',font=font)
draw.text((60,829),'Junction guide only. Keep the original illustration, colour and reflection.',fill='#25323a',font=font)
draw.text((60,873),'Colours distinguish consecutive sections of ONE body. White gaps mean underpasses.',fill='#25323a',font=font)
im.save(OUT/'18-continuity-guide.png')
print({'crossings':[(i,j,[round(float(v),1) for v in p]) for i,j,p in crossings], 'output':str(OUT/'18-continuity-guide.png')})
