# import sys
# import os
import logging

# print('This message will be displayed on the screen.')

# with open('filename.txt', 'w') as f:
#     print('This message will be written to a file.', file=f)


# #LOG_DIR = os.path.join(os.path.normpath(os.getcwd() + os.sep + os.pardir), 'logs')
# #filename = os.path.join(LOG_DIR, 'log_file_name.log')

# logging.basicConfig(filename=r"C:\Users\Milad Shahabi\Desktop\AppointmentBot\log_data.log",
#                     level = logging.WARNING,
#                     format = '%(asctime)s:%(levelname)s:%(name)s:%(message)s')

# logger = logging.getLogger("app_logger")
# logger.setLevel(logging.INFO)

# # Also log to console.
# console = logging.StreamHandler()
# logger.addHandler(console)


# print('Hi everyone')




# myapp.py
i=22
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] %(message)s",
    handlers=[
        logging.FileHandler("debug.log"),
        logging.StreamHandler()
    ]
)


logging.warning(f'{i} attempts')  
logging.info('Useful message')
logging.error('Something bad happened')