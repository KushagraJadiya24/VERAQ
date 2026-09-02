import torch
# x=torch.tensor([1.0,2.0,4.0,5.0])
# print(x,x.shape,x.dtype)

# # numpy <-> tensor
# import numpy as np
# a = np.array([1.0, 2.0, 3.0])
# print(a)
# t = torch.from_numpy(a)
# print(t)
# back = t.numpy()
# print(back)

# device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
# x = x.to(device)
# print(x.device)

w = torch.tensor(2.0, requires_grad=True)
b = torch.tensor(1.0, requires_grad=True)

y = w * 3 + b        # y = 3w + b
y.backward()          # compute dy/dw and dy/db

print(w.grad)   # tensor(3.)   -> dy/dw = 3
print(b.grad)   # tensor(1.)   -> dy/db = 1