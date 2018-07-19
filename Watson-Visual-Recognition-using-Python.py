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
    iam_api_key='apikey')

url_result = visual_recognition.detect_faces(parameters=json.dumps({'url': test_url}))

print(json.dumps(url_result, indent=2))
