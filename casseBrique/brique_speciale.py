import unittest
from enum import Enum

from brique import Brique, v2, Couleur


class TypeBrique(Enum):
    DOUBLE_SCORE = 1
    VIE_SUPP = 2

    def __str__(self) -> str:
        if self.value == self.DOUBLE_SCORE.value:
            return "Double score"

        if self.value == self.VIE_SUPP.value:
            return "Vie supplementaire"

        return ""


class BriqueSpeciale(Brique):
    effet_special: TypeBrique | None = None

    def __init__(self):
        super().__init__()

        if self.effet_special == TypeBrique.DOUBLE_SCORE:
            self.points *= 2    # ?????????

    def __str__(self):
        return super().__str__() + ". Effet special: " + str(self.effet_special)



class TestBriqueSpeciale(unittest.TestCase):
    def test_constructeur(self):
        class Brique5Points(BriqueSpeciale):
            points = 10
            effet_special = TypeBrique.DOUBLE_SCORE


        brique = Brique5Points()

        assert brique.points == 20

    def test_str(self):
        self.assertEqual(str(TypeBrique.DOUBLE_SCORE), "Double score")

        brique = BriqueSpeciale()
        brique.effet_special = TypeBrique.VIE_SUPP
        brique.points = 10
        brique.couleur = "black"
        brique.position = v2(1, 1)
        brique.size = v2(2, 2)
        brique.solidite = 5

        self.assertEqual(str(brique), "Brique black, en (1, 1), de taille (2, 2), sdt=5, pts=10. Effet special: Vie supplementaire")
