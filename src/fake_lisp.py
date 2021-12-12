# add sub mul div
# https://blog.nowcoder.net/n/da00c40c2d904f33ac985d12e03718d1
'''
输入：(mul 3 -7) 

输出：21  

输入：(add 1 2) 

输出：3 

输入：(sub (mul 2 4) (div 9 3)) 

输出：5  

输入：(div 1 0) 

输出：error 
'''
def cal(pattern: str):
    stack = []

    length = len(pattern)
    if length == 0:
        return 'error'
    
    stack.append(pattern[0])
    i = 1
    while len(stack) > 0 and i < length:
        c = pattern[i]
        if c == ' ':
            i += 1
        elif c == 'a':
            stack.append('+')
            i += 3
        elif c == 's':
            stack.append('-')
            i += 3
        elif c == 'd':
            stack.append('/')
            i += 3
        elif c == 'm':
            stack.append('*')
            i += 3
        elif c == '(':
            stack.append('(')
            i += 1   
        elif c == ')':
            right = int(stack.pop())
            left = int(stack.pop())
            symbol = stack.pop()
            left_ = stack.pop()
            if symbol == '+':
                stack.append(left + right)
            elif symbol == '-':
                stack.append(left - right)
            elif symbol == '*':
                stack.append(left*right)
            elif symbol == '/':
                if right == 0:
                    return 'error'
                stack.append(left / right)
            i += 1
        else:
            tmp = ''
            while c != ' ' and c != ')':
                tmp += c
                i += 1
                c = pattern[i]
            stack.append(int(tmp))

    
    return stack.pop()
        

if __name__ == '__main__':
    assert cal('(mul 3 -7)') == -21
    assert cal('(add 1 2)') == 3
    assert cal('(sub 1 1)') == 0
    assert cal('(div 10 2)') == 5
    assert cal('(div 10 0)') == 'error'
    assert cal('(sub (mul 2 4) (div 9 3))') == 5

