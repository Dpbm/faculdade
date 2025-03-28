%isso e uma arvore
pai(joao, ana).
pai(joao, jose).

pai(maria, jose).

pai(jose, julia).
pai(jose, iris).

pai(iris, jorge).

%rules
pais(Pai, Mae) :- 
	pai(Pai, Filho),
	pai(Mae, Filho),
	Pai \= Mae.

filho(Filho) :- pai(_, Filho).
filho(Pai, Filho) :- pai(Pai, Filho).

irmaos(Irmao1, Irmao2) :- 
	filho(Pai, Irmao1),
	filho(Pai, Irmao2),
	Irmao1 \= Irmao2.
irmao(Irmao) :- irmaos(Irmao, _).

%e avo
avo(Avo) :- 
	pai(Avo, Pai), 
	pai(Pai, _),
	Avo \= Pai.

%e tio
tio(Tio) :- 
	irmaos(Tio, Irmao), 
	pai(Irmao, _).
	
