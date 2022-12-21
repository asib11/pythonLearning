if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arrr=[]
    for i in range(0, n):
        arrr.append(arr)
    arrr.sort(reverse=True)
    print(arrr[1])