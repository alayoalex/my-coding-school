#!/usr/bin/python

import imaplib
import email
import os, sys

SOUNDS_PATH = "ruta donde está el sonido"
LISTING_LIMIT = 5 
icon_alert = "ruta donde está el icono"
sound_alert = SOUNDS_PATH + "Peow!.wav"

try:
	imap = imaplib.IMAP4_SSL('imap.uci.cu')
	imap.login("aalayo", "password")
	imap.select("inbox", readonly=True)
	typ, msg_ids = imap.search('utf-8', "UNSEEN")


	if typ == "OK":
		msgid_list = msg_ids[0].split()
		cant = len(msgid_list)
		if cant > 0:
			#preaparing notification message
			notify_title = "\"New E-Mail\""
			notify_msg = "\"There are " + str(cant) + " unseen emails in humanOS."
			
			#make a small sample list if ther aren't to many unseen emails
			if cant <= LISTING_LIMIT:
				notify_msg += "\nReceived from:"
				for mid in msgid_list:
					typ, msg_data = imap.fetch(mid, '(RFC822)')
					for data_part in msg_data:
						if isinstance(data_part, tuple):
							msg = email.message_from_string(data_part[1])
							address = msg['FROM'].split()[-1]
							#remove < > characters
							clean_address = address[1:len(address) - 1]
							notify_msg += "\n\t" + clean_address

			
			#closing the message content of the notification
			notify_msg += "\""
			notify_cmd = "notify-send -u normal -i " + icon_alert + " " + notify_title + " " +notify_msg
			os.system(notify_cmd)
			os.system("aplay -q " + sound_alert)


except Exception, ex:
	if ex.message == "LOGIN failed":
		icon_fail = "system-devices-panel-alert"
		message = "\"Login failed\" \"Invalid user or password for authentication.\nCheck your credentials.\""
		notify_cmd = "notify-send -u normal -i " + icon_fail + " " + message
		os.system(notify_cmd)

finally:
	sys.exit(0)
