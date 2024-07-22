from art import logo
import os


def cls() -> None:
    os.system('cls' if os.name == 'nt' else 'clear')


def add(value1: float, value2: float) -> float:
    return value1 + value2


def subtract(value1: float, value2: float) -> float:
    return value1 - value2


def multiply(value1: float, value2: float) -> float:
    return value1 * value2


def divide(value1: float, value2: float) -> float:
    if value2 != 0:
        return value1 / value2
    else:
        raise RuntimeError("Cannot divide by 0")


operation_map = {
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide
}


def perform_operation(first_value: float, second_value: float, operation_str: str) -> float:
    function_to_call = operation_map[operation_str]
    return function_to_call(first_value, second_value)


def output_result(first_value: float, second_value: float, operation_str: str, result: float) -> None:
    print(f"{first_value:.2f} {operation_str} {second_value:.2f} = {result:.2f}.")


def calculator() -> None:
    keep_going = True

    cls()
    print(logo)
    first_number = float(input("What's the first number?: "))
    for operation in operation_map:
        print(operation)

    while keep_going:
        operation = input("Pick an operation: ")
        second_number = float(input("What's the second number?: "))

        answer = perform_operation(first_number, second_number, operation)
        output_result(first_number, second_number, operation, answer)

        print()
        restart = input(f"Type 'y' to continue calculating with {answer:.2f}, "
                        f"or type 'n' to start a new calculation. Type 'q' to quit: ")
        if restart.lower() == 'y':
            first_number = answer
        elif restart.lower() == 'n':
            keep_going = False
            calculator()
        else:
            keep_going = False
            print("Thank you for using the calculator...")


if __name__ == "__main__":
    calculator()