(defun factorial (n)
  (setq x 1)
  (loop for i from 1 to n
	do (setq x (* x i))
	)
  (return-from factorial x)
  )

(loop for i from 1 to 16
      do (format t "~D! = ~D~%" i (factorial i))
      )

