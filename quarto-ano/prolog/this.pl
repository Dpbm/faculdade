% Representação da arvore genealogica %

% gerou(P1,P2): gerou(gerador,gerado).
 
% Fatos
 
gerou(maria, jose).

gerou(joao, jose).

gerou(joao, ana).

gerou(jose, julia).

gerou(jose, iris).

gerou(iris, jorge).
 
feminino(maria).

feminino(ana).

feminino(julia).

feminino(iris).
 
masculino(jose).

masculino(joao).

masculino(jorge).
 
% Regras
 
filho(X,Y) :- gerou(Y,X), masculino(X).

filha(X,Y) :- gerou(Y,X), feminino(X).
 
pai(X,Y) :- gerou(X,Y), masculino(X).

mae(X,Y) :- gerou(X,Y), feminino(X).
 
gfather(X,Y) :- gerou(X,Z), gerou(Z,Y), masculino(X).

%gfather(X,Y) :- pai(X,Z), gerou(Z,Y).

gmother(X,Y) :- gerou(X,Z), gerou(Z,Y), feminino(X).
 
irmao(X,Y) :- gerou(Z,X), gerou(Z,Y), masculino(X).

%irmao(X,Y) :- filho(X,Z), gerou(Z,Y).

irma(X,Y) :- gerou(Z,X), gerou(Z,Y), feminino(X).
 
tio(X,Y) :- gerou(Z,Y), irmao(X,Z), (X \= Z).

tia(X,Y) :- gerou(Z,Y), irma(X,Z), (X \= Z).
 
sobrinho(X,Y) :- (tio(Y,X);tia(Y,X)), masculino(X).

sobrinha(X,Y) :- (tio(Y,X);tia(Y,X)), feminino(X).
 
primo(X,Y) :- fliho(X,Z), (tio(Z,X);tia(Z,Y)).

prima(X,Y) :- fliha(X,Z), (tio(Z,X);tia(Z,Y)).

 