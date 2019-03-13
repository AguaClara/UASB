determine headgain per bucket dump

```python
from aide_design.play import*
def head_gain_per_dump(dump_vol, tank_width, tank_length):
  """Determines gain in hydraulic head per dump of tipping bucket
   based on geometry of influent system
  """
  tank_headgain = dump_vol / (tank_width * tank_length)
  headgain = tank_headgain
  return headgain.to(u.inch)

#applying code to current UASB design
dump_vol=16.26*u.L
tank_width=12*u.inch
tank_length=12*u.inch  
print("With current design, the head gain per dump of tipping bucket is ", head_gain_per_dump(dump_vol, tank_width, tank_length))

print((5.4*u.m).to(u.ft))
print((1.2*(u.m/u.hr)).to(u.m/u.s))

calculate max upflow velocity

def maxUpflowVelocity(reactor_height, HRT):
  """Determines max upflow velocity from reactor_height (reactor_height is height of effluent tube) and min desired HRT"""
  max_upflow_velocity=(reactor_height/HRT).to(u.m/u.s)
  return max_upflow_velocity

#applying code to current UASB design
reactor_height=49.656*u.inch
HRT=4*u.hr  
max_upflow_vel=maxUpflowVelocity(reactor_height, HRT)
print('max upflow velocity in UASB=',max_upflow_vel)

print((100*(u.m/u.hr)).to(u.m/u.s))
```
