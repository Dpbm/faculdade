from os import system
from sys import argv

def test(filename):
    for i in range(100):
        system(f'python.exe {filename}.py')
        
        print()


if __name__ == '__main__':
    if (len(argv) < 2):
        raise "Error, usage python filename"

    filename = argv[1] 

    test(filename)