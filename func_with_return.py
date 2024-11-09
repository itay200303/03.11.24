
# a.
def avg_my(x: int, y: int):
    sum_x_y = x * y / 2
    return sum_x_y
avg_my(90, 99)
avg1: float = avg_my(90, 99)
print(avg1)

# b.
def my_headline(word: str):
    upper_word = word.upper() + '!'
    return  upper_word
my_headline("python has concurred the world")
head1: str = my_headline("python has concurred the world")
print(head1)
print(head1)

# c.
def concat_list(l1: list[int], l2: list[int], l3: list[int]):
    combined_list = l1 + l2 + l3
    return combined_list
concat_list([1, 2], [3, 4, 5, 6], [7, 8, 9])
res_con: list[int] = concat_list([1, 2], [3, 4, 5, 6], [7, 8, 9])
print(res_con)
print(f"len: {len(res_con)}")
