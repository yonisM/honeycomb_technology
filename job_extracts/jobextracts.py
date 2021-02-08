#Create the spreadsheet extract of roles

from reed import ReedClient
import pandas as pd
import os


def job_extraction():

    YOUR_API_KEY = os.environ['YOUR_API_KEY']
    
    client = ReedClient(api_key=YOUR_API_KEY)
    
    role = 'Developer'
    
    params = {
        'keywords': "Developer",
        'resultsToTake': 1000,
        'locationName' : "United Kingdom",
        'postedByDirectEmployer':"True",
        'contract':"True"   
    }
    
    response = client.search(**params)
    
    all_df = pd.DataFrame(response)
    
    blacklisted = ['AMS Contingent Team','Computer Futures','Encircle Solutions','Get Staffed Online Recruitment Limited','McGregor Boyall','Method Cloud','Method Resourcing','MortgageKey','Nelson Frank','Optionis Group Ltd','REED Talent Solutions','Resource Solutions','Sanderson']
    
    
    df = all_df[~all_df['employerName'].isin(blacklisted)]
    
    
    
    roles = df.sort_values("minimumSalary", ascending=False)
    
    filename = "spreadsheets/" + role + ".csv" 
    
    roles.to_csv(filename)
