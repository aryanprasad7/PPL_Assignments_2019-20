(defun findnth(n l)
  (if (or (> n (length l)) (< n 0))
    (error "Index out of bounds.")
    (if (= n 0)
      (car l)
      (nth (- n 1) (cdr l)))))

(write (findnth 3 '(1 2 3 4 5)))
