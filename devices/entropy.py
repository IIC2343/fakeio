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
    
    def get(self, length: int) -> int:
        logging.debug(f'Entropy is generating {length} bytes')
        time.sleep(random.random(0, 1))
        return random.getrandbits(length)