import tensorflow as tf
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.applications import MobileNetV2
from tensorflow.keras.layers import Dense, GlobalAveragePooling2D, Dropout
from tensorflow.keras.models import Model
from tensorflow.keras.optimizers import Adam
import os

# Dataset Paths
TRAIN_DIR = "dataset/PlantVillage/train"
VAL_DIR = "dataset/PlantVillage/val"

# Image Parameters
IMG_SIZE = (224, 224)
BATCH_SIZE = 64

# Training Data
train_datagen = ImageDataGenerator(
    rescale=1./255,
    rotation_range=20,
    zoom_range=0.2,
    horizontal_flip=True
)

# Validation Data
val_datagen = ImageDataGenerator(rescale=1./255)

train_generator = train_datagen.flow_from_directory(
    TRAIN_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

val_generator = val_datagen.flow_from_directory(
    VAL_DIR,
    target_size=IMG_SIZE,
    batch_size=BATCH_SIZE,
    class_mode='categorical'
)

# Load MobileNetV2
base_model = MobileNetV2(
    weights='imagenet',
    include_top=False,
    input_shape=(224,224,3)
)

base_model.trainable = False

# Custom Layers
x = base_model.output
x = GlobalAveragePooling2D()(x)
x = Dropout(0.3)(x)

predictions = Dense(
    train_generator.num_classes,
    activation='softmax'
)(x)

model = Model(
    inputs=base_model.input,
    outputs=predictions
)

# Compile
model.compile(
    optimizer=Adam(learning_rate=0.0001),
    loss='categorical_crossentropy',
    metrics=['accuracy']
)


# Train
history = model.fit(
    train_generator,
    validation_data=val_generator,
    epochs=2
)

# Create model folder
os.makedirs("model", exist_ok=True)
import json

class_names = list(train_generator.class_indices.keys())

with open("model/class_names.json","w") as f:
    json.dump(class_names,f)

# Save model
model.save("model/plant_model.keras")

print("\n===================================")
print("Model Saved Successfully!")
print("Location: model/plant_model.keras")
print("===================================")