import tensorflow as tf
import logging
import shutil
import imghdr
import os
import logging


import os
import tensorflow as tf


def validating_image()->None: 
    PARENT_DIR = "./data"
    #config["local_data_dir"]
    #PARENT_DIR = [data/cat, data/dog]
    print(f"{PARENT_DIR}This is parent directory")
    num_skipped = 0
    for folder_name in ("cat","dog"):
        folder_path = os.path.join(PARENT_DIR, folder_name)
        for fname in os.listdir(folder_path):
            fpath = os.path.join(folder_path, fname)
            try:
                fobj = open(fpath, "rb")
                is_jfif = tf.compat.as_bytes("JFIF") in fobj.peek(10)
            finally:
                fobj.close()

            if not is_jfif:
                num_skipped += 1
                # Delete corrupted image
                os.remove(fpath)

    print("Deleted %d images" % num_skipped)
                

def train_valid_generator(data_dir ,IMAGE_SIZE, BATCH_SIZE ,do_data_augmentation ) :
    datagenerator_kwargs = dict(
        rescale = 1./255, validation_split = 0.20,

    )
    dataflow_kwars = dict(
        target_size = IMAGE_SIZE,
        batch_size = BATCH_SIZE,
        interpolation = "bilinear"
    )
    valid_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
        **datagenerator_kwargs)

    valid_generator = valid_datagenerator.flow_from_directory(
        directory = data_dir,
        subset = "validation",
        shuffle = False,
        **dataflow_kwars

    )

    if do_data_augmentation:
        train_datagenerator = tf.keras.preprocessing.image.ImageDataGenerator(
            rotation_range = 40,
            horizontal_flip = True,
            width_shift_range = 0.2,
            height_shift_range = 0.2,
            shear_range = 0.2,
            zoom_range = 0.2,
            **datagenerator_kwargs)

        

        logging.info("data augmetation is used for training")

    else:
        train_datagenerator = valid_datagenerator
        logging.info("data augmentation is not used for training")

    train_generator = train_datagenerator.flow_from_directory(
        directory = data_dir,
        subset = "training",
        shuffle = True,
        **dataflow_kwars
    )
    logging.info("train and valid generator is created")
    
    return train_generator, valid_generator