OPENQASM 3.0;
include "stdgates.inc";
gate rzx(p0) _gate_q_0, _gate_q_1 {
  h _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  h _gate_q_1;
}
gate ecr _gate_q_0, _gate_q_1 {
  rzx(pi/4) _gate_q_0, _gate_q_1;
  x _gate_q_0;
  rzx(-pi/4) _gate_q_0, _gate_q_1;
}
gate cs _gate_q_0, _gate_q_1 {
  p(pi/4) _gate_q_0;
  cx _gate_q_0, _gate_q_1;
  p(-pi/4) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
  p(pi/4) _gate_q_1;
}
bit[5] meas;
qubit[5] q;
ch q[0], q[1];
ecr q[4], q[2];
u2(2.855573500142355, 0.960066798262115) q[3];
cu(1.0273750027161965, 0.9559003748281104, 0.2207181709127779, 2.7603095177139787) q[2], q[4];
cs q[3], q[1];
rz(2.5971817555288377) q[0];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
