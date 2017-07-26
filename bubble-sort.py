def sort(data):
    for i in xrange(len(data)-1):
        for j in xrange(len(data)-i-1):
            if data[j]>data[j+1]:
                #space = data[j]
                #data[j] = data[j+1]
                #data[j+1] = space
                data[j],data[j+1]=data[j+1],data[j]
    return data

string_input=raw_input()
input_list=string_input.split()
input_list=[int(x) for x in input_list]

print sort(input_list)
