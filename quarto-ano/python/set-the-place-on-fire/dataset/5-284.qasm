OPENQASM 3.0;
include "stdgates.inc";
gate rcccx _gate_q_0, _gate_q_1, _gate_q_2, _gate_q_3 {
  u2(0, pi) _gate_q_3;
  u1(pi/4) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  u1(-pi/4) _gate_q_3;
  u2(0, pi) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  u1(pi/4) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  u1(-pi/4) _gate_q_3;
  cx _gate_q_0, _gate_q_3;
  u1(pi/4) _gate_q_3;
  cx _gate_q_1, _gate_q_3;
  u1(-pi/4) _gate_q_3;
  u2(0, pi) _gate_q_3;
  u1(pi/4) _gate_q_3;
  cx _gate_q_2, _gate_q_3;
  u1(-pi/4) _gate_q_3;
  u2(0, pi) _gate_q_3;
}
gate cu3(p0, p1, p2) _gate_q_0, _gate_q_1 {
  u1(p1/2 + p2/2) _gate_q_0;
  u1(-p1/2 + p2/2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  u3(-p0/2, 0, -p1/2 - p2/2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  u3(p0/2, p1, 0) _gate_q_1;
}
bit[5] meas;
qubit[5] q;
rcccx q[3], q[4], q[0], q[1];
id q[2];
cswap q[1], q[4], q[2];
cu3(3.464302308612493, 6.070619378398532, 2.927125622833062) q[3], q[0];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
