# SecurityAndResilience_Group9
Project number 1:  Adversarial examples for deep neural networks.

Goal: The aim of the project is to alter pixel values in images and find a threshold value that if surpassed makes a previously developed deep neural network
falsely classify the image. The deep neural network (DNN) will also be developed
by the group, and the project will work with images from the German Traffic
Sign Recognition Benchmark (GTSRB) data set.

## User manual
### Data pre-processing
Data pre-processing can be executed by file ‘Preprocess.py’. Before first running, variable ‘desk_root’ should be changed to the path where folder ‘Final_Training’ is located (To get this folder, first download ‘GTSRB_Final_Training_Images.zip’, then unzip it). Run the python file in the command line, the ‘train_dataset’ folder and ‘test_dataset’ folder will be formed automatically. They will be saved at the path ‘desk_root’.
‘Preprocess.ipynb’ can also be executed. It shows how we deal with images step by step. Also change the ‘desk_root’ then it can be used as normal.

### Image Manipulation (AlterImg.py)
Manipulation tool can be executed using the AlterImg.py file using the Command Line Interface(CLI) with python 3 installed. Before execution some prerequisites related to the smooth running of the application have to be done in order to fetch the input and store output files.
A directory named “Transformed” has to be created in the root directory where the AlterImg.py file is present.
Inside the “Transformed” directory four additional directories has to be created named as “Output”, “OnePixel”, “Ripple”, “saltNppr” subsequently.
Once the above steps are done now on execution of AlterImg.py a GUI will be displayed, which enables the user to select the perturbation operation, after that user can press the process command. This will enable the filedialog window to get the input files. Users can navigate to the local directories and select the folder that contains the test dataset images. 
Note: Make sure no additional folders and incompatible file types are inside the selected input folder. The permitted file types are (.jpg, .png, .ppm)
After selection of the input folder the resultant files are automatically stored in the corresponding output folder set.
Note: The operations in the blue background cannot be combined with other operations.

### DNN 
The github consists of four Python notebooks, Alexs and Camerons DNN refer to the two notebooks Alex and Cameron wrote and tested the code for the DNN. Running “Camerons DNN.ipynb” will create the pull in the data, create the neural network, and train it, take a single test image and predict an output. “Alexs DNN.ipynb” will do a similar run through, but with multiple models, demonstrating some of the various different model architectures we tried. It then also tests on the adversarial attacks, and gives an output for these. Running the “Model_comparison” notebook compares our model with and without training it on manipulated images. They are then tested on different sets of manipulated images to see the difference. 

“Demo.ipynb'' was intended for the demonstration to go with our presentation, it shows a single example of each adversal attack, demonstrating both when it worked and didn't. It keeps most of the training and setup code out, to allow for a clear example. 

### Minimum perturbation
This model could be executed by Minimum_Perturbation.ipynb file. This model is edited on Google Corlaboration, so rootpath needs to be changed to your own path where the “GTSRB” file originally in “test” file in ”data” file and “manipulated_images” file is loaded. And the path for reloading the model need to be changed to the path where “Model4_Alex.h5” file exists.
