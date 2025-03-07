from typing import Tuple
import unittest

class Couleur:
    r: int
    g: int
    b: int

    @staticmethod
    def int_to_hex_byte(val: int) -> str:
        return ("00" + f"{val:X}")[-2:]

    def to_hex(self) -> str:
        return self.int_to_hex_byte(self.r) + self.int_to_hex_byte(self.g) + self.int_to_hex_byte(self.b)

    def __str__(self) -> str:
        return f"#{self.to_hex()}"

class v2:
    x: int
    y: int

    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __str__(self) -> str:
        return f"({self.x}, {self.y})"

    def __add__(self, other):
        return v2(self.x + other.x, self.y + other.y)

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)

class Brique:
    couleur: Couleur | str
    solidite: int
    points: int

    position: v2
    size: v2

    def __init__(self):
        pass

    def __str__(self) -> str:
        return f"Brique {str(self.couleur)}, en {str(self.position)}, de taille {str(self.size)}, sdt={self.solidite}, pts={self.points}"

    def get_limits(self) -> Tuple[int, int, int, int]:
        other = self.position + self.size

        return (self.position.x, self.position.y, other.x, other.y)

    def is_hit(self, pos) -> bool:
        l1, l2, l3, l4 = self.get_limits()

        return l1 <= pos.x < l3 and l2 <= pos.y < l4

    def do_hit(self, pos) -> bool:
        if self.is_hit(pos):
            self.solidite -= 1
            return True

        return False


class TestVec(unittest.TestCase):
    def test_instance(self):
        va = v2(1, 2)
        vb = v2(3, 4)

        assert va.x == 1
        assert va.y == 2
        assert vb.x == 3
        assert vb.y == 4

    def test_add(self):
        va = v2(12, 87)
        vb = v2(-4, 7)

        vc = va + vb
        vd = vb + va 

        assert vc.x == va.x + vb.x
        assert vc.y == va.y + vb.y

        assert vc.x == vd.x
        assert vc.y == vd.y

    def test_eq(self):
        va = v2(1, 2)
        vb = v2(2, 1)

        assert not va == vb
        assert va != vb
        assert va == v2(vb.y, vb.x)


class TestBrique(unittest.TestCase):
    def test_inst_str(self):
        brique = Brique()
        brique.couleur = "red"
        brique.solidite = 3
        brique.points = 4

        brique.position = v2(1, 2)
        brique.size = v2(3, 3)

        self.assertEqual(str(brique), "Brique red, en (1, 2), de taille (3, 3), sdt=3, pts=4")

    def test_limits(self):
        brique = Brique()
        brique.position = v2(1, 2)
        brique.size = v2(3, 4)

        assert brique.get_limits() == (1, 2, 4, 6)

    def test_hit(self):
        brique = Brique()
        brique.position = v2(5, 5)
        brique.size = v2(6, 3)

        #   0 1 2 3 4 5 6 7 8 9101112
        # 3
        # 4
        # 5 . . . . .1o O O O O O . .
        # 6 . . . . . O O O3o O O . .
        # 7 . . . . . O O O O O2o4. .
        # 8 . . . .5. . . . . .6. . . 

        assert brique.is_hit(v2(5, 5))      # 1o
        assert brique.is_hit(v2(10, 7))     # 2o
        assert brique.is_hit(v2(8, 6))      # 3o
        assert not brique.is_hit(v2(11, 7)) # 4.
        assert not brique.is_hit(v2(4, 8))  # 5.
        assert not brique.is_hit(v2(10, 8)) # 6.

        brique.solidite = 4 

        assert brique.solidite == 4 

        assert brique.do_hit(v2(4, 4)) == False 
        assert brique.solidite == 4 

        assert brique.do_hit(v2(6, 6)) == True 
        assert brique.solidite == 3
