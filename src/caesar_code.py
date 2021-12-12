# 凯撒密码
def caesa_code(source: str):
    chr_list = []
    
    for i in source:
        v = (ord(i) - 96 + 3) % 26
        chr_list.append(chr(v + 96))
    
    return ''.join(chr_list)

if __name__ == '__main__':
    assert caesa_code('a') == 'd'
    assert caesa_code('abc') == 'def'
    assert caesa_code('') == ''
    