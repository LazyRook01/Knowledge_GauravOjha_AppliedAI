from logic import *

rain = Symbol("rain") #Its raining
hagrid = Symbol("hagrid") #Harry visited Hagrid
dumbledore = Symbol("dumbledore") #Harry visited dumbledore

knowledge = And(
    Implication(Not(rain), hagrid),
    Or(hagrid, dumbledore),
    Not(And(hagrid, dumbledore)),
    dumbledore
)

print(model_check(knowledge, rain))

P = Symbol("It is a Tuesday")
Q = Symbol("It is Raining")
R = Symbol("Harry will go for a run")


knowledge1 = And(Implication(And(P, Not(Q)), R),
                  P,
                  Not(Q))

print(knowledge1)

knowledge1.formula()
knowledge1.symbols()

model_check(knowledge1, R)

print(Not(P))

Biconditional(P,Q)
And(P,Q)
