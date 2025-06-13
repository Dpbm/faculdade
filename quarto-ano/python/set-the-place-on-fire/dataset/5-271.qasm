OPENQASM 3.0;
include "stdgates.inc";
gate dcx _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  cx _gate_q_1, _gate_q_0;
}
bit[5] meas;
qubit[5] q;
ccx q[0], q[2], q[3];
u3(0.4728113838384423, 3.0496675091398773, 2.0713848128880934) q[4];
cx q[1], q[2];
dcx q[4], q[0];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
