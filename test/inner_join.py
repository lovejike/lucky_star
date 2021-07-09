import pandas as pd


def data_process(input_file):
    df_origin = pd.read_excel(input_file, header=0)
    print(df_origin)

    # 提取时间
    columns_1 = ['dt_hour', 'minute', 'second']
    df1 = df_origin['date'].astype(str).str.split(':', expand=True)
    df1.columns = columns_1
    df1 = df1.drop('minute', axis=1)
    df1 = df1.drop('second', axis=1)
    print(df1)

    df_origin = df_origin.drop('date', axis=1)
    df_2016_1 = df1.join(df_origin)
    print(df_2016_1)
    return df_2016_1


res_2016_1 = data_process("2016-1.xls")
res_2016_2 = data_process("2016-2.xls")
final_res = pd.merge(res_2016_1, res_2016_2, on=['dt_hour'])
final_res.to_csv("2016_res.csv")

