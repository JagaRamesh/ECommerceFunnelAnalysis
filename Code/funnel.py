import pandas as pd
import numpy as np

def load_merge_data():
    user = pd.read_csv('user_table.csv')
    user['date'] = pd.to_datetime(user['date'])

    home = pd.read_csv('home_page_table.csv')
    home['home_page']=1
    del home['page']

    search = pd.read_csv('search_page_table.csv')
    search['search_page']=1
    del search['page']

    paymentp = pd.read_csv('payment_page_table.csv')
    paymentp['payment_page']=1
    del paymentp['page']

    paymentc = pd.read_csv('payment_confirmation_table.csv')
    paymentc['payconfirm_page']=1
    del paymentc['page']

    df1 = pd.merge(user,home,how='left',on=['user_id'])
    df2 = pd.merge(df1,search,how='left',on=['user_id'])
    df2 = df2.fillna(0)
    df3 = pd.merge(df2,paymentp,how='left',on=['user_id'])
    df3 = df3.fillna(0)
    df4 = pd.merge(df3,paymentc,how='left',on=['user_id'])
    df4 = df4.fillna(0)

    return df4

if __name__ == '__main__':
    funnel = load_merge_data()
    funnel['month'] = pd.DatetimeIndex(funnel['date']).month
