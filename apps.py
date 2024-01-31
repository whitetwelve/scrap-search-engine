import streamlit as st
import numpy as np
import cv2
import tensorflow as tf
from PIL import Image
import requests
from bs4 import BeautifulSoup
# from functions.instagram import get_bing_search_link, get_first_instagram_link

import warnings
warnings.filterwarnings("ignore")

# Load the trained TensorFlow model
model_path = "models/keras_model.h5"
model = tf.keras.models.load_model(model_path)

predicted_class = None 
# Load the labels
class_labels = open("labels.txt", "r").readlines()
st.title("Leaders image recognition")

labels = ['Fumio Kishida', 'Joe Biden', 'Narendra Modi', 'Scott Morrison']

st.write("Lihat labels")

labels_content = '\n'.join(labels)

# Download button for labels.txt
st.download_button('Download labels terlebih dahulu', labels_content, key='download_labels_button')

# Add an option to choose between image upload and camera capture
option = st.sidebar.selectbox("Pilih opsi yang ada ..", ("Upload Image", "Capture from Camera"))

if option == "Upload Image":
    uploaded_image = st.file_uploader("Masukkan gambar (jpg, png, jpeg) only!", type=["jpg", "png", "jpeg"])

    if uploaded_image is not None:
        image = Image.open(uploaded_image)
        st.image(image, caption="Uploaded Image", use_column_width=True)

        # Preprocess the image
        image_array = np.array(image.resize((224, 224))) / 255.0
        image_array = np.expand_dims(image_array, axis=0)

        # Make predictions
        prediction = model.predict(image_array)
        predicted_class_index = np.argmax(prediction)
        predicted_class = class_labels[predicted_class_index]
        predicted_class = " ".join(predicted_class.split()[1:])
        confidence = prediction[0][predicted_class_index]

        st.write(f"Dia adalah : {predicted_class}")
        st.write(f"Akurasi (%): {confidence:.2%}")  # Display confidence as percentage with 2 decimal places

elif option == "Capture from Camera":
    st.write("Camera Capture Mode")

    # Open the camera
    cap = cv2.VideoCapture(0)  # 0 indicates the default camera

    if not cap.isOpened():
        st.write("Error: Could not open camera.")
        st.stop()

    stop_camera_button_key = "stop_camera_button"  # Removed UUID to avoid unnecessary complexity

    while True:
        ret, frame = cap.read()

        if not ret:
            st.write("Error: Could not read frame from camera.")
            break

        # Display the captured frame
        st.image(frame, channels="BGR", use_column_width=True, caption="Camera Capture")  # Use BGR channels for OpenCV image

        # Preprocess the captured frame
        resized_frame = cv2.resize(frame, (224, 224)) / 255.0
        image_array = np.expand_dims(resized_frame, axis=0)

        # Make predictions
        prediction = model.predict(image_array)
        predicted_class_index = np.argmax(prediction)
        predicted_class = class_labels[predicted_class_index]
        confidence = prediction[0][predicted_class_index]

        st.write(f"Dia adalah: {predicted_class}")
        st.write(f"Akurasi (%): {confidence:.2%}")  # Display confidence as percentage with 2 decimal places

        if st.button("Stop Camera", key=stop_camera_button_key):
            break

    # Release the camera
    cap.release()

name = predicted_class

def get_bing_search_link(name):
    formatted_name = name.replace(' ', '%20')
    url = "https://www.bing.com/search?q=" + formatted_name + "instagram"
    return url

def get_first_instagram_link(search_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }

    content = requests.get(search_url, headers=headers).text
    soup = BeautifulSoup(content, 'html.parser')

    # Find the first search result link
    first_link_container = soup.find('li', class_='b_algo')
    first_link = first_link_container.find('a')['href'] if first_link_container else None

    # Check if the link contains 'https://www.instagram.com'
    if first_link and 'https://www.instagram.com' in first_link:
        return first_link
    else:
        return None

# Get the Bing search URL
search_url = get_bing_search_link(name)

# Get the first Instagram link from the search results
first_instagram_link = get_first_instagram_link(search_url)

if first_instagram_link:
    st.write("Instagram:", first_instagram_link)
else:
    st.write(f"Instagram {name} tidak ditemukan")


def get_bing_search_link(name):
    formatted_name = name.replace(' ', '%20')
    url = "https://www.google.com/search?q=" + formatted_name + "facebook"
    return url

def get_first_facebook_link(search_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }

    content = requests.get(search_url, headers=headers).text
    soup = BeautifulSoup(content, 'html.parser')

    # Find the first search result link
    first_link_container = soup.find('li', class_='b_algo')
    first_link = first_link_container.find('a')['href'] if first_link_container else None

    # Check if the link contains 'https://www.facebook.com'
    if first_link and 'https://www.facebook.com' in first_link:
        return first_link
    else:
        return None

# Get the Bing search URL
search_url = get_bing_search_link(name)

# Get the first Instagram link from the search results
first_facebook_link = get_first_facebook_link(search_url)

if first_facebook_link:
    st.write("Facebook :", first_facebook_link)
else:
    st.write(f"facebook {name} tidak ditemukan")



def get_bing_search_link(name):
    formatted_name = name.replace(' ', '%20')
    url = "https://www.bing.com/search?q=" + formatted_name + "twitter"
    return url

def get_first_twitter_link(search_url):
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.82',
    }

    content = requests.get(search_url, headers=headers).text
    soup = BeautifulSoup(content, 'html.parser')

    # Find the first search result link
    first_link_container = soup.find('li', class_='b_algo')
    first_link = first_link_container.find('a')['href'] if first_link_container else None

    # Check if the link contains 'https://www.twitter.com'
    if first_link and 'https://twitter.com/' in first_link:
        return first_link
    else:
        return None

# Get the Bing search URL
search_url = get_bing_search_link(name)

# Get the first twitter link from the search results
first_twitter_link = get_first_twitter_link(search_url)

if first_twitter_link:
    st.write("Twitter :", first_twitter_link)
else:
    st.write(f"twitter {name} tidak ditemukan")
