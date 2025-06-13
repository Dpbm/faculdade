edge(a,b,3).
edge(b,a,3).
edge(b,c,8).
edge(c,d,15).
edge(d,b,6).

withSomeWeight(X) :- edge(_,_,X).
connectsWith(X,Y) :- edge(X,Y,_).

count(T, b, a) :- 
    T is T + 3.
count(T, a, b) :-
     T is 0,
    T is T + 3,
    write(J),
    edge(b, J, _),
    count(T, b, J).

    
    
    
%count(0) :- true.
%count(1) :- false.