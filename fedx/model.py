import torch
import torch.nn as nn

torch.manual_seed(0)

X = torch.linspace(-10, 10, 100).unsqueeze(1)   # shape (100, 1)
y = 2 * X                                         # y = 2x

class TinyNet(nn.Module):
    def __init__(self):
        super().__init__()
        self.fc1 = nn.Linear(1, 8)
        self.fc2 = nn.Linear(8, 8)
        self.fc3 = nn.Linear(8, 1)

    def forward(self, x):
        x = torch.relu(self.fc1(x))
        x = torch.relu(self.fc2(x))
        x = self.fc3(x)
        return x

model = TinyNet()

loss_fn = nn.MSELoss()
optimizer = torch.optim.SGD(model.parameters(), lr=0.001)

epochs = 200

for epoch in range(epochs):
    preds = model(X)                # forward pass
    loss = loss_fn(preds, y)        # compute loss
    loss.backward()                 # backprop
    optimizer.step()                # update weights
    optimizer.zero_grad()           # clear gradients for next iteration

    if epoch % 20 == 0:
        print(f"epoch {epoch:3d}  loss {loss.item():.4f}")