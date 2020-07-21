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
            found = False
            for cover in os.listdir(album):
                if cover.startswith("cover") and (cover.endswith("jpg") or
                    cover.endswith("jpeg") or cover.endswith("png")):
                    found = True
            if not found:
                print(album)
