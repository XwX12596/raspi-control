import numpy as np
import torch


def test12(input):
    cl_net = torch.load('/home/xmh/raspi-control/classifier/model_12.pth')

    data_real = np.array(input)
    data_real = torch.from_numpy(data_real).to(torch.float32)

    x_real, y_real = cl_net(data_real)
    return int(x_real.item()), int(y_real.item())
    print('output', int(x_real.item()), int(y_real.item()))
