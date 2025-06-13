OPENQASM 3.0;
include "stdgates.inc";
gate sxdg _gate_q_0 {
  s _gate_q_0;
  h _gate_q_0;
  s _gate_q_0;
}
gate r(p0, p1) _gate_q_0 {
  u3(p0, p1 - pi/2, pi/2 - p1) _gate_q_0;
}
gate xx_plus_yy(p0, p1) _gate_q_0, _gate_q_1 {
  rz(p1) _gate_q_0;
  rz(-pi/2) _gate_q_1;
  sx _gate_q_1;
  rz(pi/2) _gate_q_1;
  s _gate_q_0;
  cx _gate_q_1, _gate_q_0;
  ry(-p0/2) _gate_q_1;
  ry(-p0/2) _gate_q_0;
  cx _gate_q_1, _gate_q_0;
  sdg _gate_q_0;
  rz(-pi/2) _gate_q_1;
  sxdg _gate_q_1;
  rz(pi/2) _gate_q_1;
  rz(-p1) _gate_q_0;
}
bit[5] meas;
qubit[5] q;
sxdg q[4];
U(5.642148117774512, 4.364954676874576, 1.8579842586651667) q[1];
r(5.690112348568308, 1.634225132850567) q[0];
u1(0.25267408208427955) q[2];
id q[3];
u1(0.7973926950194535) q[0];
rx(2.8762303015463537) q[1];
y q[4];
xx_plus_yy(3.6632264988924983, 5.5643207384634685) q[2], q[3];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
