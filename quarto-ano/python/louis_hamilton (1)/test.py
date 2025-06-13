import unittest

from hamiltonian import get_qubits_mapping

class TestGetQubitsMapping(unittest.TestCase):
    def test_mapping(self):
        mapping = get_qubits_mapping(2)

        self.assertEqual(len(mapping),4)
        self.assertEqual(list(mapping.keys()), [(0,0),(0,1),(1,0),(1,1)])
        self.assertEqual(list(mapping.values()), [0,1,2,3])




if __name__ == "__main__":
    unittest.main()