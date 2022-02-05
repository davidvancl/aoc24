import re


class ALU:
    __local_storage = {"w": 0, "x": 0, "y": 0, "z": 0}
    __loaded_instructions = []
    __actual_number = ""
    __manual_input = True
    __index = 0

    def load_instruction(self, filename):
        if len(self.__loaded_instructions) != 0:
            for line in self.__loaded_instructions:
                if len(line) > 2:
                    self.__do(line[1], line[2], line[0])
                else:
                    self.__inp(line[1])
        else:
            with open('{0}.txt'.format(filename)) as file:
                for line in file:
                    self.__loaded_instructions.append(line.strip().split())
                    instruction = line.strip().split()
                    if len(instruction) > 2:
                        self.__do(instruction[1], instruction[2], instruction[0])
                    else:
                        self.__inp(instruction[1])

    def __inp(self, variable_a):
        self.__validate_variables(variable_a)
        if self.__manual_input:
            self.__local_storage[variable_a] = int(input('Enter a number: '))
        else:
            self.__local_storage[variable_a] = int(self.__actual_number[self.__index])
            self.__index += 1

    def __do(self, variable_a, variable_b, action):
        if re.match(r"[-+]?\d+(\.0*)?$", variable_b) is not None:
            self.__validate_variables(variable_a)
            variable_b = int(variable_b)
        else:
            self.__validate_variables(variable_a, variable_b)
            variable_b = self.__local_storage[variable_b]
        self.__local_storage[variable_a] = {
            'add': self.__local_storage[variable_a] + variable_b,
            'mul': self.__local_storage[variable_a] * variable_b,
            'div': 0 if variable_b == 0 else int(self.__local_storage[variable_a] / variable_b),
            'mod': 0 if variable_b == 0 else self.__local_storage[variable_a] % variable_b,
            'eql': int(self.__local_storage[variable_a] == variable_b),
        }.get(action, 0)

    def __validate_variables(self, variable_a, variable_b=False):
        if variable_a not in self.__local_storage:
            raise Exception("There is no variable {0}".format(variable_a))
        if variable_b and variable_a not in self.__local_storage:
            raise Exception("There is no variable {0}".format(variable_b))

    def getW(self):
        return self.__local_storage['w']

    def getX(self):
        return self.__local_storage['x']

    def getY(self):
        return self.__local_storage['y']

    def getZ(self):
        return self.__local_storage['z']

    def disable_manual_input(self):
        self.__manual_input = False

    def set_number(self, number):
        self.__actual_number = number
        self.__local_storage = {"w": 0, "x": 0, "y": 0, "z": 0}
        self.__index = 0
