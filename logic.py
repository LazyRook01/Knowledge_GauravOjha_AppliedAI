import itertools

class Symbol():

    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return self.name

    def evaluate(self, model):
        try:
            return (model[self.name])
        except KeyError:
            raise Exception(f"variable {self.name} not in model")

    def formula(self):
        return self.name

    def symbols(self):
        return {self.name}

class Not():
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"Not({self.name})"

    def evaluate(self, model):
        return not self.name.evaluate(model)

    def formula(self):
        return "¬" + self.name.formula()

    def symbols(self):
        return self.name.symbols()


class And():
    def __init__(self, *conjuncts):
        self.conjuncts = list(conjuncts)

    def __repr__(self):
        conjunctions = ", ".join(
            [str(conjunct) for conjunct in self.conjuncts]
        )
        return f"And({conjunctions})"

    def add(self, conjunct):
        self.conjuncts.append(conjunct)

    def evaluate(self, model):
        return all(conjunct.evaluate(model) for conjunct in self.conjuncts)

    def formula(self):
        if len(self.conjuncts) == 1:
            return self.conjuncts[0].formula()
        return " ∧ ".join([conjunct.formula() for conjunct in self.conjuncts])

    def symbols(self):
        return set.union(*[conjunct.symbols() for conjunct in self.conjuncts])


class Or():
    def __init__(self, *disjuncts):
        self.disjuncts = list(disjuncts)

    def __repr__(self):
        disjuncts = ", ".join([str(disjunct) for disjunct in self.disjuncts])
        return f"Or({disjuncts})"

    def evaluate(self, model):
        return any(disjunct.evaluate(model) for disjunct in self.disjuncts)

    def formula(self):
        if len(self.disjuncts) == 1:
            return self.disjuncts[0].formula()
        return " ∨  ".join([disjunct.formula() for disjunct in self.disjuncts])

    def symbols(self):
        return set.union(*[disjunct.symbols() for disjunct in self.disjuncts])


class Implication():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Implication({self.left}, {self.right})"

    def evaluate(self, model):
        return ((not self.left.evaluate(model))
                or self.right.evaluate(model))

    def formula(self):
        left = self.left.formula()
        right = self.right.formula()

        return f"{left} => {right}"

    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())


class Biconditional():
    def __init__(self, left, right):
        self.left = left
        self.right = right

    def __repr__(self):
        return f"Biconditional({self.left}, {self.right})"

    def evaluate(self, model):
        return ((self.left.evaluate(model)
                 and self.right.evaluate(model))
                or (not self.left.evaluate(model)
                    and not self.right.evaluate(model)))

    def formula(self):
        left = str(self.left)
        right = str(self.right)

        return f"{left} <=> {right}"

    def symbols(self):
        return set.union(self.left.symbols(), self.right.symbols())


def create_table(symbols):
    values = [True, False]
    num_columns = len(symbols)
    all_combinations = list(itertools.product(values, repeat=num_columns))
    table = []
    for model in all_combinations:
        temp = dict()
        for symbol, value in zip(symbols, model):
            temp[symbol] = value
        table.append(temp)
        del (temp)
    return table
def model_check(knowledge, query):
    symbols = set.union(knowledge.symbols(), query.symbols())
    model_table = create_table(symbols)
    final_answers = []
    for model in model_table:
        if knowledge.evaluate(model):
            answer = query.evaluate(model)
            final_answers.append(answer)
    final_answer = all(final_answers)
    return final_answer
