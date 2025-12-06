OPENQASM 2.0;
include "qelib1.inc";

// adding a different angle
// you can create a wave pattern with the probabilities dist

qreg q[2];
creg c[4];


//h q[0];
//h q[1];
//p(pi/5) q[0];
//cx q[0], q[1];
//h q[0];


// a U pattern

h q[0];
p(pi/5) q[0];
cx q[0], q[1];
h q[0];
h q[1];
