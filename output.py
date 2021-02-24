import pandas as pd 

def out(file):
    print("変更したデータを出力します")
    str1=input("新規ファイル名を入力してください:")
    print(str1+".csvで出力します。よろしいでしょうか")
    while(1):
        chk=input("はい:1 ,いいえ:2---->")
        if int(chk)==1:
            file.to_csv(str1+".csv")
            print("出力が完了しました")
            return
        elif int(chk)==2:
            print("もう一度最初からやりなおしてください")
            return
        else:
            print("正しい入力が行われませんでした。もう一度入力してください")
    
