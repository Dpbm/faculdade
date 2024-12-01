from openqasm3 import parse

with open("test.qasm", "r") as file:
    data = file.read()
    parsed = parse(data)
    for statement in parsed.statements:
        functions = dir(statement)
        if('qubit' in functions):
            print("qubit --> ", statement.qubit.name, "[", statement.size.value, "]")
        elif('identifier' in functions):
            print('clbits --> ', statement.identifier.name, '[', statement.type.size.value, ']')
        elif("name" in functions):
            print("gate --> ", statement.name.name)
        elif("measure" in functions):
            print("measure")