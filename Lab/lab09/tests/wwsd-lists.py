test = {
  'name': 'What Would Scheme Print?',
  'points': 1,
  'suites': [
    {
      'cases': [
        {
          'code': r"""
          scm> (cons 1 2)
          (1 . 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cons 1 (cons 2 nil))
          (1 2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (car (cons 1 (cons 2 nil)))
          1
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cdr (cons 1 (cons 2 nil)))
          (2)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (list 1 2 3)
          (1 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (list 1 (cons 2 3))
          (1 (2 . 3))
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> '(1 2 3)
          (1 2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> '(2 . 3)
          (2 . 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> '(2 . (3))  ; Recall dot rule for pairs
          (2 3)
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (equal? '(1 . (2 . 3)) (cons 1 (cons 2 (cons 3 nil))))  ; Recall how boolean values are displayed
          #f
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (equal? '(1 . (2 . 3)) (cons 1 (cons 2 3)))
          #t
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (equal? '(1 . (2 . 3)) (list 1 (cons 2 3)))
          #f
          """,
          'hidden': False,
          'locked': False
        },
        {
          'code': r"""
          scm> (cons 1 '(list 2 3))  ; Recall quoting
          (1 list 2 3)
          """,
          'hidden': False,
          'locked': False
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    },
    {
      'cases': [
        {
          'code': r"""
          scm> (cons (list 2 (cons 3 4)) nil)
          e34cac8f1ba66ae521ab3ae5dcfaf28b
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (car (cdr '(127 . ((131 . (137))))))
          3c07b200dbf1fe01a6b0c5977d8b6e05
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> (equal? '(1 . ((2 . 3))) (cons 1 (cons (cons 2 3) nil)))
          f2f78bdee92fb379bc57e3ef1a6c0dc2
          # locked
          """,
          'hidden': False,
          'locked': True
        },
        {
          'code': r"""
          scm> '(cons 4 (cons (cons 6 8) ()))
          6117e327e7d53413652889593b49dd33
          # locked
          """,
          'hidden': False,
          'locked': True
        }
      ],
      'scored': True,
      'setup': r"""
      
      """,
      'teardown': '',
      'type': 'scheme'
    }
  ]
}
