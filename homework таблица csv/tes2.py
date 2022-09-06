
import re
import pandas as pd
import  zipfile
import requests




r = requests.get('https://info.stackoverflowsolutions.com/rs/719-EMH-566/images/stack-overflow-developer-survey-2022.zip')
with open('data.zip', 'wb') as file:
    file.write(r.content)
    with zipfile.ZipFile('data.zip', 'r') as data_zip:
        data_zip.extract('survey_results_public.csv')
        df = pd.read_csv('survey_results_public.csv', nrows=10000)
        pd.set_option('display.max_rows', 10000)

while True:
    user_choice = input('Please choose:\n1.Get info about Professionals\n'
                        '2.Get info about Hobbyist\n3.Get info about AGE\n'
                        '4.Info about Country\n5.Get info about Currensy\n'
                        '0.Exit\n--> ')
    if user_choice == '0':
        print('Good bye')
        exit()
    if user_choice == '1':
        print(str('Proffesionals : '), (len(df.loc[df['MainBranch'].str.contains('I am a developer by profession')]['MainBranch'])))
    elif user_choice == '2':
        print(str('Hobbyist : '), (len(df.loc[df['MainBranch'].str.contains('I code primarily as a hobby')]['MainBranch'])))
    elif user_choice == '3':
        df = pd.read_csv('survey_results_public.csv', encoding='utf-8', nrows=10000)
        df2 = df['Age']
        df3 = df['Age']
        df2 = df2.groupby(int).min().str.replace('-\d\d years old', '', regex=True).dropna().str.replace('Under',
                                                                                                         '').str.replace(
            'Prefer', '').str.replace('years old', '').str.replace('years or older', '').str.replace('not to say',                                                                                    'young')
        df4 = df2.min()
        df3 = df2.max()
        print(int(df3), 'MAX')
        print(int(df4), 'MIN')
        print((int(df3) - int(df4)) / 2, 'MEDIUM')
    elif user_choice == '4':
        print(df.groupby('Country').count().sort_values('ResponseId', ascending=False)['ResponseId'])
    elif user_choice == '5':
        print(df.groupby('Currency').count().sort_values('ResponseId', ascending=False)['ResponseId'])

#





