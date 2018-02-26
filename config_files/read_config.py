#設定を読み込むための関数群。
#辞書形式で設定項目名と値の組を返す。
import sys
import os

config_list = ["DEVIDE_INTERVAL", "OUTPUT_DIR", "INPUT_DIR"]

#エラー吐いて終了する関数
def _print_error(error_str,error_info):

    print("エラー：" + error_str % error_info)
    sys.exit()

#必要な項目がすべて辞書に存在するかチェックする関数
def _check_enough_val(arg_dict):
    for item in config_list:
        try:
            arg_dict[item]
        except KeyError:
            _print_error("%sの設定行が見当たりません。\n"
                             "%s = 値\n"
                             "の形式で書かれているか確かめてください"
                            ,(item,  item))


#辞書中の数字の変数の値が文字列のままなので数値に直す。（例："3" -> 3）
def _convert_values(arg_dict):       
    
    interval = arg_dict["DEVIDE_INTERVAL"]           
    try:
        arg_dict["DEVIDE_INTERVAL"] = float(interval)
    except ValueError:
        _print_error("DEVIDE_INTERVALに指定された値が異常です。\n"
                    "指定された値：%s", (interval))
    
    return arg_dict

#辞書に格納した変数が正常な値かチェックする。
def _check_values(arg_dict):
    for path in ["INPUT_DIR", "OUTPUT_DIR"]:
        if not os.path.isdir(arg_dict[path]):
            _print_error("%sで指定されたpath\n%s\nはディレクトリではありません"
                         ,(path, arg_dict[path]))
    

def read_config():
    config_dictionary = {}
    config_dir = os.path.dirname(__file__)
    with open(config_dir + "/config.txt", "r", encoding="utf-8") as confile:

        #現在扱っているのが何行目かを保持する変数
        current_line = 1
       
        #設定に関する行のみ取り出して、辞書に格納
        line = confile.readline()
        while line:
            line = line.strip()

            #コメント行は無視
            if(line == "" or line[0] == "#"):
                pass
            else:
                try:
                    key = line.split("=")[0].strip()
                    value = line.split("=")[1].strip()
                    config_dictionary[key] = value
                except  IndexError:
                    pass

            current_line += 1
            line = confile.readline()
        
    _check_enough_val(config_dictionary)
    config_dictionary = _convert_values(config_dictionary)
    _check_values(config_dictionary)
    
    return config_dictionary

