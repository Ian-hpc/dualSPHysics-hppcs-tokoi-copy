# 2つのCSVを比較する

import sys
import pandas as pd

if len(sys.argv) < 4:
    exit('引数が3つ渡される必要があります')

SKIP_ROWS = 3   # スキップする行数
DELIMITER = ';' # 区切り文字
P_ID = 'Idp'    # 粒子のIDの列名

df_l = pd.read_csv(sys.argv[1], skiprows=SKIP_ROWS, delimiter=DELIMITER)
df_r = pd.read_csv(sys.argv[2], skiprows=SKIP_ROWS, delimiter=DELIMITER)

# どちらかのファイルにのみ存在するIDがある場合出力する
not_in_r = (df_l[~df_l[P_ID].isin(df_r[P_ID])])[P_ID]
not_in_l = (df_r[~df_r[P_ID].isin(df_l[P_ID])])[P_ID]

if not_in_r.count() > 0:
    print(f'{sys.argv[1]}にのみ存在するID: {not_in_r.to_list()}')

if not_in_l.count() > 0:
    print(f'{sys.argv[2]}にのみ存在するID: {not_in_l.to_list()}')

# どちらにもIDが存在する行のみにする
df_l = df_l[df_l[P_ID].isin(df_r[P_ID])]
df_r = df_r[df_r[P_ID].isin(df_l[P_ID])]

# IDの順番にソートし、indexを振り直す
df_l = df_l.sort_values(P_ID).reset_index(drop=True)
df_r = df_r.sort_values(P_ID).reset_index(drop=True)

# 2つのDataFrameをCSVファイルとして出力する（デバッグ）
# df_l.to_csv('left.csv')
# df_r.to_csv('right.csv')

diff = df_l - df_r
abs = diff.abs()
describe = abs.describe()

# 結果を出力
# 差の絶対値をCSVファイルとして出力する（デバッグ）
# abs.to_csv('diff.csv')
describe.to_csv(sys.argv[3])