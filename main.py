

def raise_to_power(base_num, pow_num):
    result = 1
    for index in range(pow_num):
        result = result*base_num
    return result
print((raise_to_power(2,3)))

num_grid=[
    [1,2,3],
    [4,5,6],
    [7,8,9],
    [0]
]

print(num_grid[3][0])

def translate(phrase):
    translation= ""
    for letter in phrase:
        if letter in "AEIOIaeiou":
            if letter.isupper():
                translation = translation+ "JK"
            else:
                translation = translation + "jk"
        else:
            translation = translation + letter
    return translation


print(translate(input("Enter Key Word: ")))