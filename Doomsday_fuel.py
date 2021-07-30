from fractions import Fraction
import numpy as np

def gcd(a ,b):
    return(a if b == 0 else gcd(b,a%b))                                                       # Returns Greatest Common Divisor of a and b using the Euclidian Algorithm

def formated(fractions):
    lcm = 1    
    for i in fractions:
        if i.denominator != 1:
            lcm = lcm*i.denominator/gcd(lcm, i.denominator)                                   # LCM for fundemental-matrix probabiliti-fractions
    out = [(i*lcm).numerator for i in fractions]                                              # List of Fundemental-matrix probabilitie-fraction-numerators normalised by LCD
    out.append(lcm)                                                                           # LCD appemnded to list of normalised numerators
    return out                                                                                # returns [List of normalised numerators, denominator]

def solution(m):
    if sum (m[0]) == 0:                                                                       # if s0 to absorbing
        return [1, 1]                                                                         # return 1/1
    to_absorbing = [i for i in range(len(m)) if sum(m[i]) == 0]                               # Transitions to an absorbing state
    to_transient = [i for i in range(len(m)) if sum(m[i]) != 0]                               # Transitions to a transient state 
    P = [[float(float(n)/float(sum(state))) if n != 0 else 0 for n in state] for state in m]  # Observed Transitions -> Stochastic Transition probability Matrix
    Q = [[P[i][j] for j in to_transient]for i in to_transient]                                # Q Matrix (probability of transitioning from some transient state to another)
    R = [[P[i][j] for j in to_absorbing]for i in to_transient]                                # R Matrix (probability of transitioning from some transient state to an absorbing)
    F = np.dot(np.linalg.inv(np.identity(len(Q)) - np.asarray(Q)).tolist(), R).tolist()       # Returns Markov Fundemental Matrix of m
                                                                                              # https://en.wikipedia.org/wiki/Absorbing_Markov_chain

    return formated([Fraction(i).limit_denominator() for i in F[0]])                          # Fundemental-Matrix probabilitie-fractions
