liga(a,b,3).
liga(b,a,3).

liga(b,d,2).
liga(d,b,2).

liga(a,d,5).
liga(d,a,5).

liga(a,c,4).
liga(c,a,4).

liga(c,d,4).
liga(d,c,4).

liga(d,e,2).
liga(e,d,2).

liga(c,f,5).
liga(f,c,5).

liga(e,f,2).
liga(f,e,2).

%liga(X,Y) :- liga(X,Y,_), liga(Y,X,_)

%caminho(I,F,C) :- ((liga(I,F,C)); (liga(I,A,C1),liga(A,F,C2),(C is C1 + C2))), (I \= F).
%caminho(I,F,C) :- liga(I,A,C1),liga(A,F,C2),(C is C1 + C2), (I \= F).
%caminho2passos(I,F,C) :- liga(I,A,C1),liga(A,M,C2),liga(M,F,C3),(C is C1 + C2 + C3).

% recursivo
% vai ficar rodando inifinitamente
caminho(I,F,C) :- liga(I,F,C), (I \= F).
caminho(I,F,C) :- liga(I,A,C1), caminho(A,F,C2), (C is C1 + C2).
