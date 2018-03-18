```python
from aide_design.play import*

height_UASB = (7*u.ft).to(u.cm)
diam_UASB = (3*u.ft).to(u.cm)
HRT = 4*u.hr

UASB = UASBSize(3*u.ft, 7*u.ft)
height_cyl_wedge = UASB[0]
vol_reactor = UASB[1]
flow = UASB[2]
people_served[3]
people_served[4]


## Area of influence calculation
num_pipes = 2
crossarea_top = pc.area_circle(diam_UASB)
influence_area_pipe = crossarea_top/num_pipes


```
