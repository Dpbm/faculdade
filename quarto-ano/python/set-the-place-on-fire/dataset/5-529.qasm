OPENQASM 3.0;
include "stdgates.inc";
gate sxdg _gate_q_0 {
  s _gate_q_0;
  h _gate_q_0;
  s _gate_q_0;
}
gate dcx _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_0;
}
bit[5] meas;
qubit[5] q;
sxdg q[2];
sxdg q[0];
dcx q[3], q[1];
sxdg q[0];
h q[4];
cswap q[1], q[3], q[2];
U(5.465923156758006, 0.5446241880854061, 0.6852826226103904) q[2];
u1(3.9979603301806907) q[1];
cx q[0], q[3];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
