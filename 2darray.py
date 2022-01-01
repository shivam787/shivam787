import sys
d = sys.stdin.read().splitlines()
d = [list(map(int, f.split())) for f in d]
max_val = None
for j in range(4):
    for i in range(4):
        add = d[j][i] + d[j][i+1] + d[j][i+2]+ d[j+1][i+1] + d[j+2][i] + d[j+2][i+1] + d[j+2][i+2]
        if max_val == None:
            max_val = add
        elif add> max_val:
            max_val = add
print(max_val)
