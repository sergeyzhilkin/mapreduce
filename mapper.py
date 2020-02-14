import sys

def mapper(f):
    num_list=[]
    for num in f:
        if (num.rstrip()).isnumeric():
            num_list.append(int(num.rstrip()))
        else:
            raise ValueError(f'check charachter {num}')
    return(num_list)

def reducer(r_list):
    return sum(r_list)

to_hdfs = []
for file in sys.stdin:
    with open(f'./input/{file.rstrip()}','r') as f:        
        try:
            r_list = mapper(f)
        except ValueError as e:
            print(f'ValueError: {str(e).rstrip()} in file {str(file)}')
            break 
        to_hdfs.append(reducer(r_list))
with open('./output/to_hdfs','w') as t:
    t.write(f'{sum(to_hdfs)}')
