#!/usr/bin/env python3

import os
import logging

import devices as dv

LOGS = os.path.join(os.path.dirname(__file__), './logs/pmio.logs')

class PMIO():
    def __init__(self) -> None:
        logging.basicConfig(filename=LOGS, level=logging.DEBUG, filemode='a')
        self.devices = {
            "printer": dv.Printer(), "coprocessor": dv.Coprocessor(),
            "entropy": dv.Entropy(), "tape": dv.Tape()
        }
        self.port_map = {
            0: "print",     # printer print
            1: "get",       # entropy get bits
            2: "read",      # tape read nbytes from from head
            3: "write",     # tape write data to tape at head
            4: "nbytes",    # tape set nbytes
            5: "head",      # tape set head
            6: "A",         # coprocessor update A
            7: "B",         # coprocessor update B
            8: "OP",        # coprocessor update OP
            7: "run"        # coprocessor run
        }

    def OUT(self, port: int, data: int) -> int:
        try:
            opt = self.port_map[port]
        except KeyError:
            logging.error(f'Port {port} is not allowed')
            return None
        if opt in ["write", "nbytes", "head"]:
            data = self.devices['tape'].use(opt, data)
        elif opt in ["A", "B", "OP"]:
            data = self.devices["coprocessor"].use(opt, data)
        elif opt == "print":
            data = self.devices["printer"].use(opt, data)
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
        if opt == "read":
            data = self.devices["tape"].use(opt, data)
        elif opt == "get":
            data = str(self.devices["entropy"].use(opt, data))
        elif opt == "run":
            data = str(self.devices["coprocessor"].use(opt, data))
        else:
            logging.error(f'IN on port {port} is not allowed')
            return None
        logging.debug(f'Port {port} was read from with {data}')
        return data