import sys

# region methods for read all file and write the answer
# method for init file std output with the name parameter
def init_std_output(name_output):
    sys.stdout = open(name_output, "w")

# method for read all case from file
def read_all_case(name_input, function_problem):
    # open file input
    f = open(name_input, 'r')
    # read first line -> num cases
    test = int(f.readline())
    # resolve case
    for num_case in range(1, test+1):
        # print case with your answer
        ans = function_problem(f.readline())
        print("Case #{}: {}".format(num_case, ans))
    # close file
    f.close()
# endregion    

# region methods for solve the problem
def find_bathrooms(case):
    list_parameters = case.split(' ')
    N = int(list_parameters[0])
    K = int(list_parameters[1])
    list_bathrooms = [0] * int(N)
    for i in range(0, K):
        list_bathrooms = insert_person(list_bathrooms)
        print(list_bathrooms)
    list_r = get_empty_r(list_bathrooms)
    list_l = get_empty_l(list_bathrooms)
    return str(max(get_max(list_l, list_r))) + " " + str(max(get_min(list_l, list_r)))
        
def insert_person(list_bathrooms):
    list_r = get_empty_r(list_bathrooms)
    list_l = get_empty_l(list_bathrooms)
    #print("r:" + str(list_r))
    #print("l:" + str(list_l))
    index_list_min = [i for i, x in enumerate(get_min(list_l, list_r)) if x == max(get_min(list_l, list_r))]
    #index_list_max = [i for i, x in enumerate(get_max(list_l, list_r)) if x == max(get_max(list_l, list_r))]
    
    if(len(index_list_min) == 1):
        list_bathrooms[index_list_min[0]] = 1
    else:
        max_list = get_max(list_l, list_r)
        index_base = index_list_min[0]
        #print("min: "+str(index_list_min))
        #print("max: "+str(max_list))
        max_value = -1
        #if(len(index_list_max) == 1):
        for i in range(0, len(index_list_min)):
            if(int(max_list[index_list_min[i]]) > int(max_value)):
                max_value = max_list[index_list_min[i]]
                index_base = index_list_min[i]
        list_bathrooms[index_base] = 1
                    
    #print(list_bathrooms)
    return list_bathrooms
    

def get_empty_r(list_bathrooms):
    list_empty_r = [0] * len(list_bathrooms)
    for i in range(0, len(list_bathrooms)-1):
        if(list_bathrooms[i] == 0):
            list_empty_r[i] = int(find_empty(list_bathrooms[i+1:]))-1
    return list_empty_r

def get_empty_l(list_bathrooms):
    list_empty_l = [0] * len(list_bathrooms)
    for i in range(1, len(list_bathrooms)):
        if(list_bathrooms[i] == 0):
            list_empty_l[i] = int(find_empty(list_bathrooms[i-1::-1]))-1
    return list_empty_l

def find_empty(list_bathrooms):
    stall_i = 1
    for i in range(0, len(list_bathrooms)):
        if(list_bathrooms[i] == 1):
            stall_i = i+1
            break
        stall_i += 1
    return stall_i

def get_min(list_l, list_r):
    list_min = [0] * len(list_l)
    for i in range(0, len(list_l)):
        if(int(list_l[i]) < int(list_r[i])):
            list_min[i] = list_l[i]
        else:
            list_min[i] = list_r[i]
    return list_min
    
def get_max(list_l, list_r):
    list_max = [0] * len(list_l)
    for i in range(0, len(list_l)):
        if(int(list_l[i]) > int(list_r[i])):
            list_max[i] = list_l[i]
        else:
            list_max[i] = list_r[i]
    return list_max
    
# endregion

# region main
if __name__ == "__main__":
    #init_std_output("C-small-practice-1.out")
    func = find_bathrooms
    read_all_case("C-small-practice-1.in", func)
# endregion