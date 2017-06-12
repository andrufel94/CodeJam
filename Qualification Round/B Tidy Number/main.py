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
# method question is tidy
def is_tidy_number(number):
    is_tidy = True
    n_before = 0
    n = list(str(int(number)))
    for i in range(0, len(n)):
        # if before number is < actual number return false
        if(int(n[i]) >= n_before and is_tidy):
            n_before = int(n[i])
        else:
            is_tidy = False
    return is_tidy

# method for tranform the number in tidy number
def tidy_number_v3(number):
    # while not is tidy transform this
    while((not is_tidy_number(number))):
        number = find_tidy_number(number)
    return int(number)

# method for find optimum number tidy
def find_tidy_number(number):
    line = str(int(number))
    for i in range(0, len(line)-1):
        #print(line[i] + ">" + line[i+1])
        if(int(line[i]) > int(line[i+1])):
            number_tidy = int(number) - int(line[(i+1):(len(line))]) - 1
            break
    return number_tidy
# endregion

# region main
if __name__ == "__main__":
    init_std_output("B-large-practice.out")
    func = tidy_number_v3
    read_all_case("B-large-practice.in", func)
# endregion