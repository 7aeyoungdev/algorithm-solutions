# https://jungol.co.kr/problem/12358

n = int(input())
top_pipe = input()
bot_pipe = input()

top = True
bot = (bot_pipe[0] == 'L')

for i in range(1, n - 1):
    change = (top_pipe[i] == 'L' and bot_pipe[i] == 'L')

    ntop = (top and top_pipe[i] == 'I') or (bot and change)
    nbot = (bot and bot_pipe[i] == 'I') or (top and change)

    top, bot = ntop, nbot

if bot or (top and top_pipe[-1] == 'L'):
    print('YES')
else:
    print('NO')