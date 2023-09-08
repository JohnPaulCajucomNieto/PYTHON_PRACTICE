import numpy as np

data = []


def input_data():
    count = int(input("Enter how many numbers: "))

    for x in range(count):
        i = int(input("Enter numbers: "))
        data.append(i)

    print("Data are", str(data))


def compute_mean():
    r1 = np.mean(data)
    print(r1)


def compute_sd():
    r2 = np.std(data)
    print(r2)


def compute_variance():
    r3 = np.var(data)
    print(r3)


while True:
    user = input("1]Start 2]Exit ")

    if user == '1':
        input_data()
        user = input("1]Mean 2]Std 3]Variance ")

        if user == '1':
            compute_mean()

        elif user == '2':
            compute_sd()
        elif user == '3':
            compute_variance()
        else:
            exit()
    else:
        exit()