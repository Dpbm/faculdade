% FATOS(base de conhecimento)
% Agente lógico


nobre(X,[X|_]). %X is the head of a list
nobre(X,[_|T]) :- nobre(X,T). % recursion. If tail is the element X






















