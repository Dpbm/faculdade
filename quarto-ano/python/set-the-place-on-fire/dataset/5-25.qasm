OPENQASM 3.0;
include "stdgates.inc";
bit[5] meas;
qubit[5] q;
u3(3.269035609192232, 2.4745132964992647, 4.909987140716979) q[1];
ccx q[4], q[2], q[0];
rx(3.6857583416761517) q[3];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
