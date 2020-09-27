"""
Program: infix_to_postfix_meeker
Author: Daniel Meeker
Date: 9/26/2020

This program will allow a user to convert infix expressions
into postfix expressions.

Because there is not builtin stack library I copied and pasted
the stack class and custom exceptions from the Stack Lab into
this file.

Academic Honesty: I attest that this is my original work.
I have not used unauthorized source code, either modified or
unmodified. I have not given other fellow student(s) access
to my program.
"""


class StackEmptyException(Exception):
    pass


class StackFullException(Exception):
    pass


class Stack:
    def __init__(self, max_size=5):
        self.top = -1  # represents the top of the stack. Gets incremented when items are pushed on the stack
        self.max_size = max_size  # represents how many items can be in the stack
        self.items = ["" for x in range(max_size)]

    def is_empty(self):
        return self.top == -1

    def is_full(self):
        return self.top == self.max_size - 1
        # Shows it is full because the top will be at index
        # of 4 which is equal to a max size of 5 due to index
        # counts beginning at 0

    def push(self, item):
        if not self.is_full():
            self.top += 1
            self.items[self.top] = item
        else:
            raise StackFullException("Stack is full")

    def pop(self):
        try:
            item_str = self.peek()
            self.top -= 1
            return item_str
        except StackEmptyException:
            raise StackEmptyException("Stack is Empty")

    def peek(self):
        if not self.is_empty():  # If statement necessary otherwise it could not throw an exception
            return self.items[self.top]
        else:
            raise StackEmptyException("Stack is Empty")

    def size(self):
        return self.top + 1

    def print_stack_up(self):
        """
        In my mind print_stack_up implies starting
        at the bottom of the stack and going to the top
        but to make the unit test pass this function
        prints in reverse order starting at the top
        and going to the bottom
        :return: a string
        """
        if not self.is_empty():
            stack_str = ""
            for x in range(self.size())[::-1]:
                stack_str += str(self.items[x]) + "\n"
            return stack_str
        else:
            raise StackEmptyException("Stack is Empty")


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
                while (not output_stack.is_empty()) and \
                        (prec[output_stack.peek()] >= prec[char]):
                    postfix_list.append(output_stack.pop())
                output_stack.push(char)
        # create output
        while not output_stack.is_empty():
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
