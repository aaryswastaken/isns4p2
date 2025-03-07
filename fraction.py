import unittest


class Fraction:
    numerateur: int
    denominateur: int

    def __init__(self, numerateur: int, denominateur: int):
        if denominateur == 0:
            raise ZeroDivisionError

        self.numerateur = numerateur
        self.denominateur = denominateur

    def valeur(self, decimales: int = 2) -> float:
        return round(self.numerateur / self.denominateur, ndigits=decimales)

    def __str__(self):
        if self.denominateur == 0:
            raise ZeroDivisionError

        if self.numerateur % self.denominateur == 0:
            return f"{int(self.numerateur / self.denominateur)}"

        return f"{self.numerateur} / {self.denominateur}"

    def plus_grand_commun_diviseur(self):
        a = self.numerateur
        b = self.denominateur

        r = 0

        while b != 0:
            r = a % b
            a = b
            b = r

        return a

    def pgcd(self):
        return self.plus_grand_commun_diviseur()

    def reduire(self) -> bool:
        pgcd = self.pgcd()

        if pgcd == 1:
            return False

        self.numerateur = self.numerateur // pgcd
        self.denominateur = self.denominateur // pgcd

        return True

    @staticmethod
    def addition(f1, f2):
        out_num = f1.numerateur * f2.denominateur + f2.numerateur * f1.denominateur
        out_denum = f1.denominateur * f2.denominateur 

        res = Fraction(out_num, out_denum)

        res.reduire()

        return res

    def oppose(self):
        return Fraction(-self.numerateur, self.denominateur)

    @staticmethod
    def soustraction(f1, f2):
        return Fraction.addition(f1.oppose(), f2)

    @staticmethod
    def multiplication(f1, f2):
        out = Fraction(f1.numerateur * f2.numerateur, f1.denominateur * f2.denominateur)
        out.reduire()

        return out

    def inverse(self):
        return Fraction(self.denominateur, self.numerateur)

    @staticmethod
    def division(f1, f2):
        return Fraction.multiplication(f1, f2.inverse())

    def __eq__(self, other) -> bool:
        return self.numerateur == other.numerateur and self.denominateur == other.denominateur

    def __ne__(self, other) -> bool:
        return not self.__eq__(other)


class TestFaction(unittest.TestCase):
    def testPremier(self):
        f1 = Fraction(2, 5)
        f2 = Fraction(20, 48)
        f3 = Fraction(8, 1)

        def instantiate(a, b):
            return Fraction(a, b)

        assert f1 is not None
        assert f2 is not None
        assert f3 is not None

        assert f1.numerateur == 2
        assert f1.denominateur == 5

        self.assertRaises(ZeroDivisionError, instantiate, 4, 0)

    def testValeur(self):
        f1 = Fraction(1, 2)

        assert f1.valeur() == 0.5

        f2 = Fraction(1, 3)

        assert f2.valeur(decimales=2) == 0.33

    def testSTR(self):
        f1 = Fraction(5, 2)

        assert str(f1) == "5 / 2"

        f2 = Fraction(6, 3)

        assert str(f2) == "2"

    def testPGCD(self):
        f1 = Fraction(7, 3)

        assert f1.pgcd() == 1

        f2 = Fraction(14, 4)

        assert f2.pgcd() == 2

        f3 = Fraction(25, 15)

        assert f3.pgcd() == 5

    def testReduire(self):
        f1 = Fraction(25, 15)
        f1.reduire()

        assert f1.denominateur == 3
        assert f1.numerateur == 5

        f2 = Fraction(20, 48)
        f2.reduire()

        assert f2.numerateur == 5
        assert f2.denominateur == 12

        f3 = Fraction(10, 5)
        f3.reduire()

        assert f3.numerateur == 2
        assert f3.denominateur == 1

    def testAddition(self):
        f1 = Fraction(5, 10)
        f2 = Fraction(15, 25)

        f4 = Fraction.addition(f1, f2)
    
        assert f4.numerateur == 11
        assert f4.denominateur == 10

    def testOperations(self):
        f1 = Fraction(3, 4)
        f2 = Fraction(1, 2)

        mult = Fraction.multiplication(f1, f2)

        assert mult.denominateur == 8
        assert mult.numerateur == 3

        div = Fraction.division(f1, f2)

        assert div.numerateur == 3
        assert div.denominateur == 2

    def testEq(self):
        f1 = Fraction(4, 8)
        f2 = Fraction(1, 2)

        assert f1 != f2
        assert not f1 == f2

        f1.reduire()

        assert f1 == f2
        assert not f1 != f2
