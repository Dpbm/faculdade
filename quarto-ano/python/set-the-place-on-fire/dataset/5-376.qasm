OPENQASM 3.0;
include "stdgates.inc";
gate r(p0, p1) _gate_q_0 {
  u3(p0, p1 - pi/2, pi/2 - p1) _gate_q_0;
}
bit[5] meas;
qubit[5] q;
r(2.8409794838021876, 1.671878879802104) q[3];
cswap q[0], q[1], q[4];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
