import numpy as np
import matplotlib.pyplot as plt

class Charge:
    """a charge object defined by its position and
    charge"""
    def __init__(self, xpos=None, ypos=None,
                 charge=None):
        self.xpos = xpos
        self.ypos = ypos
        self.charge = charge

Charge1 = Charge(xpos= 0.05, ypos=0, charge=1)
Charge2 = Charge(xpos=-0.05, ypos=0, charge=1)

def potential(charge, radius):
    """Function declaration for potention definined by charge and radius"""
    e_knot=8.85418782*10**-12
    return charge/(4*np.pi*e_knot*radius)

def partial_x(x,y, h=.001):
    """Function to evaluate the partial x derivative of the function"""
    return (f(x+h),y)-f(x-h,y)/2*h

def partial_y(x,y,h=.001):
    """Function to evaluate the partial Y derivative of the function"""
    return(f(x,y+h) - f(x, y-h))/2*h

def radial_distance(x1,y1,x2,y2):
    """Function for computing distance between the two points """
    return np.sqrt((x1-x2)**2 +(y1-y2)**2)

def point_charge(x,y):
    e_knot=8.85418782*10**-12
    return (1/(4*np.pi*e_knot*(radial_distance(x,y,Charge1.xpos,Charge1.ypos))))+(1/(4*np.pi*e_knot*(radial_distance(x,y,Charge2.xpos,Charge2.ypos))))



if __name__ == "__main__":
    #generate x,y values
    spacing = 0.01 #<--spacing 0.01 m = 1 cm
    x_range = np.arange(-0.5, 0.5, spacing)
    y_range = np.arange(-0.5, 0.5, spacing)
    xs, ys  = np.meshgrid(x_range, y_range)
    potential_val = point_charge(x_range,y_range)
    Z = potential_val
    print(Z)

plt.contour([x_range,y_range], Z ,levels=[1e+10,1e+11,2.5e+11,3.5e+11], colors=['#808080', '#A0A0A0', '#C0C0C0'])
plt.show()
    

  
