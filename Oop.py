def new_func(n):
    print("".join([str(i) for i in range(1, n+1)]))

if __name__ == '__main__':
    n = int(input())
    new_func(n)
