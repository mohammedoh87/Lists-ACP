start = int(input("Enter the start of the range: "))
end = int(input("Enter the end of the range: "))

number_list = []
even_squares = []
odd_squares = []


for i in range(start, end+1):
    square = i **2
    number_list.append(square)
    if square % 2 == 0:
        even_squares.append(square)
    else:
        odd_squares.append(square)

print(number_list)

print("The original list is ", number_list)
print("The even squares are ", even_squares)
print("The odd squares are ", odd_squares)
