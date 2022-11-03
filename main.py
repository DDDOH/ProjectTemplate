import utils

# copy current folder to a result directory and save experiment information to the result folder
result_dir = '/Users/shuffleofficial/Documents/Online_Documents/22_8_2_Project_Folder_Basement/output'
result_dir = utils.create_result_folder(result_dir=result_dir, exp_label='test')

# get gpu with largest free memory
gpu_id, device = utils.get_device()


# record memory usage
memory_rec = utils.MemoryRecoder(result_dir=result_dir, with_time=False)
memory_rec.record(0)

import numpy as np
large_array = np.random.uniform(size=(1000, 1000))
memory_rec.record(1)
large_array_2 = np.random.uniform(size=(2000, 1000))
memory_rec.record(2)

memory_rec.plot()

