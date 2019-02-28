#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from gcode17 import parse
from operator import  attrgetter
import time

def time_passed(time_from):
  print(str(round(time.time() - time_from)) + ' segundos')

class Problema:
  def __init__(self, fil, col, coch, viaj, bon, pas, listViaj):
    pass

  def solve(self):
    return True

class Viaje:
  def __init__(self, xi, yi, xd, yd, ti, tf):
    pass

def main():
  parser_args = """
Main = Int Int Int Int Int Int -> 4@viaje | Problema
viaje = Int Int Int Int Int Int | Viaje
"""
  files = ['a_example']
  start_time = time.time()

  for f in files:
    print('Resolviendo ' + f)
    problem_start_time = time.time()

    problem = parse('input/' + f + '.in', parser_args, globals())
    print('Archivo parseado')
    problem.solve()
    print('Problema resuelto')
    time_passed(start_time)

  print('Tiempo total:')
  time_passed(start_time)

if __name__ == '__main__':
  sys.exit(main())
