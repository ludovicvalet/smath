#! /usr/bin/python
# -*- coding: utf8 -*-

import latexparser
import latexparser.PytexTools

myRequest = latexparser.PytexTools.Request("feuilles")
myRequest.original_filename="smath.tex"

myRequest.ok_filenames_list=["e_smath"]

myRequest.ok_filenames_list.append("les_DS")
myRequest.ok_filenames_list.append("autres_exercices_seconde")
myRequest.ok_filenames_list.append("exercices_feuilles_seconde")
