"""
Program: infix_to_postfix_meeker
Author: Daniel Meeker
Date: 9/26/2020

This program will allow a user to convert infix expressions
into postfix expressions.

Because there is not a builtin Stack library I installed one
in my pycharms so the program requires pythonds installed
to run.

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access
to my program.
"""
from pythonds.basic.stack import Stack


def get_user_input():
    expression_to_convert = input("Enter infix notation to convert to postfix:  ")
    return infix_to_postfix(expression_to_convert)


def infix_to_postfix(expression):
    prec = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}  # order of precedence
    output_stack = Stack()
    output_string = ""
    postfix_list = []
    char_list = list(expression)
    try:
        for char in char_list:
            # skip blank spaces
            if char == ' ':
                continue
            # if a letter or number add to postfix
            if char in "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz" \
                    or char in "0123456789":
                postfix_list.append(char)
            # if an open parenthesis push to stack
            elif char == '(':
                output_stack.push(char)
            # if a closed parenthesis pop from stack
            elif char == ')':
                stack_top = output_stack.pop()
                # while there is not another open parenthesis add letters and numbers to postfix
                while stack_top != '(':
                    postfix_list.append(stack_top)
                    stack_top = output_stack.pop()
            else:
                # figure out order of precedence
                while (not output_stack.isEmpty()) and \
                        (prec[output_stack.peek()] >= prec[char]):
                    postfix_list.append(output_stack.pop())
                output_stack.push(char)
        # create output
        while not output_stack.isEmpty():
            postfix_list.append(output_stack.pop())
        return "Infix: " + str(expression) + "\nPostfix: " + output_string.join(postfix_list)
    except IndexError:
        raise ValueError("Error in input expression, make sure your parenthesis have partners!")
    except KeyError:
        raise ValueError("Please limit infix to letters, numbers, and basic operands")


if __name__ == '__main__':
    print(infix_to_postfix("2+3*4"))
    print(infix_to_postfix("a*b+5"))
    print(infix_to_postfix("(1+2)*7"))
    print(infix_to_postfix("a*b/c"))
    print(infix_to_postfix("(a/(b-c+d))*(e-a)*c"))
    print(infix_to_postfix("a/b-c+d*e-a*c"))
    print(infix_to_postfix("2+3*4"))
    print(infix_to_postfix("2+3*4"))
    print(infix_to_postfix("2+3*4"))
    print(infix_to_postfix("2+3*4"))
    print(infix_to_postfix("2+3*4"))
    print(infix_to_postfix("2+3*4"))
    try:
        print(get_user_input())
    except ValueError as e:
        print(e)
    input("Press Enter to End")
