#!/bin/python

plugins = dict()

def getPlugins():
    return plugins

def register(func):
    plugins[func.__name__] = func

    return func
