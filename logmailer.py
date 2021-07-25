import os
from datetime import datetime
import time
from config import *

now = datetime.now()
for file in os.listdir(LOG_DIR):
    if file.endswith(".log"):
        file_date = time.strftime("%Y-%m-%d", time.localtime(os.path.getmtime(os.path.join(LOG_DIR, file))))
        if file_date == now.strftime("%Y-%m-%d"):
            f = open(os.path.join(LOG_DIR, file))
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


        #print(os.path.join(LOG_DIR, file))