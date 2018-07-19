# Watson Visual Recognition Tutorial: GUI

## Setup

In this method the user uses the Watson service to classify and train the system. The service is really simple to utilize. Even non-programmers can train Watson to detect the objects without coding. The following steps show how to create your own classifier.

1. **Create a Bluemix account.**

IBM Bluemix is a cloud platform with over 150 services, including all of Watson APIs. To get started visit [https://console.bluemix.net/](https://console.bluemix.net/) and create an account.

 ![Bluemix](/VisualRec_Images/ibmbluemix.png)

2. **Create Watson Visual Recognition**

In this part, click on &quot;Catalog&quot; at the top right of the page and choose &quot;Watson&quot; from the left panel beneath &quot;Platform&quot;. Then choose &quot;Visual Recognition&quot; service.

 ![rgfrgfgfdg](/VisualRec_Images/Watson_Catalog.PNG)

Next step is to determine the name of the project and create it. Also at the bottom of the page the user can choose the lite (free) or paid account.

 ![](/VisualRec_Images/VisualRec_Service.PNG)

In the next page the Watson visual recognition service shows you the credentials &quot;apikey&quot; which will be used for programming. Now the user should press the &quot;launch tool&quot; button.

 ![](/VisualRec_Images/API_Key_Credentials.PNG)

In the next page the user can use either the predefined services or define the custom classification.

## Face recognition

In this section we will investigate the Facial Recognition service. For launching this service choose &quot;faces&quot; from the overview.

 ![](/VisualRec_Images/Visual_Rec_BuiltinServices.PNG)

Then from the menu select the test option. Now you can upload the image from the middle of the page. The service automatically detects the faces and also provide some information about the estimated age and gender of the faces.

 ![](/VisualRec_Images/Dra_Drop_Images_Face_GUI.PNG)

By selecting an image the result will be as follows. As it can be seen the service provides the faces and their gender along with their estimated ages.

 ![](/VisualRec_Images/Face_Built-in_Results.PNG)

 ![](/VisualRec_Images/Age_Gender_Face_Results.PNG)

## Custom classification

For this service the user should select custom model and press the &quote;Create Model&quot; button, then choose the name of the project from &quot;Define project details&quot;. By creating the model, the user can upload the images that needs to train the model (From right side of the page). The file format should be .zip file. First add all the zip files to the service, then create the number of the classes that needed.

 ![](/VisualRec_Images/Custom_Clssification_GUI.PNG)

For example we want to train Watson to classify the dogs. For this purpose we need to prepare the .zip files with the corresponding categories. You can download the following examples for this tutorial: [beagle.zip](https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/beagle.zip), [husky.zip](https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/husky.zip), [golden retriever.zip](https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/golden-retriever.zip) and [cats.zip](https://watson-developer-cloud.github.io/doc-tutorial-downloads/visual-recognition/cats.zip). Each .zip file should have at least ten images. The .zip files which are related to dogs are positive examples and the others will be as negative examples (like cat.zip). Create the classes based on the number of classes. (in this case three positive classes and one negative class)

 ![](/VisualRec_Images/Custom_Clssification_Classes_Upload_Images_GUI.PNG)

Then drag and drop the .zip files from the right menu (which have been uploaded before) to the corresponding classes.

 ![](/VisualRec_Images/Custom_Clssification_TrainModel_GUI.PNG)


Now the model should be trained by pressing the &quot;Train model&quot; button on the upper right side of the screen. During the training process the user will not be able to make changes and the service will notify the user once the training process is complete. After this process the user can go to the test process and test the trained model. 

 ![](/VisualRec_Images/Successful_Trained_Model_GUI.PNG)

 ![](/VisualRec_Images/Custom_Calssification_Results_GUI.PNG)


The service will provide the probability in which the image belongs to the class.
