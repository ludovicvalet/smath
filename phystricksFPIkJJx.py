# -*- coding: utf8 -*-

from phystricks import *

def FPIkJJx():
    pspict,fig = SinglePicture("FPIkJJx")
    pspict.dilatation(1)

    # Ici il suffit de mettre la grille avec les nombres de 1 à 9.
    # La substitution avec les nombres de -4 à 4 se fait automatiquement.
    tableau="""
.,2,.,.,.,5,8,.,3
8,.,.,.,.,.,.,4,.
.,.,i,.,.,3,i,6,.
6,.,8,4,.,.,i,.,.
1,.,.,.,.,.,.,2,.
.,.,.,1,6,.,i,.,4
i,i,.,.,.,i,7,.,i
.,6,.,i,i,i,.,.,i
.,7,1,.,i,6,.,i,5
"""
    solution="""
9,2,6,7,4,5,8,1,3
8,3,5,6,1,9,2,4,7
4,1,7,8,2,3,5,6,9
6,5,8,4,3,2,9,7,1
1,4,3,5,9,7,6,2,8
7,9,2,1,6,8,3,5,4
3,8,4,2,5,1,7,9,6
5,6,9,3,7,4,1,8,2
2,7,1,9,8,6,4,3,5
"""

    solution_substitution="""
4,-3,1    ,2,-1,0,    3,-4,-2
3,-2,0    ,1,-4,4,   -3,-1,2
-1,-4,2   ,3,-3,-2,   0,1,4

1,0,3,     -1,-2,-3   ,4,2,-4
-4,-1,-2    ,0,4,2    ,1,-3,3
2,4,-3     ,-4,1,3,   -2,0,-1

-2,3,-1,    -3,0,-4    ,2,4,1
0,1,4,      -2,2,-1,   -4,3,-3
-3,2,-4     ,4,3,1,     -1,-2,0
"""

    from phystricks.SudokuGridGraph import sudoku_substitution
    print(sudoku_substitution(solution))

    sudoku=SudokuGrid(tableau,length=0.7)

    pspict.DrawGraphs(sudoku)
    pspict.comment="Une belle grille de sudoku avec des nombres de -4 à 4."
    fig.no_figure()
    fig.conclude()
    fig.write_the_file()
