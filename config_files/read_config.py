#設定を読み込むための関数群。
#辞書形式で設定項目名と値の組を返す。

#エラー吐いて終了する関数
def _print_error(error_str,error_info):
    import sys
    print("エラー：" + error_str % error_info)
    
    errorfile = open()
    sys.exit()

#辞書中の数字の変数の値が文字列のままなので数値に直す。（例："3" -> 3）
def _convert_values(arg_dict):
    try:
        interval = float(arg_dict[])
        


#辞書に格納した変数が正常な値かチェックする。
def _check_values(arg_dict):
    pass




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
