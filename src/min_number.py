# https://blog.nowcoder.net/n/7fc67fe568c04937b37f36da9f57d33e
# input 21,30,62,5,31
# output 21305
def min_number(nums: list) -> int:
    sorted_list = sorted(nums)
    if len(sorted_list) > 3:
        sorted_list = sorted_list[0:3]
    
    str_min = [str(x) for x in sorted_list]
    s = sorted(str_min)
    return int(''.join(s))

if __name__ == '__main__':
    assert min_number([21, 30, 62, 5, 31]) == 21305
    assert min_number([5, 21]) == 215
    

