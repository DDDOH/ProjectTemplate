
import shutil
import datetime
import os
import matplotlib.pyplot as plt


def create_result_folder(result_dir, exp_label):
    # copy current folder to a result directory
    time_str = datetime.datetime.now().strftime('%Y-%m-%d_%H-%M-%S')
    result_dir = os.path.join(result_dir, exp_label+time_str)
    # copy all the files in cwd to result_dir, except for the 'data.csv' file
    shutil.copytree('.', os.path.join(result_dir, 'source'), ignore=shutil.ignore_patterns('data.csv'))

    print('Copy code to ' + result_dir)

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

    return result_dir



def check_gpu_usage():
    """Return available memory for each GPU as a list.

    Based on https://gist.github.com/afspies/7e211b83ca5a8902849b05ded9a10696?permalink_comment_id=4127781#gistcomment-4127781
    """
    
    # Process exceptions -> we don't care about such procs
    # User exceptions -> we care ONLY about procs of this user
    pynvml.nvmlInit()
    # print ("Driver Version:", pynvml.nvmlSystemGetDriverVersion())
    deviceCount = pynvml.nvmlDeviceGetCount()
    gpus_avail_mem = []
    for i in range(deviceCount):

        handle = pynvml.nvmlDeviceGetHandleByIndex(i)
        mem = pynvml.nvmlDeviceGetMemoryInfo(handle)
        free_memory = mem.free / (1024 ** 3)
        gpus_avail_mem.append(free_memory)
        # if base_on_memory and free_memory < min_memory:
        #     continue
        #
        # free = True
        # if base_on_process:
        #     procs = [*pynvml.nvmlDeviceGetComputeRunningProcesses(handle),
        #              *pynvml.nvmlDeviceGetGraphicsRunningProcesses(handle)]
        #     for p in procs:
        #         try:
        #             process = psutil.Process(p.pid)
        #         except psutil.NoSuchProcess:
        #             continue
        #
        #         if process.name not in process_exceptions and process.username() in user_exceptions:
        #             free = False
        #             break
        # if free:
        #     free_gpus.append(str(i))

    # print(f"[[GPU INFO]] [{','.join(gpus_avail_mem)}] Free")
    # pynvml.nvmlShutdown()
    return gpus_avail_mem
    

# automatically select PyTorch device
import torch
import psutil
if torch.cuda.is_available():
    import pynvml as pynvml


def get_device(gpu_id=None):
    """
    Use cpu if gpu available.
    If gpu_id is feasible, use gpu with given gpu_id;
    otherwise select gpu with largest free memory.
    """
    
    if torch.cuda.is_available():
        gpus_avail_mem = check_gpu_usage()
        # get cuda device amount
        n_cuda = torch.cuda.device_count()
        # raise DeprecationWarning("This function is deprecated. Please use the function in utils.py")
        if gpu_id == -1 or gpu_id is None:
            print('Use GPU with largest free memory.')
            print(gpus_avail_mem)
            gpu_id = int(np.argmax(gpus_avail_mem))
        
        if gpu_id + 1 > n_cuda:
            print('No GPU available with id {}.'.format(gpu_id))
            print(gpus_avail_mem)
            gpu_id = int(np.argmax(gpus_avail_mem))
            print('Use GPU with largest free memory.')
        
        device = torch.device('cuda:{}'.format(gpu_id))
        
    else:
        print('No GPU available. Use CPU instead.')
        device = torch.device('cpu')
        gpu_id = None

        # OS = platform.system()
        # if OS == 'Windows' or OS == 'Linux':
        #     if torch.cuda.is_available():
        #         device = torch.device('cuda')
        #     else:
        #         print('No GPU available. Use CPU instead.')
        #         device = torch.device('cpu')
        # if OS == 'Darwin':
        #     if not torch.backends.mps.is_available():
        #         if not torch.backends.mps.is_built():
        #             print("MPS not available because the current PyTorch install was not "
        #                 "built with MPS enabled. Use CPU instead.")
        #         else:
        #             print("MPS not available because the current MacOS version is not 12.3+ "
        #                 "and/or you do not have an MPS-enabled device on this machine. Use CPU instead.")
        #     else:
        #         device = torch.device("mps")

    print('Using device: {}'.format(device))
    return gpu_id, device





# record and visualize memory usage
import os, psutil
process = psutil.Process(os.getpid())


class MemoryRecoder():
    def __init__(self, result_dir, with_time=False):
        self.result_dir = result_dir
        self.rec = {}
        if with_time:
            raise NotImplemented

    def record(self, label):
        self.rec[label] = process.memory_info().rss / 1024 / 1024 # in MB

    def plot(self):
        plt.figure()
        plt.plot(self.rec.keys(), self.rec.values())
        plt.title('Memory usage in MB')
        plt.savefig(os.path.join(self.result_dir, 'memory_rec.png'))
        plt.close()






