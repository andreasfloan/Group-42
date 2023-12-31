# Description of code: #

### Prerequisites:

- Python 3.6 or higher
- IfcOpenShell library

## Steps:

- **Download the IfcOpenShell library.**

  You can download the IfcOpenShell library from the following website:

    https://github.com/IfcOpenShell/IfcOpenShell

- **Install the IfcOpenShell library.**


- **Download the Python script to calculate beam properties.**

   You can download the Python script to calculate beam properties from the following link:

  https://github.com/andreasfloan/Group-42/blob/main/Assignments/A3/input/A2_1.py
  
- **Save the Python script to a folder.**

  Save the Python script to a folder on your computer.

- **Open the IFC model file.**

  Open the IFC model file that you want to calculate beam properties for.

- **Open a terminal or command prompt window.**

   Navigate to the folder where you saved the Python script in the terminal or command prompt window.

- **Run the Python script.**



## What the code does:

The Python script works by first importing the necessary libraries, including pathlib, ifcopenshell, math, and collections. Then, it defines the model name and the load and beam material strength constants.

Next, the script opens the IFC model file using the ```ifcopenshell.open()``` function. If the file does not exist, the script prints an error message and exits.

The script then checks if the model contains any beams using the ```ifcopenshell.by_type()``` function. If there are no beams in the model, the script prints an error message and exits.

For each beam in the model, the script does the following:

- Checks if the beam has ObjectPlacement and Representation properties. If not, the script prints a warning message and skips the beam.
- Extracts the beam's coordinates from the ObjectPlacement property.
- Calculates the beam's length using Pythagoras.
- Calculates the beam's maximum moment using the simple supported beam formula.
- Extracts the beam's width and height from the Representation property.
- Calculates the beam's bending stress using the bending stress formula.
- Calculates the beam's E-Module using the beam material strength constant.
- Calculates the beam's shear force using the simple supported beam formula.
- Calculates the beam's shear stress using the shear stress formula.
- Stores the beam's details in a dictionary.
- Increments the counter for similar beams based on the beam's width and height.
- Finally, the script prints the beam details dictionary and the count of similar beams


This Python script loads an IFC model and extracts all the beam elements from the model.
The script then calculates the length, width, height, maximum moment, maximum bending stress, E-module, shear force, and shear stress of each beam.
The results are stored in a dictionary called ```beam_details```.
Finally, the script prints the number of similar beams in the model.

# Here is a detailed description of each part of the code: 

https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L1-L4

These lines import the necessary libraries for the script to work.



https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L6
This line defines the name of the IFC model to be loaded. Its important to change this to the name of you own model.



https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L8-L18

These lines try to load the IFC model from the specified location. If the model cannot be found, the script will try to load it from the Blender scene. If the model still cannot be found, the script will exit with an error message.



https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L21-L24

These lines check if the model contains any beam elements. If the model does not contain any beam elements, the script will exit with an error message.



https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L27-L28

These lines define the constants used in the script, such as the load and the material strength of the beams. Until the code is developed further you need to insert the values manually.



https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L31-L34
These lines initialize the dictionary that will be used to store the beam details and the counter that will be used to count the number of similar beams.



https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L36-L45
These lines extracts the beam's coordinates from the ```ObjectPlacement property```. This makes it easier to get the dimentions and placement of the individual beams.



https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L48-L52
First, the code calculates the length of the beam using the Pythagorean theorem.
Next, the code assumes that the beam is supported at one end and simply supported at the other end. Under these assumptions, the code calculates the maximum moment (or torque) that the beam can withstand before failure.

The maximum moment can be calculated using the following formula:

```Max Moment = (q * L^2) / 8```



https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L55-L56
This line of code uses the ```getattr()``` function in Python. This function is used to get the value of an attribute in an object.

The first argument to ```getattr()``` is the object whose attribute you want to get. 
The second argument is the attribute you want to get. 
The third argument is optional and it is the value that ```getattr()``` should return if the specified attribute does not exist in the object.

In this case, the ```getattr()``` function is used to get the value of the Width and Height attribute of the beam object. If the Width or Height attribute does not exist, the ```getattr()``` function will return the default value 0.0. This is so that it doesn't affect the further calculations with false values, and just gives the value of zero.



https://github.com/andreasfloan/Group-42/blob/e5a040c8fc1722171ab48f1a30ef68f918002134/Assignments/A3/input/A2_1.py#L58-L65
This part of the code is checking if width and height are defined and have values. If they're not, it attempts to find them in the ```ObjectDefinition``` of the beam object.



https://github.com/andreasfloan/Group-42/blob/0cb7281bc8b20b4d9de29e8bef6cabb282174155/Assignments/A3/input/A2_1.py#L70-L84
These lines of code calculate various parameters related to the stress and structural properties of a beam. It starts by calculating the distance from the neutral axis to the top edge of the beam cross-section (line 70) and the second moment of area (flexural rigidity) of the beam cross-section (line 71), assuming a rectangular cross-section. 

These values are then used to calculate the maximum bending stress in the beam (line 72). Next, the code calculates the Young's modulus (modulus of elasticity) of the beam material (line 75), which is a measure of the material's stiffness.

The code then assumes a simple supported beam and calculates the shear force (line 78) and the first moment of area (statical moment) of the beam cross-section (line 81). Finally, it calculates the shear stress in the beam (line 84).



https://github.com/andreasfloan/Group-42/blob/0cb7281bc8b20b4d9de29e8bef6cabb282174155/Assignments/A3/input/A2_1.py#L87-L102

The first part of the code stores the calculated beam details in a dictionary called ```beam_details```. The dictionary's key is the beam's ID.

The second part of the code counts the number of similar beams based on their width and height. This information can be used to identify different load combinations in the model. The code uses a counter object called ```similar_beams_counter``` to keep track of the number of similar beams. The counter object's key is a tuple containing the width and height of the beam, and the value is the number of beams with those dimensions.
The ```else``` statement at the end of the code snippet handles the case where a beam does not have the required properties (```ObjectPlacement``` and ```Representation```). In this case, the code prints an error message to the console.



https://github.com/andreasfloan/Group-42/blob/0cb7281bc8b20b4d9de29e8bef6cabb282174155/Assignments/A3/input/A2_1.py#L106-L123

The first part of this part of the code iterates through the ```beam_details``` dictionary and prints out the details of each beam. For each beam, it prints the beam ID, length, width, height, maximum moment, maximum bending stress, E-module, shear force, and shear stress. This provides a summary of the structural properties and stresses for each beam in the model.

The second part of the code iterates through the ```similar_beams_counter``` dictionary and prints out the count of similar beams for each combination of width and height. This provides insight into the distribution of beam sizes and potential load combinations in the model.
