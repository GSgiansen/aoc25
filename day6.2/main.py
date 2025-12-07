
def comput():
    filepath = 'input.txt'
    ans = 0
    with open (filepath, 'r') as file:
        l = file.read().splitlines()
    m = len(l)
    n = len(l[0])
    ### last row is always operators
    operations = l[-1]
    operations = list(filter(lambda x: x != " ", operations))
    print(f"operations is {operations}")
    numberlist = [[]for i in operations]
    ###
    separators = []
    for i in range(len(l[0])):
        flag = True
        for line in l[:-1]:
            if line[i] != " ":
                flag = False
        if flag:
            separators.append(i)
    print(separators)
    numberlist[0] = list(map(lambda x:x[0:separators[0]], l[:-1]))
    numberlist[-1] = list(map(lambda x:x[separators[-1] + 1:], l[:-1]))
    for i in range(1, len(separators)):
        num = separators[i]
        for line in l[:-1]:
            numberlist[i].append(line[separators[i -1] + 1:separators[i]])
    print(numberlist)
            
    ans = 0
    print(numberlist)
    for i in range(len(numberlist)):
        lst = numberlist[i]
        small_lst = 0 if operations[i] == "+" else 1
        max_len = max(map(lambda x: len(x), lst))
        for index in range(max_len - 1, -1, -1 ):
            formed = ""
            for word in lst:
                if word[index] == " ":
                    continue
                formed += word[index]
            print(f"formed is {formed}")
            if operations[i] == "+":
                small_lst += int(formed)
            else:
                small_lst *= int(formed)
        print(f"small_lst is {small_lst}")
        ans += small_lst

    print(f"list is {numberlist}")
    print(f"ans is {ans}")

    return             
if __name__ == "__main__":
    
    comput()