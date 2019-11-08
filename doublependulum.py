import numpy as np
import scipy
import matplotlib.pyplot as plt


def deriv(vars,t,l1=1.,l2=1.,m1=1.,m2=1.,g=9.8):
    
    (theta1,theta2,omega1,omega2)=vars
    theta1dot = omega1
    theta2dot = omega2
    
 
    s1=np.sin(theta1)
    s2=np.sin(theta2)
    cd=np.cos(theta1-theta2)
    sd=np.sin(theta1-theta2)
    
  
    l1=1.*l1
    m1=1.*m1
    
    num1=-(l2/l1)*omega2**2*sd-g*(1+m1/m2)*s1 #equations of motion obtained by solving the lagrangian
    num2=(l1/l2)*omega1**2*sd-g*s2
    
    den=1.+m1/m2-cd**2
    
    omega1dot =(num1-(l2/l1)*cd*num2)/den
    omega2dot =((1+m1/m2)*num2-(l1/l2)*cd*num1)/den
    
    return np.array([theta1dot,theta2dot,omega1dot,omega2dot])


def doublependulumenergy(theta1,theta2,omega1,omega2,l1,l2,m1,m2,g):
    """ Returns the energy of a double pendulum """
    c1=np.cos(theta1)
    c2=np.cos(theta2)
    s1=np.sin(theta1)
    s2=np.sin(theta2)
    kin=(1/2)*m1*(l1*omega1)**2+(1/2)*m2*(l1*omega1*c1+l2*omega2*c2)**2+(1/2)*m2*(l1*omega1*s1+l2*omega2*s2)**2
    pot=-m1*g*l1*c1-m2*g*(l1*c1+l2*c2)
    return kin+pot


def doublependulumsolve(initial_theta1=0,initial_theta2=0,initial_omega1=0,initial_omega2=0,timestep=0.1,numstep=500,l1=1,l2=1,m1=1,m2=1,g=1):
    """ Runs ODEint for the double pendulum 
    
    sample usage:
    DoublePendulumTrajectory(initial_theta1=0.1,l1=2,l2=2,m1=1,m2=2,g=9.8)
    
    Returns a dictionary which has the following keys:
    "times", "theta1", "theta2", "omega1", "omega2", "parameters"
    
    The values associated with the first five keys are a time series.
    The parameters key returns a dictionary which stores the parameters, plus the energy of the system
    """
    
    p={"l1":l1,"l2":l2,"m1":m1,"m2":m2,"g":g}
    
    # Create a tuple containing (l1,l2,m1,m2,g)
    par=(l1,l2,m1,m2,g)        # Converts parameters to a tuple in the right order
    
    # Create a tuple containing the inital values
    initial=(initial_theta1,initial_theta2,initial_omega1,initial_omega2)
    
    # Create the list of times
    timevals=np.arange(numstep)*timestep
    
    #odeint solver
    
    sol = scipy.integrate.odeint(deriv,initial,timevals,par)
    
    # Store the results of odeint in a dictionary
    data={}
    data["times"]=tvals
    data["theta1"]=sol[:,0]
    data["theta2"]=sol[:,1]
    data["omega1"]=sol[:,2]
    data["omega2"]=sol[:,3]
    p["energy"]=doublependulumenergy(theta1=sol[0,0],theta2=sol[0,0],omega1=sol[0,0],omega2=sol[0,0],**p)
    data["parameters"]=p
    
    # Return the dictionary
    return data


def showtrajectory(data):
    "pass the data dictionary obtained as a result of solving the EOM. This function plots the trajectory of the motion"
    
    param = data["parameters"]
    l1=parameters["l1"]
    l2=parameters["l2"]
    theta1=data["theta1"]
    theta2=data["theta2"]
    x1=l1*np.sin(theta1)
    y1=-l1*np.cos(theta1)
    x2=l2*np.sin(theta2)+x1
    y2=l2*np.sin(theta2)+y1
    plt.scatter((0,),(0,))
    plt.plot(x1,y1,'g',x2,y2,'r')
    plt.show()
    return


def timeseries(data):
    "returns the time freeze of the double pendulum motion. call it with the data dictionary obtained"
    
    l1=parameters["l1"]
    l2=parameters["l2"]
    theta1=data["theta1"]
    theta2=data["theta2"]
    x1=l1*np.sin(theta1)
    y1=-l1*np.cos(theta1)
    x2=l2*np.sin(theta2)+x1
    y2=l2*np.sin(theta2)+y1
    t=data["times"]
    plt.plot(t,x1,'g+',t,y1,'g-',t,x2,'r+',t,y2,'r-')
    plt.show()
    return    


def ShowDoublePendulumPoincare(data,offset=50):
    """ Call with a dictionary containing 
    "times", "theta1", "theta2", "omega1", "omega2","parameters".
    
    Generates a Poincare section:
    plots omega2 vs theta2 when theta1=0 and omega1>0.
    """
    
    #unpack data
    parameters=data["parameters"]
    l1=parameters["l1"]
    l2=parameters["l2"]
    theta1=data["theta1"]
    theta2=data["theta2"]
    omega1=data["omega1"]
    omega2=data["omega2"]
    x1=l1*np.sin(theta1)
    y1=-l1*np.cos(theta1)
    x2=l2*np.sin(theta2)+x1
    y2=l2*np.sin(theta2)+y1
    t=data["times"]
    
    for i,the2 in enumerate(theta2):
        while (theta1[i] > -np.pi) & (omega1[i] > 0):
            the2 = the2 - (2.0*np.pi)
        while (theta1[i] < -np.pi) & (omega1[i] > 0):
            the2 = the2 + (2.0*np.pi)
            
    plt.plot(theta2,omega2,"r,")
        
    
            