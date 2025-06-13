OPENQASM 3.0;
include "stdgates.inc";
gate r(p0, p1) _gate_q_0 {
  u3(p0, p1 - pi/2, pi/2 - p1) _gate_q_0;
}
bit[5] meas;
qubit[5] q;
r(1.140984865132551, 3.539560416490305) q[3];
r(5.489038542146458, 3.4102171420738703) q[2];
p(1.8510971247656005) q[1];
x q[4];
u1(1.09080124221339) q[0];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
