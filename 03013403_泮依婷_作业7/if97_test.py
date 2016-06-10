import unittest
import if97


class Basic_Test (unittest.TestCase):

    def setUp(self):
        # Table 5
        self.tab5=[[ 3,  300,  0.100215168e-2, 0.115331273e3 ,  0.112324818e3, 0.392294792,  0.417301218e1 ,  0.150773921e4],
                   [80,  300,  0.971180894e-3, 0.184142828e3 ,  0.106448356e3,  0.368563852,  0.401008987e1,  0.163469054e4],
                   [ 3,  500,  0.120241800e-2, 0.975542239e3 ,  0.971934985e3,  0.258041912e1,  0.465580682e1,  0.124071337e4]]

    def test_Volume(self):
        places = 6
        for item in self.tab5:
            self.assertAlmostEqual(if97.Volume(item[0], item[1]), item[2], places)

    def test_Enthalpy(self):
        places = 6
        for item in self.tab5:
            self.assertAlmostEqual(if97.Enthalpy(item[0], item[1]), item[3], places)

    def test_InternalEnergy(self):
        places = 6
        for item in self.tab5:
            self.assertAlmostEqual(if97.InternalEnergy(item[0], item[1]), item[4], places)

    def test_Entropy(self):
        places = 6
        for item in self.tab5:
            self.assertAlmostEqual(if97.Entropy(item[0], item[1]), item[5], places)

    def test_IHCapacity(self):
        places = 6
        for item in self.tab5:
            self.assertAlmostEqual(if97.IHCapacity(item[0], item[1]), item[6], places)

    def test_Sound(self):
        places = 4
        for item in self.tab5:
            self.assertAlmostEqual(if97.Sound(item[0], item[1]), item[7], places)


class Backward_test(unittest.TestCase):

    def setUp(self):
        # table 7
        self.tab7 = [[3,   500,   0.391798509e3],
                     [80,  500,   0.378108626e3],
                     [80,  1500,  0.611041229e3]]
        # table 9
        self.tab9 = [[3,   0.5,   0.307842258e3],
                     [80,  0.5,   0.309979785e3],
                     [80,  3,     0.565899909e3]]

    def Test_Backword11T(self):
        places = 6
        for item in self.tab7:
            self.assertAlmostEqual(if97.Backword11T(item[0], item[1]), item[2], places)

    def test_Backward13T(self):
        places = 6
        for item in self.tab9:
            self.assertAlmostEqual(if97.Backward13T(item[0], item[1]), item[2], places)


def suitetext():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(Basic_Test))
    suite.addTest(unittest.makeSuite(Backward_test))
    return suite

if __name__ == '__main__':
    unittest.main(defaultTest='suitetext')
