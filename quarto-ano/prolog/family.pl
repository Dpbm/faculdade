gerou(joao, ana).
gerou(joao, jose).
gerou(maria, jose).
gerou(jose, julia).
gerou(jose, iris).
gerou(iris, jorge).

feminino(ana).
feminino(maria).
feminino(iris).
masculino(joao).
masculino(jose).
masculino(jorge).

sexo(ana,feminino).
sexo(maria,feminino).
sexo(iris,feminino).
sexo(joao,masculino).
sexo(jose,masculino).
sexo(jorge,masculino).

filho(X,Y) :- gerou(Y,X), masculino(X).
filha(X,Y) :- gerou(Y,X), feminino(X).

pai(X,Y) :- gerou(X,Y), masculino(X).
mae(X,Y) :- gerou(X,Y), feminino(X).

avo(X,Y) :- gerou(X,I), gerou(I,Y), masculino(X).
avo(X,Y) :-
    	pai(X,I), 
    	gerou(I, Y).

%avo_(X,Y) :- mae(X,I), gerou(I,X).
%avo_(X,Y) :- gerou(X,I), gerou(I,Y), feminino(X).

irmao(X,Y) :- gerou(I, X), gerou(I,Y), X \= Y, masculino(X).
%irmao(X,Y) :- filho(X, I), gerou(I, Y).

irma(X,Y) :- gerou(I, X), gerou(I,Y), X \= Y, feminino(X).
%irma(X,Y) :- filha(X, I), gerou(I, Y).

tio(X,Y) :- gerou(I, Y), irmao(X, I).
tia(X,Y) :- gerou(I, Y), irma(X, I).

sobrinho(X,Y) :- (tio(Y,X); tia(Y,X)), masculino(X).
sobrinha(X,Y) :- (tio(Y,X); tia(Y,X)), feminino(X). 

primo(X,Y) :- gerou(I, X), gerou(J, Y), (irmao(I,J); irma(I,J)), masculino(X).
primo(X,Y) :- gerou(I,Y), (tio(I,X),tia(I,X)), masculino(X).
primo(X, Y) :- filho(X,Z), (tio(Z,Y); tia(Z,Y)).

prima(X,Y) :- gerou(I, X), gerou(J, Y), (irmao(I,J); irma(I,J)), feminino(X).
prima(X,Y) :- gerou(I,Y), tio(I,X), feminino(X).
prima(X, Y) :- filha(X,Z), (tio(Z,Y); tia(Z,Y)).