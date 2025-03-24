%facts
joga_bem(time).

%rules
ganha(X) :- joga_bem(X).
felizes(X) :- ganha(X).
culpado(X) :- \+ joga_bem(X).
culpado(X) :- \+ felizes(X).
