# для решения этой задачи выбран стек, так как ограничений по времени не было и стек
# реализован на динамическом массиве, а операции вставки и получения элемента
# занимают О(n) (так как изменяется размер массива), из условия задачи было понятно,
# что оптимальным для ее решения будет
# стек, так как в случае с "10 2 4 * -" нам нужно соблюдать порядок выполнения согласно
# приоритету операции, принцип работы примерно такой, берем выполняем проверку на число, если это
# число добавляем его в стэк, если это оператор, то берем последние два числа в стеке,
# выполняем действие и результат помещаем обратно в стек, в результате в стеке должно
# остаться одно единственное число - ответ

import sys


class Stack:
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def size(self):
        return len(self.items)


def is_number(str):
    try:
        float(str)
        return True
    except ValueError:
        return False

def main():
    inp = sys.stdin.readline().rstrip().split()
    myStack = Stack()
    for operand in inp:
        if is_number(operand):
            myStack.push(int(operand))
        else:
            y = myStack.pop()
            x = myStack.pop()
            if operand == '/':
                ans = x // y
            elif operand == '*':
                ans = x * y
            elif operand == '-':
                ans = x - y
            elif operand == '+':
                ans = x + y

            myStack.push(ans)
    print(myStack.pop())


if __name__ == "__main__":
    main()


