Dermatological diseases are the most prevalent diseases worldwide. Despite being common, its diagnosis is extremely difficult and requires extensive experience in the domain. In this project, we provide an approach to detect various kinds of these diseases. We use a dual stage approach which effectively combines Computer Vision and Machine Learning on clinically evaluated histopathological attributes to accurately identify the disease. In the first stage, the image of the skin disease is subject to various kinds of pre-processing techniques followed by feature extraction. The second stage involves the use of Machine learning algorithms to identify diseases based on the histopathological attributes observed on analysing of the skin. Upon training and testing for the six diseases, the system produced an accuracy of up to 77.77 percent. This paper proposes a skin disease detection method based on image processing techniques. This method is mobile based and hence very accessible even in remote areas and it is completely non-invasive to patient’s skin. The patient provides an image of the infected area of the skin as an input to the prototype. Image processing techniques are performed on this image and the detected disease is displayed at the output. The proposed system is highly beneficial in rural areas where access to dermatologists is limited.

OBJECTIVES:
The objective of this project can be summarized into the following points: 
1. Develop machine learning website that in general, has the ability to: 
• Determine the affected areas in the image. 
• Determine the disease in the specified region. 
2. Develop a web interface that: 
• Capture the image, send it to the server and receiving the results back.

DATASET:
HAM10000
The HAM10000 dataset is where we will get the images needed to train our model. This is a collection of around 10,000 labelled images of 7 different types of skin lesions.
These are the types of lesions that are found in the dataset:
•	Actinic Keratoses
•	Basal Cell Carcinoma
•	Benign Keratosis
•	Dermatofibroma
•	Malignant Melanoma
•	Melanocytic Nevi
•	Vascular Lesions 

DISCUSSION: 
 Here is the web implementation of the model, I have provided a description of the project as well as some information on the types of skin assessment analysis, sourced from here.
In case if you don’t have any images to test it with, I have also provided some sample images for each of the classes. The model doesn’t fare too well with pictures of lesions that have a non-skin background because it hasn’t been trained with images such as that. As I said above, the accuracy, calculated from the HAM10000 dataset is around 77.77%, and while this is definitely not adequate for medical use, a professional backing and larger datasets would result in a model that would be ready for clinical use and at-home diagnosis.

The implications of technology such as this are huge. We could potentially eradicate misdiagnosis in clinics by using AI technology, such as this. The more data and support that we have for this, the more it can grow and become more accurate. With only 10,000 images, we achieved an accuracy of around 77.77%, but imagine how much better it could be if we had millions of images. These models would have the skills of a doctor that had literally seen and learned from millions of images. Can you imagine that?


