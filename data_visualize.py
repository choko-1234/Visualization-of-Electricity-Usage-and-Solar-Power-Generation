import pandas as pd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] = 'MS Gothic'

df = pd.read_csv('juyo-hourly-20210301.csv', 
                 encoding='shift_jis',  #csvの文字形式に合わせてencodeする
                 skiprows=54) # 55行目からデータを読み込むため

#日付と時刻を合体させ、複数日での比較や拡張性を持たせるため
df['DateTime'] = pd.to_datetime(df['DATE'] + ' ' + df['TIME'])

plt.figure(figsize=(10,6))

#電力のような連続データに適する折れ線グラフを採用した
plt.plot(df['DateTime'], df['当日実績(５分間隔値）(万kW)'],label='使用量')
plt.plot(df['DateTime'], df['太陽光発電実績(５分間隔値）(万kW)'],label='太陽光')

plt.legend()
plt.xticks(df['DateTime'][::12],df['TIME'][::12], rotation=45) # 1時間ごとに表示
plt.title(f'{df.iloc[1, 0]}の電力使用量と太陽光発電量')
plt.xlabel('時刻')
plt.ylabel('電力(万KW)')
plt.grid()
plt.show()