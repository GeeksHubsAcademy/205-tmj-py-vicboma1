import pytest
import unittest   # The test framework

from kata import apply

class Test_kata(unittest.TestCase):

    def test_apply_1(self):
        expected = [7, 5, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = apply("abacaba")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_2(self):
        expected = [0, 0, 0, 0, 1, 0, 0, 0, 1, 0, 1, 1, 2, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = apply("likemm")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_3(self):
        expected = [30, 27, 0, 0, 1, 29, 1, 46, 8, 1, 41, 27, 12, 0, 5, 1, 1, 20, 17, 35, 1, 1, 1, 39, 22, 37]
        result = apply("rkuhsxtflzvytbtwxyarsglibmhfmmikyolfmopbtkzxezjahq")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_4(self):
        expected = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 10, 5, 9, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = apply("ommnommnomm")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_5(self):
        expected = [1, 0, 0, 0, 0, 18, 0, 9, 0, 1, 1, 1, 0, 4, 1, 1, 1, 0, 0, 1, 0, 20, 0, 1, 0, 17]
        result = apply("ztvxhhkvfvlahvvvzjqvnvpnof")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_6(self):
        expected = [20, 6, 1, 7, 4, 8, 1, 0, 0, 4, 17, 0, 1, 27, 1, 0, 12, 0, 29, 5, 1, 1, 24, 41, 35, 1]
        result = apply("wwaxcdysyswdnozfxkxnqafwxtuevteqmkssjbnjygbx")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_7(self):
        expected = [1, 0, 1, 1, 1, 0, 0, 8, 1, 0, 0, 1, 10, 1, 0, 0, 0, 1, 1, 0, 16, 11, 7, 0, 0, 1]
        result = apply("muehvwcaimhwnzvrulds")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_8(self):
        expected = [0, 3, 23, 1, 1, 0, 1, 0, 13, 1, 1, 18, 1, 1, 31, 0, 1, 0, 1, 1, 0, 1, 12, 12, 1, 1]
        result = apply("ocxqcjbibmiolxcvtwziosdcgknywloe")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_9(self):
        expected = [0, 1, 0, 0, 0, 0, 1, 1, 8, 0, 1, 0, 1, 1, 0, 0, 1, 0, 1, 0, 4, 0, 1, 0, 0, 0]
        result = apply("gsniuwqubiimkh")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_10(self):
        expected = [17, 1, 0, 1, 0, 1, 1, 30, 14, 35, 1, 0, 17, 5, 32, 6, 13, 0, 1, 38, 1, 0, 1, 35, 0, 17]
        result = apply("gmotjiauxwhxhtpkzmiphhajqdbsqhnjzonxqxjhtfx")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_11(self):
        expected = [0, 9, 0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 1, 0, 1, 0, 0, 0, 1, 0, 0, 0, 0, 5, 0, 0]
        result = apply("bjxosexmb")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_12(self):
        expected = [1, 0, 0, 1, 0, 0, 0, 1, 1, 1, 0, 1, 0, 0, 0, 0, 0, 1, 0, 4, 1, 0, 0, 2, 0, 0]
        result = apply("urtadtjihlxx")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_13(self):
        expected = [4, 1, 0, 14, 1, 1, 0, 1, 9, 1, 1, 13, 1, 1, 14, 6, 1, 4, 1, 1, 0, 1, 1, 0, 0, 1]
        result = apply("lrairavnljdilkpqetopzbodhmoowsfo")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_14(self):
        expected = [1, 28, 32, 44, 0, 15, 0, 39, 0, 1, 1, 1, 29, 8, 17, 1, 46, 36, 1, 11, 0, 1, 15, 1, 47, 5]
        result = apply("wmydqthmfhrcwbwtlcqxryfmdjnsmmboznaozopcbvckhrdoyq")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_15(self):
        expected = [0, 1, 0, 0, 0, 0, 0, 0, 2, 1, 0, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = apply("jliibn")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_16(self):
        expected = [1, 1, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0]
        result = apply("apqcbf")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_17(self):
        expected = [7, 0, 1, 33, 16, 17, 44, 33, 0, 9, 26, 22, 1, 0, 32, 1, 0, 0, 15, 22, 1, 14, 1, 0, 0, 0]
        result = apply("lgtjltldhfojopoluhkvelvtofkcshsavggewamdhoskg")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_18(self):
        expected = [1, 42, 21, 1, 1, 15, 1, 24, 0, 1, 1, 1, 1, 0, 26, 7, 1, 1, 18, 8, 0, 1, 1, 29, 21, 23]
        result = apply("bzeawxrxgoqpyhztjpsbcxtzhvosfhmsyxoshdlkcbf")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 

    def test_apply_19(self):
        expected = [1, 1, 0, 0, 1, 0, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0]
        result = apply("lieaboy")
        for i in range(0,len(result)):
            assert(expected[i] == result[i]) 
    
if __name__ == '__main__':
	unittest.main()