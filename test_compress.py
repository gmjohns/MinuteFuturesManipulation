from unittest import TestCase
import pandas as pd
from pandas.util.testing import assert_frame_equal
import os


class TestGetVpp(TestCase):
    def setUp(self):
        test_file_name = 'test1.csv'
        try:
            test_data = pd.read_csv(os.getcwd() + '/minute_futures_data/' + test_file_name, sep=",", header=None)
            test_data.columns = ['date', 'time', 'open', 'close', 'high', 'low', 'volume']
            self.fixture = test_data
        except IOError:
            print('cannot open file')

    def test_get_vpp(self):
        exp = 50.0
        import compress
        assert compress.get_vpp(self.fixture) == exp, 'vpp calculation error'


class TestMakeSeq(TestCase):
    def setUp(self):
        test_file_name = 'test1.csv'
        try:
            import compress
            test_data = pd.read_csv(os.getcwd() + '/minute_futures_data/' + test_file_name, sep=",", header=None)
            test_data.columns = ['date', 'time', 'open', 'close', 'high', 'low', 'volume']
            self.fixture = compress.make_seq(test_data, vpp=50.0)
        except IOError:
            print('cannot open file')

    def test_make_seq(self):
        exp = pd.DataFrame([[0, 10.0],
                            [3, 0.0],
                            [6, 0.0],
                            [9, 0.0],
                            [10, 80.0],
                            [10, 30.0],
                            [13, 0.0],
                            [16, 20.0],
                            [19, 0.0]], columns=['index', 'rem'])
        assert_frame_equal(self.fixture, exp)


class TestCompress(TestCase):
    def setUp(self):
        test_file_name = 'test1.csv'
        try:
            import compress
            test_data = pd.read_csv(os.getcwd() + '/minute_futures_data/' + test_file_name, sep=",", header=None)
            test_data.columns = ['date', 'time', 'open', 'close', 'high', 'low', 'volume']
            self.fixture = compress.compress(test_data, seq=pd.DataFrame([[0, 10.0],
                                                                          [3, 0.0],
                                                                          [6, 0.0],
                                                                          [9, 0.0],
                                                                          [10, 80.0],
                                                                          [10, 30.0],
                                                                          [13, 0.0],
                                                                          [16, 20.0],
                                                                          [19, 0.0]], columns=['index', 'rem']))
        except IOError:
            print('cannot open file')

    def test_compress(self):
        exp = pd.DataFrame([['09/27/2009', '18:00', 1.8],
                            ['09/28/2009', '8:00', 1.0],
                            ['09/29/2009', '5:00', 2.0],
                            ['09/29/2009', '9:00', 2.0],
                            ['09/29/2009', '9:00', 2.0],
                            ['09/29/2009', '21:00', 1.6],
                            ['09/30/2009', '5:00', 1.0],
                            ['09/30/2009', '23:00', 1.8]], columns=['date', 'time', 'vwa'])
        assert_frame_equal(self.fixture, exp)
