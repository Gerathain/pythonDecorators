#!/bin/bash

import registrar

@registrar.register
def hello():
    return "hi"
