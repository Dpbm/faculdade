OPENQASM 3.0;
include "stdgates.inc";
gate ccz _gate_q_0, _gate_q_1, _gate_q_2 {
  h _gate_q_2;
  ccx _gate_q_0, _gate_q_1, _gate_q_2;
  h _gate_q_2;
}
bit[5] meas;
qubit[5] q;
id q[4];
U(0.09649225779486961, 1.2224582116257032, 0.3409543894835885) q[2];
ccz q[1], q[0], q[3];
ccx q[0], q[1], q[3];
cp(2.70087197039951) q[4], q[2];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
