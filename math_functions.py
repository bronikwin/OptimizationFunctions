# -*- coding: utf-8 -*-
"""
Created by 'kolya' on 01.06.2022 at 1:38
"""
import numpy as np

class OptimizationFunctions:
    """ optimization functions for testing optimization algorithms """
    def himmelblau(self, x_grid, y_grid):
        function = (x_grid ** 2 + y_grid - 11) ** 2 + (x_grid + y_grid ** 2 - 7) ** 2
        return function

    def himmelblau_root(self)->[[]]:
        return [[3,2],[-2.805118,3.131312],[-3.779310,-3.283186],[3.584428,-1.848126]]

    def eggholder(self, x_grid, y_grid):
        function = -(y_grid + 47) * np.sin((abs(x_grid / 2 + (y_grid + 47)))) - x_grid * np.sin((abs(x_grid - y_grid - 47)))
        return function

    def eggholder_root(self)->[[]]:
        return [[512,404.2319]]

    def rosenbrok(self, x_grid, y_grid):
        function = 100*(y_grid-x_grid**2)**2+(1-x_grid)**2
        return function

    def rosenbrok_root(self)->[[]]:
        return [[1,0]]

    def rastrigin(self, x_grid, y_grid):
        function = 0.1*x_grid**2+0.1*y_grid**2-4*np.cos(0.8*x_grid)-4*np.cos(0.8*y_grid)+8
        return function

    def rastrigin_root(self)->[[]]:
        return [[0,0]]

    def sombrero(self, x_grid, y_grid):
        function = (1-np.sin((x_grid**2+y_grid**2)**0.5)**2)/(1+0.001*(x_grid**2+y_grid**2))
        return function

    def grienwank(self, x_grid, y_grid):
        function = -10/(0.005*(x_grid**2+y_grid**2)-np.cos(x_grid)*np.cos(y_grid/2**0.5)+2)+10
        return function

    def de_jong_2(self, x_grid, y_grid):
        function = -100/(100*(x_grid**2-y_grid)+(1-x_grid)**2+1)+100
        return function

    def multiexternal4(self, x_grid, y_grid):
        function = -0.5*(x_grid**2+x_grid*y_grid+y_grid**2)*(1+0.5*np.cos(1.5*x_grid)*np.cos(3.2*x_grid*y_grid)*np.cos(3.14*y_grid)+
                                                             0.5*np.cos(2.2*x_grid)*np.cos(4.8*x_grid*y_grid)*np.cos(3.5*y_grid))
        return function

    def rana_function(self, x_grid, y_grid):
        function = x_grid*np.sin((abs(y_grid+1-x_grid))**0.5)*np.cos((abs(y_grid+1+x_grid))**0.5)+(y_grid+1)*np.cos((abs(y_grid+1-x_grid))**0.5)*np.sin((abs(y_grid+1+x_grid))**0.5)
        return function

    def bill_function(self, x_grid, y_grid):
        function = (1.5-x_grid+x_grid*y_grid)**2+(2.25-x_grid+x_grid*y_grid**2)**2+(2.625-x_grid+x_grid*y_grid**3)**2
        return function

    def bill_function_root(self)->[[]]:
        return [[3,0.5]]

    def bukin_6_function(self, x_grid, y_grid):
        function = 100*(abs(y_grid-0.01*x_grid**2))**0.5+0.01*abs(x_grid+10)
        return function

    def bukin_6_function_root(self)->[[]]:
        return [[-10,1]]

    def izom_function(self, x_grid, y_grid):
        function = -np.cos(x_grid)*np.cos(y_grid)*np.exp(-((x_grid-np.pi)**2+(y_grid-np.pi)**2))
        return function

    def izom_function_root(self)->[[]]:
        return [[np.pi,np.pi]]

    def cross_tray_function(self, x_grid, y_grid):
        function = -0.0001*(abs(np.sin(x_grid)*np.sin(y_grid)*np.exp(abs(100-(x_grid**2+y_grid**2)**0.5/np.pi)))+1)*0.1
        return function

    def cross_tray_function_root(self)->[[]]:
        return [[1.34941,-1.34941],[1.34941,1.34941],[-1.34941,1.34941],[-1.34941,-1.34941]]

    def shaffer_2(self, x_grid, y_grid):
        function = 0.5+((np.sin(x_grid**2-y_grid**2))**2-0.5)/(1+0.001*(x_grid**2+y_grid**2))**2
        return function

    def shaffer_2_root(self)->[[]]:
        return [[0,0]]

    def shaffer_4(self, x_grid, y_grid):
        function = 0.5+(np.cos(np.sin(abs(x_grid**2-y_grid**2)))**2-0.5)/(1+0.001*(x_grid**2+y_grid**2))**2
        return function

    def shaffer_4_root(self)->[[]]:
        return [[0,1.25313]]

    def holder_function(self, x_grid, y_grid):
        function = -abs(np.sin(x_grid)*np.cos(y_grid)*np.exp(abs(1-(x_grid**2+y_grid**2)**0.5/np.pi)))
        return function

    def levi_13_function(self, x_grid, y_grid):
        function = np.sin(3*np.pi*x_grid)**2+(x_grid-1)**2*(1+np.sin(3*np.pi*y_grid)**2)+(y_grid-1)**2*(1+np.sin(2*np.pi*y_grid)**2)
        return function

    def levi_13_function_root(self)->[[]]:
        return [[1,1]]

    def ecli_function(self, x_grid, y_grid):
        function = -20*np.exp(-0.2*(0.5*(x_grid**2+y_grid**2))**0.5)-np.exp(0.5*np.cos(2*np.pi*x_grid)+np.cos(2*np.pi*y_grid))+np.e+20
        return function

    def ecli_function_root(self)->[[]]:
        return [[0,0]]

    def matias_function(self, x_grid, y_grid):
        function = 0.26*(x_grid**2+y_grid**2)-0.48*x_grid*y_grid
        return function

    def matias_function_root(self)->[[]]:
        return [[0,0]]

    def goldshein_price(self, x_grid, y_grid):
        function =(1+(x_grid+y_grid+1)**2*(19-14*x_grid+3*x_grid**2-14*y_grid+6*x_grid*y_grid+3*y_grid**2))*(30+(2*x_grid-3*y_grid)**2*(18-32*x_grid+12*x_grid**2+48*y_grid-36*x_grid*y_grid+27*y_grid**2))
        return function

    def goldshein_price_root(self)->[[]]:
        return [[0,-1]]

    def katnikov_function(self, x_grid, y_grid):
        function =0.5*(x_grid**2+y_grid**2)*(2*0.8+0.8*np.cos(x_grid*1.5)*np.cos(y_grid*3.14)+0.8*np.cos(5**0.5*x_grid)*np.cos(3.5*y_grid))
        return function


    def ellipsoid(self, x_grid, y_grid):
        a = 1
        b = 1
        c = 1
        function = ((1 - x_grid ** 2 / a ** 2 - y_grid ** 2 / b ** 2) ** c ** 2)
        return function


    def hipperboloid(self, x_grid, y_grid):
        a = 1
        b = 1
        c = 1
        function = (-(1 - x_grid ** 2 / a ** 2 - y_grid ** 2 / b ** 2) ** c ** 2)
        return function


    def parabaloid(self, x_grid, y_grid):
        a = 1
        b = 1
        function = (x_grid ** 2 / a ** 2 + y_grid ** 2 / b ** 2)
        return function


    def hyperb_paraboloid(self, x_grid, y_grid):
        a = 1
        b = 1
        c = 1
        function = (x_grid ** 2 / a ** 2 - y_grid ** 2 / b ** 2) / c
        return function


if __name__ == '__main__':
    pass
