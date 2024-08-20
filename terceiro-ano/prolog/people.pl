person(sam).
person(mark).
person(robert).
person(ann).

relative(ann, mark).
relative(ann, robert).
relative(mark, sam).
relative(robet, mark).

relative(mark, ann) :- relative(ann, mark).
relative(robert, ann) :- relative(ann, robert).
relative(sam, mark) :- relative(mark, sam).
relative(mark, robert) :- relative(robet, mark).

et(john) :- \+ person(john).
