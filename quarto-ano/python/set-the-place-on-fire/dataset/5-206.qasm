OPENQASM 3.0;
include "stdgates.inc";
bit[5] meas;
qubit[5] q;
ccx q[4], q[3], q[0];
ch q[2], q[1];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
