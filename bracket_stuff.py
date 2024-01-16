import re
from Classes.stack import Stack

def tokenize_expression(exp):
    # Use regular expression to tokenize the expression
    pattern = r"(\(|\)|\+|\-|\*\*|\*|\/|\d+)"
    tokens = re.findall(pattern, exp.replace(" ", ""))
    return tokens

def bracket_check_and_normalize(exp):
    if not bracket_checking(exp):
        return False
    result = parsing_exp(equation)
    return result
    

def bracket_checking(exp):
    count = 0
    for i in exp:
        if i == "(":
            count += 1
        elif i == ")":
            count -= 1

    return count == 0

def add_brackets(exp):
    operators = {"**": 3, "*": 2, "/": 2, "+": 1, "-": 1}
    tokens = tokenize_expression(exp)

    while len(tokens) > 1:
        operator_list = []
        operator_list_index = []

        for i, token in enumerate(tokens):
            if token in operators:
                operator_list_index.append(i)
                operator_list.append(token)

        max_precedence = max(operators.values())

        for precedence in range(max_precedence, 0, -1):
            for operator_index, operator in enumerate(operator_list_index):
                if operators[tokens[operator]] == precedence:
                    tokens = (
                        tokens[: operator - 1]
                        + [f"({tokens[operator - 1]}{tokens[operator]}{tokens[operator + 1]})"]
                        + tokens[operator + 2 :]
                    )
                    operator_list_index.pop(operator_index)
                    operator_list.pop(operator_index)
                    break

    return tokens[0]

def run_add_brackets_recursive(lst, level):
    result = ""
    temp = ""
    count = 0
    for i, item in enumerate(lst):
        
        # If a list, recursive
        if isinstance(item, list):
            if count % 2 != 0 and count >= 3:
                result += add_brackets(temp)
            else:
                result += temp
            temp = ""
            count = 0
            result += run_add_brackets_recursive(lst[i], level + 1)
            
        else:
            temp += item
            count += 1
            
    # If no lists
    if level == 1 and len(result) != 0 and result[0] != "(":
        result = "(" + result + ")"
        
    if count % 2 != 0 and count >= 3:
        result += add_brackets(temp)  
    else:
        result += temp  # Move this line here
        
    if level == 1 and result[-1] != ")":
        result = "(" + result + ")"

    return result

def parsing_exp(exp):
    exp = exp.replace("(", "[").replace(")", "]")
    exp_str = ""
    for index, i in enumerate(exp):
        if i != " ":
            if i == "[" or i == "]":
                s = i
            else:
                s = f"'{i}'"
            if len(exp_str) == 0 or (len(exp_str) > 0 and exp[index-1] == "[") or i == "]":
                exp_str += f"{s}"
            else:
                exp_str += f", {s}"

    if not (exp_str[0] == "[" and exp_str[-1] == "]"):
        exp_str = "[" + exp_str + "]"

    exp_str = exp_str.replace("'*', '*'", "'**'")

    exp_str = list(eval(exp_str))
    result = run_add_brackets_recursive(exp_str, 1)
    return result

if __name__ == "__main__":
    equation = "2+4*5**2-7"
    result = bracket_check_and_normalize(equation)
    print(result)