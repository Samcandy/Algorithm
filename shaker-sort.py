#python3 environment

def sharker_sort(lst):
    bottom = 0
    top =len(lst)-1
    
    while bottom < top:
        
        for i in range(bottom,top):
            if lst[i] > lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
        top = top-1
        print(top)
        for j in range(top,bottom,-1):
            if lst[j] < lst[j-1]:
                lst[j],lst[j-1]=lst[j-1],lst[j]
        bottom += 1
    return lst


#python2.x raw_input() rename python3 input()
string_input=input()
input_list=string_input.split()
input_list=[int(x) for x in input_list]

print(sharker_sort(input_list))
