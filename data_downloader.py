import os
import argparse
import urllib.request
import shutil
import yaml
import time

"""
Utility script to assist in downloading a dataset
"""

LOG_DOWNLOAD_ROOT = "http://data.csail.mit.edu/rlg_manipulation/pdccompressed/logs_proto"

def download_single_episode(name, # str: episode name
                            destination_dir, # where to save the episode
                            extract=True, # whether or not to extract the compressed file
                            cleanup=True, # delete .zip file afterward
                            log_download_root=None,
                            overwrite=False,
                            ):
    """
    Downloads a single episode from the webserver to the specified destination_dir
    """

    print("\n\n----- Processing episode %s ---------" % (name))
    if log_download_root is None:
        log_download_root = LOG_DOWNLOAD_ROOT

    dest_file = os.path.join(destination_dir, '%s.tar.gz' % (name))
    dest_folder = os.path.join(destination_dir, name)

    try:

        if overwrite:
            try:
                os.remove(dest_file)
            except IOError:
                pass

            try:
                shutil.rmtree(dest_folder)
            except IOError:
                pass


        if not os.path.isdir(dest_folder):
            if not os.path.exists(dest_file):
                print("Downloading episode")
                start_time = time.time()
                url = log_download_root + "/%s.tar.gz" % (name)

                # Download the file from `url` and save it locally under `file_name`:
                with urllib.request.urlopen(url) as response, open(dest_file, 'wb') as out_file:
                    shutil.copyfileobj(response, out_file)

                print("Downloading took %.2f seconds" % (time.time() - start_time))

            else:
                print("Episode already downloaded" % (name))

            print("Extracting episode to %s" %(destination_dir))
            shutil.unpack_archive(dest_file, destination_dir)
        else:
            print("Episode already extracted")

        # remove dest_file
        if cleanup:
            try:
                os.remove(dest_file)
            except IOError:
                pass

    except KeyboardInterrupt:
        # cleanup files if we had a KeyboardInterrup
        try:
            os.remove(dest_file)
        except IOError:
            pass

        try:
            shutil.rmtree(dest_folder)
        except IOError:
            pass



def test_download_single_episode():
    dest_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data')
    if not os.path.isdir(dest_dir):
        os.makedirs(dest_dir)

    name = "2018-04-07-20-22-05"
    download_single_episode(name, dest_dir)


if __name__ == "__main__":


    parser = argparse.ArgumentParser()
    parser.add_argument("--config_file",
                        help="Full path to yaml file containing list of episodes (e.g. config/all_episodes.yaml)",
                        required=True)

    parser.add_argument("--dest",
                        help="(optional) full path to destination dir",
                        required=False,
                        default=os.path.join(os.path.dirname(os.path.abspath(__file__)), 'data'))

    parser.add_argument("--overwrite",
                        help="(optional) whether or not to overwrite existing logs",
                        action='store_true',
                        default=False,
                        required=False)

    args = parser.parse_args()

    project_root = os.path.dirname(os.path.abspath(__file__))
    config_file = os.path.join(project_root, args.config_file)
    config = yaml.safe_load(open(config_file, 'r'))

    for episode_name in config['episodes']:
        download_single_episode(episode_name,
                                destination_dir=args.dest,
                                extract=True,
                                cleanup=True,
                                overwrite=args.overwrite
                                )


