def action():
    "Evaluate a single variable"
    import re

    from Classes.stack import Stack
    from Classes.binaryTree import BinaryTree
    from Classes.parseTree import buildParseTree, evaluate
            
    def evaluate(tree):
        leftTree = tree.getLeftTree()
        rightTree = tree.getRightTree()
        op = tree.getKey()
        if leftTree != None and rightTree != None:
            if op == '+':
                return evaluate(leftTree) + evaluate(rightTree)
            elif op == '-':
                return evaluate(leftTree) - evaluate(rightTree)
            elif op == '*':
                return evaluate(leftTree) * evaluate(rightTree)
            elif op == '/':
                return evaluate(leftTree) / evaluate(rightTree)
            elif op == '**':
                return evaluate(leftTree) ** evaluate(rightTree)
        else:
            return tree.getKey()
        
    if __name__ == '__main__':
        
        # Main program
        exp =  '((200 + (4*3.14))   / (2**3) )'

        tree = buildParseTree(exp)
        tree.printPreorder(0)
        print(f'The expression: {exp}\
            evaluates to: {evaluate(tree)}')