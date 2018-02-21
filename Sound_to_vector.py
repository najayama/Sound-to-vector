###全体の流れは以下の通り
#１．設定ファイルの読み込み
#２．変換すべきファイルのリストの取得
#３．リストのそれぞれのファイルについて、
#    {
#    音声ファイルを区切る
#    フーリエ変換
#    結果の書き出し
#    }


import config_files.read_config as read_config

#設定ファイルの読み込み。
config_dict = read_config.read_config()

devide_interval = config_dict["DEVIDE_INTERVAL"]
output_dir = config_dict["OUTPUT_DIR"]
input_dir = config_dict["INPUT_DIR"]


#INPUT_DIR 直下の音声ファイルのリストを作成。
#音声ファイルを区切る
#フーリエ変換
#結果の書き出し



