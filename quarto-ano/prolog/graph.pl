liga(a,b,3).
liga(b,d,2).
liga(a,d,5).
liga(a,c,4).
liga(c,d,4).
liga(d,e,2).
liga(c,f,5).
liga(e,f,2).

liga(X,Y) :- liga(X,Y_), liga(Y,X_).
