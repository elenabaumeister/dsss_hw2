import random


def random_integer(lower_boundary, upper_boundary):
    """
    Random integer in range of min to max is returned.

    Parameters
    ----------
    lower_boundary : int
        Lower bound of the random integer.
    upper_boundary : int
        Upper bound of the random integer.

    Returns
    -------
    int
        Random integer in the range of min to max.
    """
    try:
        return random.randint(lower_boundary, upper_boundary)
    except ValueError:
        print("Please enter valid integers for the range.")
    except TypeError:
        print("Please enter integers for the range.")


def random_sign():
    """
    Randomly '+', '-', '*' sign is returned.

    Returns
    -------
    str
        Random sign from the list ['+', '-', '*'].

    """
    return random.choice(['+', '-', '*'])


def calculation(int1, int2, sign):

    """
    Mathematical problem and its answer are calculated.

    Parameters
    ----------
    int1 : int
        First random integer of the calculation.
    int2 : int
        Second random integer of the calculation.
    sign : str
        Random sign of the calculation.

    Returns
    -------
    calculation_string : str
        Formula of the math problem.
    result : int
        Result of the math problem.
    """
    calculation_string = f"{int1} {sign} {int2}"
    if sign == '+':
        result = int1 + int2
    elif sign == '-':
        result = int1 - int2
    else:
        result = int1 * int2
    return calculation_string, result


def math_quiz():
    """
    Math quiz game is played. User is asked to solve math problems and the score is calculated.
    """
    points = 0  # initialize points
    t_q = 3  # number of total questions

    print("Welcome to the Math Quiz Game!")
    print("You will be presented with math problems, and you need to provide the correct answers.")

    for _ in range(t_q):
        # two random integers and a random sign are generated
        int_1 = random_integer(1, 10)
        int_2 = random_integer(1, 5)
        sign = random_sign()

        # formula and result of the math problem are calculated
        formula, result = calculation(int_1, int_2, sign)
        print(f"\nQuestion: {formula}")
        # user can enter its answer
        useranswer = input("Your answer: ")
        useranswer = int(useranswer)

        if useranswer == result:
            print("Correct! You earned a point.")
            points += 1
        else:
            print(f"Wrong answer. The correct answer is {result}.")

    print(f"\nGame over! Your score is: {points}/{t_q}")


if __name__ == "__main__":
    math_quiz()
