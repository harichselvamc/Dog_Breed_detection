import streamlit as st
import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Load the trained model
model = tf.keras.models.load_model("dogclassification.h5")

# Define class names
class_names = {
        "0": "Afghan",
        "1": "African Wild Dog",
        "2": "Airedale",
        "3": "American Hairless",
        "4": "American Spaniel",
        "5": "Basenji",
        "6": "Basset",
        "7": "Beagle",
        "8": "Bearded Collie",
        "9": "Bermaise",
        "10": "Bichon Frise",
        "11": "Blenheim",
        "12": "Bloodhound",
        "13": "Bluetick",
        "14": "Border Collie",
        "15": "Borzoi",
        "16": "Boston Terrier",
        "17": "Boxer",
        "18": "Bull Mastiff",
        "19": "Bull Terrier",
        "20": "Bulldog",
        "21": "Cairn",
        "22": "Chihuahua",
        "23": "Chinese Crested",
        "24": "Chow",
        "25": "Clumber",
        "26": "Cockapoo",
        "27": "Cocker",
        "28": "Collie",
        "29": "Corgi",
        "30": "Coyote",
        "31": "Dalmation",
        "32": "Dhole",
        "33": "Dingo",
        "34": "Doberman",
        "35": "Elk Hound",
        "36": "French Bulldog",
        "37": "German Sheperd",
        "38": "Golden Retriever",
        "39": "Great Dane",
        "40": "Great Perenees",
        "41": "Greyhound",
        "42": "Groenendael",
        "43": "Irish Spaniel",
        "44": "Irish Wolfhound",
        "45": "Japanese Spaniel",
        "46": "Komondor",
        "47": "Labradoodle",
        "48": "Labrador",
        "49": "Lhasa",
        "50": "Malinois",
        "51": "Maltese",
        "52": "Mex Hairless",
        "53": "Newfoundland",
        "54": "Pekinese",
        "55": "Pit Bull",
        "56": "Pomeranian",
        "57": "Poodle",
        "58": "Pug",
        "59": "Rhodesian",
        "60": "Rottweiler",
        "61": "Saint Bernard",
        "62": "Schnauzer",
        "63": "Scotch Terrier",
        "64": "Shar_Pei",
        "65": "Shiba Inu",
        "66": "Shih-Tzu",
        "67": "Siberian Husky",
        "68": "Vizsla",
        "69": "Yorkie"
}
st.markdown(
    """
    <style>
    .centered-title {
        text-align: center;
    }
   
    </style>
    """,
    unsafe_allow_html=True,
)
st.title("Dog Breed Detection App")

# Upload an image for classification
uploaded_image = st.file_uploader("Upload a dog image", type=["jpg", "png", "jpeg"])

if uploaded_image is not None:
    image = tf.image.decode_image(uploaded_image.read(), channels=3)
    image = tf.image.resize(image, (224, 224))
    image = np.expand_dims(image, axis=0) / 255.0

    st.image(uploaded_image, caption="Uploaded Image", use_column_width=True)
    if st.button("Classify"):
        prediction = model.predict(image)
        predicted_class = np.argmax(prediction, axis=-1)
        st.write(f"Predicted Breed: {class_names[str(predicted_class[0])]}")
