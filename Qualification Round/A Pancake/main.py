import sys

# get num flipper or impossible
def Pancake_Flipper(case):
    list_parameters = case.split(' ')
    S = list(list_parameters[0])
    K = int(list_parameters[1])
    ans = 0
    for i in range(0, len(S)-K+1):
        if(S[i] == '-'):
            for j in range(i,i+K):
                S[j] = '+' if S[j] == '-' else '-'
            ans += 1
    for i in range(0, len(S)):
        if(S[i] == '-'):
            ans = 'IMPOSSIBLE'
    return (ans)

#sys.stdin = open("A-small-practice.in", "r")
#sys.stdout = open("A-small-practice.out", "w")

sys.stdin = open("A-small-practice.in", "r")
sys.stdout = open("A-large-practice.out", "w")

# open file input
f = open("A-large-practice.in", 'r')
# read first line -> num cases
test = int(f.readline())
# resolve case
for num_case in range(1, test+1):
    ans = Pancake_Flipper(f.readline())
#    print("Case #"+str(num_case)+": "+str(ans))
    print("Case #{}: {}".format(num_case, ans))
f.close()