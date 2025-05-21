import numpy as np

# 替换为你的 bin 文件路径
bin_path = '/Users/xiaohe/Downloads/veloparser-master/output_bin/0_frame_205316.289254.bin'

# 每个点通常由 4 个 float32 构成：x, y, z, intensity（KITTI 格式）
point_cloud = np.fromfile(bin_path, dtype=np.float32)

# 计算点数
point_cloud = point_cloud.reshape(-1, 4)

print("点云形状（N x dim）：", point_cloud.shape)
print("前几个点：\n", point_cloud[:20000])