import os
import sys
from shutil import copyfile

os.system("find . -name '.DS_Store' -exec rm -rf {} \;")

artworks = "/Volumes/2t/Images/Artist/"
base_dir = sys.argv[1]
for artist in os.listdir(base_dir):
    artist_dir = f"{base_dir}/{artist}"
    if os.path.isfile(artist_dir):
        continue
    for alb in os.listdir(artist_dir):
        if not os.path.isfile(alb):
            album = f"{artist_dir}/{alb}"
            if os.path.isfile(album):
                continue
            numbered_right = False
            for track in os.listdir(album):
                if track.endswith("flac") or track.endswith("dsf"):
                    if track.startswith("01 ") or track.startswith("1-01 "):
                        numbered_right = True
                        break
            if not numbered_right:
                print(album)
