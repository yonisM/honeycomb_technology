import schedule
from send_email import extract_send


extract_and_send = extract_send()

schedule.every().day.at("00:00").do(extract_and_send)

