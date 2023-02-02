'''
    ganha primeiro turno --> mais da metade dos votos (descontando branco e nulo)
        senao os dois mais votados vao para o segundo turno

'''
n = int(input())

candidates = []
votes = []

for i in range(n):
    candidates.append(input())

for i in range(n + 2):
    votes.append(int(input()))

total_votes = sum(votes)
total_valids = total_votes - sum(votes[-1:])

needed = total_valids / 2

total_votes_per_candidate_for_second_turne = []

for i, total_per_candidate in enumerate(votes[:-2]):

    if total_per_candidate > needed:
        print(f'{candidates[i]} foi o vencedor da eleição')
        print(f'Total de votos: {total_votes}')
        print(f'Votos válidos: {total_valids}')
        exit()

    else:
        total_votes_per_candidate_for_second_turne.append({
            'candidate': candidates[i],
            'votes': total_per_candidate
        })

total_votes.sort(key = lambda x:x['votes'], reverse=True)

print('Haverá segundo turno entre:')
print(total_votes_per_candidate_for_second_turne[0]['candidate'])
print(total_votes_per_candidate_for_second_turne[1]['candidate'])
print(f'Total de votos: {total_votes}')
print(f'Votos válidos: {total_valids}')


