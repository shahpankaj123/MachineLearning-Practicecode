import requests
from bs4 import BeautifulSoup
import pandas as pd

url="https://merojob.com"

res = requests.get(url)
job_company_list=[]
job_position_list=[]
job_url_list=[]
if res.status_code ==200:
    soup =BeautifulSoup(res.content,'lxml')
    jobs=soup.find_all('div', class_='col-md-4 border-right border-bottom job-card')
    for job in jobs:
        company=job.find('div',class_='media-body')
        postion=company.find('h3',class_='h6')
        job_position = postion.find('span', itemprop='title')
        job_company=company.a.text.strip()
        #job_position=postion.text.strip()
        job_url=url + company.a['href']
        job_company_list.append(job_company)
        job_url_list.append(job_url)
        if job_position is None:
            job_position_list.append(' ')
        else:    
            job_position_list.append(job_position.text.strip())
    job_data =pd.DataFrame(
        {
            'Job_company':job_company_list,
            'job_url':job_url_list,
            'job_position':job_position_list
        }
    ) 
    print(job_data)
    job_data.to_csv('job.csv',index=False)  



    
    
