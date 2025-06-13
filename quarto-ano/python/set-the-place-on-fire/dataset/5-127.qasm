OPENQASM 3.0;
include "stdgates.inc";
gate cu3(p0, p1, p2) _gate_q_0, _gate_q_1 {
  u1(p1/2 + p2/2) _gate_q_0;
  u1(-p1/2 + p2/2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  u3(-p0/2, 0, -p1/2 - p2/2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  u3(p0/2, p1, 0) _gate_q_1;
}
gate rccx _gate_q_0, _gate_q_1, _gate_q_2 {
  u2(0, pi) _gate_q_2;
  u1(pi/4) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  u1(-pi/4) _gate_q_2;
  cx _gate_q_0, _gate_q_2;
  u1(pi/4) _gate_q_2;
  cx _gate_q_1, _gate_q_2;
  u1(-pi/4) _gate_q_2;
  u2(0, pi) _gate_q_2;
}
bit[5] meas;
qubit[5] q;
cu3(3.8547442727092576, 0.952308959936095, 2.1113321536702405) q[2], q[1];
rccx q[4], q[3], q[0];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
