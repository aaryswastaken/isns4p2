import unittest
from typing import List, Tuple

from brique import Brique, Couleur, v2
from brique_speciale import TypeBrique, BriqueSpeciale


class CasseBriques():
    briques: List[Brique]
    score: int = 0

    def __init__(self):
        self.briques = []
        self.score = 0

    def ajouter_brique(self, brique: Brique) -> None:
        self.briques.append(brique)

    def str_briques(self) -> str:
        out = "" 
        l = len(self.briques) - 1

        for (i, brique) in enumerate(self.briques):
            out += str(brique)

            if i < l:
                out += "\n"

        return out

    def afficher_briques(self) -> None:
        print(self.str_briques())

    def filter_briques(self, x_pos) -> List[int]:
        out = []

        for (i, brique) in enumerate(self.briques):
            l1, _, l3, _ = brique.get_limits()
            
            if l1 <= x_pos < l3:
                out.append(i)

        return out 

    def impact_brique(self, x_pos) -> Tuple[int | None, bool]:
        ftd = self.filter_briques(x_pos)

        if len(ftd) == 0:
            return None, False
        
        sel = None
        _max = -10
        s_index = None
        for index in ftd:
            _, _, _, l4 = self.briques[index].get_limits()

            if l4 - 1 > _max or sel is None:
                sel = self.briques[index]
                _max = l4 - 1
                s_index = index 

        if sel is None or s_index is None:
            return None, False

        res = sel.do_hit(v2(x_pos, _max))

        if not res:
            raise Exception("There has been an error :(")

        if sel.solidite == 0:
            self.briques.pop(s_index)
            return s_index, True 

        return s_index, False

    def afficher_score(self) -> None:
        print(f"Le score est de: {self.score}")


class TestCasseBriques(unittest.TestCase):
    def setUp(self):
        brique1 = Brique()
        brique1.couleur = "red"
        brique1.solidite = 3
        brique1.points = 4

        brique1.position = v2(1, 2)
        brique1.size = v2(3, 3)

        self.brique1 = brique1 


        class Brique5Pts(BriqueSpeciale):
            points = 10
            effet_special = TypeBrique.DOUBLE_SCORE


        brique2 = Brique5Pts()
        brique2.couleur = "black"
        brique2.solidite = 5 

        brique2.position = v2(4, 2)
        brique2.size = v2(2, 1)

        self.brique2 = brique2


    def test_init(self):
        cb = CasseBriques()

        assert cb.briques is not None 
        assert len(cb.briques) == 0

        assert cb.score == 0

    def test_ajout_brique(self):
        cb = CasseBriques()


        assert len(cb.briques) == 0
        cb.ajouter_brique(self.brique1)

        self.assertEqual(str(cb.briques[0]), "Brique red, en (1, 2), de taille (3, 3), sdt=3, pts=4")

        assert self.brique2.points == 20
        cb.ajouter_brique(self.brique2)

        assert len(cb.briques) == 2 
        assert cb.briques[1] is not None

    def test_str_briques(self):
        cb = CasseBriques() 

        cb.ajouter_brique(self.brique2)
        cb.ajouter_brique(self.brique1)

        txt = cb.str_briques()

        assert len(txt.split("\n")) == 2
    
    def test_filter_brique(self):
        cb = CasseBriques()

        assert len(cb.filter_briques(10)) == 0


        brique1 = Brique()
        brique1.position = v2(1, 1)
        brique1.size = v2(2, 2)

        cb.ajouter_brique(brique1)

        assert len(cb.briques) == 1 
        assert len(cb.filter_briques(10)) == 0 
        assert len(cb.filter_briques(2)) == 1 

        brique2 = Brique()
        brique2.position = v2(7, 2)
        brique2.size = v2(10, 2)
        cb.ajouter_brique(brique2)

        brique3 = Brique()
        brique3.position = v2(10, 4)
        brique3.size = v2(2, 1)
        cb.ajouter_brique(brique3)

        assert len(cb.briques) == 3 
        assert len(cb.filter_briques(10)) == 2 
        assert len(cb.filter_briques(9)) == 1 

    def test_impact_brique(self):
        cb = CasseBriques()

        brique1 = Brique()
        brique1.position = v2(7, 2)
        brique1.size = v2(5, 1)
        brique1.solidite = 5 
        cb.ajouter_brique(brique1)

        assert cb.briques[0].solidite == 5 
        assert len(cb.filter_briques(10)) == 1 

        index, res = cb.impact_brique(10)

        assert index == 0 and res == False  # res = False -> not destroyed 
        assert cb.briques[0].solidite == 4 

        brique2 = Brique()
        brique2.position = v2(10, 3)
        brique2.size = v2(4, 2)
        brique2.solidite = 10 
        cb.ajouter_brique(brique2)

        brique3 = Brique()
        brique3.position = v2(1, 1)
        brique3.size = v2(2, 1)
        brique3.solidite = 15 
        cb.ajouter_brique(brique3) 

        assert len(cb.briques) == 3 
        assert cb.briques[0].solidite == 4 and cb.briques[1].solidite == 10 and cb.briques[2].solidite == 15

        index, res = cb.impact_brique(10)

        assert index == 1 and res == False 
        assert cb.briques[0].solidite == 4 and cb.briques[1].solidite == 9 and cb.briques[2].solidite == 15 

        for _ in range(10):
            _, _ = cb.impact_brique(10)

        assert len(cb.briques) == 2 
        assert cb.briques[0].solidite == 3 and cb.briques[1].solidite == 15
