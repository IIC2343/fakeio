#!/usr/bin/env python3

import os
import logging
import time

LOGS = os.path.join(os.path.dirname(__file__), './logs/tape.logs')
TAPEDIR = os.path.join(os.path.dirname(__file__), './tapes/tape1.tape')

class Tape():
    def __init__(self) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
        self.tape = bytearray()
        self.__head = 0
        self.next_head = 0
        self.__nbytes = 0
        self.length = 0
        self.mount(TAPEDIR)
    
    @property
    def head(self) -> int:
        return self.__head

    @head.setter
    def head(self, value: int) -> None:
        if value < 0:
            logging.debug(f'Head {value} cannot be negative')
            return None
        self.next_head = value
    
    @property
    def nbytes(self) -> int:
        return self.__nbytes

    @nbytes.setter
    def nbytes(self, value: int) -> None:
        self.__nbytes = value
    
    def use(self, opt: str, data: int) -> None:
        match opt:
            case 'read':
                ret = self.__read()
                return ret
            case 'write':
                self.__write(data)
            case 'nbytes':
                self.nbytes = data
            case 'head':
                self.head = data
            case 'length':
                return str(self.length)
    
    def mount(self, tapedir: str) -> None:
        tape_path = os.path.join(os.path.dirname(__file__), tapedir)
        with open(tape_path, 'rb') as tape:
            self.tape = tape.read()
            self.length = len(self.tape)
        logging.debug(f'Tape of length {self.length} mounted at {tape_path}')

    def __read(self) -> str:
        pointer = self.next_head
        def seek_delay(head: int, pointer: int) -> None:
            time.sleep(abs(head - pointer) / 10)
        def read_delay() -> None:
            time.sleep(self.nbytes / 10)
        if pointer > self.length:
            logging.debug(f'Pointer {pointer} is out of range')
            return None
        seek_delay(self.head, pointer)
        self.head = pointer
        if pointer + self.nbytes > self.length:
            self.nbytes = self.length - pointer
        logging.debug(f'Reading {self.nbytes} bytes from {pointer}')
        read_delay()
        data = self.tape[pointer:pointer+self.nbytes]
        data = data.decode('utf-8')
        return data

    def __write(self, data: int) -> None:
        def seek_delay(head: int, pointer: int) -> None:
            time.sleep(abs(head - pointer) / 10)
        def write_delay(nbytes: int) -> None:
            time.sleep(nbytes / 10)
        pointer = self.next_head
        if pointer > self.length:
            logging.debug(f'Pointer {pointer} is out of range')
            return None
        seek_delay(self.head, pointer)
        self.head = pointer
        data = str(data)
        data = bytearray([int(data[i:i+2]) for i in range(0, len(data), 2)])
        nbytes = len(data)
        if pointer + nbytes > self.length:
            nbytes = self.length - pointer
        logging.debug(f'Writing {nbytes} bytes to {pointer}')
        write_delay(nbytes)
        self.tape = self.tape[:pointer] + data + self.tape[pointer+nbytes:]
        tape_path = os.path.join(os.path.dirname(__file__), TAPEDIR)
        with open(tape_path, 'wb') as tape:
            tape.write(self.tape)
