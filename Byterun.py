# -*- coding:utf-8 -*-

class interrupter(object):
    def __init__(self):
        self.stack = []
        self.environment = {}

    def Load_name(self, name):
        val = self.environment[name]
        self.stack.append(val)

    def Store_name(self, name):
        val = self.stack.pop()
        self.environment[name] = val

    def Add_two_number(self):
        number1 = self.stack.pop()
        number2 = self.stack.pop()
        result = number1 + number2
        self.stack.append(result)

    def Load_number(self, number):
        self.stack.append(number)

    def Print_result(self):
        print(self.stack.pop())

    def Parse_argument(self, instruction, argument, what_to_execute):
        names = ["LOAD_NAME", "STORE_NAME"]
        numbers = ["LOAD_VALUE"]

        if instruction in names:
            argument = what_to_execute["names"][argument]
        if instruction in numbers:
            argument = what_to_execute["numbers"][argument]
        return argument

    def Run_code(self, what_to_execute):
        instructions = what_to_execute["instructions"]
        for each_step in instructions:
            instruction, argument = each_step
            argument = self.Parse_argument(instruction, argument, what_to_execute)

            if instruction == "LOAD_VALUE":
                self.Load_name(argument)
            elif instruction == "ADD_TWO_VALUES":
                self.Add_two_number()
            elif instruction == "PRINT_ANSWER":
                self.Print_result()
            elif instruction == "STORE_NAME":
                self.Store_name(argument)
            elif instruction == "LOAD_NAME":
                self.Load_name(argument)