#!/usr/bin/env python3

import os
import logging

LOGS = os.path.join(os.path.dirname(__file__), './logs/entropy.logs')

class Coprocessor():
    def __init__(self) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
        self.registers = {"A": float(), "B": float(), "OP": int()}
        self.op_map = {0: "FADD", 1: "FSUB", 2: "FMUL", 3: "FDIV"}
        self.operation = None
    
    def use(self, opt: str, data: int) -> None:
        logging.debug(f'Coprocessor used with {opt} {f"and {data}" if data is not None else ""}')
        match opt:
            case 'A':
                self.registers["A"] = data
            case 'B':
                self.registers["B"] = data
            case 'OP':
                self.registers["OP"] = data
            case 'run':
                ret = self.__run()
                return ret
    
    def __run(self) -> None:
        if self.registers["OP"] is None:
            logging.debug(f'OP register not set')
            return None
        try:
            self.operation = self.op_map[self.registers["OP"]]
        except KeyError:
            logging.debug(f'Operation {self.registers["OP"]} is not allowed')
            return None
        if self.operation == "FADD":
            self.registers["A"] += self.registers["B"]
        elif self.operation == "FSUB":
            self.registers["A"] -= self.registers["B"]
        elif self.operation == "FMUL":
            self.registers["A"] *= self.registers["B"]
        elif self.operation == "FDIV":
            self.registers["A"] /= self.registers["B"]
        logging.debug(f'Operation {self.operation} ran')
        return self.registers["A"]
