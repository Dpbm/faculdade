OPENQASM 3.0;
include "stdgates.inc";
gate r(p0, p1) _gate_q_0 {
  u3(p0, p1 - pi/2, pi/2 - p1) _gate_q_0;
}
bit[5] meas;
qubit[5] q;
cy q[0], q[4];
cswap q[2], q[1], q[3];
r(1.1278662641805104, 0.2539586615170296) q[0];
cswap q[4], q[3], q[1];
U(3.769109981744244, 0.43780330789777394, 1.350932051616674) q[2];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
