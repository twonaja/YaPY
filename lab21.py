# для решения этой задачи я решил выбрать для тела очереди массив, объявлять его длину лучше сразу,
# (создать некое подобие статического массива)
# так как у динамического массива некоторые операции занимают O(n), соответсвенно надо было для парвильного заполнения
# контроллировать голову и хвост, это нужно чтобы операции вставки и удаления элемента занимали О(1)
# (благодаря тому, что не динамически изменяем массив, а лишь изменяем "указатели" на голову и хвост), информация о
# релевантной длине также поддерживается исскуственно. Все реализованные функции работают О(1)



import sys
import array

class myDeq:
    def __init__(self, maxLen):
        self.__mxLn = maxLen
        self.__head = 0
        self.__tail = 0
        self.__ln = 0
        self.dqBody = array.array('i', [0] * self.__mxLn)

    def pushBack(self, el):
        if self.__ln != self.__mxLn:
            self.dqBody[self.__tail] = el
            self.__tail = (self.__tail + 1) % self.__mxLn
            self.__ln += 1
        else:
            print('error')

    def popBack(self):
        if self.__ln != 0:
            tmp = self.dqBody[self.__tail - 1]
            self.__tail = (self.__tail - 1) % self.__mxLn
            self.__ln -= 1
            return tmp
        else:
            return 'error'

    def pushFront(self, el):
        if self.__ln != self.__mxLn:
            self.dqBody[self.__head - 1] = el
            self.__head = (self.__head - 1) % self.__mxLn
            self.__ln += 1
        else:
            print('error')

    def popFront(self):
        if self.__ln != 0:
            tmp = self.dqBody[self.__head]
            self.__head = (self.__head + 1) % self.__mxLn
            self.__ln -= 1
            return tmp
        else:
            return 'error'

def main():
    count = int(input())
    n = int(input())
    mdq = myDeq(n)

    for i in range(0, count):
        cmd = sys.stdin.readline().rstrip().split()

        if cmd[0] == 'push_front':
            mdq.pushFront(int(cmd[1]))
        elif cmd[0] == 'pop_back':
            print(mdq.popBack())
        elif cmd[0] == 'push_back':
            mdq.pushBack(int(cmd[1]))
        elif cmd[0] == 'pop_front':
            print(mdq.popFront())

if __name__ == '__main__':
    main()



