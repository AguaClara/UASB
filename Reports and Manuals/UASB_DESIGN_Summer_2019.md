
```python
import aguaclara.core.head_loss as minorloss
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

pipes.ID_sch40(4*u.inch)
class UASBtest:
  def __init__(
          self,
          temp = 10 * u.degC, #estimated temp at IAAWTF
          pipe_diam = 1.0 * u.inch, #diameter of the influent pipe
          n_elbows = 2, #the number of elbows in the influent pipe
          pipe_roughness = .0015 * u.mm, # PVC pipe roughness
          time_dump = 2* u.s, #NOTE: get better value with actual testing, this is a rough estimate
          UASB_diameter = 10 * u.inch,
          UASB_height = 8 * u.ft, #this height refers to the height of the pipe that is used to make the UASB canister, NOT the water level in the UASB.
          HRT = 6 * u.hr, #minimum HRT of wastewater in reactor for adequate treatment NOTE: some studies have shown 6 hrs is optimal
          target_upflow_vel= 10 * u.m/u.hr, #target up flow velocity to fluidize sludge blanket
          diameter_drain_pipe= 3 * u.inch, #diameter of the pipe that connects the holding tank to influent pipe ( 3 inches was chosen so that the area was similar to that of one section in drain tank in previous design.)
          descending_sewage_vel= .2 * u.m/u.s, #Maximum velocity that will allow air bubbles to rise out of reactor. Must only be achieved in beginning of influent pipe systems, not throughout.
          ww_gen_rate = 10.8 * u.L/u.hr, #Wastewater Generation per Person
          angle_sludge_weir=60*u.degrees, #angle of sludge weir
          percent_sludge= .7, #based on summer 2018 team research
          diam_sludge_granules = .5 * u.mm, #this is the lower end of range of diameters for sludge, goes up to 3 mm https://www.ncbi.nlm.nih.gov/pmc/articles/PMC6070658/ so this would correspond to a slower setting particle
          rho_sludge= 1383 * u.g/u.L, #density of sludge granules. source:https://www.ijsr.net/archive/v4i4/SUB153022.pdf
          rho_water=1 *u.g/u.mL,
          lift= 10*u.cm, #to make sure that lift height is significant
          effluent_pipe_diameter=1*u.inch,
          tippingbucket_diameter=6.25 * u.inch

):
      """Instantiate a UASB object, representing a real UASB component.
      :param Q: Flow rate of water water through the UASB.
      :type Q: float * u.L/u.s
      :param temp: Water temperature of the UASB
      :type temp: float * u.degC
      :param cannister_diam: diameter of the UASB canister
      :type cannister_diam: float * u.ft
      :param effluent_H: height of effluent line in UASB
      :type effluent_H: float * u.ft
      :param vol_dump: volume of one complete dump from tipping bucket
      :type vol_dump: float * u.L
      :param pipe_diam: ID of the influent pipes
      :type pipe_diam: float * u.inch
      :param n_elbows: number of 90 degree elbows per influent pipe
      :type n_elbows: float * dimensionless
      :param pipe_roughness: roughness of influent pipes
      :type pipe_roughness: float * u.m
      :returns: object
      :rtype: UASB
      """
      self.temp = temp
      self.pipe_diam = pipes.ID_sch40(pipe_diam)
      self.n_elbows = n_elbows
      self.pipe_roughness = pipe_roughness
      self.time_dump = time_dump
      self.UASB_diameter = pipes.ID_sch40(UASB_diameter)
      self.HRT = HRT
      self.target_upflow_vel=target_upflow_vel
      self.diameter_drain_pipe=pipes.ID_sch40(diameter_drain_pipe)
      self.descending_sewage_vel=descending_sewage_vel
      self.percent_sluge=percent_sludge
      self.UASB_height=UASB_height
      self.effluent_pipe_diameter=pipes.ID_sch40(effluent_pipe_diameter)
      self.ww_gen_rate=ww_gen_rate
      self.lift=lift
      self.tippingbucket_diameter=tippingbucket_diameter

  @property
  def UASB_area(self):
    """This function calculates the surface area of the UASB canister """
    area= pc.area_circle(self.UASB_diameter)
    return area

  @property
  def vol_dump(self):
    vol=self.lift*self.UASB_area
    return vol

  @property
  def area_drain_pipe(self):
    area=pc.area_circle(self.diameter_drain_pipe)
    return area

  @property
  def HG_per_dump(self):
    """This function calculates the head gain per dump, assuming that the water level in the canister is in line with the bottom of the "drain pipe" that connects the holding tank to the 1 inch influent pipe """
    HG=self.vol_dump/self.area_drain_pipe
    return HG

  @property
  def length_drain_pipe(self):
    """This function calculates the length of the drain pipe necessary so that the volume of 1 dump from the tipping bucket fills the drain pipe"""
    h=(self.HG_per_dump).to(u.inch)
    return h  

  @property
  def water_level_height(self):
    """This function determines the height of the water level in the reactor. The water level is supposed to be in line with the bottom of the drain pipe"""
    #NOTE: how much "safety" do we want here? also, are
    return self.UASB_height

  @property
  def volume_UASB(self):
    """this function calculates volume of liquid inside UASB reactor, not including influent pipes"""
    vol=self.UASB_area*self.water_level_height
    return vol

  @property
  def flow_rate_avg(self):
    """this function estimates the max flow rate, given min HRT and volume of fluid inside canister, that the UASB can handle"""
    Qmax=(self.volume_UASB)/self.HRT
    return Qmax

  @property
  def upflow_vel_avg(self):
    """this function calculates the average up flow velocity of in the UASB canister"""
    up_v=self.flow_rate_avg/self.UASB_area
    return up_v

  @property
  def aggregate_k(self):
    """This function calculates  the aggregate minor loss coefficient of the drain system from the holding tank into the 'canister' aka the 10 inch clear PVC pipe"""
    influent_K=self.n_elbows*minorloss.EL90_K_MINOR+minorloss.PIPE_EXIT_K_MINOR+minorloss.PIPE_ENTRANCE_K_MINOR
    return influent_K

  @property
  def drain_time(self):
    """This function calculates how long it takes for a dump from the tipping bucket to drain into the tank, assuming that the bottom of the drain pipe (which connects the 1.5 inch pipe to the holding tank) is in line with the water level in the canister and does not begin draining out until the dump is complete. Note that this time should be approximately the same as the time it takes for the tipping bucket to fill up/fast enough to produce desired up flow velocity in the tank"""
    #NOTE: should we include minor loss from holding tank to drain tank, or assume water just starts from drain tank
    #NOTE: drain time also might drastically underestimate actual drain time, since all the water from the tipping bucket won't necessarily go straight into the drain pipe from the tipping bucket, but could linger around the bottom of the holding tank.  
    time = 8*self.area_drain_pipe/(np.pi*(self.pipe_diam)**2)*(self.HG_per_dump*self.aggregate_k/(2*pc.gravity))**(1/2)
    return time    


  @property
  def upflow_velocity_pulse_average(self):
    """this function estimates the average upflow velocity in the canister during a pulse by dividing the time it takes for a dump from the tipping bucket to drain into the system to get a "pulse flow rate" and then dividing that by the cross sectional area of the UASB to get an estimate for "pulse up flow velocity"""
    UASB_Q_dump=self.vol_dump/self.drain_time ##calculate flow rate through UASB as water from a dump of tipping bucket flows through the system
    up_vel=UASB_Q_dump/self.UASB_area
    return up_vel.to(u.m/u.s)

  @property
  def bucket_fill_time(self):
    """This function determines the estimated time it will take the tipping bucket to fill, using the estimated volume of one dump from the new, smaller tipping bucket size and the flow rate of water entering the UASB, according to the function flow_rate_max"""
    UASB_Q_dump=self.vol_dump/self.drain_time #calculate flow rate through UASB as water from a dump of tipping bucket flows through the system
    up_vel=UASB_Q_dump/self.UASB_area
    return up_vel.to(u.m/u.s)

  @property
  def num_people_served(self):
    """This function estimates the number of people that could be served by a UASB reactor of this size"""
    num=self.ww_gen_rate/self.flow_rate_avg
    num=num.to(u.dimensionless)
    return num

  @property
  def pivot_height(self):
    """This function estimates the height of the pivots on the tipping bucket, so that the bucket will dump at desired volume"""
    return (self.vol_dump/pc.area_circle(self.tippingbucket_diameter)).to(u.inch)

test=UASBtest(pipe_diam=1.5*u.inch, lift=6*u.cm)
data ={'UASB element':['Diameter Canister', 'Diameter Influent Pipe', 'Number of Elbows in Influent', 'Average Up flow Pulse Velocity', 'Tipping Bucket Dump Volume', 'Length Pulse Pipe', 'Diameter Pulse Pipe', 'Water Level Height', 'Lift', 'Pivot Height' ],
       'Measurement': [test.UASB_diameter, test.pipe_diam, test.n_elbows, (test.upflow_velocity_pulse_average).to(u.mm/u.s), test.vol_dump.to(u.gal), test.length_drain_pipe, test.diameter_drain_pipe, test.water_level_height, test.lift, test.pivot_height]}

print((test.upflow_vel_avg).to(u.mm/u.s))
df=pd.DataFrame(data)
print(df)
