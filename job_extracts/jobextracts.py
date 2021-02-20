#Create the spreadsheet extract of roles

from reed import ReedClient
import pandas as pd
from datetime import datetime



def job_extraction():

    YOUR_API_KEY = '16a21e02-a94e-4a30-8d1c-8497a7cb43d2'
    
    client = ReedClient(api_key=YOUR_API_KEY)
        
    params = {
        'keywords': "Developer",
        'resultsToTake': 1000,
        'locationName' : "United Kingdom",
        'postedByRecruitmentAgency ':"false",
        'postedByDirectEmployer':"true"
        }
    
    response = client.search(**params)
    
    all_df = pd.DataFrame(response)
    
    
    blacklisted = ['AMS Contingent Team','Computer Futures','And Digital','Encircle Solutions','Amber Resourcing','Get Staffed Online Recruitment Limited','McGregor Boyall','Method Cloud','Method Resourcing','MortgageKey','Nelson Frank','Optionis Group Ltd','REED Talent Solutions','Resource Solutions','Sanderson']
    
    
    df = all_df[~all_df['employerName'].isin(blacklisted)]
    
    
    
    roles = df.sort_values("minimumSalary", ascending=False)

    file_date =  datetime.strftime(datetime.now(), '%y.%m.%d')

    
    filename = "spreadsheets/" + file_date + "_Clients_to_call.csv" 
    
    roles.to_csv(filename)
