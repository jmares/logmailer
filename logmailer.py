import os
from datetime import datetime
import time
from config import DEST_EMAIL, LOG_DIR

now = datetime.now()
for file in os.listdir(LOG_DIR):
    if file.endswith(".log"):
        # get the full path for the file, incl. the file
        file_full_path = os.path.join(LOG_DIR, file)
        # get the last modified time
        file_mod_time = time.localtime(os.path.getmtime(file_full_path))  
        # get the last modified date
        file_mod_date = time.strftime("%Y-%m-%d", file_mod_time)
        # compare last modified date to current date
        if file_mod_date == now.strftime("%Y-%m-%d"):
            f = open(file_full_path)
            text = f.read()
            title = file.split('_')[0] 
            try:
                p = os.popen('msmtp -t', 'w')
                p.write(f"To:{DEST_EMAIL}\nSubject: {title}\n\n{text}")
                p.close()
                print('Message send.')
            except Exception as e:
                print('Caught exception!')
                print(e)
