# main.py

while True:
    print("数値を入力してください")
    input_num = int(input()) # 入力コマンド

    if input_num == 0:
        print('プログラムを終了します')
        break
    # -- ここに処理を追加してみよう --
    elif input_num == 334:
        print("なんでや！阪神関係ないやろ！")
    elif input_num == 1:
        print("aiueo")
    else:
        print('該当するコマンドがありません')
