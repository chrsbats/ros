import unittest
import ros
import numpy
from scipy.stats import norm

TOLERENCE = 0.2

class TestROS(unittest.TestCase):
    

        
    def test_ros(self):
        print "Testing on synthesized data"
        m = 10.0
        s = 30.0
        print "actual mean", m
        print "actual std", s
        x = norm.rvs(loc=m, scale=s, size=100000)
        real_estimated_mean = x.mean()
        real_estimated_std = x.std()
        print 'actual estimated mean',real_estimated_mean
        print 'actual estimated std',real_estimated_std
        lower_bound = x.mean() - (x.std() / 2.0)
        y = numpy.array([i for i in x if i > lower_bound])
        filtered = len(x) - len(y)
        nd = filtered
        print "non detects", nd
        print 'naive mean', y.mean()
        print 'naive std', y.std()
        
        stats = ros.ros(y,nd)
        print 'calculated mean',stats[0]
        print 'calculated std',stats[1]

        print 'error in mean fit', numpy.sqrt((stats[0] - m ) ** 2.0)
        print 'error in std fit', numpy.sqrt((stats[0] - m ) ** 2.0)
        assert numpy.sqrt((stats[0] - m ) ** 2.0) < TOLERENCE
        assert numpy.sqrt((stats[1] - s ) ** 2.0) < TOLERENCE


if __name__ == '__main__':
    unittest.main()

