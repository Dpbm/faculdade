(defun sum(l)
  (reduce  #'+ l)
)

(defun mul(l)
  (reduce  #'* l)
)

(defparameter numbers (list 1 2 3 4 5 6 7 8 9))

(print numbers)
(format t "~%first: ~d~%" ( first numbers ))
(format t "second: ~d~%" ( second numbers ))
(format t "sum: ~d~%" ( sum numbers ))
(format t "multplication: ~d~%" ( mul numbers ))
