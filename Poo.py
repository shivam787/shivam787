def mutate_string (string, position, character):
    chars = list(string)
    chars[position] = character
    return "".join(chars)
if __name__ == '__main__':
    s = input()
    i, c = input().split()
    s_new = mutate_string(s, int(i), c)
    print(s_new)

def count_strings (string, sub_string):
    count_sub = 0
    for i in range(len(string)):
        if string[i:].startswith(sub_string):
            count_sub += 1
    return count_sub
    
if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()

    count = count_strings(string, sub_string)
    print(count)

N,M = map(int, input().split())

N, M = map(int, input().split())
for i in range(1, N, 2):
    print(int((M - 3 * i) / 2) * '-' + (i * '.|.') + int((M - 3 * i) / 2) * '-')
print(int((M - 7) / 2) * '-' + 'WELCOME' + int((M - 7) / 2) * '-')
for i in range(N - 2, -1, -2):
    print(int((M - 3 * i) / 2) * '-' + (i * '.|.') + int((M - 3 * i) / 2) * '-')
