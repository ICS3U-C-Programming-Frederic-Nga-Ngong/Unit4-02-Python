#!/usr/bin/env python3
# Created By: Fred
# Date: Feb 18 2008
# Calculates factorial.


def main():
    print("This code calculates factorial \n")

    # Get number from the user
    usernum_str = input("Enter a positive number \n")

    try:

        # Cast it to an integer
        user_num = int(usernum_str)
        
        if user_num == 1 or user_num == 0:
                print("\n{}! = 1".format(user_num))

        # Number should not be zero
        elif user_num < 0:
                print("\nThe number has to be greater than zero. Please, enter a new one.")
        else:
                factorial = 1
                counter = 1
                while True:
                    factorial = factorial * counter
                    counter = counter + 1
                    if user_num <= counter:
                        break

        # Display factorial to the user
        print("{}! = {}".format(user_num, factorial))

        # If number is not an integer, tell the user to use another one
    except ValueError:
        print(
            "\n{} is not a valid integer. Please, enter a new one".format(usernum_str)
        )


print("\nThanks for using the code")

if __name__ == "__main__":

    main()
