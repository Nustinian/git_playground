import psycopg2
import smtplib, ssl, getpass

class Database:  
  def __init__(self):
    self.connection = psycopg2.connect("dbname='height-db' user='postgres' password='password123' host='localhost' port='5432'")
    self.cursor = self.connection.cursor()
    self.cursor.execute("CREATE TABLE IF NOT EXISTS heights (email TEXT UNIQUE, height INTEGER)")
    self.connection.commit()

  def insert(self, email, height):
    self.cursor.execute("INSERT INTO heights VALUES(%s, %s) ON CONFLICT (email) DO UPDATE SET height = %s WHERE heights.email = %s", (email, height, height, email))
    self.connection.commit()

  def view(self):
    self.cursor.execute("SELECT height FROM heights")
    rows = self.cursor.fetchall()
    return rows

  def return_average_height(self):
    total = 0
    entries = len(self.view())
    for i in range(entries):
      total += self.view()[i][0]
    return '%.1f'%(total / entries)

port = 465
password = getpass.getpass("Type your password and press enter: ")
context = ssl.create_default_context()
smtp_server = "smtp.gmail.com"
sender_email = "sentfromaustin@gmail.com"
message = "The average height of all participants thus far is {average}cm."

def send_email(email, average):
  try:
    with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
      server.login(sender_email, password)
      server.sendmail(sender_email, email, message.format(average = average))
      print("success!!")
  except:
    print("something went wrong")