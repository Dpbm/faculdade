OPENQASM 3.0;
include "stdgates.inc";
gate cu1(p0) _gate_q_0, _gate_q_1 {
  u1(p0/2) _gate_q_0;
  cx _gate_q_0, _gate_q_1;
  u1(-p0/2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  u1(p0/2) _gate_q_1;
}
bit[5] meas;
qubit[5] q;
cswap q[1], q[4], q[2];
crx(2.4254849885616085) q[3], q[0];
ccx q[4], q[3], q[1];
cu1(2.3150531753252106) q[2], q[0];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
