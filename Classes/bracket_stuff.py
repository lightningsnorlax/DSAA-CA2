# Name: Lim Yu Yang Ian & Yadanar Aung
# Admin No.: 2201874 & 2214621
# Class: DAAA/FT/2B/07

# -------------------------
# Imports
# -------------------------
import re
from Classes.stack import Stack

# -------------------------
# Bracketting Class
# -------------------------
class Bracketting():
    def __init__(self, exp, bracket_check):
        self.__exp = exp
        self.__flag = True
        self.__operators = ["**", "*", "/", "+", "-"]
        self.__bracket_check = bracket_check
        self.__pattern = self.__getPattern()

    def __is_valid_decimal_or_variable_name(self, s):
        if '.' in s:
            return s.replace('.', '', 1).isdigit()
        elif s.isalpha():
            return True
        # Check for sin cos tan
        elif len(s) == 5 and s[:3] in ["sin", "cos", "tan"] and s[3:].isdigit() and int(s[3:]) in [30, 45, 60]:
            return True
        # Checks for e
        elif len(s) == 2 and s[0] == "e" and s[1].isdigit():
            return True
        # Checks for log
        elif len(s) >= 4 and s[:3] == "log" and s[3:].isdigit():
            return True
        return s.isdigit()
    
    def __getPattern(self):
        new_pattern = r"(\(|\)|"
        for i in self.__operators:
            for char in i:
                new_pattern += f"\\{char}"
            new_pattern += "|"
        new_pattern += r"\d+\.\d+|\d+|\b\w+\b)"
        return new_pattern
    
    def __tokenize_expression(self, exp):
        # Use regular expression to tokenize the expression
        tokens = re.findall(self.__pattern, exp.replace(" ", ""))
        return tokens
    
    def return_tokens(self):
        return self.__tokenize_expression(self.__exp)
    
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
        tokens = self.__tokenize_expression(temp_exp)
        flagging = True
        for i in tokens:
            if self.__is_valid_decimal_or_variable_name(i):
                digit_count += 1
            elif i in self.__operators:
                operator_count += 1
                
            if self.__is_valid_decimal_or_variable_name(i) and flagging:
                flagging = False
            elif i in self.__operators and not flagging:
                flagging = True
            else:
                return False
            
        # Rule 3, number of operators should be 1 less than number of digits
        if operator_count != digit_count - 1:
            return False
        
        # Bracket checking
        bracketted = self.parsing_exp()
        if bracketted == "error":
            return False
        
        if not self.__bracket_check:
            if bracketted != self.__exp.replace(" ", ""):
                return False
        
        return True

    def __add_brackets(self, exp):
        operators = {"**": 3, "*": 2, "/": 2, "+": 1, "-": 1}
        tokens = self.__tokenize_expression(exp)

        # Iterate through the tokens in reverse order
        i = len(tokens) - 1
        while i >= 0:
            if tokens[i] in operators:
                operator = tokens[i]
                # Find the operands surrounding the operator
                operand1_index = i - 1
                operand2_index = i + 1
                # Check if the indices are valid
                if operand1_index >= 0 and operand2_index < len(tokens):
                    # Create a new token with brackets around the operands and the operator
                    new_token = f"({tokens[operand1_index]}{operator}{tokens[operand2_index]})"
                    # Replace the operands and the operator with the new token
                    tokens = tokens[:operand1_index] + [new_token] + tokens[operand2_index + 1 :]
                else:
                    # Invalid indices, handle the error or break the loop
                    break
            # Move to the previous token
            i -= 1

        # Return the result
        return tokens[0]
    
    # # recursive function to look at every layer of list, to bracket (calls add_bracket function)
    # def run_add_brackets_recursive(self, lst, level):
    #     result = ""
    #     temp = ""
    #     count = 0
    #     for i, item in enumerate(lst):
            
    #         # If a list, recursive
    #         if isinstance(item, list):
    #             if count % 2 != 0 and count >= 3:
    #                 result += self.add_brackets(temp)
    #             elif count >= 3:
    #                 if temp[0].isnumeric():
    #                     result += self.add_brackets(temp[:-1])
    #                     result += temp[-1]
    #                 elif temp[-1].isnumeric():
    #                     result += temp[1]
    #                     result += self.add_brackets(temp[1:])
                    
    #             else:
    #                 result += temp
    #             temp = ""
    #             count = 0
    #             result += self.run_add_brackets_recursive(lst[i], level + 1)
                
    #         else:
    #             temp += item
    #             count += 1
                
    #     # If no lists
    #     if level == 1 and len(result) != 0 and result[0] != "(":
    #         result = "(" + result + ")"
            
    #     if count % 2 != 0 and count >= 3:
    #         result += self.add_brackets(temp)  
    #     else:
    #         result += temp  # Move this line here
            
    #     if level == 1 and result[-1] != ")":
    #         result = "(" + result + ")"
    #     print(result, lst)
    #     return result

    # recursive function to look at every layer of list, to bracket (calls add_bracket function)
    def __run_add_brackets_recursive(self, lst, level):
        result = ""
        temp = ""
        count = 0
        added_flag = False
        error_flag = False
        for i, item in enumerate(lst):
            
            # If a list, recursive
            if isinstance(item, list):
                
                if count % 2 != 0 and count >= 3:
                    result += self.__add_brackets(temp)
                elif count >= 3:
                    if temp[0].isnumeric():
                        result += self.__add_brackets(temp[:-1])
                        result += temp[-1]
                        added_flag = True
                    elif temp[-1].isnumeric():
                        result += temp[1]
                        result += self.__add_brackets(temp[1:])
                        added_flag = True
                    
                else:
                    result += temp
                if len(item) < 3:
                    error_flag = True
                temp = ""
                count = 0
                returnResult = self.__run_add_brackets_recursive(lst[i], level + 1)
                if returnResult == "error":
                    error_flag = True
                else:
                    result += returnResult
                
            else:
                temp += item
                count += 1
                
        # If no lists   
        if count % 2 != 0 and count >= 3 and not error_flag:
            result += self.__add_brackets(temp)  
            added_flag = True
        else:
            result += temp  # Move this line here
        
        if not added_flag:
            result = "(" + result + ")"
        
        if level == 1 and len(result) != 0 and result[0] != "(":
            result = "(" + result + ")"

        # if level == 1 and result[-1] != ")":
        #     print("adding final", result)
        #     result = "(" + result + ")"

        if error_flag:
            result = "error"
        return result

    def parsing_exp(self):
        tokens = self.__tokenize_expression(self.__exp)
        print(tokens)
        exp_str = " "
        for token in tokens:
            if token != " ":
                if token == "(":
                    s = "["
                elif token == ")":
                    s = "]"
                else:
                    s = f"'{token}'"

                if ((token == "(" )and exp_str[-1] in ["(", ")"] or token == ")") or (exp_str[-1] == "[" or exp_str[-1] == " "):
                    exp_str += f"{s}"
                else:
                    exp_str += f", {s}"

        if not (exp_str[1] == "[" and exp_str[-1] == "]"):
            exp_str = "[" + exp_str[1:] + "]"
        exp_str = list(eval(exp_str))

        result = self.__run_add_brackets_recursive(exp_str, 1)
        return result