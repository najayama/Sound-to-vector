import os

#設定ファイルの読み込み。

os.chdir("config_files")

with open("config_files/") as config_file:
    LINE = config_file.read()
    while LINE:
        if LINE[0:14] == "DEVIDE_INTERVAL":
            DEVIDE_INTERVAL = float()
    
    
os.chdir("..")
    
    
