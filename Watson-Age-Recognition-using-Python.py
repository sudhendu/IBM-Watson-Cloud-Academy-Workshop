
#**Real-Time Face Detection:**
'''
The sample code for real time face detection will be as follows. In this code the camera frame is captured by the openCV library and then is applied to the built-in face detection. The returned results from the Watson in analyzed and plotted.
'''

from __future__ import print_function
import json
from os.path import join, dirname
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException

import tkinter
import matplotlib.pyplot as plt
import matplotlib.image as mpimg
import matplotlib.patches as patches
import numpy as np
import cv2  

credentials = {
  "apikey": "Ke2LxGiWbq9RrPhJTpFIicaCKMPoo5IjbsJoz3ALFUQu",
  "iam_apikey_description": "Auto generated apikey during resource-key operation for Instance - crn:v1:bluemix:public:watson-vision-combined:us-south:a/da20230063068158ff98a08cdacec83e:89391483-d1f5-4633-a7b6-b2457dd318de::",
  "iam_apikey_name": "auto-generated-apikey-67993ac6-2429-4566-acf4-f754f8d555d4",
  "iam_role_crn": "crn:v1:bluemix:public:iam::::serviceRole:Manager",
  "iam_serviceid_crn": "crn:v1:bluemix:public:iam-identity::a/da20230063068158ff98a08cdacec83e::serviceid:ServiceId-1e617c12-fd1f-420f-8e3c-8b3c4528bc5f",
  "url": "https://gateway.watsonplatform.net/visual-recognition/api"
} 

visual_recognition = VisualRecognitionV3(
    version='2018-03-19',
    url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_api_key=credentials['apikey'])
counter=0    
camera = cv2.VideoCapture(0)
fig,ax = plt.subplots(1)

while(True):
	return_value, image = camera.read()
	cv2.imwrite('opencv'+str(0)+'.png', image)
	url_result=visual_recognition.detect_faces(images_file=open('opencv0.png','rb'))

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
			
		cv2.putText(image,str(face['age']['min']), (x+180,y+w+30), font, 1, (0, 0, 255), 	thickness=3)
			
		cv2.putText(image,"Age (max):", (x,y+w+60), font, 1, (0, 0, 255),thickness=3)

		cv2.putText(image,str(face['age']['max']), (x+180,y+w+60), font, 1, (0, 0, 255), thickness=3)

		cv2.imshow("frame", image)


	if cv2.waitKey(1) & 0xFF == ord('q'):
			break

