#!/usr/bin/env python3

import os
import logging

LOGS = os.path.join(os.path.dirname(__file__), './logs/entropy.logs')

class Coprocessor():
    def __init__(self) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
        self.registers = {"A": float(), "B": float()}
        self.allowed_operations = ["FADD", "FSUB", "FMUL", "FDIV"]
        self.operation = str()
    
    @property
    def operation(self) -> str:
        return self.operation

    @operation.setter
    def operation(self, value: str) -> None:
        if value not in self.allowed_operations:
            logging.debug(f'Operation {value} is not allowed')
            return None
        self.operation = value
    
    def run(self) -> None:
        if self.operation == "FADD":
            self.registers["A"] += self.registers["B"]
        elif self.operation == "FSUB":
            self.registers["A"] -= self.registers["B"]
        elif self.operation == "FMUL":
            self.registers["A"] *= self.registers["B"]
        elif self.operation == "FDIV":
            self.registers["A"] /= self.registers["B"]
        logging.debug(f'Operation {self.operation} ran')
        return None
