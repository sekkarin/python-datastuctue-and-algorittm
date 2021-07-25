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
    String = "a-(b+c*d)/e"
    postfix = ""
    # if 'a' in "+-/%)*(":
    #     print("True")
    # else:
    #     print("False")
    for ch in String:
        if ch not in "+-/%)*(":
            postfix += ch
        elif ch == '(':
            stack.add(ch)
        elif ch == ')':
            while stack.peek() != '(':
                postfix += stack.peek()
                stack.remove()
            stack.remove()
        else:
            stack.add(ch)
    while(stack.lengghtStack() !=  0):
        postfix += stack.peek()
        stack.remove()
    print(postfix)

