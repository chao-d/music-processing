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
            first_album = f"{artist_dir}/{alb}"
            if os.path.isfile(first_album):
                continue
            for cover in os.listdir(first_album):
                if cover.startswith("cover") and (cover.endswith("jpg") or
                    cover.endswith("jpeg") or cover.endswith("png")):
                    extension = cover[cover.find(".")+1:]
                    copyfile(f"{first_album}/{cover}", f"{artist_dir}/{artist}.{extension}")
            break
