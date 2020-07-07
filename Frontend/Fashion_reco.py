import pandas as pd
import numpy as np
import tensorflow as tf
from tensorflow.keras import Model
from tensorflow.keras.applications.resnet50 import ResNet50
from tensorflow.keras.preprocessing import image
from tensorflow.keras.applications.resnet50 import preprocess_input, decode_predictions
from tensorflow.keras.layers import GlobalMaxPooling2D
import ipyplot
from numpy import dot
from numpy.linalg import norm
import operator
from PIL import Image




def model_start():

    tf.__version__

    #img_width, img_height, _ = load_image("15970.jpg").shape
    img_width, img_height = 80, 60
    # Pre-Trained Model
    base_model = ResNet50(weights='imagenet',
                          include_top=False,
                          input_shape=(img_width, img_height, 3))
    base_model.trainable = False

    # Add Layer Embedding
    model = tf.keras.Sequential([
        base_model,
        GlobalMaxPooling2D()
    ])
    emb_dict = np.load('embed_dict.npy', allow_pickle='TRUE').item()
    model.summary()
    return model, emb_dict


def get_embedding(model, img_path):
    # Reshape
    img = image.load_img(img_path, target_size=(80, 60))
    # img to Array
    x = image.img_to_array(img)
    # Expand Dim (1, w, h)
    x = np.expand_dims(x, axis=0)
    # Pre process Input
    x = preprocess_input(x)
    return model.predict(x).reshape(-1)


def query(img_path, n, emb_dict, model, save_dir):
    emb_query = get_embedding(model, img_path)
    dist = {}
    max_dist = 10000
    b = emb_query
    for key in emb_dict:
        a = emb_dict[key]
        distance = 1 - dot(a, b)/(norm(a)*norm(b))
        if len(dist.keys()) < n:
            dist[key] = distance
            max_dist = max(dist.values())
            continue
        if distance >= max_dist:
            continue
        dist[key] = distance
        keyMax = max(dist.items(), key=operator.itemgetter(1))[0]
        dist.pop(keyMax)
    #sort_orders = sorted(dist.items(), key=lambda x: x[1], reverse=True)
    imgs = []
    for k in dist.keys():
        imgs.append("dataset/images/" + k)

    #pyplot.plot_images(imgs, max_images=20, img_width=150)
    print(imgs)

    count = 0
    for img in imgs:
        count += 1
        im = Image.open(img)
        im.save(save_dir + "reco_"+str(count)+".png")
    print(count)


def main():
    save_dir = "/home/hari/Desktop/Hari/CS endeavours/Walmart-Hackathon/Frontend/static/images/"
    model, emb_dict = model_start()
    x = "test_images/test3.jpg"
    ipyplot.plot_images([x], max_images=20, img_width=150)
    query(x, 12, emb_dict, model, save_dir)


if __name__ == '__main__':
    main()
