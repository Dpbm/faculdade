OPENQASM 3.0;
include "stdgates.inc";
gate r(p0, p1) _gate_q_0 {
  u3(p0, p1 - pi/2, pi/2 - p1) _gate_q_0;
}
bit[5] meas;
qubit[5] q;
s q[3];
r(0.8395161534507519, 5.885080009039416) q[0];
t q[1];
r(4.038736617375929, 4.185946427026657) q[2];
sdg q[4];
p(0.796142340144168) q[1];
t q[2];
u2(4.882320786983403, 2.4978194822711233) q[3];
cx q[0], q[4];
sx q[3];
p(5.481591618355121) q[0];
y q[2];
u2(3.737625785980114, 2.335177050460189) q[4];
t q[1];
barrier q[0], q[1], q[2], q[3], q[4];
meas[0] = measure q[0];
meas[1] = measure q[1];
meas[2] = measure q[2];
meas[3] = measure q[3];
meas[4] = measure q[4];
