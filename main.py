import os
import os.path

def main():
    if not os.path.exists('./result'):
        os.makedirs('./result')

    num1 = int(input('Enter the first number: '))
    num2 = int(input('Enter the second number: '))

    addition_result = (num1 + num2) ** 2
    subtraction_result = num1 - num2
    multiplication_result = num1 * num2
    
    if num2 != 0:
        division_result = num1 / num2
    else:
        division_result = "Undefined (division by zero)"

    with open('./result/file.txt', 'w') as f:
        f.write("First number: " + str(num1) + '\n')
        f.write("Second number: " + str(num2) + '\n')
        f.write("Addition Result: " + str(addition_result) + '\n')
        f.write("Subtraction Result: " + str(subtraction_result) + '\n')
        f.write("Multiplication Result: " + str(multiplication_result) + '\n')
        f.write("Division Result: " + str(division_result) + '\n')

    print(f'The addition result is: {addition_result}')
    print(f'The subtraction result is: {subtraction_result}')
    print(f'The multiplication result is: {multiplication_result}')
    print(f'The division result is: {division_result}')

if __name__ == '__main__':
    main()
