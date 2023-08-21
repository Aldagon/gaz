import tensorflow as tf
from tensorflow import keras
import numpy as np

# Создаем набор данных для обучения и тестирования нейронной сети
# Пример: обучим сеть на распознавание рукописных цифр из набора данных MNIST

# Загружаем данные
mnist = keras.datasets.mnist
(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

# Нормализуем данные
train_images, test_images = train_images / 255.0, test_images / 255.0

# Создаем модель нейронной сети
model = keras.Sequential([
    keras.layers.Flatten(input_shape=(28, 28)),     # Входной слой: изображения 28x28 пикселей
    keras.layers.Dense(128, activation='relu'),     # Скрытый слой с 128 нейронами и функцией активации ReLU
    keras.layers.Dropout(0.2),                     # Слой для предотвращения переобучения (dropout)
    keras.layers.Dense(10, activation='softmax')   # Выходной слой с 10 нейронами (10 классов) и softmax для классификации
])

# Компилируем модель
model.compile(optimizer='adam',
              loss='sparse_categorical_crossentropy',
              metrics=['accuracy'])

# Обучаем модель
model.fit(train_images, train_labels, epochs=5)

# Оцениваем точность модели
test_loss, test_acc = model.evaluate(test_images, test_labels)
print("\nТочность на тестовых данных:", test_acc)
