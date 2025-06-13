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
bit[5] meas;
qubit[5] q;
U(4.387310577903217, 1.690710532441551, 3.1840145037441174) q[0];
p(5.055560377914734) q[3];
t q[4];
cu3(2.2764736137220276, 3.8065385157644376, 4.278942110416169) q[1], q[2];
rcccx q[2], q[1], q[0], q[4];
rx(5.440725508922616) q[3];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
