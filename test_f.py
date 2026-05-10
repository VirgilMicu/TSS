import unittest
from cont import ContCurent, Tranzactie
import random as r

class Tests(unittest.TestCase):

    def test_clase_echivalenta (self):
        c = ContCurent("1234567")
        with self.assertRaises(ValueError): c = ContCurent("123a4eer56")
        with self.assertRaises(ValueError): c = ContCurent("3456")
        with self.assertRaises(ValueError): c = ContCurent("x1234fdasdf5")
        with self.assertRaises(ValueError): c = ContCurent(765431021)
        with self.assertRaises(ValueError): c = ContCurent(['7', '6', '5', '4', '3', '2', 'x', '2'])
        with self.assertRaises(ValueError): c = ContCurent(['6', '5', '4', '3', '2', '1'])
        with self.assertRaises(ValueError): c = ContCurent(('c', 0, 2, 3, 4, 5, 6, 7))
        self.assertEqual(c.nrcont, "1234567")
        c.procesare_tranzactie(10, 1, "1224567")
        self.assertIn(Tranzactie(1, 1000, 1, "1224567"), c.tranzactii)

        #procesare tranzactii
        c.procesare_tranzactie(1, 1, "2345678")
        self.assertEqual(c._balanta, 1100)
        self.assertIn(Tranzactie(2, 100, 1, "2345678"), c.tranzactii)
        with self.assertRaises(Exception): c.procesare_tranzactie(1, 1, "12345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(1, 1, "1234567")
        c.procesare_tranzactie(3, 2, "2345678"); 
        self.assertEqual(c._balanta, 800)
        self.assertIn(Tranzactie(3, 300, 2, "2345678"), c.tranzactii)
        with self.assertRaises(Exception): c.procesare_tranzactie(4, 2, "123456l")
        with self.assertRaises(Exception): c.procesare_tranzactie(4, 2, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(4, 0, "1234557")
        with self.assertRaises(Exception): c.procesare_tranzactie(4, 3, "12345673")
        with self.assertRaises(Exception): c.procesare_tranzactie(4, 3, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(4, '1', "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(4, '1', "12345673")
        with self.assertRaises(Exception): c.procesare_tranzactie(4, [1], "1234567")

        c.procesare_tranzactie(20.01, 1, "2345678")
        self.assertEqual(c._balanta, 2801)
        self.assertIn(Tranzactie(4, 2001, 1, "2345678"), c.tranzactii)
        with self.assertRaises(Exception): c.procesare_tranzactie(100, 1, "12345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, 1, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, 2, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, 2, "123456l")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, 2, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, 0, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, 3, "12345673")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, 3, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, '1', "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, '1', "12345673")
        with self.assertRaises(Exception): c.procesare_tranzactie(100, (1,), "1234567")

        with self.assertRaises(Exception): c.procesare_tranzactie(0, 1, "2345678");
        with self.assertRaises(Exception): c.procesare_tranzactie(-1, 1, "12345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(-1, 1, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(0, 2, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(-2, 2, "123456l")
        with self.assertRaises(Exception): c.procesare_tranzactie(-3, 2, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(-3, 3, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(0, 0, "12345673")
        with self.assertRaises(Exception): c.procesare_tranzactie(0, 3, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(-3, '1', "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(0, '1', "12345673")
        with self.assertRaises(Exception): c.procesare_tranzactie(0, '1', "1234567")

        with self.assertRaises(Exception): c.procesare_tranzactie("1", 1, "2345678");
        with self.assertRaises(Exception): c.procesare_tranzactie([1], 1, "12345678")
        with self.assertRaises(Exception): c.procesare_tranzactie([1], 1, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie((1,), 2, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie([3], 2, "123456l")
        with self.assertRaises(Exception): c.procesare_tranzactie([2], 2, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie('2', 0, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie('7', 3, "12345673")
        with self.assertRaises(Exception): c.procesare_tranzactie((3,), 3, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie('2', '1', "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie('7', '1', "12345673")
        with self.assertRaises(Exception): c.procesare_tranzactie((3,), [1], "1234567")
    

    def test_boundary (self): # suplimentare 
        with self.assertRaises(ValueError): c = ContCurent("123456")
        with self.assertRaises(ValueError): c = ContCurent("x12345")
        c = ContCurent("1234567")
        with self.assertRaises(ValueError): c = ContCurent("x12345a")
        with self.assertRaises(ValueError): c = ContCurent("12345678")
        with self.assertRaises(ValueError): c = ContCurent("78x12345")
        with self.assertRaises(ValueError): c = ContCurent(123456)
        with self.assertRaises(ValueError): c = ContCurent(['6', '5', '4', '3', '2', 'x'])
        with self.assertRaises(ValueError): c = ContCurent(1234567)
        with self.assertRaises(ValueError): c = ContCurent(['7', '6', '5', '4', '3', '2', 'x'])
        with self.assertRaises(ValueError): c = ContCurent(87654321)
        with self.assertRaises(ValueError): c = ContCurent(['8', '7', '6', '5', '4', '3', '2', 'x'])

        assert c.nrcont == "1234567"
        assert c._balanta == 0
        c.procesare_tranzactie(100, 1, "1224567")

        id = 2
        bl = c._balanta
        r.seed = 99
        for N in range (1, 5): 
            if N == 1: cont = "0123456"
            if N == 2: cont = "01234567" 
            if N == 3: cont = "1234567"
            if N == 4: cont = "1234568"
            for T in range (1, 6):
                tip = T - 1 
                for S in range (1, 8):
                    if T == 5:
                        tip = '1' if int (r.random() * 1000) % 2 == 0 else [1]
                    if S == 1: suma = (c._balanta - 1) / 100
                    if S == 2: suma = (c._balanta ) / 100
                    if S == 3: suma = (c._balanta + 1) / 100
                    if S == 4: suma = 0.01
                    if S == 5: suma = 0
                    if S == 6: suma = - 0.01
                    if S == 7: suma = '100s'
                    # conditiile din if: contditiile in care trebuie sa avem exceptie
                    #print(suma, tip, cont, c._balanta, N, T, S)
                    if (N in [2, 3] or T in [1, 4, 5] or not (isinstance(suma,int) or isinstance(suma,float))  or suma <= 0 or (tip == 2 and suma * 100 > c._balanta)):
                        with self.assertRaises(Exception): c.procesare_tranzactie(suma, tip, cont)
                    else:
                        try:
                            
                            c.procesare_tranzactie(suma, tip, cont)
                        except: 
                            self.fail()
                        mx = max (t.id for t in c.tranzactii)   
                        self.assertEqual(mx, id)
                        bl += int(round(suma * 100)) * (1 if tip==1 else -1)
                        self.assertIn(Tranzactie(id, int(round(suma * 100)), tip, cont), c.tranzactii)
                        self.assertEqual(bl, c._balanta)
                        id += 1  
                           
                    
    def test_statement_coverage(self):
        pass


if __name__ == '__main__':
    unittest.main()


