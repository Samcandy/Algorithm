#python3 environment

def select_sort(lst):
    len_lst = len(lst)
    exchange_count = 0
    for i in range(len_lst-1):
        min_index = i
        for j in range(i+1,len_lst):
            if lst[min_index]>lst[j]:
                min_index=j
        if min_index != i:
            lst[min_index],lst[i] = lst[i],lst[min_index]
            exchange_count +=1
            print('iteration #{}: {}'.format(i,lst))
    print('Total {} swappings'.format(exchange_count))
    return lst

#python2.x raw_input() rename python3 input()
string_input=input()
input_list=string_input.split()
input_list=[int(x) for x in input_list]

print(select_sort(input_list))
