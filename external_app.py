import requests
import pandas as pd
import json
import datetime

def get_data(url):
    payload={}
    headers = {}

    response = requests.request("GET", url, headers=headers, data=payload)

    return(response.text)


def get_low_salary_workers(df):
    mean_salary = df['salary'].mean()
    today = datetime.datetime.now()
    df['heir_date'] = pd.to_datetime(df['heir_date'])
    delta = today - df['heir_date']
    df['years_work'] = delta.map(lambda x : round(x.days/365,2))
    low_salary = df.loc[
              (df['years_work'] > 0.00001) &
              (df['salary'] < mean_salary)]
    if low_salary.shape[0] == 0:
        print("No worker found")
    else:
        out_file = "low_salary.tsv"
        low_salary.to_csv(out_file, sep="\t", index=None)
        print("Results are at file {}".format(out_file))

def workers_salary():
    url = "http://127.0.0.1:8000/api/workers/"
    df = pd.DataFrame.from_dict(json.loads(get_data(url))) # get data from API into panda DF
    get_low_salary_workers(df) # calculate salary and print to file workers working > 1Y with low salary

if __name__ == "__main__":
    workers_salary()