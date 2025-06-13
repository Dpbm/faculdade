OPENQASM 3.0;
include "stdgates.inc";
gate rzz(p0) _gate_q_0, _gate_q_1 {
  cx _gate_q_0, _gate_q_1;
  rz(p0) _gate_q_1;
  cx _gate_q_0, _gate_q_1;
}
gate r(p0, p1) _gate_q_0 {
  u3(p0, p1 - pi/2, pi/2 - p1) _gate_q_0;
}
bit[5] meas;
qubit[5] q;
ch q[3], q[4];
rzz(2.8910706349199633) q[1], q[0];
rx(3.053442527495424) q[2];
U(6.153213845211945, 4.037318547148271, 5.682086265810648) q[2];
sx q[3];
u2(1.525140598192428, 5.216107656613481) q[0];
sdg q[4];
U(4.37914845780066, 4.433653518364068, 1.5708954675907942) q[1];
r(3.451320060208876, 0.8976802687478699) q[0];
r(0.9559847274804304, 0.7157437720299282) q[4];
s q[2];
u1(3.215583084776512) q[3];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
