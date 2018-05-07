def execution (l1):
    for i in range(0,len(l1)):
        if l1[i] != 'A' and l1[i] != 'B' and l1[i] != 'L' and l1[i] != 'R':
            print("invalid operation")
            return False
    return True
def process(matrix):
    l1 = []
    for i in range(0,5):
        j = 0
        while j < 5:
            if matrix[i][j] == ' ':
                k = input("enter input characters:")
                if k == 'Z':
                    print("your programme stopped")
                    exit()
                while k != '0':
                    l1.append(k)
                    k = input()
                break
            j = j + 1
        if j < 5:
            break
    s = execution(l1)
    if s == True:
        for p in range(0,len(l1)):
            if l1[p]  == 'B':
                        i = i + 1
                        if i  > 4:
                            print("This puzzle has no  configuration")
                            exit()
                        else:
                            temp = matrix[i][j]
                            matrix[i][j] = matrix[i-1][j]
                            matrix[i-1][j] = temp
            elif l1[p]  == 'R':

                        j = j + 1
                        if j  > 4:
                            print("This puzzle has no configuration")
                            exit()
                        else:
                            temp = matrix[i][j]
                            matrix[i][j] = matrix[i][j-1]
                            matrix[i][j-1] = temp
            elif l1[p]  == 'L':

                        j = j - 1
                        if j < 0:
                            print("This puzzle has no configuration")
                            exit()
                        else:
                            temp = matrix[i][j]
                            matrix[i][j] = matrix[i][j+1]
                            matrix[i][j+1] = temp
            elif l1[p]  == 'A':

                        i = i - 1
                        if i < 0:
                            print("This puzzle has no configuration")
                            exit()
                        else:
                            temp = matrix[i][j]
                            matrix[i][j] = matrix[i+1][j]
                            matrix[i+1][j] = temp
    else:
        exit()
    return  matrix
num = 0
while True:
    matrix1 = []
    matrix =[]
    num = num + 1
    s1 = input()
    if len(s1) == 5:
        s2 = input()
        if len(s2) == 5:
            s3 = input()
            if len(s3) == 5:
                s4 = input()
                if len(s4) == 5:
                    s5 = input()
                    if len(s5) == 5:
                        matrix = [list(s1),list(s2),list(s3),list(s4),list(s5)]
                        matrix1 = process(matrix)
                    else:
                        print("you have entered more number of characters")
                        continue
                else:
                    print("you have entered more number of characters")
                    continue
            else:
                print("you have entered more number of characters")
                continue
        else:
            print("you have entered more number of characters")
            continue
    else:
        print("you have entered more number of characters")
        continue
    print("Puzzle #",num,":")
    result = ' '
    for i in range(0,5):
        for j in range(0,5):
            ch = matrix1[i][j]
            result = result + ch + ' '
        result = result + '\n' +' '
    print(result[:-1])
