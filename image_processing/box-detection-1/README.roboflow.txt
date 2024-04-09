
box detection - v1 2024-04-09 5:03pm
==============================

This dataset was exported via roboflow.com on April 9, 2024 at 12:24 PM GMT

Roboflow is an end-to-end computer vision platform that helps you
* collaborate with your team on computer vision projects
* collect & organize images
* understand and search unstructured image data
* annotate, and create datasets
* export, train, and deploy computer vision models
* use active learning to improve your dataset over time

For state of the art Computer Vision training notebooks you can use with this dataset,
visit https://github.com/roboflow/notebooks

To find over 100k other datasets and pre-trained models, visit https://universe.roboflow.com

The dataset includes 2397 images.
Box are annotated in Tensorflow TFRecord (raccoon) format.

The following pre-processing was applied to each image:
* Resize to 640x480 (Stretch)

The following augmentation was applied to create 3 versions of each source image:
* Random shear of between -14° to +14° horizontally and -14° to +14° vertically
* Random brigthness adjustment of between -23 and +23 percent
* Salt and pepper noise was applied to 1.13 percent of pixels

The following transformations were applied to the bounding boxes of each image:
* Random shear of between -10° to +10° horizontally and -10° to +10° vertically


