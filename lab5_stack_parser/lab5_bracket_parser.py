class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        return self.items.pop()

    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        return None


def is_balanced(expression):
    stack = Stack()

    bracket_map = {
        ')': '(',
        ']': '[',
        '}': '{'
    }

    for char in expression:
        if char in "([{":
            stack.push(char)

        elif char in ")]}":
            if stack.is_empty():
                return False

            top = stack.pop()

            if top != bracket_map[char]:
                return False

    return stack.is_empty()


if __name__ == "__main__":
    # Required examples
    expr1 = "{[()()]}"
    expr2 = "{[(])}"

    print("LABORATORY ACTIVITY NO. 5")
    print("Stack-Based Parenthesis & Arithmetic Parser")
    print("=" * 45)

    print("\nProvided Examples:")
    print(f"Is {expr1} balanced? {is_balanced(expr1)}")
    print(f"Is {expr2} balanced? {is_balanced(expr2)}")

    # Five customized mathematical expressions
    test_expressions = [
        ("(2 + 3) * [4 - 1]", True),
        ("{(a + b) * [c - d]}", True),
        ("((8 / 2) + 5)", True),
        ("([)]", False),
        ("{[(x + y)]", False)
    ]

    print("\nFive Customized Mathematical Expressions:")
    print("-" * 65)

    for expression, expected in test_expressions:
        result = is_balanced(expression)
        status = "PASS" if result == expected else "FAIL"

        print(f"Expression: {expression}")
        print(f"Balanced: {result}")
        print(f"Expected: {expected}")
        print(f"Status: {status}")
        print("-" * 65)

    # Display stack states for {[()]}
