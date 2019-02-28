#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from gcode17 import parse
from operator import attrgetter
import time


def time_passed(time_from):
    print(str(round(time.time() - time_from)) + ' segundos')


class Problema:
    def __init__(self, n_fotos, list_fotos):
        self.nFotos = n_fotos
        self.listFotos = list_fotos

    def solve(self):
        print(self.nFotos)
        print(self.listFotos)
        return True


class Foto:
    def __init__(self, orientacion, n_etiquetas, list_etiquetas):
        self.orientacion = orientacion
        self.nEtiquetas = n_etiquetas
        self.listEtiquetas = list_etiquetas
        self.listEtiquetas[-1] = self.listEtiquetas[-1].strip()
        print(self.listEtiquetas)


class Slideshow:
    def __init__(self):
        self.listaslides = list()

    def addlista(self, slide):
        self.listaslides.append(slide)


class Slide:
    def __init__(self):
        self.listafotos = list()

    def addslide(self, foto):
        self.listafotos.append(foto)


def main():
    parser_args = """
Main = Int -> 1@foto | Problema
foto = String Int *String | Foto
"""
    files = ['a_example.txt']
    start_time = time.time()

    for f in files:
        print('Resolviendo ' + f)
        problem_start_time = time.time()

        problem = parse('in/' + f, parser_args, globals())
        print('Archivo parseado')
        problem.solve()
        print('Problema resuelto')
        time_passed(start_time)

    print('Tiempo total:')
    time_passed(start_time)


if __name__ == '__main__':
    sys.exit(main())
