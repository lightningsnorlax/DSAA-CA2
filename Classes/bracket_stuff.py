import re
from Classes.stack import Stack

class Bracketting():
    def __init__(self, exp, bracket_check):
        self.__exp = exp
        self.__flag = True
        self.__operators = ["**", "*", "/", "+", "-"]
        self.__bracket_check = bracket_check
        self.__pattern = self.getPattern()
    
    def getPattern(self):
        new_pattern = r"(\(|\)|"
        for i in self.__operators:
            for char in i:
                new_pattern += f"\\{char}"
            new_pattern += "|"
        new_pattern += r"\d+)"
        return new_pattern
    
    def tokenize_expression(self, exp):
        # Use regular expression to tokenize the expression
        tokens = re.findall(self.__pattern, exp.replace(" ", ""))
        return tokens
    
        # Check that brackets match up accordingly, open and close brackets
    def bracket_checking(self):
        
        # Setting temps variables
        bracket_count = 0
        operator_count = 0
        digit_count = 0
        
        for i in self.__exp:
            if i == "(":
                bracket_count += 1
            elif i == ")":
                bracket_count -= 1
            
        # Rule 1, brackets should cancel each other out
        if bracket_count != 0:
            return False
        
        # Rule 2, every digit should be followed by an operator and then followed by a digit
        temp_exp = self.__exp.replace(" ", "").replace("(", "").replace(")", "")
        tokens = self.tokenize_expression(temp_exp)
        print(tokens)
        flagging = True
        for i in tokens:
            if i.isdigit():
                digit_count += 1
            elif i in self.__operators:
                operator_count += 1
                
            if i.isdigit() and flagging:
                flagging = False
            elif i in self.__operators and not flagging:
                flagging = True
            else:
                return False
            
        # Rule 3, number of operators should be 1 less than number of digits
        if operator_count != digit_count - 1:
            return False
        
        # # Rule 4, every bracket should have at least 1 operator and 2 digits
        # if '(' in self.__exp and ')' in self.__exp:
        #     if '()' in self.__exp:
        #         return False
            
        #     for match in re.finditer(r'\(\D+|\D+\)', self.__exp):
        #         return False
        return True
    
    def bracket_check_and_normalize(self, exp):
        if not self.bracket_checking(exp):
            return False
        result = self.parsing_exp(exp)
        return result

    def add_brackets(self, exp):
        operators = {"**": 3, "*": 2, "/": 2, "+": 1, "-": 1}
        tokens = self.tokenize_expression(exp)

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

    # recursive function to look at every layer of list, to bracket (calls add_bracket function)
    def run_add_brackets_recursive(self, lst, level):
        result = ""
        temp = ""
        count = 0
        for i, item in enumerate(lst):
            
            # If a list, recursive
            if isinstance(item, list):
                if count % 2 != 0 and count >= 3:
                    result += self.add_brackets(temp)
                elif count >= 3:
                    if temp[0].isnumeric():
                        result += self.add_brackets(temp[:-1])
                        result += temp[-1]
                    elif temp[-1].isnumeric():
                        result += temp[1]
                        result += self.add_brackets(temp[1:])
                    
                else:
                    result += temp
                temp = ""
                count = 0
                result += self.run_add_brackets_recursive(lst[i], level + 1)
                
            else:
                temp += item
                count += 1
                
        # If no lists
        if level == 1 and len(result) != 0 and result[0] != "(":
            result = "(" + result + ")"
            
        if count % 2 != 0 and count >= 3:
            result += self.add_brackets(temp)  
        else:
            result += temp  # Move this line here
            
        if level == 1 and result[-1] != ")":
            result = "(" + result + ")"

        return result

    # turns brackets into list
    def parsing_exp(self):
        temp_exp = self.__exp.replace("(", "[").replace(")", "]")
        exp_str = ""
        for index, i in enumerate(temp_exp):
            if i != " ":
                if i == "[" or i == "]":
                    s = i
                else:
                    s = f"'{i}'"
                if len(exp_str) == 0 or (len(exp_str) > 0 and temp_exp[index-1] == "[") or i == "]":
                    exp_str += f"{s}"
                else:
                    exp_str += f", {s}"

        if not (exp_str[0] == "[" and exp_str[-1] == "]"):
            exp_str = "[" + exp_str + "]"

        exp_str = exp_str.replace("'*', '*'", "'**'")

        exp_str = list(eval(exp_str))
        print(exp_str)
        result = self.run_add_brackets_recursive(exp_str, 1)
        return result
            
if __name__ == "__main__":       
    brackets = Bracketting("2+4*5**2-7")
    print(brackets.bracket_checking())



# def bracket_check_and_normalize(exp):
#     if not bracket_checking(exp):
#         return False
#     result = parsing_exp(exp)
#     return result



# def add_brackets(exp):
#     print("exp", exp)
#     operators = {"**": 3, "*": 2, "/": 2, "+": 1, "-": 1}
#     tokens = tokenize_expression(exp)

#     while len(tokens) > 1:
#         operator_list = []
#         operator_list_index = []

#         for i, token in enumerate(tokens):
#             if token in operators:
#                 operator_list_index.append(i)
#                 operator_list.append(token)

#         max_precedence = max(operators.values())

#         for precedence in range(max_precedence, 0, -1):
#             for operator_index, operator in enumerate(operator_list_index):
#                 if operators[tokens[operator]] == precedence:
#                     tokens = (
#                         tokens[: operator - 1]
#                         + [f"({tokens[operator - 1]}{tokens[operator]}{tokens[operator + 1]})"]
#                         + tokens[operator + 2 :]
#                     )
#                     operator_list_index.pop(operator_index)
#                     operator_list.pop(operator_index)
#                     break

#     return tokens[0]

# # recursive function to look at every layer of list, to bracket (calls add_bracket function)
# def run_add_brackets_recursive(lst, level):
#     result = ""
#     temp = ""
#     count = 0
#     for i, item in enumerate(lst):
        
#         # If a list, recursive
#         if isinstance(item, list):
#             if count % 2 != 0 and count >= 3:
#                 result += add_brackets(temp)
#             elif count >= 3:
#                 if temp[0].isnumeric():
#                     result += add_brackets(temp[:-1])
#                     result += temp[-1]
#                 elif temp[-1].isnumeric():
#                     result += temp[1]
#                     result += add_brackets(temp[1:])
                
#             else:
#                 result += temp
#             temp = ""
#             count = 0
#             result += run_add_brackets_recursive(lst[i], level + 1)
            
#         else:
#             temp += item
#             count += 1
            
#     # If no lists
#     if level == 1 and len(result) != 0 and result[0] != "(":
#         result = "(" + result + ")"
        
#     if count % 2 != 0 and count >= 3:
#         result += add_brackets(temp)  
#     else:
#         result += temp  # Move this line here
        
#     if level == 1 and result[-1] != ")":
#         result = "(" + result + ")"

#     return result

# # turns brackets into list
# def parsing_exp(exp):
#     exp = exp.replace("(", "[").replace(")", "]")
#     exp_str = ""
#     for index, i in enumerate(exp):
#         if i != " ":
#             if i == "[" or i == "]":
#                 s = i
#             else:
#                 s = f"'{i}'"
#             if len(exp_str) == 0 or (len(exp_str) > 0 and exp[index-1] == "[") or i == "]":
#                 exp_str += f"{s}"
#             else:
#                 exp_str += f", {s}"

#     if not (exp_str[0] == "[" and exp_str[-1] == "]"):
#         exp_str = "[" + exp_str + "]"

#     exp_str = exp_str.replace("'*', '*'", "'**'")

#     exp_str = list(eval(exp_str))
#     print(exp_str)
#     result = run_add_brackets_recursive(exp_str, 1)
#     return result

# if __name__ == "__main__":
#     equation = "2+4*5**2-7"
#     result = bracket_check_and_normalize(equation)
#     print(result)