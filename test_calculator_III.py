import unittest

class ExpressionEvaluator:
    @staticmethod
    def evaluate(tokens):
        tokens = ExpressionEvaluator._normalize(tokens)
        values = []
        operators = []

        for token in tokens:
            if ExpressionEvaluator._is_number(token):
                values.append(float(token))
            elif token == "(":
                operators.append(token)
            elif token == ")":
                while operators and operators[-1] != "(":
                    ExpressionEvaluator._apply_operator(values, operators.pop())
                operators.pop()  # Remove '('
            elif ExpressionEvaluator._is_operator(token):
                while (operators and operators[-1] != "(" and
                       ExpressionEvaluator._precedence(operators[-1]) >=
                       ExpressionEvaluator._precedence(token)):
                    ExpressionEvaluator._apply_operator(values, operators.pop())
                operators.append(token)

        while operators:
            ExpressionEvaluator._apply_operator(values, operators.pop())

        return values.pop()

    @staticmethod
    def _apply_operator(values, op):
        right = values.pop()
        left = values.pop()
        if op == "+": values.append(left + right)
        elif op == "-": values.append(left - right)
        elif op == "*": values.append(left * right)
        elif op == "/": values.append(left / right)

    
    @staticmethod
    def _normalize(tokens):
        result = []
        for i, token in enumerate(tokens):
            if token in ["+", "-"] and (i == 0 or tokens[i - 1] in ["+", "-", "*", "/", "("]):
                result.append("0")
            result.append(token)
        return result

    @staticmethod
    def _is_operator(token):
        return token in ["+", "-", "*", "/"]

    @staticmethod
    def _precedence(op):
        return 2 if op in ["*", "/"] else 1

    @staticmethod
    def _is_number(token):
        try:
            float(token)
            return True
        except ValueError:
            return False

class UnitTests(unittest.TestCase):
    def test_addition(self):
        self.assertAlmostEqual(ExpressionEvaluator.evaluate(["2", "+", "3"]), 5.0)

    def test_operator_precedence(self):
        self.assertAlmostEqual(ExpressionEvaluator.evaluate(["2", "+", "3", "*", "4"]), 14.0)

    def test_parentheses(self):
        self.assertAlmostEqual(ExpressionEvaluator.evaluate(["(", "2", "+", "3", ")", "*", "4"]), 20.0)

    def test_subtraction(self):
        self.assertAlmostEqual(ExpressionEvaluator.evaluate(["10", "-", "4"]), 6.0)

    def test_division(self):
        self.assertAlmostEqual(ExpressionEvaluator.evaluate(["8", "/", "2"]), 4.0)

    def test_unary_positive(self):
        self.assertAlmostEqual(ExpressionEvaluator.evaluate(["+", "2"]), 2.0)

    def test_unary_negative(self):
        self.assertAlmostEqual(ExpressionEvaluator.evaluate(["-", "2"]), -2.0)   

    def test_complex_expression(self):
        self.assertAlmostEqual(ExpressionEvaluator.evaluate(["(", "2", "+", "3", ")", "*", "(", "10", "-", "4", ")"]), 30.0)

if __name__ == "__main__":
    unittest.main()