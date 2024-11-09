# a.
def ascending_my(x: int, y: int):
    if x > y:
        x, y = y, x
    for i in range(x, y + 1):
        print(i)


ascending_my(-12, 7)


# b.
def my_details(digit: str):
    print(digit[0], digit[6], digit[13])


my_details("AI is the best")


# c.
def say_bool(bool1: bool = True):
    if bool1:
        print("yes")
    else:
        print("no")


say_bool(True)
say_bool(False)


# d.
def print_zugi(l1: list[int]):
    for number in l1:
        if number % 2 == 0:
            print("even")
        else:
            print("odd")


print_zugi([5, 3, 2, 10, 15, 14, 14])


# e.
def statistics_my(sum_grades: list[int]):

    max_grade = max(sum_grades)
    min_grade = min(sum_grades)
    count = len(sum_grades)
    average = sum(sum_grades) / count

    print(f"max grade: {max_grade}")
    print(f"min grade: {min_grade}")
    print(f"how many grades: {count}")
    print(f"average grade: {average:.2f}")


def main():
    sum_grades = []
    while True:
        grade: int = int(input("enter new grade: "))
        if grade == -99:
            break
        elif 0 <= grade <= 100:
            sum_grades.append(grade)
        else:
            print("you have to print grade between 0 - 100")
    statistics_my([90, 80, 105, 55, 10, -99])
main()
