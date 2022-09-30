import json
import numpy as np


class ModelParameters:
    def __init__(self):
        self.info="Quadcopter Model Parameters"

        self.f=open('model.json')
        self.json_data=json.load(self.f)

        self.m=self.json_data["m"]
        self.g=self.json_data["g"]
        self.Ix=self.json_data["Ix"]
        self.Iy=self.json_data["Iy"]
        self.Iz=self.json_data["Iz"]

        self.A,self.B=self.__state_space()

    
    def __state_space(self):
        A=np.array([[0,0,0,1,0,0,0,0,0,0,0,0],
                    [0,0,0,0,1,0,0,0,0,0,0,0],
                    [0,0,0,0,0,1,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,-self.g,0,0,0,0],
                    [0,0,0,0,0,0,self.g,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,1,0,0],
                    [0,0,0,0,0,0,0,0,0,0,1,0],
                    [0,0,0,0,0,0,0,0,0,0,0,1],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0],
                    [0,0,0,0,0,0,0,0,0,0,0,0]                         
                ])
        
        B=np.array([[0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [1/self.m,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,0,0,0],
                    [0,1/self.Ix,0,0],
                    [0,0,1/self.Iy,0],
                    [0,0,0,1/self.Iz],
                ])
        
        return A,B

