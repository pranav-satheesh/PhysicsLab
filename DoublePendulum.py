# <nbformat>2</nbformat>
# <markdowncell>
#
#  DoublePendulum.py
#  
#
#  Created by Mueller on 8/25/08.
# 
# <codecell>
import numpy
import scipy, scipy.integrate, scipy.optimize
import pylab

# <codecell>
def DoublePendulumDerivArray(vars,t,l1=1.,l2=1.,m1=1.,m2=1.,g=1.):
    """ variables are (theta1,theta2,omega1,omega2)
    parameters are the following: l1,l2,m1,m2,g
    if any are unspecified, they are taken to be equal to 1.
    
    returns array([dt_theta1,dt_theta2,dt_omega1,dt_omega2])
    
    Sample usage:
    DoublePendulumDerivArray((1,0,0,0),0,l1=2,l2=2,m1=1,m2=2,g=9.8)
    """
    (theta1,theta2,omega1,omega2)=vars        # Unpacks the variables
    dt_theta1=omega1
    dt_theta2=omega2
    s1=numpy.sin(theta1)
    s2=numpy.sin(theta2)
    cd=numpy.cos(theta1-theta2)
    sd=numpy.sin(theta1-theta2)
    #insurance against integer division
    l1=1.*l1
    m1=1.*m1
    num1=-(l2/l1)*omega2**2*sd-g*(1+m1/m2)*s1
    num2=(l1/l2)*omega1**2*sd-g*s2
    den=1.+m1/m2-cd**2
    dt_omega1=(num1-(l2/l1)*cd*num2)/den
    dt_omega2=((1+m1/m2)*num2-(l1/l2)*cd*num1)/den
    return numpy.array([dt_theta1,dt_theta2,dt_omega1,dt_omega2])

# <codecell>    
def doublependulumenergy(theta1,theta2,omega1,omega2,l1,l2,m1,m2,g):
    """ Returns the energy of a double pendulum """
    c1=numpy.cos(theta1)
    c2=numpy.cos(theta2)
    s1=numpy.sin(theta1)
    s2=numpy.sin(theta2)
    kin=(1/2)*m1*(l1*omega1)**2+(1/2)*m2*(l1*omega1*c1+l2*omega2*c2)**2+(1/2)*m2*(l1*omega1*s1+l2*omega2*s2)**2
    pot=-m1*g*l1*c1-m2*g*(l1*c1+l2*c2)
    return kin+pot

# <codecell>
def DoublePendulumTrajectory(initial_theta1=0,initial_theta2=0,initial_omega1=0,initial_omega2=0,
    timestep=0.1,numstep=500,l1=1,l2=1,m1=1,m2=1,g=1) :
    """ Runs ODEint for the double pendulum 
    
    sample usage:
    DoublePendulumTrajectory(initial_theta1=0.1,l1=2,l2=2,m1=1,m2=2,g=9.8)
    
    Returns a dictionary which has the following keys:
    "times", "theta1", "theta2", "omega1", "omega2", "parameters"
    
    The values associated with the first five keys are a time series.
    The parameters key returns a dictionary which stores the parameters, plus the energy of the system
    """
    # Create a tuple containing (l1,l2,m1,m2,g)
    pass
    # Create a tuple containing the inital values
    pass
    # Create the list of times
    pass
    # Run odeint
    pass
    # Store the results of odeint in a dictionary
    pass
    # Return the dictionary
    pass
    

# <codecell>    
def ShowDoublePendulumTrajectory(data):
    """ Call with a dictionary containing 
    "times", "theta1", "theta2", "omega1", "omega2","parameters"
    
    Will plot the x-y trajectory of the two pendulum bobs
    """
    pass
    
# <codecell>
def ShowDoublePendulumTimeSeries(data):
    """ Call with a dictionary containing 
    "times", "theta1", "theta2", "omega1", "omega2","parameters"
    
    Will plot x1,y1,x2,y2 as a function of time
    """
    pass
    

# <codecell>
def ShowDoublePendulumPoincare(data):
    """ Call with a dictionary containing 
    "times", "theta1", "theta2", "omega1", "omega2","parameters".
    
    Generates a Poincare section:
    plots omega2 vs theta2 when theta1=0 and omega1>0.
    """
    #unpack data
    pass
    #bracket times where theta1 passes through n*2pi for some n, and with omega1>0
    pass
    #interpolate between these bracketed times to find theta2 and omega2 at those times.
    pass
    #make a scatter plot
    pass
    
# <codecell>
def lininterp(xvals,yvals):
    """ xvals and yvals are tuples of length 2:
    taking (x0,y0) and (x1,y1) to be points defining a line
    finds the value of y when x=0"""
    pass
    


# <markdowncell>
# Copyright (C) Cornell University
# All rights reserved.
# Apache License, Version 2.0


