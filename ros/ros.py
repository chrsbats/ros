
from scipy.stats import norm
from scipy.optimize import fmin_powell, fmin_bfgs
import numpy


BIG_NUMBER = 100000.0



def ros(data,non_detect_count,distribution=norm):
    '''
    Fit a censored dataset to a normal distribution.  It is assumed the censored data is less than the smallest valid value in the data.
    TODO: Add more than one inequality into the data using the method described here: 
    http://www.itrcweb.org/gsmc-1/Content/GW%20Stats/5%20Methods%20in%20indiv%20Topics/5%207%20Nondetects.htm
    '''
    data.sort()
    sample_size = len(data)
    nd = non_detect_count
    index = range(nd,sample_size+nd)
    index = [(i)/float(sample_size+nd) for i in index]
    index = numpy.array(index)

    start_mean = data.mean()
    start_std = data.std()

    def calc_error(x):
        error = 0.0
        if x[1] < 0:
            error = (BIG_NUMBER * sample_size - x[1])** 2.0
            return error
        
        estimated_values = distribution.ppf(index,loc=x[0], scale=x[1])
        error = numpy.sum((data - estimated_values) ** 2.0)
        return error

    x = fmin_bfgs(calc_error,numpy.array([start_mean,start_std]))
    
    return x

   