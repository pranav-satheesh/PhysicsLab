def euler(y,t,dt,derivs):
    y_next = y + derivs(y,t)*dt
    return y_next



def rk2(y,time,dt,derivs):
    
    k0 = dt*derivs(y,time)
    k1 = dt*derivs(y+k0,time+dt)
    
    y_next = y+ 0.5*(k0+k1)
    
    return y_next


def rk4(y,time,dt,derivs):
    k1 = dt*derivs(y,time)
    k2 = dt*derivs(y+k1/2,time + dt/2)
    k3 = dt*derivs(y+k2/2,time + dt/2)
    k4 = dt*derivs(y+k3,time + dt)
    
    y_next = y + (1.0/6)*(k1+2*k2+2*k3+k4)
    
    return y_next

    
    