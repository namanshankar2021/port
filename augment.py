# !pip install Augmentor
import Augmentor
import os

def augment_images(input_folder, output_folder, target_count):
    # Create an Augmentor pipeline
    pipeline = Augmentor.Pipeline(input_folder, output_folder)

    # Add augmentation operations to the pipeline (example: rotation, flip)
    pipeline.rotate(probability=0.7, max_left_rotation=10, max_right_rotation=10)
    pipeline.flip_left_right(probability=0.5)

    # Set the number of output images to generate
    pipeline.sample(target_count - len(os.listdir(output_folder)))

if __name__ == "__main__":
    input_folder = "clicked"
    output_folder = "fake"
    target_count = 1200

    augment_images(input_folder, output_folder, target_count)
