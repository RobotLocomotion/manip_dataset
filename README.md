# Robot Locomotion Group Manipulation Dataset
This repo contains instructions on how to download the datasets used in the following papers.

- [DenseObjectNets](https://github.com/RobotLocomotion/pytorch-dense-correspondence)
- [kPAM](https://sites.google.com/view/kpam)


## Downloading Specific Episodes

An episode (also known as a scene) consists of many images for which relative camera poses are known. See [here](https://github.com/RobotLocomotion/pytorch-dense-correspondence/blob/master/doc/data_organization.md) for more information. A list of episodes can be found in [config/all_episode.yaml](config/all_episodes.yaml). Downloading a list of episodes specified in a `yaml` file can be accomplished by running

```angular2
python3 data_downloader.py --config_file <full_path_to_config> --dest <full_path_to_dest_dir>  
```

This will download the episodes the specified destination directory. For example to download the entire dataset use

```angular2
python3 data_downloader.py --config_file "config/all_episodes.yaml"
```

The config files [`config/kpam_mugs.yaml`](config/kpam_mugs.yaml) and [`config/kpam_shoes.yaml`](config/kpam_shoes.yaml) contain the episodes used for shoes and mugs repsectively in the kPAM paper.


## kPAM Keypoint Annotations
Can be downloaded using [this](http://data.csail.mit.edu/rlg_manipulation/kpam_annotations.zip) link.