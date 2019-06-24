import argparse
import numpy as np

def get_args():
    parser = argparse.ArgumentParser()

    parser.add_argument("--images_dir", type=str)
    parser.add_argument("--mats_dir", type=str)
    parser.add_argument("--lands_dir", type=str)
    parser.add_argument("--transform", action="store_true")

    parser.add_argument("--resume", action="store_true")
    parser.add_argument("--start_epoch", type=int, default=0)

    parser.add_argument("--test_img", type=str)

    parser.add_argument("--checkpoint", type=str, help="path to saved model")

    return parser.parse_args()


def gaussian_distribution(center_x, center_y, size=400):
    img = np.zeros((size, size))
    for i in range(center_x - 10, center_x + 10):
        for j in range(center_y - 10, center_y + 10):
            exp_fact = ((i - center_x) ** 2) / 2 + ((j - center_y) ** 2) / 2
            img[i, size - 1 - j] = 1 / np.sqrt(2 * np.pi) * np.exp(-exp_fact)

    img /= np.sum(img)
    return img


def to_cuda(data, use_cuda):
    input_ = data.float()
    if use_cuda:
        input_ = input_.cuda()
    return input_


def num_flat_features(x):
    return np.product(x.size()[1:])


def get_coords(out, sz=0.25, thr=0.3):
    mat = np.sum(out >= thr, axis=0)

    pts = np.argwhere(mat >= thr)

    x, y = pts[:, 0], pts[:, 1]
    z = sz * mat[mat > 0].reshape(-1, )
    assert len(x) == len(y) == len(z)

    return x, y, z