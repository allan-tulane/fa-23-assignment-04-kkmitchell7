import math, queue
from collections import Counter

####### Problem 3 #######

test_cases = [('book', 'back'), ('kookaburra', 'kookybird'), ('elephant', 'relevant'), ('AAAGAATTCA', 'AAATCA')]
alignments = [('b--ook', 'bac--k'), ('kook-ab-urr-a', 'kooky-bi-r-d-'), ('relev--ant','-ele-phant'), ('AAAGAATTCA', 'AAA---T-CA')]

def MED(S, T):
    # TO DO - modify to account for insertions, deletions and substitutions
    if (S == ""):
        return(len(T))
    elif (T == ""):
        return(len(S))
    else:
        if (S[0] == T[0]):
            return(MED(S[1:], T[1:]))
        else:
            return(1 + min(MED(S, T[1:]), MED(S[1:], T)))

def fast_MED(S, T, MED={}):
    # TODO -  implement top-down memoization
    if (S,T) in MED:
        return MED[(S,T)]
    if (S == ""):
        MED[(S,T)] = len(T)
    elif (T == ""):
        MED[(S,T)] = len(S)
    else:
        if (S[0] == T[0]):
            MED[(S,T)] = fast_MED(S[1:], T[1:], MED)
        else:
            MED[(S,T)] = 1 + min(fast_MED(S, T[1:], MED), fast_MED(S[1:], T, MED))
    return MED[(S,T)]

def fast_align_MED(S, T, MED={}, alignments={}):
    # TODO - keep track of alignment
    if (S,T) in alignments:
        return alignments[(S,T)]
    if (S == ""):
        MED[(S,T)] = len(T)
        alignments[S,T] = ("-"*len(T),T)
    elif (T == ""):
        MED[(S,T)] = len(S)
        alignments[S,T] = (S,"-"*len(S))
    else:
        if (S[0] == T[0]):
            MED[S,T] = fast_MED(S[1:],T[1:],MED)
            alignments[S,T] = (S[0]+fast_align_MED(S[1:],T[1:],MED,alignments)[0],T[0]+fast_align_MED(S[1:],T[1:],MED,alignments)[1])
        else:
            if fast_MED(S[1:],T,MED) < fast_MED(S,T[1:], MED):
                MED[S,T] = 1+fast_MED(S[1:],T,MED)
                alignments[S,T] = (S[0] +fast_align_MED(S[1:],T,MED,alignments)[0], "-" + fast_align_MED(S[1:],T,MED,alignments)[1])
            else:
                MED[S,T] = 1 + fast_MED(S,T[1:],MED)
                alignments[S,T] = ("-" +fast_align_MED(S,T[1:],MED,alignments)[0], T[0] + fast_align_MED(S,T[1:],MED,alignments)[1])
    return alignments[S,T]


"""
Notice that in the process of computing the optimal edit
  distance, we can also keep track of the actual sequence of edits to
  each position of $S$ and $T$. Update your implementation of `fast_MED` to
  return the optimal edit distance as well as an *alignment* of the
  two strings which show the edits that yield this distance. An
  alignment just shows what changes are made to $S$ to transform it to
  $T$. For example, suppose $S$=`relevant` and $T$=`elephant`. If
  insertion and deletion costs are both equal to $1$, then the
  edit distance between $S$ and $T$ is 4 and an
  alignment of these two strings would look like this:

  `relev--ant`\
  `-ele-phant`

Implement `fast_align_MED` to return the aligned versions of $S$ and $T$,
and test your code with `test_alignment`.
"""

def test_MED():
    for S, T in test_cases:
        assert fast_MED(S, T) == MED(S, T)
                                 
def test_align():
    for i in range(len(test_cases)):
        S, T = test_cases[i]
        align_S, align_T = fast_align_MED(S, T)
        assert (align_S == alignments[i][0] and align_T == alignments[i][1])

test_MED()