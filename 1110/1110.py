first_no = int(input())
second_no = 0
result_no = 0
roof_counter = 1

if not (0 <= first_no <= 99):
    exit()

number_checker = first_no

while True:
    second_no = first_no % 10
    first_no = int(first_no / 10)
    result_no = first_no + second_no
    first_no = (second_no * 10) + result_no % 10

    if (number_checker == first_no):
        break;
    else:
        roof_counter += 1

print(roof_counter)