```python
#pwd
#cd UASB/
from aide_design.play import*
from UASB_size import*
height_UASB = (7*u.ft).to(u.cm)
diam_UASB = (3*u.ft).to(u.cm)
HRT = 4*u.hr

UASB = UASBSize(3*u.ft, 7*u.ft)
height_cyl_wedge = UASB[0]
vol_reactor = UASB[1]
flow = UASB[2]
people_served = UASB[3]
people_served_bw = UASB[4]

def influence_area(n_pipes, diam):
  ## n_pipes = number of influent pipes in UASB
  ## diam = diameter of UASB reactor
  ca = pc.area_circle(diam)
  ia = ca/n_pipes
  print('The influence area of each pipe is ', ia)
  return ia

## Area of influence calculation
num_pipes = 2
infl_area_UASBpipe = influence_area(num_pipes, diam_UASB)


print('The influence area of each pipe is ', influence_area_pipe)
```
