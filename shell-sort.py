#python3 environment
"""
input: an array a of length n with array elements numbered 0 to n − 1
inc ← round(n/2)
while inc > 0 do:    
    for i = inc .. n − 1 do:        
        temp ← a[i]        
        j ← i        
        while j ≥ inc and a[j − inc] > temp do:            
            a[j] ← a[j − inc]            
            j ← j − inc        
        a[j] ← temp    
    inc ← round(inc / 2)
"""

def shell_sort(list):
    n = len(list)
    # Initial step size
    gap = n // 2
    while gap > 0:
        for i in range(gap, n):
            # Each step is inserted into the sort
            temp = list[i]
            j = i
            # insert sort
            while j >= gap and list[j - gap] > temp:
                list[j] = list[j - gap]
                j -= gap
            list[j] = temp
        # get new step size; "//" is get integer
        gap = gap // 2
    return list

#python2.x raw_input() rename python3 input()
string_input=input()
input_list=string_input.split()
input_list=[int(x) for x in input_list]
print(shell_sort(input_list))
