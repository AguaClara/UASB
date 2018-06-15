from aide_design.play import*

temp = 27 * u.degC

nu = pc.viscosity_kinematic(temp)
HL = 50 *u.cm #headloss
v_exit = 0.3 * u.m/u.s #exit velocity of sewage
D_exit = 50 *u.mm #exit diameter of influent pipe
v_descend = 0.2 *u.m/u.s #descending sewage velocity
D_pipe = 100 *u.mm
P_biogas = 0 *u.atm #pressure inside UASB reactor due to biogas buildup



L_pipe = 11 * u.ft
PipeRough = 0.0015 *u.m
KMinor = 5

Q_pulse = v_descend*pc.area_circle(D_pipe) #pulse flow rate
print(Q_pulse)

HL_effective = HL - P_biogas/(pc.density_water(temp)*pc.gravity) #effective headloss
print(HL_effective)


pc.diam_pipe(Q_pulse, HL, L_pipe, nu, PipeRough, KMinor)

pc.diam_pipe(Q_pulse, HL_effective, L_pipe, nu, PipeRough, KMinor)
