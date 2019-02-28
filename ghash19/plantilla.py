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
        self.slideShow = Slideshow()
    # para cada foto de lsit fotos, crear un objeto slide (metiendole la foto con addslide) y meterlo en Slideshow (con addlista)

    def solve(self):
        self.ordenafotos()
        self.createSlideShow()
        print(self.listFotos)
        return True

    def ordenafotos(self):
        self.listFotos.sort(key=lambda x: x.nEtiquetas, reverse=True)

    def createSlideShow(self):
        for photo in self.listFotos:
            slide = Slide()
            slide.add(photo)
            self.slideShow.addslide(slide)


class Foto:
    def __init__(self, orientacion, n_etiquetas, list_etiquetas):
        self.orientacion = orientacion
        self.nEtiquetas = n_etiquetas
        self.listEtiquetas = list_etiquetas
        self.listEtiquetas[-1] = self.listEtiquetas[-1].strip()

    def __repr__(self):
        return str(self.nEtiquetas)


class Slideshow:
    def __init__(self):
        self.listaslides = list()

    def addslide(self, slide):
        self.listaslides.append(slide)


class Slide:
    def __init__(self):
        self.listafotos = list()

    def add(self, foto):
        self.listafotos.append(foto)


def main():
    parser_args = """
Main = Int -> 1@foto | Problema
foto = String Int *String | Foto
"""
    files = ['c_memorable_moments.txt']  # a_example.txt, b_lovely_landscapes.txt, c_memorable_moments.txt, d_pet_pictures.txt, e_shyny_selfies.txt
    start_time = time.time()

    for f in files:
        print('Resolviendo ' + f)
        problem_start_time = time.time()

        problem = parse('in/' + f, parser_args, globals())
        print('Archivo parseado')
        problem.solve()
        print('Problema resuelto')
        time_passed(problem_start_time)

    print('Tiempo total:')
    time_passed(start_time)


if __name__ == '__main__':
    sys.exit(main())
