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
        self.length = 0
        self.head = 0
    
    def mount(self, tapedir: str) -> None:
        tape_path = os.path.join(os.getcwd, tapedir)
        logging.debug(f'Tape mounted at {tape_path}')
        with open(tape_path, 'rb') as tape:
            self.tape = tape.read()
            self.length = len(self.tape)
    
    def unmount(self, tapedir: str) -> None:
        tape_path = os.path.join(os.getcwd, tapedir)
        logging.debug(f'Tape unmounted from {tape_path}')
        with open(tape_path, 'wb') as tape:
            tape.write(self.tape)

    def read(self, pointer: int, nbytes: int=0) -> str:
        def seek_delay(head: int, pointer: int) -> None:
            time.sleep(abs(head - pointer) / 10)
        def read_delay(nbytes: int) -> None:
            time.sleep(nbytes / 10)
        if pointer > self.length:
            logging.debug(f'Pointer {pointer} is out of range')
            return None
        seek_delay(self.head, pointer)
        self.head = pointer
        if pointer + nbytes > self.length:
            nbytes = self.length - pointer
        logging.debug(f'Reading {nbytes} bytes from {pointer}')
        read_delay(nbytes)
        data = self.tape[pointer:pointer+nbytes]
        data = data.decode('utf-8')
        return data

    def write(self, pointer: int, data: str) -> None:
        def seek_delay(head: int, pointer: int) -> None:
            time.sleep(abs(head - pointer) / 10)
        def write_delay(nbytes: int) -> None:
            time.sleep(nbytes / 10)
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
