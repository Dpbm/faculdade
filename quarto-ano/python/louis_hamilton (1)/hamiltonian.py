from data_types import MappingAttacks, MappingQubits, Hamiltonian

def get_qubits_mapping(n:int) -> MappingQubits:
    qubits_mapping = {}
    qubit = 0
    for i in range(n):
        for j in range(n):
            qubits_mapping[(i,j)] = qubit
            qubit += 1
    return qubits_mapping

def get_queens_possible_attacks(n:int) -> MappingAttacks:
    attacks = {}

    for i in range(n):
        for j in range(n):
            pos = (i,j)

            attacks[pos] = []

            cols = [(next_i, j) for next_i in range(n) if next_i != i] # same coloumn
            rows = [(i, next_j) for next_j in range(n) if next_j != j] # same row

            for c,r in zip(cols,rows):
                attacks[pos].append(c)
                attacks[pos].append(r)

            # improve this part

            # top left
            current_i = i
            current_j = j
            while current_i > 0 and current_j > 0:
                current_i -= 1
                current_j -= 1
                attacks[pos].append((current_i, current_j))

            # bottom right
            current_i = i
            current_j = j
            while current_i < n-1 and current_j < n-1:
                current_i += 1
                current_j += 1
                attacks[pos].append((current_i, current_j))

            # top right 
            current_i = i
            current_j = j
            while current_i > 0 and current_j < n-1:
                current_i -= 1
                current_j += 1
                attacks[pos].append((current_i, current_j))

            # bottom left 
            current_i = i
            current_j = j
            while current_i < n-1 and current_j > 0:
                current_i += 1
                current_j -= 1
                attacks[pos].append((current_i, current_j))


    return attacks            

def get_hamiltonian(n:int, attacks:MappingAttacks, qubits_map:MappingQubits) -> Hamiltonian:
    hamiltonian = []
    coeff = -1.0
    total_qubits = n*n
    
    for att in attacks.values():
        pauli_str = ["I"] * total_qubits
        for attack in att:
            pauli_str[qubits_map[attack]] = "Z"

        pauli_str = "".join(pauli_str)
        hamiltonian.append((coeff, pauli_str))

    return hamiltonian



"""
CASES

1. no attacks

ZZZ and ZZZZ --> both gonna be 1, so the coeff should be -1

2. even number of attacks

ZZZ --> gonna be 1, so the coeff must be 1 as well

3. odd number of attacks

ZZZ --> gonna be -1, so the coeff must be -1

         
""" 