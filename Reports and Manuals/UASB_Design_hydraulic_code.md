
```python
from aguaclara.core.units import unit_registry as u
from aguaclara.core import physchem as pc
from aguaclara.core import pipes as pipes
from aguaclara.core import head_loss as HL
from aguaclara.core import utility as ut
from aguaclara.core import constants as con
from aguaclara.research import floc_model as fm
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

vol_d=16.26 * u.L #volume from one dump of the tipping bucket. This will need to be confirmed with testing once we have fabricated altered design for tipping bucket

def max_t_drain(vol_dump, Q):
  """time between dumps of tipping bucket, this should be maximum drain time so that the bucket will empty out between each dump, for cleaning and clog identification.
  t=vol_dump/Q"""
  return t.to(u.s)

def H_walls(vol_dump, W_FDT, t_walls,overflow_H):
  """this function calculates the height of the flow dividing walls, so that if a complete tip were to fill the flow dividing tank before it started draining out, the water level would be an inch above the top of the flow dividing tank. vol_dump=volume from one dump from tipping bucket; W_FDT=width of flow dividing tank; t_walls=thickness of the flow dividing walls; overflow_H=desired height of overflow over walls"""
  H_walls=(vol_dump-overflow_H*W_FDT**2)/(W_FDT**2-t_walls*W_FDT-t_walls*(W_FDT-t_walls)) #calculate H_walls by setting vol_dump equal to volume inside flow dividing system accounting for the volume that the flow dividing walls occupy
  H_walls=H_walls.to(u.inch)
  return H_walls


W_FDT_test= 12*u.inch#width of flow dividing walls
t_walls_test=1.5*u.inch
vol_dump_test=17 *u.L
overflow_test=1*u.inch  

H_walls_test=H_walls(vol_dump_test, W_FDT_test, t_walls_test, overflow_test)
print(H_walls_test)

def min_H_FDT(H_walls, overflow_H):
  """This function returns the minimum height of flow dividing tank."""
  min_H=head_gain_per_dump(H_walls, overflow_H)

def head_gain_per_dump(H_walls, overflow_H):
  """this is the assumed head gain if flow splits evenly in the flow dividing tank and does not start emptying out until the tip is over."""
  HG=H_walls+overflow_H
  HG=HG.to(u.inch)
  return HG

HG_per_dump_test=head_gain_per_dump(H_walls_test, overflow_test)
print(HG_per_dump_test)

def influent_K(n_90el):
  """this function calculates the minor loss coefficient of one of the influent pipes into the overall reactor. n_90elbows=number of 90 elbows in an influent pipe, D_pipe is the diameter of an influent pipe. Chose to calculate for minor loss because in the UASB design, minor losses are much more significant than major lossess."""
  influent_K=n_90el*HL.EL90_K_MINOR+HL.PIPE_EXIT_K_MINOR+HL.PIPE_ENTRANCE_K_MINOR
  return influent_K

def t_drain_fail_case(D_pipe, W_FDT, H_walls, n_90el):
  """ this function is meant to test fail case, to see how long it will take a section to drain in the case that all of the water from a tipping bucket dump goes into only one section of the flow dividing tank """
  A_FDT=W_FDT**2 #calculate the area of the flow dividing tank
  K_tot=influent_K(n_90el)
  t_drain=8*A_FDT/(np.pi*D_pipe**2)*(H_walls*K_tot/(2*pc.gravity))**.5 #from equation (97) in FCM_derivations section in AguaClara textbook
  return t_drain.to(u.s)

##Testing the function  t_fail_case
D_pipe_test=1*u.inch
n_90el_test=3
t_drain_fail_case_test=t_drain_fail_case(D_pipe_test, W_FDT_test, H_walls_test, n_90el_test)
print('If the influent pipes have a diameter of', D_pipe_test, 'and the width of the flow dividing tank is', W_FDT_test, 'then if all of the water went into only one section of of the flow dividing tank, that sections would take', t_drain_fail_case_test, ' to drain.')

def t_drain_even(D_pipe, W_FDT, H_walls, overflow_H, n_90el):
  """This function returns the estimated drain time from the FDT in the case that water from the tipping bucket fills up the sections evenly and quickly, so that water doesn't start draining until each section is full of water/there is water overflowing the dividing walls. headgain=headgain per dump """
  A_FDT=W_FDT**2 #calculate the area of the flow dividing tank
  K_tot=influent_K(n_90el)
  HG= head_gain_per_dump(H_walls, overflow_H)
  t_drain=8*A_FDT/(np.pi*D_pipe**2)*(HG*K_tot/(2*pc.gravity))**.5 #from equation (97) in FCM_derivations section in AguaClara textbook
  return t_drain.to(u.s)


t_drain_even_test=t_drain_even(D_pipe_test, W_FDT_test, H_walls_test,overflow_test, n_90el_test)  
print('If the influent pipes have a diameter of', D_pipe_test, 'and the width of the flow dividing tank is', W_FDT_test, 'then if all of the water went into only one section of of the flow dividing tank, that sections would take', t_drain_even_test, ' to drain.')



def D_pipe(W_FDT, t_drain, n_90el, H_walls, overflow_H):
  """This function returns the best diameter pipe to get the desired t_drain, given a flow dividing tank and goal drain time for the flow dividing tank. This is calculated based on case where flow divides evenly between sections and does not start draining until dump is complete."""
  A_FDT=W_FDT**2
  H=head_gain_per_dump(H_walls, overflow_H)
  K_tot=influent_K(n_90el)
  D=((8*W_FDT**2)/(np.pi*t_drain))**1/2*((H*K_tot)/(2*pc.gravity))**(1/4) #From equation 96 in AC textbook.
  return D.to(u.inch)

##Testing D_pipe function
Q_test= .08 * (u.L/u.s)#flow rate entering the UASB from Summer 2018 report
t_drain_test=max_t_drain(vol_d, Q_test)
print(t_drain_test)
D=D_pipe(W_FDT_test, t_drain_test, n_90el_test, H_walls_test, overflow_test)

def upflow_vel(t_drain_even, UASB_diameter, vol_dump):
  """this function calculates an estimate for upflow velocity in the UASB reactor assuming that water from the dump is divided evenly into sections and does not start draining until dump is complete. Ideally, this velocity will be faster than the settling velocity of sludge particles, which is approximately .03 m/s. """
  UASB_Q_dump=vol_dump/t_drain_even ##calculate flow rate through UASB as water from a dump of tipping bucket flows through the system
  UASB_CA=pc.area_circle(UASB_diameter)
  up_vel=UASB_Q_dump/UASB_CA
  return up_vel.to(u.m/u.s)

##Testing upflow_vel function
UASB_diameter_test=3*u.ft
upflow_vel_test=upflow_vel(t_drain_even_test, UASB_diameter_test, vol_d)
print(upflow_vel_test)


##NOW USING HYDRAULIC CODE TO TEST DIFFERENT DESIGN OPTIONS

W_FDT= #width of the flow dividing tank; this will be an array of available square HDPE buckets
```

##Future Work for Python Documentation
In the future, the team plants to instantiate a UASB object to represent a real UASB. The team will also import available HDPE tank dimensions and HDPE pipe sizing, so that it can test the available combinations with ease to determine the optimal design for the UASB influent system, and then use that to update the onShape model. The team also needs to do testing with the tipping bucket to make a more informed decision about optimal drain time.
