OPENQASM 3.0;
include "stdgates.inc";
gate rzz(p0) _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
}
gate r(p0, p1) _gate_q_0 {
  u3(p0, p1 - pi/2, pi/2 - p1) _gate_q_0;
}
bit[5] meas;
qubit[5] q;
cx q[1], q[2];
rzz(4.185027827469675) q[0], q[3];
r(3.1519545275061267, 0.10672528216784469) q[4];
rzz(1.8238374355777396) q[2], q[3];
ry(0.5958768563358287) q[0];
p(2.8968680293698226) q[4];
x q[1];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
