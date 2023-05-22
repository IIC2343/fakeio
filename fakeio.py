#!/usr/bin/env python3

import os
import logging
import time

import devices as dv

LOGS = os.path.join(os.path.dirname(__file__), './logs/pmio.logs')

class PMIO():
    def __init__(self) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
        logging.debug(f'PMIO initialized at {time.time()}')
        self.devices = {
            "printer": dv.Printer(), "coprocessor": dv.Coprocessor(),
            "entropy": dv.Entropy(), "tape": dv.Tape()
        }
        self.port_map = {
            0: "print",     # printer print
            1: "get",       # entropy get number
            2: "read",      # tape read nbytes from from head
            3: "write",     # tape write data to tape at head
            4: "nbytes",    # tape set nbytes
            5: "head",      # tape set head
            6: "A",         # coprocessor A
            7: "B",         # coprocessor B
            8: "OP",        # coprocessor OP
            9: "run",       # coprocessor run
            10: "length"    # tape get length
        }

    def OUT(self, port: int, data: int) -> int:
        try:
            opt = self.port_map[port]
        except KeyError:
            logging.error(f'Port {port} is not allowed')
            return None
        if opt in ["write", "nbytes", "head"]:
            self.devices['tape'].use(opt, data)
        elif opt in ["A", "B", "OP"]:
            self.devices["coprocessor"].use(opt, data)
        elif opt == "print":
            self.devices["printer"].use(opt, data)
        else:
            logging.error(f'OUT on port {port} is not allowed')
            return None
        logging.debug(f'Port {port} was written to with {data}')
        return 0

    def IN(self, port: int) -> str:
        data = None
        try:
            opt = self.port_map[port]
        except KeyError:
            logging.error(f'Port {port} is not allowed')
            return None
        if opt == "read" or opt == "length":
            out = str(self.devices["tape"].use(opt, data))
        elif opt == "get":
            out = str(self.devices["entropy"].use(opt, data))
        elif opt == "run":
            out = str(self.devices["coprocessor"].use(opt, data))
        else:
            logging.error(f'IN on port {port} is not allowed')
            return None
        logging.debug(f'Port {port} was read from with {out}')
        return out