OPENQASM 3.0;
include "stdgates.inc";
gate r(p0, p1) _gate_q_0 {
  u3(p0, p1 - pi/2, pi/2 - p1) _gate_q_0;
}
bit[5] meas;
qubit[5] q;
cu(4.942730979429844, 1.4930256935999198, 2.814960189139308, 0.3499681000550641) q[3], q[0];
cp(0.6279967110808224) q[4], q[2];
ry(0.6515459296359923) q[1];
ccx q[4], q[2], q[3];
rx(5.755353384455705) q[0];
r(1.9644546407408592, 4.788889751525725) q[1];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
