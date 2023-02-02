def test(N, names):
    players = {}
    points = [6, 4, 3, 2, 1]
    counter = 0
    for _ in range(N):
        for point in points:
            player = names[counter]
            players[player] = players.get(player, 0) + point
            counter += 1

    sorted_players = dict(sorted(players.items(), key=lambda score: score[1], reverse=True))

    for player, score in sorted_players.items():
        print(f'{player}: {score}')

names_file = open('data.txt', 'r')
names = [name.replace("\n", '') for name in names_file.readlines()]
test(20, names)
names_file.close()
