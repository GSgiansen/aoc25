
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
    # print(f"operations is {operations}")
    numberlist = [0 if i == "+" else 1 for i in operations]
    for line in l[:-1]:
        line = line.strip()
        line = line.split(" ")
        line = list(filter(lambda x: x != "", line))
        # print(line)
        for i in range(len(line)):
            if operations[i] == "*":
                numberlist[i] *= int(line[i])
            else:
                ### add to number
                numberlist[i] += int(line[i])
    ans = sum(numberlist)
    print(f"list is {numberlist}")
    print(f"ans is {ans}")

    return             
if __name__ == "__main__":
    
    comput()