# -*- coding: utf-8 -*-

import smtplib
from email.mime.text import MIMEText
from random import randint


file_players = open('players.txt', 'rb')
players = file_players.read()
file_players.close()

file_names = open('players_names.txt', 'rb')
names = file_names.read()
file_names.close()

fp = open('message_chosen.txt', 'rb')
msg_text_chosen = fp.read()
fp.close()

fd = open('message_default.txt', 'rb')
msg_text_default = fd.read()
fd.close()

fr = open('rules.txt', 'rb')
msg_rules = fr.read()
fr.close()

players_list = players.split('\n')
players_list.pop()

names_list = names.split('\n')
names_list.pop()

#draw
chosen = randint(0, len(players_list)-1)

save_result= str()

for index in xrange(len(players_list)):
    msg_text = str()
    if index==chosen:
        msg_text += msg_text_chosen
        save_result+='chosen '+ names_list[index]+' email: '+players_list[index]+'\n'
    else:
        msg_text += msg_text_default
        
    msg_text += msg_rules
    msg = MIMEText(msg_text)
        
    msg['Subject'] = 'You have been assigned!'
    msg['From'] = 'The Sticker HQ <you@example.com>'
    msg['To'] = players_list[index]

    s = smtplib.SMTP('localhost')
    s.sendmail(msg['From'], [msg['To']], msg.as_string())
    s.quit()
    

#save the result, just in case
#file_result = open('do_not_open', 'wb')
#file_result.write(save_result)
#file_result.close()

