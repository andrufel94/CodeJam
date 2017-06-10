import sys

#method for init file std output with the name parameter
def init_std_output(name_output):
    sys.stdout = open(name_output, "w")

def read_all_case(name_input, function_problem):
    # open file input
    f = open(name_input, 'r')
    # read first line -> num cases
    test = int(f.readline())
    # resolve case
    for num_case in range(1, test+1):
        #
        ans = function_problem(f.readline())
    #    print("Case #"+str(num_case)+": "+str(ans))
        print("Case #{}: {}".format(num_case, ans))
    f.close()

def tydi_number(number):
    while((not is_tidy_number(number)) and int(number) > 0):
        print(number)
        if(contain_cero(number)):
            #print(pos_cero(number))
            number = int(number)-(10**pos_cero(number))
        else:
            number = int(number)-1
    return int(number)
    
def is_tidy_number(number):
    is_tidy = True
    n_before = 0
    n = list(str(int(number)))   
    for i in range(0, len(n)):
        if(int(n[i]) >= n_before and is_tidy):
            n_before = int(n[i])
        else:
            is_tidy = False
    return is_tidy

def contain_cero(number):
    return "0" in str(number)

def pos_cero(number):
    n = list(str(int(number)))
    for i in range(len(n)-1, -1, -1):
        if(int(n[i]) == 0):
            return (len(n)-1)-i

# main
if __name__ == "__main__":
    #init_std_output("B-large-practice.out")
    func = tydi_number
    read_all_case("B-large-practice.in", func)
    
    
    