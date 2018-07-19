# Watson Visual Recognition Tutorial: Python

## Installing Dependencies
This part represents how to use python programming and utilize the Watson visual recognition. The prerequisites will be &quot;Watson Developer Cloud SDK&quot;. In order to install it, use pip3 or easy\_install :
```python
Pip3 install --upgrade watson-developer-cloud
```
or

easy\_install --upgrade watson-developer-cloud

## Accessing the Visual Recognition Service
In order to access the service (APIs) the credentials are required.  For getting the service credentials, the user needs to create the service (Visual Recognition Service) through the [IBM cloud](https://console.bluemix.net).

1. Log in to the IBM cloud
2. Go to the catalog
3. Select Watson visual recognition service
4. Choose the name and create the service
5. Now in the next page the user can see the credentials &quot;apikey, etc.&quot;

**Note:  ** Instantiation with API key works only with Visual Recognition service instances created before May 23, 2018. Visual Recognition instances created after May 22 use IAM.
```python
from watson_developer_cloud import VisualRecognitionV3
# In the constructor
visual_recognition = VisualRecognitionV3(version='2018-05-22', api_key='<api_key>')


# After instantiation
visual_recognition = VisualRecognitionV3(version='2018-05-22')
visual_recognition.set_api_key('<api_key>')
```
After installing the IBM cloud SDK, the user can call the build-in service or create the custom classification from the python and use them.

**Face Detection:**

In this part the face detection service is used to detect the human faces. A python code for utilizing this service will be as follows:
```python
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches

test_url='https://www.runscope.com/static/img/public/customer-portrait-human-api.png'

# creating a VR instance

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_api_key='…………')

url_result = visual_recognition.detect_faces(parameters=json.dumps({'url': test_url}))

print(json.dumps(url_result, indent=2))
```
More detail about “visual_recognition.detect_faces()” function:
```python
def detect_faces(self,
                     images_file=None,
                     parameters=None,
                     images_file_content_type=None,
                     images_filename=None,
                     url=None,
                     **kwargs);
```
Analyze and get data about faces in images. Responses can include estimated age and gender, and the service can identify celebrities. This feature uses a built-in classifier, so you do not train it on custom classifiers. The Detect faces method does not support general biometric facial recognition.

        :param file images_file: An image file (.jpg, .png) or .zip file with images. Include no more than 15 images. You can also include images with the `url` property in the **parameters** object.  All faces are detected, but if there are more than 10 faces in an image, age and gender confidence scores might return scores of 0.
        :param str parameters: (Deprecated) A JSON object that specifies a single image (.jpg, .png) to analyze by URL. The parameter can be sent as a string or a file.  Example: `{\"url\":\"http://www.example.com/images/myimage.jpg\"}`.
        :param str images_file_content_type: The content type of images_file.
        :param str images_filename: The filename for images_file.
        :param str url: The URL of an image to analyze. Must be in .gif, .jpg, .png, or .tif format. The minimum recommended pixel density is 32X32 pixels per inch, and the maximum image size is 10 MB. Redirects are followed, so you can use a shortened URL.  You can also include images with the **images_file** parameter.
        :param dict headers: A `dict` containing the request headers
        :return: A `dict` containing the `DetectedFaces` response.
        :rtype: dict

Matplotlib or the other libraries can be used to plot the results. In order to install Matplotlib visit [Matplolib installation instructions](https://matplotlib.org/users/installing.html).
```python
fig,ax = plt.subplots(1)
for i in range(0,len(url_result['images'][0]['faces'])):
    face=url_result['images'][0]['faces'][i]
    faceloc = face['face_location']
    x,y,w,h = faceloc['left'],faceloc['top'],faceloc['width'],faceloc['height']
# Create a Rectangle patch
    rect = patches.Rectangle((x,y),w,h,linewidth=1,edgecolor='r',facecolor='none')
    #img=mpimg.imread('your_image.png')
    ax.add_patch(rect)
    # Create figure and axes

img = mpimg.imread(test_url)
ax.imshow(img)
plt.show()
```
By running the code the result will be as follows:
``` python
{
  "images": [
    {
      "faces": [
        {
          "age": {
            "min": 41,
            "max": 44,
            "score": 0.8015439
          },
          "face_location": {
            "height": 119,
            "width": 101,
            "left": 95,
            "top": 55
          },
          "gender": {
            "gender": "MALE",
            "score": 0.9999509
          }
        }
      ],
      "source_url": "https://www.runscope.com/static/img/public/customer-portrait-human-api.png",
      "resolved_url": "https://www.runscope.com/static/img/public/customer-portrait-human-api.png"
    }
  ],
  "images_processed": 1
}
```

 ![](https://github.ibm.com/Evan-Woods/Tutorials/blob/master/VisualRec_Images/Face_Rec_Python.PNG)


**Creating Visual Recognition Custom classifier:**

This part presents the custom classifier using Watson Visual Recognition service. In order to start with the custom classifier, first the user need to prepare the images corresponding to each classes. (Ten images for each class) and put the images into the .zip file. Then the following python code will create the classes and train the model.
```python
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

with open('./beagle.zip', 'rb') as beagle, open(
        './golden-retriever.zip', 'rb') as goldenretriever, open(
            './husky.zip', 'rb') as husky, open(
                './cats.zip', 'rb') as cats:
    model = visual_recognition.create_classifier(
        'dogs',
        beagle_positive_examples=beagle,
        goldenretriever_positive_examples=goldenretriever,
        husky_positive_examples=husky,
        negative_examples=cats)
print(json.dumps(model, indent=2))
```

**The returned result from Watson will be:**

 ![](/VisualRec_Images/Custom_Classifier_Python.png)

**Note:**

- The classifier\_id is the ID that user can call the class and test it.
- By each executing the code, Watson creates the classifier with the new classifier\_id. So if the user wants to change the classifier, it is better to remove the previous classifier and train the model again. (Training process should be done only once)



After training the model, in order to test the model the user can call the created classifier by using the following codes:
```python
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np
import cv2


with open('C:/Users/hmohamm2/Desktop/Test_Image.jpeg', 'rb') as images_file:
	results_data  = visual_recognition.classify(
		images_file,
		threshold='0.6',
		classifier_ids='dogs_992830017')
	print(json.dumps(results_data , indent=2))

#The result from Watson will be as follows:

classifiers_result =  results_data['images'][0]['classifiers']
classes_result = classifiers_result[0]['classes']

fig,ax = plt.subplots(1)
font = cv2.FONT_HERSHEY_SIMPLEX

img = mpimg.imread('C:/Users/hmohamm2/Desktop/Test_Image.jpeg')
cv2.putText(img,classes_result[0]['class'], (20,30), font, 1, (0, 0, 255), thickness=3)
cv2.putText(img,str(classes_result[0]['score']), (20,60), font, 1, (0, 0, 255), thickness=3)
	
ax.imshow(img)
plt.show()

```

 ![](/VisualRec_Images/Custom_classification_Results_Dog.PNG)

**Real-Time Face Detection:**

The sample code for real time face detection will be as follows. In this code the camera frame is captured by the openCV library and then is applied to the built-in face detection. The returned results from the Watson in analyzed and plotted.

```python
from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np
import cv2  

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_api_key='…………')
counter=0    
camera = cv2.VideoCapture(0)
fig,ax = plt.subplots(1)


while(True):

      return_value, image = camera.read()
      cv2.imwrite('opencv'+str(0)+'.png', image)
url_result                            =visual_recognition.detect_faces(images_file=open('opencv0.png','rb'))

for i in range(0,len(url_result['images'][0]['faces'])):
face=url_result['images'][0]['faces'][i]
faceloc = face['face_location']
x,y,w,h = faceloc['left'],faceloc['top'],faceloc['width'],faceloc['height']
		
# Create a Rectangle patch around the detected face
rect = cv2.rectangle(image,(x,y),(x+w,y+h),(0, 255, 0), thickness=3)
		
# Add the corresponding face information to the image 
font = cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(image,face['gender']['gender'], (x,y+w), font, 1, (0, 255, 0),thickness=3)
		
cv2.putText(image,"Age (min):", (x,y+w+30), font, 1, (0, 0, 255),thickness=3)
		
cv2.putText(image,str(face['age']['min']), (x+180,y+w+30), font, 1, (0, 0, 255), thickness=3)
		
cv2.putText(image,"Age (max):", (x,y+w+60), font, 1, (0, 0, 255),thickness=3)

cv2.putText(image,str(face['age']['max']), (x+180,y+w+60), font, 1, (0, 0, 255), thickness=3)

cv2.imshow("frame", image)


if cv2.waitKey(1) & 0xFF == ord('q'):
		break
```
