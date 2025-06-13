% Como precisamos saber a ligação entre casais, foi necessário
% adicionar novos membros na árvore, assim como novos fatos 
% para prosseguir com o requisitado.

gerou(maria, jose).
gerou(joao, jose).
gerou(joao, ana).
gerou(jose, julia).
gerou(jose, iris).
gerou(iris, jorge).

% novos membros
gerou(marcelo, pedro).
gerou(marcelo, rodolfo).
gerou(jose, talita).
gerou(maria, claudia).

feminino(clara).
feminino(ana).
feminino(talita).
feminino(maria).
feminino(julia).
feminino(iris).
feminino(claudia).

masculino(pedro).
masculino(rodolfo).
masculino(marcos).
masculino(marcelo).
masculino(jose).
masculino(joao).
masculino(jorge).

% casal presente no grafo
casado(maria, joao).
% casais ficticios
casado(pedro, clara).
casado(rodolfo, ana).
casado(marcos, talita).
casado(claudia, jorge).
casado(iris,marcelo).

filho(X,Y) :- gerou(Y,X), masculino(X).
filha(X,Y) :- gerou(Y,X), feminino(X).

pai(X,Y) :- gerou(X,Y), masculino(X).
mae(X,Y) :- gerou(X,Y), feminino(X).

gfather(X,Y) :- gerou(X,Z), gerou(Z,Y), masculino(X).
gmother(X,Y) :- gerou(X,Z), gerou(Z,Y), feminino(X).

% uma vez que algumas queries requerem testar irmao(X,X), precisamos
% verificar se Y é diferente de Y.
irmao(X,Y) :- gerou(Z,X), gerou(Z,Y), masculino(X), (X \= Y).
irma(X,Y) :- gerou(Z,X), gerou(Z,Y), feminino(X), (X \= Y).

tio(X,Y) :- gerou(Z,Y), irmao(X,Z), (X \= Z).
tia(X,Y) :- gerou(Z,Y), irma(X,Z), (X \= Z).

sobrinho(X,Y) :- (tio(Y,X);tia(Y,X)), masculino(X). 
sobrinha(X,Y) :- (tio(Y,X);tia(Y,X)), feminino(X).

primo(X,Y) :- filho(X,Z), (tio(Z,Y);tia(Z,Y)).
prima(X,Y) :- filha(X,Z), (tio(Z,Y);tia(Z,Y)).


% como maria é conjuge de joão da mesma forma que joão é conjuge de Maria, 
% essa regra define que não importa a ordem de chamada, maria esta para joão
% como joão está para maria.
casal(X,Y) :- casado(X, Y); casado(Y, X).


% X é marido/esposa de Y
marido(X,Y) :- casal(X,Y), masculino(X).
esposa(X,Y) :- casal(X,Y), feminino(X).


% X é cunhado(a) de Y
cunhado(X,Y) :- marido(X, Z), (irmao(Y,Z);irma(Y,Z)).
cunhada(X,Y) :- esposa(X, Z), (irmao(Y,Z);irma(Y,Z)).

% X é genro/nora de Y
genro(X,Y) :- marido(X,Z), gerou(Y,Z).
nora(X,Y) :- esposa(X,Z), gerou(Y,Z).

% X é sogro(a) de Y
sogro(X,Y) :- casal(Y,Z), pai(X,Z).
sogra(X,Y) :- casal(Y,Z), mae(X,Z).

% X é cocunhado(a) de Y
cocunhado(X,Y) :- cunhado(X,Z), (marido(Z,Y);esposa(Z,Y)).
cocunhada(X,Y) :- cunhada(X,Z), (marido(Z,Y);esposa(Z,Y)).

