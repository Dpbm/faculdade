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
cu(3.4779643216257834, 5.251673532125265, 2.677660908979194, 3.1375813452392247) q[3], q[0];
cswap q[1], q[4], q[2];
ecr q[3], q[1];
cs q[4], q[0];
U(4.853863958623955, 0.050642410369769, 4.563036677740748) q[2];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
