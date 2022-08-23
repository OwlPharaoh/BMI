
is_black = False
is_male = False

if is_black and is_male:
    print("dog is a black male")
if is_black and not (is_male):
    print("dog is a black female")
elif not(is_black) and is_male:
    print("dog male, but not black")
else:
    print("dog is neither black nor male")

def min_num(num1, num2, num3, num4):
    if num1 <= num2 and num1 <= num3 and num1 <= num4:
        return num1
    elif num2 <= num1 and num2 <= num3 and num2 <= num4:
        return num2
    elif num3 <= num1 and num3 <= num3 and num3 <= num4:
        return num3
    else:
        return num4

print(min_num(1,2,3,0.5))

num1 = float(input("Enter first number: "))
op = input("Enter Operator: ")
num2= float(input("Enter second number: "))

if op == "+":
    print(num1 + num2)
elif op == "-":
    print(num1 - num2)
elif op == "/":
    print(num1 / num2)
elif op == "*":
    print(num1 * num2)
else:
    print("Invalid Operator")



monthconversions = {
    0: "January",
    1: "February",
    2: "March",
}

print(monthconversions.get(5, "Munch"))

j = 2
while j <= 20:
    print(j)
    j *= 2

print("done")

secret_word = "goat"
guess = ""
guess_count = 0
guess_limit = 3
out_of_guesses = False


while guess != secret_word and not out_of_guesses:
    if guess_count < guess_limit:
        guess = input("Enter guess: ")
        guess_count += 1
    else:
        out_of_guesses = True

if out_of_guesses:
    print("Out of Guesses, You Lose!")
else:
    print("You Win!")