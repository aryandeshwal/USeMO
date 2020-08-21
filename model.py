import math
import numpy as np
from sklearn.gaussian_process import GaussianProcessRegressor
from sklearn.gaussian_process.kernels import RBF, ConstantKernel,Matern
import logging

class GaussianProcess:
    def __init__(self, dim):
        self.dim = dim
        sqrdExp =  RBF(length_scale=1)
        self.xValues = []
        self.yValues = []
        self.model = GaussianProcessRegressor(kernel=sqrdExp,normalize_y=True,n_restarts_optimizer=10)
     
    def fitModel(self):
        self.model.fit(self.xValues, self.yValues)
    def fitprevModel(self):
        self.model.fit(self.xValues[:-1], self.yValues[:-1])
    
    def addSample(self, x, y):
        self.xValues.append(x)
        self.yValues.append(y)

    def getPrediction(self, x):
        mean, std = self.model.predict(x.reshape(1,-1),return_std=True)
        return mean, std