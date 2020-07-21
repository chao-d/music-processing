import os
import shutil


os.system("find . -name '.DS_Store' -exec rm -rf {} \;")

for artist in os.listdir("./"):
    artist_dir = f"./{artist}"
    if os.path.isfile(artist_dir):
        continue
    for alb in os.listdir(artist_dir):
        alb_dir = f"{artist_dir}/{alb}"
        if os.path.isfile(alb_dir):
            if alb == '.DS_Store':
                os.remove(alb_dir)
            continue
        for vol in os.listdir(alb_dir):
            vol_dir = f"{alb_dir}/{vol}"
            if os.path.isdir(vol_dir):
                for music_file in os.listdir(vol_dir):
                    file_path = f"{vol_dir}/{music_file}"
                    if os.path.isdir(file_path):
                        print("error when checking file_path")
                    shutil.move(file_path, alb_dir)
                os.rmdir(vol_dir)
        shutil.move(alb_dir, "./")
    try:
        os.rmdir(artist_dir)
    except Exception:
        print("error when removing artist directory")
        for ds in os.listdir(artist_dir):
            if ds == '.DS_Store':
                os.remove(f"{artist_dir}/{ds}")
        os.rmdir(artist_dir)
