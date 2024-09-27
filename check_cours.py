import threading
import requests
from bs4 import BeautifulSoup
import smtplib
import time

from email.mime.text import MIMEText


def send_email(subject, body, sender, recipients, password):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")
    
#subject = "CS 436 Galiba yer buldum"
#body = "site burasi : https://suis.sabanciuniv.edu/prod/bwckschd.p_disp_detail_sched?term_in=202302&crn_in=22216"
subject = "Course Check"
body = "Mail body"
#sender gmail
sender = "sender@gmail.com"
recipients = ["recepient1@gmail.com","recepient2@gmail.com"]
#sender email password
password = "password"

#send_email(subject,body,sender,recipients,password)


def check_remaining_count(url,course):
    found = 0
    cnt = 0
    try:
        while True:
            cnt+=1
            # Make a GET request to the website
            response = requests.get(url)
            #print(response.raw)
            # Check if the request was successful (status code 200)
            if response.status_code == 200:
                # Parse the HTML content of the page
                soup = BeautifulSoup(response.text, "lxml")

                # Locate the table with the specified class
                tables = soup.find_all('table', class_='datadisplaytable')
                #print(f"Tabel size : {len(tables)}")
                table = ''
                
                for item in tables:
                    caption = item.find('caption')
                    #print("-------Caption")
                    #print(caption)
                    if caption and caption.text.strip() == 'Registration Availability':
                        table = item
                #print("------Table:")
                #print(table)

                table_inside = table.find_all("tr")
                headers = table_inside[0].find_all("th")
                values = table_inside[1].find_all("td")
                #print("------headers:")
                #print(headers)
                #print("------values")
                #print(values)
                flag = False
                email_body = ''
                for i in range(3):
                    header = headers[i].text
                    value = values[i].text
                    email_body += f"{header} : {value}\n"
                    if(header == "Remaining" and value != "0"):
                        flag = True
                        found+=1
                if(flag):
                    send_email(f"{course} PLACES",email_body,sender,recipients,password)              
                else :
                    print(f'Not found({course}) : {cnt} , found count : {found},\n{email_body}')
                '''
                if table:
                    # Find all rows in the table body
                    rows = table.find('tbody').find_all('tr')

                    # Get the index of each column
                    headers = [header.text.strip().lower() for header in rows[0].find_all('th')]
                    remaining_count_index = headers.index('remaining')

                    # Check the remaining count in the first row
                    remaining_count = int(rows[1].find_all('td')[remaining_count_index].text.strip())

                    if remaining_count == 0:
                        print(remaining_count)
                        print("Found yeaah")
                        #send_email("Course Availability", "The remaining count is 0!")
                        break  # Stop checking once remaining count is 0
                else:
                    print("Unable to locate the table with the specified class on the page.")
                '''
            else:
                print(f"Failed to retrieve the webpage({course}). Status code: {response.status_code}")

            # Wait for some time before the next check (adjust the delay as needed)
            time.sleep(2)  # 10 minutes delay
    except Exception as e:
        print(f"({course})An error occurred: {e}")

# Example usage
cs_436_url = 'https://suis.sabanciuniv.edu/prod/bwckschd.p_disp_detail_sched?term_in=202302&crn_in=22216'
cs_449_url = 'https://suis.sabanciuniv.edu/prod/bwckschd.p_disp_detail_sched?term_in=202302&crn_in=22080'

#check_remaining_count(cs_449_url,"CS 449")

# Create two threads, each running the print_string_thread function with a different string
thread1 = threading.Thread(target=check_remaining_count, args=(cs_436_url,"CS 436"))
#thread2 = threading.Thread(target=check_remaining_count, args=(cs_449_url,"CS 449"))

# Start the threads
thread1.start()
#thread2.start()

try:
    # Keep the main thread alive to allow the two threads to run indefinitely
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    # Handle Ctrl+C to gracefully stop the threads
    thread1.join()
    #thread2.join()

