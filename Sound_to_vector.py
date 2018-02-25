###全体の流れは以下の通り
#０．あとで使う関数の定義
#１．設定ファイルの読み込み
#２．変換すべきファイルのリストの取得
#３．リストのそれぞれのファイルについて、
#    {
#    音声ファイルをロード
#    フーリエ変換
#    結果の書き出し
#    }

import os
import csv
import wave
import numpy as np
import scipy.fftpack
import config_files.read_config as read_config

#０．あとで使う関数の定義
def load_wave(wf, devide_interval):
    #秒をフレームに換算
    frame = wf.getframerate() * devide_interval
    data = wf.getnframes(frame)
    
    ######kokokara
    if wf.getnchannels() == 2:


#設定ファイルの読み込み。
config_dict = read_config.read_config()

devide_interval = config_dict["DEVIDE_INTERVAL"]
output_dir = config_dict["OUTPUT_DIR"]
input_dir = config_dict["INPUT_DIR"]
print("入力ディレクトリ：{}\n出力ディレクトリ：{}\n区切る間隔:{}秒".format(
    input_dir
    , output_dir
    , devide_interval))

#INPUT_DIR 直下の音声ファイルのリストを作成。
ls = os.listdir(input_dir)
input_files = []
for filename in ls:
    if filename[-4:] == ".wav":
        input_files.append(filename)
        
numfiles = len(input_files)
current = 0
#各ファイルを処理していく
for infname in input_files:
    #進捗を出力
    current += 1
    outfname = output_dir + "/" + infname[:-4] + ".csv"
    print("{}/{}:{} -> {}".format(numfiles, current, infname, outfname))
    
    #入出力ファイルを開く
    inf = wave.open(input_dir + "/" + "infname" , "r")
    outf = open(outfname,"w", newline="")

    #指定秒数音声ファイルをロード
    
    
    
    inf.close()
    outf.close()

#フーリエ変換
#結果の書き出し



