OPENQASM 3.0;
include "stdgates.inc";
gate rzz(p0) _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
}
bit[5] meas;
qubit[5] q;
u2(2.780136243582973, 4.102807924749327) q[1];
ry(1.5041816158103012) q[0];
rx(5.196898669879441) q[3];
rzz(6.1722348673065985) q[2], q[4];
cswap q[2], q[1], q[3];
t q[0];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
