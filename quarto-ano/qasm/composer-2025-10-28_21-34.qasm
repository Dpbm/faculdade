OPENQASM 2.0;
include "qelib1.inc";


qreg q[4];
creg c[4];

gate ring q1,q2,q3 {
    ry(1.9106332362490184) q1;
}

gate cring s, q1, q2, q3 {
    ring q1, q2, q3;
}

cring q[0], q[1], q[2], q[3];