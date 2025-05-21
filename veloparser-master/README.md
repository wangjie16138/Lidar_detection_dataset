### Veloparser

Veloparser is a simple application which does following:

- Supports just Velodyne VLP16 at the moment.
- Takes a pcap file recorded by Velodyne lidar as input.
- Extracts all Frames from the pcap file.
- Saves both data-frames and position-frames.
- __Data frames__ are saved as __Point Clouds (.pcd)__ and/or as __plain Text-File__. 
- __Position frames__ are saved only as __Text-File__
- Converts frame's timestamps to GPS Week of Second format for synchronization with IMU/GNSS devices
- Can be parameterizes by yaml file.

The reason why i wrote it, is simply that i could not find any simple way without installing ROS (Robot operating software)
or other huge c++-based lib that does 'just' extract the point clouds and GPS-Timestamps from pcap-file.

##### Usage

Assuming using Anaconda python distribution:
```bash
~$ cd \path-to-veloparser-repo\
~/veloparser$ conda env create -f environment.yml
~/veloparser$ conda activate veloparser
~/veloparser$ python main.py -p /home/user/my.pcap -o /home/user/output_folder -c params.yaml
python main.py -p /Users/xiaohe/labelCloud/2025-05-20-17-13-58_Velodyne-VLP-16-Data.pcap -o /Users/xiaohe/Downloads/veloparser-master/output -c params.yaml
```
Note, the `params.yaml` can be updated according to your setup.  For example, specifying whether GPS was available.
	
##### Dependencies
Veloparser has following package dependencies:
- dpkt
- numpy
- tqdm
- yaml

Please make sure that all of those packages are installed (pip or conda).

##### Output
Below a sample out of 2 Points in a __point cloud file__

``
Time [musec], X [m], Y [m], Z [m], ID, Intensity, Latitude [Deg], Longitudes [Deg], Distance [m]
2795827803, 0.032293, 5.781942, -1.549291, 0, 6, 0.320, -15.000, 5.986
2795827806, 0.083565, 14.399564, 0.251350, 1, 6, 0.333, 1.000, 14.402
``

All __Point Cloud__ PCD-Files have following fields:
1) X-Coordinate
2) Y-Coordinate
3) Z-Coordinate
4) Intensity

They can also be opened and visualized with any point-cloud rendering software like (open3d, pcl, ...)
