if __name__ == '__main__':
    a = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        a.append([name, score])
        a.sort(key = lambda u: u[1])
    b ={a}
    for i in range(len(a)):
        if a[1][1] == a[i][1]:
            a.sort()#(key= lambda u: u[0])
            print(a[i][0])
        
    #print(a[1][0])

# 4
# Rachel
# -50
# Mawer
# -50
# Sheen
# -50
# Shaheen
# 51