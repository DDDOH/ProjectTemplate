import numpy as np

def save_plot_data(plot_func):
    """A wrapper that save visualization data to npy file.
    
    Args:
        plot_func (function): The function that generates the plot, and should return the path to the save data (including the file name).
                              Add this decorator to the head of your function, and the input of your functions will be automatically saved
                              at the directory specified by the return of your function.
    """
    def wrapper(*args, **kwargs):
        to_save = {'args': args, 'kwargs': kwargs}
        fig_dir_name = plot_func(*args, **kwargs)
        # fig_dir_name = fig_dir_name.replace('.', '_')
        np.save(fig_dir_name +'.npy', to_save)
    return wrapper



# Example usage:
if __name__ == '__main__':
    import matplotlib.pyplot as plt
    import os


    @save_plot_data # add decorator here
    def visualize_func(input_data_1, input_data_2, file_name):
        # Your self-defined visualization function
        plt.figure()
        plt.plot(input_data_1, input_data_2)

        plt.savefig(os.path.join('figures', file_name))


        return os.path.join('figures', file_name) # return the figure path along with the file name such that we know where to save your data.


    data_1 = [1,2,3]
    data_2 = [2,3,4]
    visualize_func(data_1, data_2, '1')
    visualize_func(data_1, input_data_2=data_2, file_name='2')



