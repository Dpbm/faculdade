#!/usr/bin/python3

import sys
import json

class ScratchProject:
    def __init__(self, json_data):
        self.variables = get_variables(json_data)
        self.blocks = get_variables(json_data)
    

    def 




def get_variables(json_data):
    if(not json_data):
        return {}
    
    variables = json_data['targets'][0]['variables']

    variables_data = {}

    for variable in variables.items():
        variable_id = variable[0]
        variable_name = variable[1][0]
        variable_value = variable[1][1]

        variables_data[variable_name] = {
            "id": variable_id,
            "value": variable_value
        }


    return variables_data

def get_blocks(json_data):
    if(not json_data):
        return {}

    blocks = json_data['targets'][1]['blocks']

    return blocks

def main(filename):
    scratch_project_json_data = {}


    with open(filename, 'r') as scratch_project_file:
        scratch_project_json_data = json.load(scratch_project_file)


    project = ScratchProject(scratch_project_json_data)


if __name__ == '__main__':
    arguments = sys.argv

    if(len(arguments) != 2):
        print("Usage: python.exe main.py project.json")
        exit(1)

    filename = arguments[1]

    main(filename)
