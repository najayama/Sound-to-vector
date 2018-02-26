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

#指定秒数音声ファイルをロードしてnumpy_array形式で返す
def load_wave(wf, devide_interval, freq):
    #秒をフレームに換算
    frame = freq * devide_interval

    #整数データを量子化ビット数に応じて正規化    
    raw_data = wf.readframes(int(frame))
    if wf.getsampwidth() == 2:
        x = np.frombuffer(raw_data, dtype="int16") / (32768.0)
    else:
        x = np.frombuffer(raw_data, dtype= "u1") / (256)
        x = [(i - 128) / 128 for i in x]
    
    #もしもステレオなら足して二で割ってモノラルにする
    if wf.getnchannels() == 2:
        left = x[0::2]
        right = x[1::2]
        x = [(i + j) / 2 for i, j in zip(left, right)]
    wf.close()
        
    return x
        
        


#１．設定ファイルの読み込み。
config_dict = read_config.read_config()

devide_interval = config_dict["DEVIDE_INTERVAL"]
output_dir = config_dict["OUTPUT_DIR"]
input_dir = config_dict["INPUT_DIR"]
print("入力ディレクトリ：{}\n出力ディレクトリ：{}\n区切る間隔:{}秒".format(
    input_dir
    ,  output_dir
    ,  devide_interval))

#INPUT_DIR 直下の音声ファイルのリストを作成。
ls = os.listdir(input_dir)
input_files = []
for filename in ls:
    if filename[-4:] == ".wav":
        input_files.append(filename)
        
numfiles = len(input_files)
current_file = 0
#各ファイルを処理していく
for infname in input_files:
    #進捗を出力
    current_file += 1
    outfname = output_dir + "/" + infname[:-4] + ".csv"
    print("[{}/{}]: {} -> {}".format(numfiles, current_file, infname, outfname))
    
    #入出力ファイルを開く
    inf = wave.open(input_dir + "/" + infname , "r")
    outf = open(outfname,"w", newline="")

    freq = inf.getframerate()
    
    current_buffer = 0
    x = load_wave(inf, devide_interval, freq)
    while x:
        current_buffer += 1
        X = scipy.fftpack.fft(x)
        freqlist = scipy.fftpack.fftfreq(int(freq * devide_interval),  d=1.0/freq)
        
        #振幅スペクトル
        amplitudeSpectrum = [np.sqrt(c.real ** 2 + c.imag ** 2) for c in X]
        data = np.c_[freqlist, amplitudeSpectrum]
        
        #出力
        writer = csv.writer(outf)
        writer.writerows([[
            "start = {}seq".format(current_buffer * devide_interval)
            , "end = {}seq".format((current_buffer+1) * devide_interval)], ])
        writer.writerows(data)
        
        
        
        
        
        
        
        
        
        
        
        
    
    
    
    
    
    inf.close()
    outf.close()

#フーリエ変換
#結果の書き出し



