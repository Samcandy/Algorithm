#python3 environment
def insert_sort(lst):
    n=len(lst)
    if n==1:
        return lst
#python2.x range,xrange --> python3 range
    for i in range(1,n):
        for j in range(i,0,-1):
            if lst[j]<lst[j-1]:
                lst[j-1],lst[j]=lst[j],lst[j-1]
    return lst
#python2.x raw_input() rename python3 input()
string_input=input()
input_list=string_input.split()
input_list=[int(x) for x in input_list]
print(insert_sort(input_list))
