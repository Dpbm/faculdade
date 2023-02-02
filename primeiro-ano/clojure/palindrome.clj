(def required_word (read-line))


(defn reversed_word[word](apply str (reverse word)))
(defn check_palindrome[word](= (reversed_word word) word))

(println 
    (if 
        (check_palindrome required_word) 
        "It's a palindrome" 
        "It's not a palindrome"
    )
)