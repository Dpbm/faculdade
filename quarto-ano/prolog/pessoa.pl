%facts are represented with lowercase letters and variables with capital ones

%nascer
nascer(pedro,marilia).
nascer(marco,blumenal).

%ficar
fica(marilia, saoPaulo).
fica(blumenal,santaCatarina).

%regras
paulista(Pessoa) :- nascer(Pessoa,Cidade), fica(Cidade,saoPaulo).
