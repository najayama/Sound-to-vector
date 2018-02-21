#設定を読み込むための関数群。
#辞書形式で設定項目名と値の組を返す。

#エラー吐いて終了する関数
def _print_error(error_str,error_info):
    import sys
    print("エラー：" + error_str % error_info)
    sys.exit()


#辞書中の数字の変数の値が文字列のままなので数値に直す。（例："3" -> 3）
def _convert_values(arg_dict):
    
    
    #設定項目が見当たらなかった際のメッセージを出力する関数。
    def _p_how_to_define(item_name):
        _print_error("%sの設定行が見当たりません。\n"
                     "%s = 値\n"
                     "の形式で書かれているか確かめてください")
        
        interval = arg_dict["DEVIDE_INTERVAL"]    
    try:
        arg_dict["DEVIDE_INTERVAL"] = float(interval)
        
    except IndexError:
        _p_how_to_define("DEVIDE_INTERVAL")
    except ValueError:
        _print_error("DEVIDE_INTERVALに指定された値が異常です。\n"
                    "指定された値：%s", (interval))
        


#辞書に格納した変数が正常な値かチェックする。
def _check_values(arg_dict):
    pass


def read_config():
    config_dictionary = {}
    
    with open("config_files/config.txt", "r") as confile:

        #現在扱っているのが何行目かを保持する変数
        current_line = 1
       
        #設定に関する行のみ取り出して、辞書に格納
        line = confile.readline()
        while line:
            line = line.strip()

            #コメント行は無視
            if(line == "" or line[0] = "#"):
                pass
            else:
                try:
                    key = line.split("=")[0].strip()
                    value = line.split("=")[1].strip()
                    config_dictionary[key] = value
                except  IndexError:
                    _print_error(
                        "設定ファイル%d行目が異常です。\n"
                    "A = B\nの形か確認してください。\n"
                    "%d行目：%s"
                    , (current_line, current_line, line)
                    )
                    
            current_line += 1
            line = confile.readline()
        
    config_dictionary = _convert_values(config_dictionary)
    config_dictionary = _check_values(config_dictionary)
    
    return config_dictionary

