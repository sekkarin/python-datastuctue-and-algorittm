from stack import Stack

if __name__ == '__main__':

    stack = Stack()
    String = "e+a-(b+c+f)*d"
    postfix = ""
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