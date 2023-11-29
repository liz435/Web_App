import h5py
import tensorflow as tf
import sys

def load_model():
    pkl_file= "network-snapshot-000060.pkl" # @param {type:"string"}
    folder_pkl_file = "00005-stylegan3-t-dataset-gpus1-batch32-gamma10" # @param {type:"string"}
    output_images_dest = "GAN/final" # @param {type:"string"}

    output_images_dest = "/content/drive/MyDrive/" + output_images_dest

    seed_min = 5000 # @param {type:"number"}
    num_images_generated = 10 # @param {type:"number"}
    seed_max = seed_min + num_images_generated

    url= trained_dataset + "/" + folder_pkl_file + "/" + pkl_file

    !python /content/stylegan3/gen_images.py \
    --network={url} \
    --outdir={output_images_dest} --seeds={seed_min}-{seed_max}

def test():
    print('z')