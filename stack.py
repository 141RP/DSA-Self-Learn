#NOTE: DIGITS WILL ONLY BE SINGLE DIGITS
#Take the infix expression: 3 * ( 8 + 2 ) - 3 * 4 - ( 1 - 4 )
    # Prefix: - - * 3 + 8 2 * 3 4 + 1 4
    # Postfix: 3 8 2 + * 3 4 * - 1 4 + -

#Using only one stack, conver a Prefix to a Postfix

digits = "0123456789"
operators = "+-*/"
stack = []
def preToPost(pre):
    pointer = len(pre)-1
    stack.clear()
    while pointer >= 0:
        if pre[pointer] != " " and pre[pointer] in digits:
            stack.append(pre[pointer])
            pointer -= 1
        elif pre[pointer] != " " and pre[pointer] in operators:
            A = stack.pop()
            B = stack.pop()
            string = A + B + pre[pointer]
            stack.append(string)
            pointer -= 1
        else:
            pointer -= 1

    print(stack[0])
    print(stack[0] == post)

print("\nTest Case 1")
pre = "- - * 3 + 8 2 * 3 4 + 1 4"
post = "382+*34*-14+-"
preToPost(pre)

print("\nTest Case 2")
pre = "+ * 9 4 - 7 2"
post = "94*72-+"
preToPost(pre)

print("\nTest Case 3")
pre = "- + 5 * 6 3 / 8 4"
post = "563*+84/-"
stack.clear()
preToPost(pre)

print("\nTest Case 4")
pre = "* - 8 2 + 3 7"
post = "82-37+*"
preToPost(pre)

print("\nTest Case 5")
pre = "+ - 9 1 * 2 6"
post = "91-26*+"
preToPost(pre)
