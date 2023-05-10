#!/usr/bin/env python3

import os
import logging
import random
import time

LOGS = os.path.join(os.path.dirname(__file__), './logs/entropy.logs')
SEED = 42

random.seed(SEED)

class Entropy():
    def __init__(self) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
    
    def use(self, opt: str, data: int) -> None:
        match opt:
            case 'get':
                self.__get()

    def __get(self) -> int:
        time.sleep(random.random(0, 1))
        return random.randint(0, 255)