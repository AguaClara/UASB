```python
pwd
cd UASB/
from aide_design.play import*
from UASB_size import*

# Characteristics of UASB, set parameters
height_UASB = (7*u.ft).to(u.cm)
diam_UASB = (3*u.ft).to(u.cm)
HRT = 4*u.hr

UASB = UASBSize(diam_UASB, height_UASB)
height_cyl_wedge = UASB[0]
vol_reactor = UASB[1]
flow = UASB[2]
people_served = UASB[3]
people_served_bw = UASB[4]

#################################################################
############    Influent Pipe Calculations    ###################
#################################################################

# function calculates the influence area of each pipe in the reactor
def influence_area(n_pipes, diam):
  ## n_pipes = number of influent pipes in UASB
  ## diam = diameter of UASB reactor
  ca = pc.area_circle(diam) # ca = cross sectional area at top
  ia = ca/n_pipes           # ia = influence area
  print('The influence area of each pipe is ', ia)
  return ia

# function calculates the pipe diameter based on flow, desired exit velocity, and number of pipes

def suggested_pipe_diam(flow_tot, v_exit, n_pipes):
  flow_per_pipe = flow_tot/n_pipes
  sugg_area = flow_per_pipe/v_exit
  sugg_diam = (pc.diam_circle(sugg_area)).to(u.mm)
  print('The suggested pipe diameter is ', sugg_diam)
  return sugg_diam

## Area of influence calculation for 2 pipes
num_pipes = 2
infl_area_UASBpipe = influence_area(num_pipes, diam_UASB)
print('The influence area of each pipe is ', infl_area_UASBpipe)

## Pipe diameter calculation based on flow & exit velocity
velocity_exit = 0.4 *(u.m/u.s)
pipe_diam = suggested_pipe_diam(flow, velocity_exit, num_pipes)


```
