import numpy as np
import matplotlib.pyplot as plt


class DataLoader:
    def __init__(self):
        self.info="Data loader"

        self.states=[]
        self.inputs=[]
        self.refs=[]

    def add_data(self,x=[],u=[],ref=[]):
        if len(x)!=0:
            self.states.append(x)
        if len(u)!=0:
            self.inputs.append(u)
        if len(ref)!=0:
            self.refs.append(ref)

    
    def vis(self,poses=False,vels=False,angles=False,rates=False,refs=False,inputs=False):
        self.states=np.array(self.states)
        self.inputs=np.array(self.inputs)
        self.refs=np.array(self.refs)

        if poses==True:
            plt.plot(self.states[:,0],label='px')
            plt.plot(self.states[:,1],label='py')
            plt.plot(self.states[:,2],label='pz')

            if refs==True:
                plt.plot(self.refs[:,0],label='px_ref')
                plt.plot(self.refs[:,1],label='py_ref')
                plt.plot(self.refs[:,1],label='pz_ref')

            plt.legend()
            plt.xlabel('time')
            plt.ylabel('position(m)')
            plt.show()

        plt.cla()
        if vels==True:
            plt.plot(self.states[:,3],label='vx')
            plt.plot(self.states[:,4],label='vy')
            plt.plot(self.states[:,5],label='vz')

            if refs==True:
                plt.plot(self.refs[:,3],label='vx_ref')
                plt.plot(self.refs[:,4],label='vy_ref')
                plt.plot(self.refs[:,5],label='vz_ref')

            plt.legend()
            plt.xlabel('time')
            plt.ylabel('velocity(m/s)')
            plt.show()
    

        plt.cla()
        if angles==True:
            plt.plot(self.states[:,6],label='phi')
            plt.plot(self.states[:,7],label='theta')
            plt.plot(self.states[:,8],label='psi')

            if refs==True:
                plt.plot(self.refs[:,6],label='phi_ref')
                plt.plot(self.refs[:,7],label='theta_ref')
                plt.plot(self.refs[:,8],label='psi_ref')

            plt.legend()
            plt.xlabel('time')
            plt.ylabel('angle(radian)')
            plt.show()

        plt.cla()
        if rates==True:
            plt.plot(self.states[:,9],label='p')
            plt.plot(self.states[:,10],label='q')
            plt.plot(self.states[:,11],label='r')

            if refs==True:
                plt.plot(self.refs[:,9],label='p_ref')
                plt.plot(self.refs[:,10],label='q_ref')
                plt.plot(self.refs[:,11],label='r_ref')

            plt.legend()
            plt.xlabel('time')
            plt.ylabel('rates(rad/s)')
            plt.show()

        plt.cla()
        if inputs==True:
            plt.plot(self.inputs[:,0],label='u1')
            plt.plot(self.inputs[:,1],label='u2')
            plt.plot(self.inputs[:,2],label='u3')
            plt.plot(self.inputs[:,3],label='u4')

            plt.legend()
            plt.xlabel('time')
            plt.ylabel('inputs')
            plt.show()


