#!/usr/bin/env python3

import os
import logging
import time

LOGS = os.path.join(os.path.dirname(__file__), './logs/tape.logs')

class Tape():
    def __init__(self) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
        self.tape = bytearray()
        self.head = 0
        self.next_head = 0
        self.nbytes = 0
        self.length = 0
    
    @property
    def head(self) -> int:
        return self.head

    @head.setter
    def head(self, value: int) -> None:
        self.next_head = value
    
    @property
    def nbytes(self) -> int:
        return self.nbytes

    @nbytes.setter
    def nbytes(self, value: int) -> None:
        self.nbytes = value
    
    def use(self, opt: str, data: int) -> None:
        match opt:
            case 'read':
                self.__read(data)
            case 'write':
                self.__write(data)
            case 'nbytes':
                self.nbytes = data
            case 'head':
                self.head = data
    
    def mount(self, tapedir: str) -> None:
        tape_path = os.path.join(os.getcwd, tapedir)
        with open(tape_path, 'rb') as tape:
            self.tape = tape.read()
            self.length = len(self.tape)
        logging.debug(f'Tape mounted at {tape_path}')
    
    def unmount(self, tapedir: str) -> None:
        tape_path = os.path.join(os.getcwd, tapedir)
        with open(tape_path, 'wb') as tape:
            tape.write(self.tape)
        logging.debug(f'Tape unmounted from {tape_path}')

    def __read(self, pointer: int) -> str:
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

    def __write(self, data: str) -> None:
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
        data = data.encode('utf-8')
        nbytes = len(data)
        if pointer + nbytes > self.length:
            nbytes = self.length - pointer
        logging.debug(f'Writing {nbytes} bytes to {pointer}')
        write_delay(nbytes)
        self.tape[pointer:pointer+nbytes] = data
