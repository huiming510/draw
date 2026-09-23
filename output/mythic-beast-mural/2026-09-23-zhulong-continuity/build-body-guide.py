"""Render the same continuous route as a standalone, occlusion-aware tube diagram."""
from pathlib import Path
import numpy as np
from PIL import Image, ImageDraw, ImageFont, ImageFilter

base=Path(__file__).parent
ns={'__file__':str(base/'trace-guide.py')}
exec((base/'trace-guide.py').read_text(encoding='utf-8').split("im=Image.new")[0],ns)
p=ns['pts']; arc=ns['arc']; count=len(p)
for a,b in zip(ns['curves'],ns['curves'][1:]):
    assert a[-1]==b[0], 'The guide must remain a single continuous path'
radius=np.interp(arc/arc[-1],[0,.07,.2,.8,1],[2,26,65,68,45])
# Depth changes are smooth along the single tube. They realize the chosen over/under order.
z=np.interp(np.arange(count),[0,300,500,570,680,750,810,1000],[0,0,0,300,300,240,150,150])
depth=np.full((1024,1536),-10000.,dtype=np.float32)
owner=np.full((1024,1536),-1,dtype=np.int32)
for k,((x,y),r,zk) in enumerate(zip(p,radius,z)):
    x0=max(0,int(x-r-1)); x1=min(1536,int(x+r+2))
    y0=max(0,int(y-r-1)); y1=min(1024,int(y+r+2))
    yy,xx=np.ogrid[y0:y1,x0:x1]
    squared=r*r-(xx-x)**2-(yy-y)**2
    surface=zk+np.sqrt(np.maximum(0,squared))
    old=depth[y0:y1,x0:x1]
    take=(squared>=0)&(surface>old)
    old[take]=surface[take]
    owner[y0:y1,x0:x1][take]=k
rgb=np.full((1024,1536,3),(255,250,240),dtype=np.uint8)
palette=[(100,159,194),(157,146,198),(211,177,87),(206,121,102)]
for lo,hi,c in [(0,200,palette[0]),(200,500,palette[1]),(500,800,palette[2]),(800,1001,palette[3])]:
    rgb[(owner>=lo)&(owner<hi)]=c
edges=np.zeros(owner.shape,dtype=bool)
for dy,dx in [(0,1),(1,0)]:
    other=np.roll(owner,(dy,dx),(0,1))
    edges|=((owner>=0)!=(other>=0))|((owner>=0)&(other>=0)&(np.abs(owner-other)>90))
edge_image=Image.fromarray((edges*255).astype('uint8')).filter(ImageFilter.MaxFilter(3))
rgb[np.array(edge_image)>0]=(37,50,58)
im=Image.fromarray(rgb)
d=ImageDraw.Draw(im); font=ImageFont.truetype('C:/Windows/Fonts/arial.ttf',26)
d.text((60,800),'ONE BODY, SAME LARGE LOOPS. COLOURS SHOW CONSECUTIVE SECTIONS.',fill='#25323a',font=font)
d.text((60,845),'Red head/neck -> gold front loop -> violet rear arch -> blue tail.',fill='#25323a',font=font)
d.text((60,890),'Structure reference only. Use the artwork for all surface details.',fill='#25323a',font=font)
im.save(base/'19-body-structure-guide.png')
print({'output':str(base/'19-body-structure-guide.png'),'continuous_segments':len(ns['curves']),'endpoints':[list(ns['curves'][0][0]),list(ns['curves'][-1][-1])]})
