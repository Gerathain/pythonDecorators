#!/bin/python3

import registrar
import os
import importlib

for f in os.listdir("plugins"):
    importlib.import_module("plugins." + os.path.splitext(f)[0])


def main():
    plugins = registrar.getPlugins()
    for key in plugins.keys():
        print(key)
        print(plugins[key]())

if __name__ == "__main__":
    main()
