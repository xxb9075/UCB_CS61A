; Q1
(define (compose-all funcs)
  (if (null? funcs)
    (lambda (x) x)
    (lambda (x) ((compose-all (cdr funcs)) ((car funcs) x)))
  )
)

; Q2
(define (tail-replicate x n)
  (define (helper s k)
    (if (= k 0)
      s
      (helper (cons x s) (- k 1))
    )
  )
  (helper nil n)
)