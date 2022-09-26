#!/usr/bin/env python3

import argparse

parser = argparse.ArgumentParser()

parser.add_argument("-t", "--target", type=str, help="choose which one do you want to see 'voltage', 'resistance' or 'current'")
args = parser.parse_args()

if args.target == "voltage":
    resistance = float(input("Resistance: "))
    current    = float(input("Current   : "))
    voltage    = current * resistance

    print("Voltage is", voltage)

elif args.target == "current":
    voltage    = float(input("Voltage: "))
    resistance = float(input("Resistance: "))
    current    = voltage / resistance

    print("Current is", current)

elif args.target == "resistance":
    voltage    = float(input("Voltage: "))
    current    = float(input("Current: "))
    resistance = voltage / current
    print("Resistance is", resistance)
