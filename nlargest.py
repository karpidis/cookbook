"""Find in a list n largest files"""
import heapq
import random


def main():
    nea_lista = random_list()
    print(nea_lista)
    print(biggest_numbers(3, nea_lista))
    deuteri_lista = random_list()
    print(deuteri_lista)
    print(smallest_numbers(3, deuteri_lista))


def random_list():
    tyhaia_lista = [random.randint(0, 1000) for _ in range(0, random.randint(0, 50))]
    return tyhaia_lista


def biggest_numbers(n, lista):
    return heapq.nlargest(n, lista)


def smallest_numbers(n, lista):
    return heapq.nlargest(n, lista)


if __name__ == "__main__":
    main()
