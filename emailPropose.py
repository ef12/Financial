import pandas as pd, os, smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

def get_propose_and_email():
    Analysis = pd.read_csv("C:\\Users\\efrank\\Documents\\SW_Dev\\Financial\\Daily_Stock_Report\\OBV_Ranked.csv")  # Read in the ranked stocks
    top10 = Analysis.head(10)  # I want to see the 10 stocks in my analysis with the highest OBV values
    bottom10 = Analysis.tail(10)  # I also want to see the 10 stocks in my analysis with the lowest OBV values

    try:
        gmail_user = 'frankehud@gmail.com'
        gmail_password = 'ihrkhofegyrbpuqq'
        
        sent_from = gmail_user
        to = ['frankehud@gmail.com', 'revitalroz@hotmail.com'] # ['me@gmail.com', 'bill@gmail.com']

        body = """\
        Your highest ranked OBV stocks of the day:
        """ + top10.to_string(index=False) + """\
        Your lowest ranked OBV stocks of the day:
        """ + bottom10.to_string(index=False) + """\
        Sincerely,
        Your Computer"""
        
        msg = MIMEMultipart()
        msg['To'] = ", ".join(to)
        msg['From'] = sent_from
        msg['subject'] = "Daily Stock Report"
        msg.attach(MIMEText(body,'plain'))
        
        message = msg.as_string()

        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.ehlo()
        server.starttls()
        server.ehlo()
        server.login(gmail_user, gmail_password)
        server.sendmail(sent_from, to, message)
        server.quit()

        print("Email sent!")
    except:
        print("Something went wrong...")
