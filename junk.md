```python
""" importing """
from aide_design.play import*

Q_in = 350*u.L/u.hr
H_L = 5*u.cm
Temperature = 20 * u.degC
Nu=pc.viscosity_kinematic(Temperature)
Nu
roughness = 0.1 *u.mm
K_minor=2
Length = 1*u.m
D_settledtube=pc.diam_pipe(Q_in,H_L,Length,Nu,roughness,K_minor)

print(D_settledtube.to(u.mm))
help(pc.diam_pipe)
```
