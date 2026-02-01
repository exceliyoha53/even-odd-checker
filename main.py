def check_even_odd(number):
    """Returns a dictionary mapping numbers to Even or Odd
    and saves the result to a file"""

    result = {i: "Even" if i % 2 == 0 else "Odd" for i in range(1, number + 1)}

    with open("result.txt", mode="w") as requirements:
        for key, value in result.items():
            requirements.write(f"{key}: {value}\n")

    return result


def main():
    name = input("Enter your Name: ")
    number = int(input("Enter a number: "))

    print(f"\nHello {name}, checking numbers...\n")
    check_even_odd(number)
    print("Results saved to results.txt")


if __name__ == "__main__":
    main()
