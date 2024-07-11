# Use-a-Pre-trained-Image-Classifier-to-Identify-Dog-Breeds-project
In this project, we used a created image classifier to identify dog breeds. We were asked to focus on Python and not on the actual classifier.

 We utilized an image classification application employing a convolutional neural network (CNN) for this image classification task. CNNs excel at detecting features in images such as colors, textures, and edges, and then using these features to identify objects in the images. The CNN we used had already learned features from a vast dataset of 1.2 million images known as ImageNet. We explored three different CNN architectures (AlexNet, VGG, and ResNet) to determine which is best for the application, and provided a classifier function in classifier.py to classify images using these CNNs.

Some dog breeds bear a striking resemblance to each other. The algorithm's ability to distinguish between similar-looking dog breeds improves with exposure to a greater number of images of those breeds. We have identified several pairs of similar-looking dog breeds, including Great Pyrenees and Kuvasz, German Shepherd and Malinois, and Beagle and Walker Hound.

Note: You might need to install the libraries used in the project by running:

pip install package-name (replacing package name with the actual package name) in the (command prompt)
