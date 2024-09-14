import tensorflow as tf
import os
import time
import joblib
import logging
from src.utils.all_utils import get_timestamp


def create_and_save_checkpoint_callbacks(callbacks_dir, checkpoint_dir) :
    pass


def create_and_save_tensorboard_callbacks(callbacks_dir, tensorboard_log_dir) :
    unique_name = get_timestamp("tb_log")
    tb_running_log_dir = os.path.join(tensorboard_log_dir, unique_name)
    tensorboard_callbacks = tf.keras.callbacks.TensorBoard(log_dir = tb_running_log_dir)

    tb_callbacks_filepath = os.path.join(callbacks_dir, "tensorboard_cb.cb")
    joblib.dump(tensorboard_callbacks, tb_callbacks_filepath)

    logging.info(f"tensorborad callback is being saved at { tb_callbacks_filepath}")