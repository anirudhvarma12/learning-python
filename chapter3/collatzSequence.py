# Collatz Sequence practice project from Automate Boring Stuff - Chapter 3
# https://automatetheboringstuff.com/chapter3/


def collatz(number):
    if (number % 2) == 0:
        print(number//2)
        return number//2
    else:
        output = 3*number+1
        print(output)
        return output


def main():
    print("Enter a number")
    try:
        input_number = int(input())
        result = input_number
        while not result == 1:
            result = collatz(result)
    except ValueError:
        print("Enter a valid number")

if __name__ == '__main__':
    main()
