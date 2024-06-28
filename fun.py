import os
import cv2
import face_recognition

train_images = []
test_images = []

for root, dirs, files in os.walk("lfw_more2"):
    for i, file in enumerate(files):
        image_path = os.path.join(root, file)
        image = cv2.imread(image_path)

        # Use the first image in each subfolder for encoding
        if i == 0:
            try:
                train_encodings = [face_recognition.face_encodings(image)[0]]
            except IndexError:
                print(f"Error encoding image {image_path}")
                break
        # Use the second image in each subfolder for testing
        elif i == 1:
            test_images.append(image)
    # Compare faces after processing second image in the folder
    if len(test_images) > 0:
        test_encodings = [face_recognition.face_encodings(image)[0] for image in test_images]
        matches = face_recognition.compare_faces(train_encodings, test_encodings, tolerance=0.464)
        for i, match in enumerate(matches):
            if match:
                print(f"Test image {i + 1} is a match.")
            else:
                print(f"Test image {i + 1} is not a match.")
        # Reset test_images list for next folder
        test_images = []
