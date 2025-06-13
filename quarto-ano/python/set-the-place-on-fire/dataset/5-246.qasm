OPENQASM 3.0;
include "stdgates.inc";
gate ccz _gate_q_0, _gate_q_1, _gate_q_2 {
  h _gate_q_2;
  ccx _gate_q_0, _gate_q_1, _gate_q_2;
  h _gate_q_2;
}
gate r(p0, p1) _gate_q_0 {
  u3(p0, p1 - pi/2, pi/2 - p1) _gate_q_0;
}
bit[5] meas;
qubit[5] q;
cswap q[4], q[3], q[1];
crx(0.065787955217301) q[2], q[0];
rx(3.0584095436139) q[4];
ccz q[0], q[2], q[1];
t q[3];
sdg q[1];
p(6.22610112958473) q[2];
r(6.042388499306705, 4.087079707958984) q[3];
t q[0];
s q[4];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
