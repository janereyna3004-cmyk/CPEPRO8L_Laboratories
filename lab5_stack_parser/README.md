# Laboratory Activity No. 5
## Stack-Based Parenthesis & Arithmetic Parser

**Name:** Mary Jane Y. Reyna  
**Date:** September 5, 2026  
**Course Code:** CPEPRO8L  
**Course Title:** Data Structures and Algorithms  
**Term:** First Semester, AY 2026–2027

---

## 1. Objectives

1. Build a custom Stack class using a dynamic list.
2. Check whether brackets `()`, `[]`, and `{}` are balanced.
3. Understand stack `push()` and `pop()` operations.
4. Apply the Last-In, First-Out (LIFO) principle to expression parsing.
5. Test the program using mathematical expressions with balanced and unbalanced brackets.

---

## 2. Program Description

The program uses a custom `Stack` class to determine whether brackets in an expression are balanced.

The Stack class contains the following methods:

- `__init__()` — Initializes an empty stack.
- `is_empty()` — Checks whether the stack is empty.
- `push(item)` — Adds an item to the stack.
- `pop()` — Removes and returns the top item. It raises an `IndexError` if the stack is empty.
- `peek()` — Returns the top item without removing it, or `None` if the stack is empty.

The `is_balanced(expression)` function checks the opening and closing brackets. It returns `True` if all brackets match in the correct order and `False` if they do not.

---

## 3. How to Run the Program

**Filename:** `lab5_bracket_parser.py`

### Steps

1. Open Visual Studio Code.
2. Open the folder containing `lab5_bracket_parser.py`.
3. Open the terminal by selecting **Terminal → New Terminal**.
4. Run the following command:

```bash
python lab5_bracket_parser.py
```

If the command does not work, try:

```bash
py lab5_bracket_parser.py
```

5. Press Enter to execute the program.

---

## 4. Provided Examples and Results

The program tests the two expressions provided in the laboratory activity.

| Expression | Expected Result | Explanation |
|---|---|---|
| `{[()()]}` | `True` | All brackets match in the correct order. |
| `{[(])}` | `False` | The closing brackets do not match the correct opening brackets. |

### Expected Console Output

```text
Provided Examples:
Is {[()()]} balanced? True
Is {[(])} balanced? False
```

The first expression is balanced because each opening bracket has a corresponding closing bracket. The second expression is unbalanced because the brackets close in the wrong order.

---

## 5. Five Customized Mathematical Expressions

The following expressions are used to test the program.

| No. | Expression | Expected Result | Explanation |
|---|---|---|---|
| 1 | `(2 + 3) * [4 - 1]` | `True` | Parentheses and square brackets are correctly matched. |
| 2 | `{(a + b) * [c - d]}` | `True` | Curly braces, parentheses, and square brackets are correctly matched. |
| 3 | `((8 / 2) + 5)` | `True` | All parentheses are correctly matched. |
| 4 | `([)]` | `False` | The brackets close in the wrong order. |
| 5 | `{[(x + y)]` | `False` | The opening curly brace does not have a matching closing curly brace. |

### Expected Test Results

All five customized expressions should display `PASS` when the actual result matches the expected result.

```text
Expression: (2 + 3) * [4 - 1]
Balanced: True
Expected: True
Status: PASS
-----------------------------------------------------------------
Expression: {(a + b) * [c - d]}
Balanced: True
Expected: True
Status: PASS
-----------------------------------------------------------------
Expression: ((8 / 2) + 5)
Balanced: True
Expected: True
Status: PASS
-----------------------------------------------------------------
Expression: ([)]
Balanced: False
Expected: False
Status: PASS
-----------------------------------------------------------------
Expression: {[(x + y)]
Balanced: False
Expected: False
Status: PASS
```

---

## 6. Stack Trace for `{[()]}`

The expression `{[()]}` demonstrates how the stack changes during the parsing process.

The stack follows the **Last-In, First-Out (LIFO)** principle, meaning the last item pushed onto the stack is the first item removed.

| Step | Character | Operation | Stack State |
|---|---|---|---|
| 1 | `{` | Push `{` | `['{']` |
| 2 | `[` | Push `[` | `['{', '[']` |
| 3 | `(` | Push `(` | `['{', '[', '(']` |
| 4 | `)` | Pop `(` because it matches | `['{', '[']` |
| 5 | `]` | Pop `[` because it matches | `['{']` |
| 6 | `}` | Pop `{` because it matches | `[]` |

### Analysis

1. The opening curly brace `{` is pushed onto the stack.
2. The opening square bracket `[` is pushed onto the stack.
3. The opening parenthesis `(` is pushed onto the stack.
4. The closing parenthesis `)` matches and removes `(`.
5. The closing square bracket `]` matches and removes `[`.
6. The closing curly brace `}` matches and removes `{`.

At the end of the process, the stack is empty. Therefore, the expression `{[()]}` is balanced.

### Expected Final Result

```text
Is {[()]} balanced? True
```

---

## 7. Conclusion

This laboratory activity demonstrates how a stack can be used to check balanced brackets in mathematical expressions. By implementing the `Stack` class and the `is_balanced()` function, I learned how push and pop operations help identify matching brackets and detect incorrect bracket sequences.

The five customized expressions test the program using both balanced and unbalanced brackets. The stack trace for `{[()]}` illustrates how the stack changes at every step until all brackets are matched.

Overall, this activity helped me understand the Last-In, First-Out (LIFO) principle and its practical application in expression parsing.