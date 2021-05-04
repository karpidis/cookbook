""" 2nd cookbook recipe
Count Average without the best and worst result
"""
import random


def main():
    grades = [random.randint(5, 10) for _ in range(0, 52)]
    print(grades)
    grades.sort()
    print(drop_first_last(grades))


def drop_first_last(grades):
    first, *middle, last = grades
    return sum(middle)/len(middle)


if __name__ == "__main__":
    main()
