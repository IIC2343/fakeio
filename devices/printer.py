#!/usr/bin/env python3

import os
import logging
import time

LOGS = os.path.join(os.path.dirname(__file__), './logs/printer.logs')
PAPER = os.path.join(os.path.dirname(__file__), './paper.txt')

class Printer():
    def __init__(self) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
    
    def print(self, data: int) -> None:
        data = chr(data)
        logging.debug(f'Printer is printing {data}')
        time.sleep(len(data) / 10)
        with open(PAPER, 'a') as paper:
            paper.write(data)
        return None