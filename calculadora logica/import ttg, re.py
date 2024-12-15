import ttg, re

class Calculator:
    def __init__(self):
        self.expression = ""
        self.truth_table = ""
        self.valuation = ""

    def replace_characters(self, input_string):
        replacements = {
            '→': ' => ',
            '↔': ' = ',
            'v': ' or ',
            '⊻': ' xor ',
            '∧': ' and ',
            '~': 'not '
        }
        pattern = re.compile('|'.join(re.escape(key) for key in replacements.keys()))
        return pattern.sub(lambda match: replacements[match.group(0)], input_string)

    def get_propositions(self):
        if self.expression != "":
            values = re.findall(r"\b(?!and\b|or\b|not\b|xor\b)\w+\b", self.expression)

            propositions = list(dict.fromkeys(values)) # removing duplicates

            return propositions
        else:
            print("Error: Must set expression first")
            raise SyntaxError

    def get_valuation(self):
        if self.expression != "":
            if self.valuation == "Contingency":
                self.valuation = "A expressão é uma contingência."
            elif self.valuation == "Tautology":
                self.valuation = "A expressão é uma tautologia."
            elif self.valuation == "Contradiction":
                self.valuation = "A expressão é uma contradição."
            return self.valuation
        else:
            print("Error: Must set expression first")
            raise SyntaxError

    def get_truth_table(self):
        return self.truth_table

    def set_expression(self, expression):
        self.expression = self.replace_characters(expression)
        propositions = self.get_propositions()
        self.truth_table = ttg.Truths(propositions, [self.expression])
        self.valuation = self.truth_table.valuation()
        