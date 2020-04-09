import tkinter as tk
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email import encoders


def gui():
    
    def send_mail():
        smtp_ssl_host = 'smtp.gmail.com'
        smtp_ssl_port = 465
        username = 'temp.mail.mca@gmail.com'
        password = 'qwerty@1234'
        sender = 'temp.mail.mca@gmail.com'
        targets = to_ent.get()
        msg = MIMEMultipart()
        msg = MIMEText(body_text.get("1.0",'end-1c'))
        msg['To'] = to_ent.get()
        msg['From'] = sender
        msg['CC'] = cc_ent.get()
        msg['BCC'] = bcc_ent.get()
        msg['Subject'] = sub_ent.get()
        
        #File attachment code:
        #msg.attach(MIMEText(body_text.get("1.0",'end-1c'), 'plain'))
        #attach_file_name = 'abc.jpg'
        #attach_file = open(attach_file_name, 'rb') # Open the file as binary mode
        #payload = MIMEBase('application', 'octate-stream')
        #payload.set_payload((attach_file).read())
        #encoders.encode_base64(payload) #encode the attachment
        #add payload header with filename
        #payload.add_header('Content-Decomposition', 'attachment', filename=attach_file_name)
        #msg.attach(payload)
        
        try:
            server = smtplib.SMTP_SSL(smtp_ssl_host, smtp_ssl_port)
            server.login(username, password)
            server.send_mail(sender, targets, msg.as_string())
        except Exception as e:
            print("error is: ", e)
        
    root = tk.Tk()
    root.title("Compose Mail")
   
    #labels
    to_lbl = tk.Label(root,text="To:")
    cc_lbl = tk.Label(root,text="CC:")
    bcc_lbl = tk.Label(root,text="BCC:")
    sub_lbl = tk.Label(root,text="Subject:")
    body_lbl = tk.Label(root,text="Message:")
    
       
    #entries and buttons
    to_ent = tk.Entry(root, width = 40)
    cc_ent = tk.Entry(root, width = 40)
    bcc_ent = tk.Entry(root, width = 40)
    sub_ent = tk.Entry(root, width = 40)
    body_text = tk.Text(root, wrap = 'word', height = 16, width = 60)
    submit_btn = tk.Button(root, text = "Submit", command = send_mail)
    att_btn = tk.Button(root, text = "Attach File")
    
     #placement of labels, entries and buttons
    to_lbl.place(x = 5,y = 5)
    to_ent.place(x = 35,y = 5)
    cc_lbl.place(x = 5,y = 35)
    cc_ent.place(x = 35,y = 35)
    bcc_lbl.place(x = 5,y = 65)
    bcc_ent.place(x = 40,y = 65)
    sub_lbl.place(x = 5,y = 95)
    sub_ent.place(x = 55,y = 95)
    att_btn.place(x = 5,y = 125)
    body_lbl.place(x = 5,y = 155)
    body_text.place(x = 5,y = 175)
    submit_btn.place(x = 5,y = 440)
        
    root.geometry("500x500")
    
    root.mainloop()

if __name__=="__main__":
    gui()