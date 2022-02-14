import argparse
import time
import numpy as np
import pandas as pd

import brainflow
from brainflow.board_shim import BoardShim, BrainFlowInputParams, LogLevels, BoardIds
from brainflow.data_filter import DataFilter, FilterTypes, AggOperations


    
BoardShim.enable_dev_board_logger()

params = BrainFlowInputParams()
params.ip_port = 0
params.serial_port = '/dev/cu.usbserial-DQ007SNX'
params.mac_address = ''
params.other_info = ''
params.serial_number = ''
params.ip_address = ''
params.ip_protocol = 0
params.timeout = 0
params.file = ''
    
board = BoardShim(0, params)
    
    
board.prepare_session()
# board.start_stream () # use this for default options
board.start_stream(45000, None)
time.sleep(2)
# data = board.get_current_board_data (256) # get latest 256 packages or less, doesnt remove them from internal buffer
data = board.get_board_data()  # get all data and remove it from internal buffer
board.stop_stream()
board.release_session()

print(data)

# set default display to show all rows and columns:
pd.set_option('display.max_columns', None)
pd.set_option('display.max_rows', None)



data = pd.DataFrame(data)

display(data)

#board.get_timestamp_channel(0)
#board.get_eeg_channels(0)
#board.get_sampling_rate(0)
#board.get_other_channels(0)
#board.get_accel_channels(0)
