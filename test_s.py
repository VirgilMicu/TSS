import unittest
from cont import ContCurent, Tranzactie

class Tests(unittest.TestCase):

    def test_statement_si_branch_coverage (self):
        with self.assertRaises(ValueError): c = ContCurent(1234567)
        with self.assertRaises(ValueError): c = ContCurent("123456")
        c = ContCurent("1234567")
        self.assertEqual(c.nrcont, "1234567")

        #procesare tranzactii
        with self.assertRaises(Exception): c.procesare_tranzactie("10", 1, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(10, 1, "abc")
        with self.assertRaises(Exception): c.procesare_tranzactie(10, 1, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(-10, 1, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(10, 9, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(1000, 2, "2345678")
        c.procesare_tranzactie(10, 1, "2345678")
        self.assertIn(Tranzactie(1, 1000, 1, "2345678"), c.tranzactii)
        self.assertEqual(1000, c._balanta)
        c.procesare_tranzactie(5, 2, "2345678")
        self.assertIn(Tranzactie(2, 500, 2, "2345678"), c.tranzactii)
        self.assertEqual(500, c._balanta)

    def test_condition_coverage (self):            
        with self.assertRaises(ValueError): c = ContCurent(1234567)
        with self.assertRaises(ValueError): c = ContCurent("123456")
        with self.assertRaises(ValueError): c = ContCurent("123456a")
        c = ContCurent("1234567")
        self.assertEqual(c.nrcont, "1234567")

        #procesare tranzactii
        with self.assertRaises(Exception): c.procesare_tranzactie(10, 1, "123")
        with self.assertRaises(Exception): c.procesare_tranzactie(10.0, 1, "123")
        with self.assertRaises(Exception): c.procesare_tranzactie(10, 1, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(-10, 1, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(10, 9, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(1000, 2, "2345678")
        c.procesare_tranzactie(10, 1, "2345678")
        self.assertIn(Tranzactie(1, 1000, 1, "2345678"), c.tranzactii)
        self.assertEqual(1000, c._balanta)
        c.procesare_tranzactie(5, 2, "2345678")
        self.assertIn(Tranzactie(2, 500, 2, "2345678"), c.tranzactii)
        self.assertEqual(500, c._balanta)

    def test_circuite_independente(self):            
        with self.assertRaises(ValueError): c = ContCurent(1234567)
        with self.assertRaises(ValueError): c = ContCurent("123456")
        c = ContCurent("1234567")
        self.assertEqual(c.nrcont, "1234567")

        #procesare tranzactii
        with self.assertRaises(Exception): c.procesare_tranzactie("10", 1, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(10, 1, "abc")
        with self.assertRaises(Exception): c.procesare_tranzactie(10, 1, "1234567")
        with self.assertRaises(Exception): c.procesare_tranzactie(-10, 1, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(10, 9, "2345678")
        with self.assertRaises(Exception): c.procesare_tranzactie(1000, 2, "2345678")
        c.procesare_tranzactie(10, 1, "2345678")
        self.assertIn(Tranzactie(1, 1000, 1, "2345678"), c.tranzactii)
        self.assertEqual(1000, c._balanta)
        c.procesare_tranzactie(5, 2, "2345678")
        self.assertIn(Tranzactie(2, 500, 2, "2345678"), c.tranzactii)
        self.assertEqual(500, c._balanta)

if __name__ == '__main__':
    unittest.main()


