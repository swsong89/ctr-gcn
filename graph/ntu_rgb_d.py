import sys
import numpy as np

sys.path.extend(['../'])
from graph import tools # s如果需要生成效果图的话需要把这个注释调

num_node = 25
self_link = [(i, i) for i in range(num_node)]
inward_ori_index = [(1, 2), (2, 21), (3, 21), (4, 3), (5, 21), (6, 5), (7, 6),
                    (8, 7), (9, 21), (10, 9), (11, 10), (12, 11), (13, 1),
                    (14, 13), (15, 14), (16, 15), (17, 1), (18, 17), (19, 18),
                    (20, 19), (22, 23), (23, 8), (24, 25), (25, 12)]
inward = [(i - 1, j - 1) for (i, j) in inward_ori_index]
outward = [(j, i) for (i, j) in inward]
neighbor = inward + outward

class Graph:
    def __init__(self, labeling_mode='spatial'):
        self.num_node = num_node
        self.self_link = self_link
        self.inward = inward
        self.outward = outward
        self.neighbor = neighbor
        self.A = self.get_adjacency_matrix(labeling_mode)

    def get_adjacency_matrix(self, labeling_mode=None):
        if labeling_mode is None:
            return self.A
        if labeling_mode == 'spatial':
            A = tools.get_spatial_graph(num_node, self_link, inward, outward)  # 本身。入度不需要标准化，出度需要标准化权重
        else:
            raise ValueError()
        return A

if __name__ == '__main__':
    import tools
    g = Graph().A
    import matplotlib.pyplot as plt
    # for i, g_ in enumerate(g):
    plt.imshow(g[0], cmap='gray')
    cb = plt.colorbar()
    plt.savefig('./graph_identidy.png')
    cb.remove()
    # plt.show()

    plt.imshow(g[1], cmap='gray')
    cb = plt.colorbar()
    plt.savefig('./graph_inward.png')
    cb.remove()
    # plt.show()

    plt.imshow(g[2], cmap='gray')
    cb = plt.colorbar()
    plt.savefig('./graph_outward.png')
    cb.remove()
    # plt.show()

    plt.imshow(np.sum(g,0), cmap='gray')
    cb = plt.colorbar()
    plt.savefig('./graph_all.png')
    cb.remove()
    # plt.show()