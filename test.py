from LinearModel import LinearModel
from DataLoader import DataLoader
import numpy as np

model=LinearModel()
loader=DataLoader()

for i in range(100):
    u=np.zeros((4,1))
    x=model.update(u=u)
    loader.add_data(x=x,u=u,ref=np.zeros((12,1)))

    


loader.vis(refs=True,vels=True,poses=True,angles=True,rates=True,inputs=True)
