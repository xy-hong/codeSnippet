import os
from typing import List
import math


def split(file_path: str, package_nums: int, buff_size: int=1024*1024):
    """ 把单个文件切分成多个文件

    @file_path  要切分的文件路径
    @package_nums   切分块数量
    @buff_size  读写时的 buff 长度，默认 1 MB
    """
    file_size = os.path.getsize(file_path)
    package_size = math.ceil(file_size / package_nums)
    no = 0
    f = open(file_path, 'rb')
    bs = f.read(buff_size)
    p = open(f'./part_{no}', 'wb')
    part_size = 0
    while bs:
        p.write(bs)
        part_size += len(bs)
        if part_size >= package_size:
            no += 1
            p.close()
            part_size = 0
            p = open(f'part_{no}', 'wb')
        bs = f.read(buff_size)
    
    p.close()
    f.close()


def merge(file_path_list: List[str], to_file_path: str, buff_size: int=1024*1024):
    """ 把多个文件组合成一个文件

    @file_path_list 文件路径数组
    @to_file_path   合并文件名称
    @buff_size  读写时的 buff 长度，默认 1 MB
    
    """
    to_file = open(to_file_path, 'wb')
    for file_path in file_path_list:
        f = open(file_path, 'rb')
        bs = f.read(buff_size)
        while bs:
            to_file.write(bs)
            bs = f.read(buff_size)
        
        f.close()
    
    to_file.close()


#if __name__ == '__main__':
    # split('./规约及最佳实践.md', 2)
    # merge(['part_0', 'part_1', 'part_2', 'part_3'], './合并.md')
