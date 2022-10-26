<<<<<<< ours
# copy current folder to a result directory
import shutil
import platform
import datetime
import os

if platform.system() == 'Darwin':
    result_dir = '/Users/shuffleofficial/Offline_Documents/FutureRL/tmp_results'
else:
    result_dir = '/home/yufeng/FutureRL_tmp'
time_str = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
result_dir = os.path.join(result_dir, 'NF_'+time_str)
# copy all the files in cwd to result_dir, except for the 'data.csv' file
shutil.copytree('.', os.path.join(result_dir, 'source'), ignore=shutil.ignore_patterns('data.csv'))



# save experiment information to the result folder
import sys
import time
txt_file_name = 'Experiment information.txt'

str_cmd = 'terminal command for this result folder:\npython '
for _ in sys.argv:
    str_cmd += _
str_cmd += '\n\n'

text_file = open(os.path.join(result_dir, txt_file_name), "w")
n = text_file.write(str_cmd)

# get current time and time zone    
str_time = 'Job start time: ' + datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S') + ', time zone: ' + str(time.tzname[1])
str_time += '\n\n'
text_file.write(str_time)

text_file.write('Current working directory: ' + os.getcwd())
text_file.close()



=======
import utils

result_dir = utils.create_result_folder()
gpu_id, device = utils.get_device()
>>>>>>> theirs

