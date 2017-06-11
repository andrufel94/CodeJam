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
        number =  find_preceding_tidy(number)
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

# new version to get is tidy
def tydi_number_v2(number):
    while(is_tidy_number_v2(number) > -1):
        print(number)
        if(contain_cero(number)):
            number = int(number)-(pos_cero(number))
        else:
            number = int(number)-(10**is_tidy_number_v2(number))
    return int(number)
    

# new version to get is tidy
def is_tidy_number_v2(number):
    pos_val = -1
    n = list(str(int(number)))
    for i in range(0, len(n)-1):
        if(int(n[i]) > int(n[i+1])):
            pos_val = (len(n)-2)-i
            break
    return pos_val

def contain_cero(number):
    return "0" in str(number)

def pos_cero(number):
    n = list(str(int(number)))
    for i in range(len(n)-1, -1, -1):
        if(int(n[i]) == 0):
            return 1 if ((len(n)-1)-i) == 0 else (int(n[i+1])+1)*(10**((len(n)-2)-i))

#external method
def find_preceding_tidy(number):
    line = str(number)
    prev = "0"
    for i, digit in enumerate(line):
        if digit < prev:
            left_part = str(int(line[:i])-1)
            right_part = "9" * (len(line) - i)
            return left_part + right_part
        prev = digit

# main
if __name__ == "__main__":
    #init_std_output("B-large-practice.out")
    func = tydi_number_v2
    read_all_case("B-large-practice.in", func)
    
    
    