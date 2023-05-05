#!/usr/bin/env python3

import os
import logging
import re

import devices as dv
import instructions as ins

LOGS = os.path.join(os.path.dirname(__file__), './logs/computer.logs')

class Computer():
    def __init__(self, program_path: str) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
        self.cpu = self.CPU()
        self.ram = self.RAM()
        self.rom = self.ROM(program_path)
        self.Coprocessor = dv.Coprocessor()
        self.entropy = dv.Entropy()
        self.printer = dv.Printer()
        self.tape = dv.Tape()
    

    class CPU():
        def __init__(self) -> None:
            self.csr = bytearray(0x00 for _ in range(0, 1))
            self.dreg = {"A": int(), "B": int()}
            self.pc = int()
            self.z = bool()

        def run(self) -> None:
            logging.debug('CPU is running')
        
        def hart(self) -> None:
            while True:
                pass
    

    class RAM():
        def __init__(self) -> None:
            self.memory = bytearray(0x00 for _ in range(0, 128))
        
        @property
        def memory(self) -> bytearray:
            return self.memory
        
        @memory.setter
        def memory(self, address: int, value: int) -> None:
            self.memory[address] = value
        
        @memory.getter
        def memory(self, address: int) -> int:
            return self.memory[address]
    

    class ROM():
        def __init__(self, program_path: str) -> None:
            self.program = self.load_program(program_path)
            logging.debug(f'Program {program_path} loaded')
        
        def load_program(self, program_path: str) -> list:
            file = open(program_path, 'r')
            program = file.readlines()
            file.close()
            for i,line in enumerate(program):
                if not re.match(ins.REGEX, line):
                    logging.debug(f'Program {program_path} is not valid')
                    return None
                else:
                    program[i] = {line.split()[0]: line.split()[1:]}
            return program


    def turn_on(self):
        logging.debug('Computer is turning on')
        self.CPU().run()
    
    def turn_off(self):
        logging.debug('Computer is turning off')