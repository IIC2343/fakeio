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
                ret = self.__get()
                return ret

    def __get(self) -> int:
        time.sleep(random.randint(0, 5))
        return random.randint(0, 255)