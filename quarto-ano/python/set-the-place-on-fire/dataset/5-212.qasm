OPENQASM 3.0;
include "stdgates.inc";
gate rzz(p0) _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
}
bit[5] meas;
qubit[5] q;
rzz(4.5927885404896855) q[3], q[0];
rzz(0.8529603929352981) q[2], q[4];
u3(1.7918704648152295, 1.3663525119582387, 1.6953773177155957) q[1];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
