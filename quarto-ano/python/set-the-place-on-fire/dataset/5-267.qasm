OPENQASM 3.0;
include "stdgates.inc";
bit[5] meas;
qubit[5] q;
U(0.17081697787536035, 0.7129133952810816, 5.267373601630808) q[0];
cswap q[1], q[3], q[4];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
