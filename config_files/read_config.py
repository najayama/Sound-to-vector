#設定を読み込むためのファイル。辞書形式で設定項目と値の組を返す。

def perror(invalid_line, line_number):
    import sys
    print("エラー：設定ファイルの%d行目の値が異常です。" % (line_number))
    print("問題のライン：%s" % (invalid_line))
    sys.exit()

#保守の観点からいうと変数名の組と値を辞書に
#いれんのは関数にやらせたほうがきれいで追加しやすいコードになりそう。
def read_config():
    config_dictionary = {}

    
    with open("config.txt", "r") as confile:
        #設定の書いてある行のみ取り出す
        line_number = 1
        line = confile.readline()
        while line:
            if(line.strip()[:15] == "DEVIDE_INTERVAL"):
                try:
                    config_dictionary["DEVIDE_INTERVAL"] = float(line.split()[2])
                except:
                    perror(line, line_number)
            elif(line.strip()[:10] == "OUTPUT_DIR"):
                try:
                    config_dictionary["OUTPUT_DIR"] = line.split()[2]
                except:
                    perror(line,line_number)
            elif(line.strip()[:])
