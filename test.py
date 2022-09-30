from LinearModel import LinearModel
import numpy as np

model=LinearModel()

for i in range(100):
    x=model.update(u=np.zeros((4,1)))

print(x)
