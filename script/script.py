import argparse
from os import path, listdir
from pathlib import Path
from shutil import copyfile
import sys

default_target_path = ['Pictures', 'Wallpaper']

def home_directory():
    return Path.home()

def read_args(argv):
    parser = argparse.ArgumentParser(description='Copy lock screen wallpaper to destination directory.')
    parser.add_argument('--destination', '-d', dest='dest_directory', metavar='Destination directory', type=str, default=str(path.join(home_directory(), *default_target_path)), help='the desination, default is $HOME/Pictures/Wallpaper')
    
    return parser.parse_args(argv).dest_directory

def get_lock_screen_asset_path():
    windows_lock_screen_asset_path = ['AppData', 'Local', 'Packages', 'Microsoft.Windows.ContentDeliveryManager_cw5n1h2txyewy', 'LocalState', 'Assets']

    return path.join(home_directory(), *windows_lock_screen_asset_path)

def get_lock_screen_wallpaper_path():
    lock_screen_asset_path = get_lock_screen_asset_path()

    max_size = 0
    nearly_max_size = 0

    wallpaper_1_path = ''
    wallpaper_2_path = ''

    for f in listdir(lock_screen_asset_path):
        f_path = path.join(lock_screen_asset_path, f)
        size = path.getsize(f_path)

        if size >= max_size:
            nearly_max_size = max_size
            wallpaper_2_path = wallpaper_1_path
            max_size = size
            wallpaper_1_path = f_path
        elif size >= nearly_max_size:
            nearly_max_size = size
            wallpaper_2_path = f_path

    return (wallpaper_1_path, wallpaper_2_path)

def copy_file_to_dest_directory(file_path, dest_directory):
    copyfile(file_path, path.join(dest_directory, Path(file_path).name + '.jpg'))

def main():
    dest_directory = read_args(sys.argv[1:])
    wallpaper_1_path, wallpaper_2_path = get_lock_screen_wallpaper_path()
    copy_file_to_dest_directory(wallpaper_1_path, dest_directory)
    copy_file_to_dest_directory(wallpaper_2_path, dest_directory)
    
if __name__ == '__main__':
    main()
