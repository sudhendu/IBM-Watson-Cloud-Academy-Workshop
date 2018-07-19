## Visual Recognition Using Command Line Interface
In order to utilize Watson visual recognition using CLI, the user first needs to create a visual recognition service and keep the API credential key. (More detail about how to create a service using CLI can be found **here** ) After creating the visual recognition service, **the user should open an Anaconda Prompt and change the directory to the desired path**. In order to use the service using the CLI we have:

1. **Classify an image using built in classification service**

In this part the user should issue the following command and replace {your\_api\_key} with the service credential you kept earlier and {IMAGE\_NAME} with your image name. Also in order to classify an image using a built in service use {classify} in the command.
```curl
curl -X POST -u "apikey:YOUR_API_Key" --form "images_file=@IMAGE_NAME.jpg" https://gateway.watsonplatform.net/visual-recognition/api/v3/classify?version=2018-03-19
```
By running the command the result will be as follows:
```python
{
    "images": [
        {
            "classifiers": [
                {
                    "classifier_id": "default",
                    "name": "default",
                    "classes": [
                        {
                            "class": "banana",
                            "score": 0.562,
                            "type_hierarchy": "/fruit/banana"
                        },
                        {
                            "class": "fruit",
                            "score": 0.788
                        },
                        {
                            "class": "diet (food)",
                            "score": 0.528,
                            "type_hierarchy": "/food/diet (food)"
                        },
                        {
                            "class": "food",
                            "score": 0.528
                        },
                        {
                            "class": "honeydew",
                            "score": 0.5,
                            "type_hierarchy": "/fruit/melon/honeydew"
                        },
                        {
                            "class": "melon",
                            "score": 0.501
                        },
                        {
                            "class": "olive color",
                            "score": 0.973
                        },
                        {
                            "class": "lemon yellow color",
                            "score": 0.789
                        }
                    ]
                }
            ],
            "image": "fruitbowl.jpg"
        }
    ],
    "images_processed": 1,
    "custom_classes": 0
}
```


1. **Face Detection**

In this part the user should issue the following command and replace {your\_api\_key} with the service credential you kept earlier and {IMAGE\_NAME} with your image name. Also in order to classify an image using a built in service use { detect\_faces} in the command.
```curl
curl -X POST -u "apikey: YOUR_API_Key " –form "images_file=@Hillary.jpg" https://gateway.watsonplatform.net/visual recognition/api/v3/detect_faces?version=2018-03-19
```
By running the command the result will be as follows:
```python
{
    "images": [
        {
            "faces": [
                {
                    "age": {
                        "min": 50,
                        "max": 53,
                        "score": 0.8261783
                    },
                    "face_location": {
                        "height": 744,
                        "width": 606,
                        "left": 460,
                        "top": 373
                    },
                    "gender": {
                        "gender": "FEMALE",
                        "score": 0.9999988
                    }
                }
            ],
            "image": "Hillary.jpg"
        }
    ],
    "images_processed": 1
}
```

1. **Custom Classification**

In this part the user should first prepare the positive and negative images which are needed for the training process. Then create the .zip files for each category and put them at the desired directory, then issue the following command. As it can be seen, the beagle.zip, golden-retriever.zip and husky.zip are the positive categories and cats.zip is the negative category. Also the user can choose the name of the classes using &quot;name = YOUR\_DesiredName&quot;.
```curl
curl -X POST -u "apikey: YOUR_API_Key " -F "beagle_positive_examples=@beagle.zip" –F "goldenretriever_positive_examples=@golden-retriever.zip" –F "husky_positive_examples=@husky.zip" -F "negative_examples=@cats.zip" -F "name=dogs" https://gateway.watsonplatform.net/visual-recognition/api/v3/classifiers?version=2018-03-19
```
By running the command the result will be as follows:
```python
{
    "classifier_id": "dogs_7720130",
    "name": "dogs",
    "status": "training",
    "owner": "142f8f3e-c092-40fb-8a37-845874bd155f",
    "created": "2018-06-06T16:07:06.714Z",
    "updated": "2018-06-06T16:07:06.714Z",
    "classes": [
        {
            "class": "beagle"
        },
        {
            "class": "husky"
        },
        {
            "class": "goldenretriever"
        }
    ],
    "core_ml_enabled": true
}
```

Also the user can see the list of all classes that have been created by issuing the following command:
```curl
curl -u "apikey:YOUR_API_Key" https://gateway.watsonplatform.net/visual recognition/api/v3/classifiers?verbose=true&version=2018-03-19
```
The following command along with {classifier\_id} can help to delete the created custom class.
```curl
curl -X DELETE -u "apikey: YOUR_API_Key " https://gateway.watsonplatform.net/visual-recognition/api/v3/classifiers/classifier_id?version=2018-03-19
```
