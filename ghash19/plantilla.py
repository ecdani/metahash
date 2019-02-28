#!/usr/bin/env python
# -*- coding: utf-8 -*-

import sys
from gcode17 import parse
from operator import attrgetter
import time
import math


def time_passed(time_from):
    print(str(round(time.time() - time_from)) + ' segundos')


class Problema:
    def __init__(self, n_fotos, list_fotos):
        self.nFotos = n_fotos
        self.listFotos = list_fotos
        for index, photo in enumerate(self.listFotos):
            photo.id = index

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
        pop_list_photos = self.get_h_photos_list()

        # ordenacion inicial
        pop_list_photos.sort(key=lambda x: x.nEtiquetas,
                             reverse=True)  # ¿hay que asignarlo?

        # primera
        photo_izq = pop_list_photos.pop(0)
        slide = Slide()
        slide.add(photo_izq)
        self.slideShow.addslide(slide)

        for index, photo in enumerate(pop_list_photos):
            n_tags_a_buscar = math.ceil(photo_izq.nEtiquetas/2)
            for index2, photo2 in enumerate(pop_list_photos):
                photo2.score(n_tags_a_buscar)
            pop_list_photos.sort(key=lambda x: x.score, reverse=True)
            print(pop_list_photos)
            photo_dch = pop_list_photos.pop(0)

            slide = Slide()
            slide.add(photo_dch)
            self.slideShow.addslide(slide)
            photo_izq = photo_dch

    def createSlideShow2(self):
        pop_list_photos = self.get_v_photos_list()
        tmp_slide_list = list()
        for index, photo in enumerate(pop_list_photos):
            photo_1 = pop_list_photos.pop(0)
            photo_2 = pop_list_photos.pop(0)
            slide = Slide()
            slide.add(photo_1)
            slide.add(photo_2)
            tmp_slide_list.append(slide)

        pop_list_photos = self.get_h_photos_list()
        for index, photo in enumerate(pop_list_photos):
            photo_1 = pop_list_photos.pop(0)
            slide = Slide()
            slide.add(photo_1)
            tmp_slide_list.append(slide)
        # ordenacion inicial
        tmp_slide_list.sort(key=lambda x: x.nEtiquetas,
                            reverse=True)  # ¿hay que asignarlo?

        # primera
        slide_izq = tmp_slide_list.pop(0)
        self.slideShow.addslide(slide_izq)

        for index, photo in enumerate(tmp_slide_list):
            n_tags_a_buscar = math.ceil(slide_izq.nEtiquetas/2)
            for index2, slide2 in enumerate(tmp_slide_list):
                slide2.score(n_tags_a_buscar)
            tmp_slide_list.sort(key=lambda x: x.score, reverse=True)
            print(tmp_slide_list)
            slide_dch = tmp_slide_list.pop(0)

            self.slideShow.addslide(slide_dch)
            slide_izq = slide_dch

    def get_h_photos_list(self):
        return list(filter(lambda x: x.orientacion == "H", self.listFotos.copy()))

    def get_v_photos_list(self):
        return list(filter(lambda x: x.orientacion == "V", self.listFotos.copy()))


class Foto:
    def __init__(self, orientacion, n_etiquetas, list_etiquetas):
        self.orientacion = orientacion
        self.nEtiquetas = n_etiquetas
        self.listEtiquetas = list_etiquetas
        self.listEtiquetas[-1] = self.listEtiquetas[-1].strip()
        self.id = 0
        self.score = 0

    def __repr__(self):
        return str(self.id)

    def score(self, n_tags_a_buscar):
        # Cuanto el numero de tags de la foto se desvia mas de la foto actual es peor score. 0 es optimo.
        # Cuanto MAS, PEOR.
        self.score = abs(n_tags_a_buscar - self.nEtiquetas)


class Slideshow:
    def __init__(self):
        self.listaslides = list()

    def addslide(self, slide):
        self.listaslides.append(slide)


class Slide:
    def __init__(self):
        self.listafotos = list()
        self.nEtiquetas = 0

    def add(self, foto):
        self.listafotos.append(foto)
        self.nEtiquetas += foto.nEtiquetas

    def score(self, n_tags_a_buscar):
        # Cuanto el numero de tags de la foto se desvia mas de la foto actual es peor score. 0 es optimo.
        # Cuanto MAS, PEOR.
        self.score = abs(n_tags_a_buscar - self.nEtiquetas)


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
