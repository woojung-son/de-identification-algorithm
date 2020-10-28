import pandas as pd

df = pd.read_csv('./data/output/k_cyber_security_output.csv', encoding='utf-8')

qi_dict = {}

for i, row in df.iterrows():
    if not qi_dict.get(tuple([row['성별'], row['나이'], row['주소']])):
        qi_dict[tuple([row['성별'], row['나이'], row['주소']])] = [row['일련번호']]
    else:
        qi_dict[tuple([row['성별'], row['나이'], row['주소']])].append(row['일련번호'])

# qi_dict

map(lambda x: len(x), qi_dict.values())

for k, v in qi_dict.items():
    if len(v) == 1:
        print(k, v)