```python
pwd
cd C:\\Users\\EN-CE-AC\\github\\UASB
# cd UASB/
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
.

#################################################################
############    Influent Pipe Calculations    ###################
#################################################################

# function calculates the influence area of each pipe in the reactor
def influence_area(n_pipes, diam):
  ## n_pipes = number of influent pipes in UASB
  ## diam = diameter of UASB reactor
  ca = pc.area_circle(diam) # ca = cross sectional area at top
  ia = ca/n_pipes           # ia = influence area
  return ia

# function calculates the pipe diameter based on flow, desired exit velocity, and number of pipes

def suggested_pipe_diam(flow_tot, v_exit, n_pipes):
  flow_per_pipe = flow_tot/n_pipes
  sugg_area = flow_per_pipe/v_exit
  sugg_diam = (pc.diam_circle(sugg_area)).to(u.mm)
  print('The suggested pipe diameter is ', sugg_diam)    
  return sugg_diam



# function calculates the flow in the pipe based on desired exit velocity, pipe diameter, and number of pipes
def flow_given_pipediam(p_d, v_exit, n_pipes):


## Area of influence calculation for 2 pipes
num_pipes = 2
infl_area_UASBpipe = influence_area(num_pipes, diam_UASB)
print('The influence area of each pipe is ', infl_area_UASBpipe)

## Pipe diameter calculation based on flow & exit velocity
velocity_exit = 0.3 *(u.m/u.s)
flow2 = 0.08*(u.L/u.s)
pipe_diam = suggested_pipe_diam(flow2, velocity_exit, num_pipes)

## Pulse flow for tank w/ aperture
def pulseflow(D_ap, H):
  # D_ap = diameter of aperture in bottom of tank
  # H = initial, "tipping point" height of WW
  C_c = 0.62   # For sharp aperture-would this be true?
  C_v = 0.97   # For water
  g = pc.gravity
  Q = (C_c*C_v*(pc.area_circle(D_ap))*(2*g*H)**(1/2)).to(u.L/u.s)
  # print('The pulseflow for the given aperture area and WW height is ' , Q)
  return Q

def height_wastewater(D_ap, D_pipe):
  C_c = 0.62   # For sharp aperture-would this be true?
  C_v = 0.97   # For water
  g = pc.gravity


## Given aperture diameter & WW height, what is the necessary pipe size for 2 pipes?
diam_ap = 10*u.cm
Height_WW = 0.3*u.m
flow_pulse = pulseflow(diam_ap,Height_WW)
print(flow_pulse)
pipe_diam_pulse = suggested_pipe_diam(flow_pulse, velocity_exit, num_pipes)

## Given aperture diameter & pipe size(2 pipes), what is the necessary height of WW in tank?


```
