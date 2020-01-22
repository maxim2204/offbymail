import email
import imaplib
import os

f = open('text.txt', 'r')
ch = f.read()
ch = int(ch)
f.close

while True:
        mail = imaplib.IMAP4_SSL('imap.yandex.ru')
        mail.login('test@taurl.space', '12345678990')
        mail.list()
        mail.select("inbox")
        result, data = mail.search(None, "ALL")
        print(result)
        ids = data[0]
        #print(ids)
        if data[0] != b'':
                print("Mail")
                id_list = ids.split()
                if len(id_list) > ch:
                        latest_email_id = id_list[-1]
                        result, data = mail.fetch(latest_email_id, "(RFC822)")
                        raw_email = data[0][1]
                        email_message = email.message_from_bytes(raw_email)
                        #print(email_message['To'])
                        print(email_message['From'].split("<")[1][:-1])
                        print(email_message['Subject'])

                        '''
                        print(email_message['Text'])
                        print(email_message['Content-Type'])
                        if email_message.is_multipart():
                            print("message is multypart")
                        else:
                            print("message is not multypart")'''

                        body = email_message.get_payload()
                        print(body)
                        print("\n")

                        if "Shutdown" in body:
                            f = open('text.txt', 'w')
                            f.write(str(ch+1))
                            myCmd = 'shutdown /s /t 0'
                            os.system(myCmd)
                            break