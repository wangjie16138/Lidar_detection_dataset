from pypcd import pypcd
import os
import argparse
import numpy as np

def parse_config():
    parser = argparse.ArgumentParser(description = "convert pcd to bin with intensity")
    parser.add_argument("--pcd_file_path", help="pcd file path or dir", type=str, default='/Users/xiaohe/Downloads/veloparser-master/output/velodynevlp16/data_pcl')
    parser.add_argument("--bin_file_path", help="bin file path or dir", type=str, default='/Users/xiaohe/Downloads/veloparser-master/output_bin/')
    return parser.parse_args()

def save_bin_file(pcd_file_path, save_bin_path):
    if not os.path.exists(save_bin_path):
        os.makedirs(save_bin_path)
        print("创建输出目录：" + save_bin_path)

    for root, _, files in os.walk(pcd_file_path):
        for filename in files:
            if not filename.endswith(".pcd"):
                continue

            pcd_file = os.path.join(root, filename)
            pc = pypcd.PointCloud.from_path(pcd_file)

            x = pc.pc_data['x']
            y = pc.pc_data['y']
            z = pc.pc_data['z']
            if 'intensity' in pc.pc_data.dtype.names:
                intensity = pc.pc_data['intensity']
            else:
                intensity = np.zeros_like(x)

            points = np.stack((x, y, z, intensity), axis=-1).astype(np.float32)

            bin_file_name = os.path.join(save_bin_path, filename.replace('.pcd', '.bin'))
            print(f"{pcd_file} -> {bin_file_name}")
            points.tofile(bin_file_name)

def main():
    args = parse_config()
    save_bin_file(args.pcd_file_path, args.bin_file_path)

if __name__ == "__main__":
    main()