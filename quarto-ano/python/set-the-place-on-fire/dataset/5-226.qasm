OPENQASM 3.0;
include "stdgates.inc";
gate ccz _gate_q_0, _gate_q_1, _gate_q_2 {
  h _gate_q_2;
  ccx _gate_q_0, _gate_q_1, _gate_q_2;
  h _gate_q_2;
}
bit[5] meas;
qubit[5] q;
tdg q[0];
z q[3];
ccz q[1], q[2], q[4];
crx(5.2933135143120875) q[2], q[1];
u3(0.074904963144144, 5.7134966919780155, 2.447180115961006) q[0];
u3(2.7437948924137734, 0.33427807788163766, 2.109099646488378) q[4];
t q[0];
ccx q[3], q[4], q[1];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
