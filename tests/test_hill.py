from pycipher import Hill
import unittest

class TestHill(unittest.TestCase):
    
    def test_encipher(self):
        ct = Hill("frep").encipher("thesteakdoesnotexist")
        ct_ref = "gzoahgoutooarchgrext"
        self.assertEqual(ct, ct_ref)

    def test_decipher(self):
        pt = Hill("frep").decipher("gzoahgoutooarchgrext")
        pt_ref = "thesteakdoesnotexist"
        self.assertEqual(pt, pt_ref)
        