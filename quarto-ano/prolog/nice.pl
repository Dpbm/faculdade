trabalhador(marcelo).
trabalhador(ronaldo).
vagabundo(teu-cu).

nada(X) :- not(trabalhador(X)), not(vagabundo(X)).
filosofo(Y) :- nada(Y); vagabundo(Y).