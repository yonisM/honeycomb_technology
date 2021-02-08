import schedule
from send_email import extract_send
import os

extract_and_send = extract_send()

schedule.every().day.at("23:52").do(extract_and_send)

os.remove('spreadsheets/Developer.csv')