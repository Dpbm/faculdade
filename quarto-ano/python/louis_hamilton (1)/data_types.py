from typing import Dict, Tuple, List

Board = List[List[int]]
Position = Tuple[int,int]
MappingQubits = Dict[Position, int]
Attacks = List[Position]
MappingAttacks = Dict[Position, Attacks]
Hamiltonian = List[Tuple[float, str]]