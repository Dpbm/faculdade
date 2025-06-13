OPENQASM 3.0;
include "stdgates.inc";
gate cu1(p0) _gate_q_0, _gate_q_1 {
  u1(p0/2) _gate_q_0;
  cx _gate_q_0, _gate_q_1;
  u1(-p0/2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  u1(p0/2) _gate_q_1;
}
gate dcx _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_0;
}
bit[5] meas;
qubit[5] q;
cu1(3.0965932493624018) q[1], q[3];
crx(5.597682581463799) q[4], q[2];
s q[0];
sx q[1];
u3(4.323723908417485, 5.083870837467228, 4.860867619821789) q[3];
dcx q[4], q[2];
rz(1.8053145334693774) q[0];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
