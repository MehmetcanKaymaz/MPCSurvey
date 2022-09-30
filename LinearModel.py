import numpy as np
from ModelLoader import ModelParameters 

class LinearModel:
    def __init__(self,x_init=np.zeros((12,1)),dt=0.001,N=1):
        self.info="Linear Quadcopter Dynamic Model"
        
        self.parameters=ModelParameters()#quadcopter model parameters

        self.N=N#number of iteration to evaluate model for given input
        self.dt=dt#step size for numeric integration
        self.x=x_init#initial states

        # State-space model: x(k+1)=Ax(k)+Bu(k)
        self.A=np.eye(12)+self.parameters.A*self.dt
        self.B=self.parameters.B*self.dt

    def update(self,u):
        #evaluation of dynamic model N times for given 'u'
        for i in range(self.N):
            self.x=self.__update_state(self.x,u)#update states 1 time for given u

        return self.x
    
    def __update_state(self,x,u):
        return self.A@x+self.B@u


