import numpy as np
from PIL import Image
import random
import cv2
import os


# The class of Network without change

class NeuralNetwork:
    def __init__(self):
        self.w1 = np.random.randn(784, 64) * 0.1
        self.w2 = np.random.randn(64, 10) * 0.1
        self.lr = 0.05

    def sigmoid(self, x) : return 1 / (1 + np.exp(-x))
    def sigmoid_deriv(self, x) : return x * (1 - x)  # مشتق sigmoid

    def train(self, x, y_target):
        h = self.sigmoid(np.dot(x, self.w1))
        out = self.sigmoid(np.dot(h, self.w2))

        error = y_target - out
        d_out = error * self.sigmoid_deriv(out)  #گرادیان لایه خروجی
        error_h = d_out.dot(self.w2.T)
        d_h = error_h * self.sigmoid_deriv(h)

        self.w2 += h.T.reshape(64, 1).dot(d_out.reshape(1, 10)) * self.lr
        self.w1 += x.reshape(784, 1).dot(d_h.reshape(1, 64)) * self.lr

    
    def predict(self, x):
        h = self.sigmoid(np.dot(x, self.w1))
        out = self.sigmoid(np.dot(h, self.w2))
        
        return np.argmax(out)


def augmented_data(image_path, label):
    img_orig = Image.open(image_path)
    img_orig = img_orig.convert("L")
    arr = np.array(img_orig)

    _, arr= cv2.threshold(arr, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
    img_orig = Image.fromarray(arr)

    mask = arr < 240

    ys, xs = np.where(mask)
    if len(xs) > 0 and len(ys) > 0:
        left = xs.min()
        right = xs.max()
        top = ys.min()
        botton = ys.max()
        img_orig = img_orig.crop((left, top, right + 1, botton + 1))
    
    img_orig.thumbnail((24, 24))
    canvas = Image.new("L", (28, 28), 255)
    x = (28 - img_orig.width) // 2
    y = (28 - img_orig.height) // 2
    canvas.paste(img_orig, (x, y))
    img_orig = canvas
    
    data = []

    target = np.zeros(10)
    target[label] = 1
    arr = (255 - np.array(img_orig)) / 255.0
    data.append((arr.flatten(), target))
    return data
'''
    for _ in range(num_samples):
        img = img_orig.rotate(random.uniform(-15, 15), fillcolor=255)
        scale = random.uniform(0.8, 1.0)
        img = img.resize((int(28*scale), int(28*scale)))

        canvas = Image.new("L", (28, 28), 255)
        x = (28 - img.width) // 2
        y = (28 - img.height) // 2
        #canvas.paste(img, (random.randint(-2, 4), random.randint(-2, 4)))
        canvas.paste(img, (x, y))
        arr = (255 - np.array(canvas)) / 255.0

        #if label == 1 and _ == 1:
        #    Image.fromarray(
        #        (arr * 255 - 255).astype(np.uint8)
        #    ).save("B_After_augment.png")
#
        #if random.random() < 0.001:
        #    debug_image = Image.fromarray(
        #        (arr * 255 - 255).astype(np.uint8)
        #    )
        #    debug_image.save("debug_augmented3.jpg")
      
        target = np.zeros(10)
        target[label] = 1

        data.append((arr.flatten(), target))

    return data
'''
# اجرای اصلی
# بارگذاری و پردازش اولیه همه عکسها

all_samples = []
print("Editing.....")
classes = ["الف", "ب", "پ", "ت","ث", "ج", "چ", "ح", "خ", "د"]
base_dir = "."

for label, cls in enumerate(classes):
    class_dir = os.path.join(base_dir, cls)
    for filename in os.listdir(class_dir):
        if filename.lower().endswith((".jpg", ".png", ".jpeg")):
            full_path = os.path.join(class_dir, filename)

    #print(filename, os.path.exists(filename))
            if os.path.exists(full_path):
                augmented = augmented_data(full_path, label)
                all_samples.extend(augmented)
            else:
                print(f"warning: {filename} does not exist!!")

# تقسیم داده ها به دو بخش اموزش و ازمون

random.shuffle(all_samples)

train_data = all_samples[:390]
test_data = all_samples[390:]

print("train_data = ", len(train_data))
print("test_data = ", len(test_data))

#random.shuffle(all_samples)
#train_data = all_samples

# اموزش شبکه

nn = NeuralNetwork()
epochs = 400

for epoch in range(epochs):
    random.shuffle(train_data)
    for x, y_target in train_data:
        nn.train(x, y_target)

    if (epoch + 1) % 400 == 0:
        print("Epochs done!!")

print("Train complted!!")

print("\nPer-class accuracy:")

for class_idx, class_name in enumerate(classes):

    total = 0
    correct = 0

    for x, y in train_data:

        if np.argmax(y) == class_idx:
            total += 1

            if nn.predict(x) == class_idx:
                correct += 1

    if total > 0:
        print(
            f"{class_name}: "
            f"{100 * correct / total:.2f}% "
            f"({correct}/{total})"
        )

correct = 0

for x, y in train_data:
    prediction = nn.predict(x)
    if prediction == np.argmax(y):
        correct += 1
#print("Train Accuracy :", correct / len(train_data) * 100)

#ارزیابی شبکه با داده های ازمون

correct_predictions = 0
for x, y_true in test_data:
    prediction = nn.predict(x)
    if prediction == np.argmax(y_true):
        correct_predictions += 1
#***'''

#print("all_samples =", len(all_samples))
#
#split_index = int(len(all_samples) * 0.8)
#
#train_data = all_samples[:split_index]
#test_data = all_samples[split_index:]
#
#print("train_data =", len(train_data))
#print("test_data =", len(test_data))

#print("train_data = ", len(train_data))

#****

accuracy = (correct_predictions / len(test_data)) * 100
print(f"Network accuracy : {accuracy:.2f}%")

#تابع تست دستی

def test_maual(nn, image_path):
    try:
        img = Image.open(image_path)
        img = img.convert("L")
        arr = np.array(img)
        #****
        _, arr= cv2.threshold(arr, 0, 255, cv2.THRESH_BINARY + cv2.THRESH_OTSU)
        img = Image.fromarray(arr)

        mask = arr < 240

        ys, xs = np.where(mask)
        if len(xs) > 0 and len(ys) > 0:
            left = xs.min()
            right = xs.max()
            top = ys.min()
            botton = ys.max()
            img = img.crop((left, top, right + 1, botton + 1))
        
        img.thumbnail((24, 24))
        canvas = Image.new("L", (28, 28), 255)
        x = (28 - img.width) // 2
        y = (28 - img.height) // 2
        canvas.paste(img, (x, y))
        img = canvas
        #*********
        img.save('debug_test3.jpg')

        print("saved_debug_test.jpg")
        #*********
        arr = (255 - np.array(img)) / 255.0
        arr = arr.flatten()

        predict_digit = nn.predict(arr)
        print(f"The photo {os.path.basename(image_path)} is {classes[predict_digit]} ")
        return predict_digit
    except FileExistsError:
        print(f"{image_path} does not exist!!")
        return None
    except Exception as e:
        print(f"error {image_path} : {e}")
        return None
    
test_maual(nn, 'test3.jpg')


