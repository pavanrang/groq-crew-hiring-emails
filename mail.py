import smtplib
import csv
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Email configuration
sender_email = "pavan.sv.ranga@gmail.com"
receiver_email = "satyapavanr8@gmail.com"
password = "owpebvlvrgnpfocv"


# Path to the folder containing output text files
output_folder = "output/"

# Read data from CSV file
csv_file_path = "data/clients_medium.csv"  # Path to CSV file
with open(csv_file_path, newline='') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        receiver_email = row['email']
        first_name = row['first_name']

        # Read content from the text file
        text_file_path = os.path.join(output_folder, f"{first_name}.txt")
        with open(text_file_path, "r") as text_file:
            body = text_file.read()

        # Create message
        message = MIMEMultipart()
        message["From"] = sender_email
        message["To"] = receiver_email
        message["Subject"] = f"Personalized Email for {first_name}"

        message.attach(MIMEText(body, "plain"))

        # Connect to SMTP server and send email
        with smtplib.SMTP("smtp.gmail.com", 587) as server:
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, message.as_string())

        print(f"Email sent to {receiver_email}")

# Create message
message = MIMEMultipart()
message["From"] = sender_email
message["To"] = receiver_email
message["Subject"] = "Test Email from Python"

body = "This is a test email sent from Python."
message.attach(MIMEText(body, "plain"))

# Connect to SMTP server
with smtplib.SMTP("smtp.gmail.com", 587) as server:
    server.starttls()
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message.as_string())
