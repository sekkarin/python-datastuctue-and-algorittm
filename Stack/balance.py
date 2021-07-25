from stack import Stack

if __name__ == '__main__':
    stack = Stack()
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
