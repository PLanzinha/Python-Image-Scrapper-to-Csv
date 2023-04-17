import os
from PIL import Image
import numpy as np
import pandas as pd


def images_to_csv(image_folder, csv, common_size=(64, 64)):
    image_data = []

    for root, dir, files in os.walk(image_folder):
        for filename in files:
            if filename.lower().endswith(('.jpg', '.jpeg', '.png', '.webp')):
                try:
                    image_path = os.path.join(root, filename)
                    image = Image.open(image_path).convert("L")
                    image = image.resize(common_size)

                    image_array = np.array(list(image.getdata()))

                    image_data.append(image_array)
                except Exception as error:
                    print(f"Error with the following file: '{filename}' - {error}")

    if not image_data:
        print("No images found in the folders and sub-folders")
        exit()

    data_array = np.array(image_data)

    columns = [f'pixel_{i}' for i in range(len(data_array[0]))]

    df = pd.DataFrame(data_array, columns=columns)
    df.to_csv(csv, index=False)


if __name__ == "__main__":
    input_folder = 'download'
    csv = input("Enter the file name.\n") + '.csv'

    if csv.endswith('.csv'):
        print("Enter a file name without the '.csv' extension please!")
    else:
        images_to_csv(input_folder, csv)

