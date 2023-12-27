import time
import pandas as pd

tables=[]


for i in range(0,1):


    url='https://www.screener.in/screens/356009/bse-nse-company-list/?page={0}'.format(i*100)

    print('processing index {0}'.format(i*100))

    try:
        df = pd.read_html(url)[0]
        tables.append(df)
        time.sleep(1)

    except Exception as e:
        print(e)
        continue


results=pd.concat(tables, axis=0)

results.to_excel('Screen_Result.xlsx', index=False)