#!/usr/bin/env python3

# Created by: Layla Michel
# Created on: June 14, 2021
# This program asks the user to create a list, state what math operator to use
# on the list, and displays the new list

import math


def math_list(list_result, operation, second_num):
    # performs a math operation on a list and returns an empty list if there
    # is a ZeroDivisionError
    new_list = []
    for number in list_result:
        if operation == '+':
            new_list.append(number + second_num)
        elif operation == '-':
            new_list.append(number - second_num)
        elif operation == '*':
            new_list.append(number * second_num)
        elif operation == '/':
            try:
                new_list.append(number / second_num)
            except ZeroDivisionError:
                break
        elif operation == '%':
            try:
                new_list.append(number % second_num)
            except ZeroDivisionError:
                break
    return new_list


def main():
    # greet user
    print("This program does a math operation on a list of numbers to create a\
 new list.")

    while True:
        # ask user to enter each number of the list
        number_elements = input("Enter a list of numbers (i.e. 1 2 3 4 5): ")

        # each string seperated by a space is added to a list
        string_list = []
        string_list = [item for item in number_elements.split()]

        number_list = []
        for element in string_list:
            # converts each element from string to float and adds it to a new
            # list
            try:
                element_float = float(element)

                number_list.append(element_float)
            except ValueError:
                # removes elements that aren't numbers
                print("{} is not a number so it will be removed.\
". format(element))
        if number_list == []:
            # asks the user to reenter numbers in the list if the list is empty
            print("The list is empty, try again.")
        else:
            break

    print()
    while True:
        # asks the user what kind of operation they want to perform on the list
        user_oper = input("Enter what kind of operation you want to perform on\
 the list (i.e. +, -, *, /, %): ")

        if (user_oper == '+'):
            # check if it's an addition
            print()
            while True:
                # get the second number of the operation
                user_second_num = input("What number do you want to add to\
 each number? ")
                try:
                    # convert from string to float
                    user_second_num_float = float(user_second_num)
                    break
                except ValueError:
                    # error message if the input is not a number
                    print("{} is not a valid number, try again.\
". format(user_second_num))
            break
        elif (user_oper == '-'):
            # check if it's a subtraction
            print()
            while True:
                # get the second number of the operation
                user_second_num = input("What number do you want to subtract\
 to each number? ")
                try:
                    # convert from string to float
                    user_second_num_float = float(user_second_num)
                    break
                except ValueError:
                    # error message if the input is not a number
                    print("{} is not a valid number, try again.\
". format(user_second_num))
            break
        elif (user_oper == '*'):
            # check if it's a multiplication
            print()
            while True:
                # get the second number of the operation
                user_second_num = input("What number do you want to multiply\
 each number by? ")
                try:
                    # convert from string to float
                    user_second_num_float = float(user_second_num)
                    break
                except ValueError:
                    # error message if the input is not a number
                    print("{} is not a valid number, try again.\
". format(user_second_num))
            break
        elif (user_oper == '/'):
            # check if it's a division
            print()
            while True:
                # get the second number of the operation
                user_second_num = input("What number do you want to divide\
 each number by? ")
                try:
                    # convert from string to float
                    user_second_num_float = float(user_second_num)
                    break
                except ValueError:
                    # error message if the input is not a number
                    print("{} is not a valid number, try again.\
". format(user_second_num))
            break
        elif (user_oper == '%'):
            # check if the user wants the remainder
            print()
            print("Notice: if any number in the list is a decimal, the\
 decimal will be dropped for this calculation.")

            # create list of only integers if the user is doing a mod operation
            number_list_mod = []
            for numbers in number_list:
                numbers_int = math.trunc(numbers)
                number_list_mod.append(numbers_int)

            # display the updated list of just integers
            print("Here is the updated list: {}". format(number_list_mod))
            print()
            while True:
                # get the second number of the operation
                user_second_num = input("What number do you want to divide\
 each number by? ")
                try:
                    # convert from string to int
                    user_second_num_int = int(user_second_num)
                    break
                except ValueError:
                    # error message if the input is not a number
                    print("{} is not a valid number, try again.\
". format(user_second_num))
            break
        else:
            # error message if the operator is not a valid one
            print("{} is not a valid operator, try again.". format(user_oper))

    if user_oper == "%":
        # call math_list function if the user is using %
        user_list_result = math_list(number_list, user_oper,
                                     user_second_num_int)
    else:
        # call math_list function if the user is using a different operator
        user_list_result = math_list(number_list, user_oper,
                                     user_second_num_float)

    if user_list_result == []:
        print()
        # error message if the list is empty, which means there was a
        # ZeroDivisionError
        print("Cannot divide by zero.")
    elif user_oper == '%':
        print()
        # display the resulting list as integers instead of floats
        user_list_mod = []
        for number in user_list_result:
            number = int(number)
            user_list_mod.append(number)
        # display the first list, operator, second number and the new list
        print("{0} {1} {2} = {3}". format(number_list_mod, user_oper,
                                          user_second_num, user_list_mod))
    elif user_oper == '*' and user_second_num_float == 0:
        print()
        # display the resulting list as integers instead of floats if the
        # operator was * and the second number was 0
        user_list_multiply = []
        for number in user_list_result:
            number = int(number)
            user_list_multiply.append(number)
        # display the first list, operator, second number and the new list
        print("{0} {1} {2} = {3}". format(number_list, user_oper,
                                          user_second_num, user_list_multiply))
    else:
        print()
        # display the first list, operator, second number and the new list
        print("{0} {1} {2} = {3}". format(number_list, user_oper,
                                          user_second_num, user_list_result))


if __name__ == "__main__":
    main()
