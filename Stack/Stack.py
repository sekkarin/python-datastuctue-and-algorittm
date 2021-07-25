class Stack:
    def __init__(self):
        self.stack = []

    def add(self, dataval):
        self.stack.append(dataval)
        # Use list append method to add element
        # if dataval not in self.stack:
        #     self.stack.append(dataval)
        #     return True
        # else:
        #     return False
    # Use peek to look at the top of the stack

    def peek(self):
        return self.stack[-1]

    # look element all
    def __str__(self):
        return "ข้อมูล : {} จำนวนข้อมูล : {}".format(self.stack, len(self.stack))

    # remove element top
    def remove(self):
        if len(self.stack) <= 0:
            return ("No element in the Stack")
        else:
            return self.stack.pop()

    def lengghtStack(self):
        return len(self.stack)


if __name__ == '__main__':

    stack = Stack()
    # stack.add("a")
    # stack.add("b")
    # stack.add("{")
    # stack.add("d")
    # stack.add("e")
    # stack.add("{")
    # stack.add("f")
    # stack.add("g")
    # stack.add("}")
    # stack.add("h")
    # stack.add("{")
    # stack.add("i")
    # stack.add("}")
    # stack.add("}")
    # stack.add("j")
    # stack.add("}")
    # stack.add("k")
    # print(stack.peek())
    # stack.remove()
    # print(stack.peek())
    i = 0
    massage = "abcad{ad}}{a{dd}"
    # print(len(massage))
    # print(massage[0])
    while i < len(massage):

        ch = massage[i]
        if ch == '{':
            stack.add('{')
        elif ch == '}':
            if stack.lengghtStack() != 0:
                stack.remove()

        i += 1
    else:
        if stack.lengghtStack() > 0:
            print("Not have balance")
        else:
            print('It have balance')

    print(stack)
