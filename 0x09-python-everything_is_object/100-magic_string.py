#!/usr/bin/python3
def magic_string(MG=[0]):
    MG[0] += 1
    return str("BestSchool, " * (MG[0] - 1)) + "BestSchool"
