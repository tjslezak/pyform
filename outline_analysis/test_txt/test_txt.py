"""Test read_txt_outlines.py"""
import unittest
class Test_read_txt(unittest.TestCase):
    def setUp(self):
        self.null = "./null.txt"
        self.single_val = "./1val.txt"
        self.odd_vals = "./odd_vals.txt"
        self.single_pt = "./1pt.txt"
        self.two_pts = "./2pts.txt"
        self.multi_pts = "./multi_pts.txt"

    def test_null(self):
        """Test empty txt file"""
        self.assertIsNone(rto.txtToDict(self.null))

    def test_single_pt(self):
        """Test single val .txt raises error"""
        self.assertRaises(RuntimeError, rto.txtToDict, self.single_val)

    def test_odd_vals(self):
        """Test odd number of vals .txt raises error"""
        self.assertRaises(RuntimeError, rto.txtToDict, self.odd_vals)

    def test_single_pt(self):
        """Test single point .txt"""
        actual = rto.txtToDict(self.single_pt)
        expected = {'Lat': [22.1], 'Lon': [310.0]}
        self.assertDictEqual(actual, expected)

    def test_two_pts(self):
        """Test two point .txt"""
        actual = rto.txtToDict(self.two_pts)
        expected = {'Lat': [23.0, 22.7], 'Lon': [311.8, 312.1]}
        self.assertDictEqual(actual, expected)

    def test_multi_pts(self):
        """Test multiple points .txt"""
        actual = rto.txtToDict(self.multi_pts)
        expected = {'Lat': [12.1, 13.5, 16.5, 12.5, 0.6, -10.9],
                    'Lon': [30.0, 41.5, 20.7, 0.2, -20.3, 10.1]}
        self.assertDictEqual(actual, expected)

if __name__ == "__main__":
    import sys, os
    OA_PATH = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    if not OA_PATH in sys.path:
        sys.path.append(OA_PATH)
    import read_txt_outlines as rto
    unittest.main()
