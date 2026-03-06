from pathlib import Path

import numpy as np
from PIL import Image
from tensorflow.keras.applications.mobilenet_v2 import (
    MobileNetV2,
    decode_predictions,
    preprocess_input,
)

MODEL = MobileNetV2(weights="imagenet")


def map_label_to_category(label: str) -> str:
    label = label.lower()

    cat_keywords = [
        "cat", "kitten", "tabby", "lynx", "tiger", "lion",
        "jaguar", "leopard", "cheetah", "cougar", "snow_leopard"
    ]

    dog_keywords = [
        "dog", "puppy", "retriever", "terrier", "spaniel", "hound",
        "shepherd", "poodle", "bulldog", "beagle", "chihuahua",
        "pug", "boxer", "doberman", "rottweiler", "collie",
        "husky", "malamute", "mastiff", "dachshund", "setter",
        "pinscher", "corgi"
    ]

    bird_keywords = [
        "bird", "hen", "cock", "eagle", "owl", "vulture", "kite",
        "parrot", "finch", "robin", "magpie", "jay", "bulbul",
        "ostrich"
    ]

    car_keywords = [
        "car", "cab", "jeep", "limousine", "minivan",
        "sports_car", "convertible", "racer", "model_t"
    ]

    bicycle_keywords = [
        "bicycle", "bike", "mountain_bike", "unicycle"
    ]

    motorcycle_keywords = [
        "motorcycle", "moped", "motor_scooter"
    ]

    person_keywords = [
        "person", "man", "woman", "boy", "girl", "bride", "groom",
        "scuba_diver"
    ]

    if any(word in label for word in cat_keywords):
        return "Cat"

    if any(word in label for word in dog_keywords):
        return "Dog"

    if any(word in label for word in bird_keywords):
        return "Bird"

    if any(word in label for word in car_keywords):
        return "Car"

    if any(word in label for word in bicycle_keywords):
        return "Bicycle"

    if any(word in label for word in motorcycle_keywords):
        return "Motorcycle"

    if any(word in label for word in person_keywords):
        return "Person"

    return "Other"


def predict_image(image_path):
    image_path = Path(image_path)

    img = Image.open(image_path).convert("RGB")
    img = img.resize((224, 224))

    arr = np.array(img, dtype=np.float32)
    arr = np.expand_dims(arr, axis=0)
    arr = preprocess_input(arr)

    predictions = MODEL.predict(arr, verbose=0)
    decoded = decode_predictions(predictions, top=20)[0]

    grouped_scores = {}

    for _, label, score in decoded:
        category = map_label_to_category(label)
        probability = float(score) * 100

        grouped_scores[category] = grouped_scores.get(category, 0) + probability

    
    filtered_scores = {
        category: value
        for category, value in grouped_scores.items()
        if category != "Other"
    }

    if filtered_scores:
        best_label = max(filtered_scores, key=filtered_scores.get)
        total_known = sum(filtered_scores.values())
        display_probability = round((filtered_scores[best_label] / total_known) * 100, 2)
    else:
        best_label = "Other"
        display_probability = round(grouped_scores.get("Other", 0), 2)

    return {
        "label": best_label,
        "probability": display_probability,
    }