#!/usr/bin/env python3

import os
import logging
import re

import devices as dv
import instructions as ins

LOGS = os.path.join(os.path.dirname(__file__), './logs/computer.logs')

class Computer():
    def __init__(self, program_path: str, echo: bool=False) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
        self.cpu = self.CPU(echo)
        self.ram = self.RAM()
        self.rom = self.ROM(program_path)
        self.devices = {
            "printer": dv.Printer(), "coprocessor": dv.Coprocessor(), "entropy": dv.Entropy(), "tape": dv.Tape()
        }
        

    class CPU():
        def __init__(self, echo: bool = False) -> None:
            self.csr = bytearray(0x00 for _ in range(0, 1))
            self.dreg = {"A": int(), "B": int()}
            self.echo = echo

        def run(self) -> None:
            logging.debug('CPU is running')
            for inst in self.rom.program:
                for op, args in inst.items():
                    getattr(self, op)(args)
                    if self.echo:
                        print(f'{op} {args}')
                    match op:
                        case 'ADD':
                            self.ADD(args)
                        case 'SUB':
                            self.SUB(args)
                        case 'AND':
                            self.AND(args)
                        case 'OR':
                            self.OR(args)
                        case 'XOR':
                            self.XOR(args)
                        case 'NOT':
                            self.NOT(args)
                        case 'MOV':
                            self.MOV(args)
                        case 'IN':
                            self.IN(args)
                        case 'OUT':
                            self.OUT(args)     
        
        def ADD(self, args: list) -> None:
            try:
                self.dreg[args[0]] += self.dreg[args[1]]
            except KeyError:
                self.dreg[args[0]] += int(args[1])
            return None

        def SUB(self, args: list) -> None:
            try:
                self.dreg[args[0]] -= self.dreg[args[1]]
            except KeyError:
                self.dreg[args[0]] -= int(args[1])
            return None

        def AND(self, args: list) -> None:
            try:
                self.dreg[args[0]] &= self.dreg[args[1]]
            except KeyError:
                self.dreg[args[0]] &= int(args[1])
            return None
    
        def OR(self, args: list) -> None:
            try:
                self.dreg[args[0]] |= self.dreg[args[1]]
            except KeyError:
                self.dreg[args[0]] |= int(args[1])
            return None

        def XOR(self, args: list) -> None:
            try:
                self.dreg[args[0]] ^= self.dreg[args[1]]
            except KeyError:
                self.dreg[args[0]] ^= int(args[1])
            return None
        
        def NOT(self, args: list) -> None:
            try:
                self.dreg[args[0]] = ~self.dreg[args[0]]
            except KeyError:
                self.dreg[args[0]] = ~int(args[0])
            return None

        def MOV(self, args: list) -> None:
            try:
                self.dreg[args[0]] = self.dreg[args[1]]
            except KeyError:
                try:
                    self.dreg[args[0]] = int(args[1])
                except ValueError:
                    dir = int(args[1].replace('(','').replace(')',''))
                    self.dreg[args[0]] = self.ram.memory(dir)
            return None

        def IN(self, args: list) -> None:
            try:
                self.dreg[args[0]] = self.csr[0]
            except KeyError:
                self.dreg[args[0]] = int(args[0])
            return None

        def OUT(self, args: list) -> None:
            try:
                self.csr[0] = self.dreg[args[0]]
            except KeyError:
                self.csr[0] = int(args[0])
            return None
    

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