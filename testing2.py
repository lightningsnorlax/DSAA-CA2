from Classes.binaryTree import BinaryTree
from Classes.stack import Stack
import re



def tokenize_expression(exp):
    # Use regular expression to tokenize the expression
    pattern = r"(\(|\)|\+|\-|\*|\/|\*\*|\d+)"
    tokens = re.findall(pattern, exp.replace(" ", ""))
    return tokens


def buildParseTree(exp):
    tokens = tokenize_expression(exp)
    print(tokens)

    stack = Stack()

    tree = BinaryTree("?")
    stack.push(tree)

    currentTree = tree

    for t in tokens:
        if t == "(":
            currentTree.insertLeft("?")
            stack.push(currentTree)
            currentTree = currentTree.getLeftTree()
        elif t in ["+", "-", "*", "/", "**"]:
            currentTree.setKey(t)
            currentTree.insertRight("?")
            stack.push(currentTree)
            currentTree = currentTree.getRightTree()
        elif t.isdigit():
            currentTree.setKey(float(t))
            parent = stack.pop()
            currentTree = parent
        elif t == ")":
            currentTree = stack.pop()
        else:
            raise ValueError

    return tree


def evaluate(tree):
    leftTree = tree.getLeftTree()
    rightTree = tree.getRightTree()
    op = tree.getKey()

    if leftTree != None and rightTree != None:
        if op == "+":
            return evaluate(leftTree) + evaluate(rightTree)
        elif op == "-":
            return evaluate(leftTree) - evaluate(rightTree)
        elif op == "*":
            return evaluate(leftTree) * evaluate(rightTree)
        elif op == "/":
            return evaluate(leftTree) / evaluate(rightTree)
        elif op == "**":
            return evaluate(leftTree) ** evaluate(rightTree)
    else:
        return tree.getKey()


if __name__ == "__main__":
    # Main program
    exp = "(2 + (4 * 5))"
    tree = buildParseTree(exp)
    tree.printInorder(0)
    print(f"The expression: {exp} evaluates to: {evaluate(tree)}")

    exp_without_parentheses = "2 + 4 * 5"
    tree_without_parentheses = buildParseTree(exp_without_parentheses)
    tree_without_parentheses.printInorder(0)
    print(f"The expression: {exp_without_parentheses} evaluates to: {evaluate(tree_without_parentheses)}")