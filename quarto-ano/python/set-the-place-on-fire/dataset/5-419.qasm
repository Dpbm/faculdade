OPENQASM 3.0;
include "stdgates.inc";
gate rxx(p0) _gate_q_0, _gate_q_1 {
  h _gate_q_0;
  h _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  h _gate_q_1;
  h _gate_q_0;
}
gate rzz(p0) _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
}
gate sxdg _gate_q_0 {
  s _gate_q_0;
  h _gate_q_0;
  s _gate_q_0;
}
gate cu3(p0, p1, p2) _gate_q_0, _gate_q_1 {
  u1(p1/2 + p2/2) _gate_q_0;
  u1(-p1/2 + p2/2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  u3(-p0/2, 0, -p1/2 - p2/2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  u3(p0/2, p1, 0) _gate_q_1;
}
gate cu1(p0) _gate_q_0, _gate_q_1 {
  u1(p0/2) _gate_q_0;
  cx _gate_q_0, _gate_q_1;
  u1(-p0/2) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  u1(p0/2) _gate_q_1;
}
bit[5] meas;
qubit[5] q;
rxx(6.24474994926698) q[2], q[1];
rzz(3.2378257668167105) q[4], q[3];
sx q[0];
z q[4];
sxdg q[1];
ccx q[0], q[3], q[2];
cu3(0.06080025161843403, 0.17557673644870242, 4.223621246031764) q[0], q[3];
s q[1];
cu1(4.427246717447997) q[4], q[2];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
