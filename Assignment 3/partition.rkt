;Written by Lukas Bozinov for CS3342, Prof: Lucian Ilie

#lang scheme

(define (partition pred lst) ; define a function, "partition", which takes a predicate and a list as args
  (letrec ((partition-helper ;define recursive helper for partitioning w/ 3 args: list to process, nums to include in the final list, and nums not to include in the final list
            (lambda (lst DoInclude DoNotInclude)
              (if (null? lst) ;if the list is empty
                  (list (reverse DoInclude) (reverse DoNotInclude)) ;if statement=true, return list of reversed lists
                  ;else block
                  (let ((head (car lst)) ;define head as 1st elem in list
                        (tail (cdr lst))) ;define tail as rest of list
                    (if (pred head) ;check "if head is predicate": if true, add to DoInclude
                        (partition-helper tail (cons head DoInclude) DoNotInclude)
                        (partition-helper tail DoInclude (cons head DoNotInclude)))))))) ;else don't
                        ;continue processing
    (partition-helper lst '() '()))) ;run actual function