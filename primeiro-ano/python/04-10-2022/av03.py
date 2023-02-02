N = int(input())

players = {}
points = [6, 4, 3, 2, 1]

for _ in range(N):
    for point in points:
        player = input()
        players[player] = players.get(player, 0) + point

sorted_players = dict(sorted(players.items(), key=lambda score: score[1], reverse=True))

for player, score in sorted_players.items():
    print(f'{player}: {score}')
