import json

with open('project.json') as json_file:
    json_data = json.load(json_file)

    blocks_data = json_data['targets'][1]["blocks"].values()

    opcodes = []

    for i in blocks_data:
        try:
            opcodes.append(f'{i["opcode"]}\n')
        except Exception as error:
            print(f'error --> {error} --> {i}')

    with open('opcodes.txt', 'w') as opcodes_file:
        opcodes_file.writelines(opcodes)

