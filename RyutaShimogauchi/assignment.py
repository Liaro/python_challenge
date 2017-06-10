import numpy as np


def assignment1():
    listFrom1to10 = list(range(1, 11))
    print('{}'.format(listFrom1to10))


def assignment2():
    evenFrom1to10 = list(range(2, 11, 2))
    print('{}'.format(evenFrom1to10))


def assignment3():
    alphabets = ['a', 'b', 'c', 'd', 'e', 'f']
    intAlphDict = {i: alphabets[i] for i in range(len(alphabets))}
    print('{}'.format(intAlphDict))


class Human():
    counter = 0

    def __init__(self, name, age, sex, height, weight):
        self.name = name
        self.age = age
        self.sex = sex
        self.height = height
        self.weight = weight
        self.incrementCounter()

    def incrementAge(self):
        self.age += 1

    def incrementCounter(self):
        Human.counter += 1


def assignment4():
    Yamada = Human("山田", 23, "male", 170.3, 60.2)
    print('counter value:{}'.format(Human.counter))
    print('{0.name}:\n\tage:{0.age}\n\tsex:{0.sex}\n\theight:{0.height}\n\tweight:{0.weight}\n'.format(Yamada))
    Takahashi = Human("高橋", 30, "female", 165.2, 46.2)
    print('counter value:{}'.format(Human.counter))
    print('{0.name}:\n\tage:{0.age}\n\tsex:{0.sex}\n\theight:{0.height}\n\tweight:{0.weight}\n'.format(Takahashi))
    Yamada.incrementAge()
    print("increment {}'s age.".format(Yamada.name))
    print('{0.name}:\n\tage:{0.age}\n\tsex:{0.sex}\n\theight:{0.height}\n\tweight:{0.weight}\n'.format(Yamada))


def assignment5():
    A = np.random.randint(0, 10, (3, 3))
    B = np.random.randint(0, 10, (3, 3))
    C = np.matmul(A, B)
    print('A={}\nB={}\nA*B=\n{}'.format(A, B, C))


def assignment6():
    a = np.random.randint(1, 10, 5)
    b = np.random.randint(1, 10, 5)
    c = np.dot(a, b) / (np.linalg.norm(a) * np.linalg.norm(b))
    print('a={}\nb={}\ncos of a and b is {}.'.format(a, b, c))

if __name__ == '__main__':
    assignment1()
    assignment2()
    assignment3()
    assignment4()
    assignment5()
    assignment6()
