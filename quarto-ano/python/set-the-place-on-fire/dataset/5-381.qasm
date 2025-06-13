OPENQASM 3.0;
include "stdgates.inc";
gate rzx(p0) _gate_q_0, _gate_q_1 {
  h _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  h _gate_q_1;
}
bit[5] meas;
qubit[5] q;
rx(3.294192692397614) q[4];
tdg q[0];
ccx q[2], q[1], q[3];
u2(3.5208974517764813, 0.6406777881840637) q[2];
ccx q[4], q[0], q[1];
cswap q[0], q[4], q[2];
rzx(1.0629104781600338) q[1], q[3];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
