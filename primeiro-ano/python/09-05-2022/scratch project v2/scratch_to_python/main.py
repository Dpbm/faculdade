#!/usr/bin/python3

import sys
import json
from random import uniform

class ScratchProject:
    def __init__(self, json_data):
        self.variables = get_variables(json_data)
        self.blocks = get_variables(json_data)
    
    def set_variable(self, variable_name, value):
        if(not self.variables[variable_name]):
            raise f"{variable_name} doesn't exists"

        self.variables[variable_name] = value

    def change_variable(self, variable_name, value):
        if(not self.variables[variable_name]):
            raise f"{variable_name} doesn't exists"

        self.variables[variable_name] += value

    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        return a / b

    def pick_random(self, start_value=1, end_value=10):
        return uniform(start_value, end_value)

    def greater_than(self, a, b):
        return a > b

    def less_than(self, a, b):
        return a < b

    def equals(self, a, b):
        return a == b

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
