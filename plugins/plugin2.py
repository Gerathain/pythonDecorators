#!/bin/python3

import registrar

@registrar.register
def bye():
    return "bye-bye"
