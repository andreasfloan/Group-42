### **Markdown file** 

**Use case:**
Analyzing a IFC file to get data from different structural elements in the building and calculate the structural capasity.

**Who is the use case for?**
This use case is for structural engineers, architects, and other professionals who need to calculate the load bearing capacity of structural elements in a building from an IFC file

**What disciplinary (non BIM) expertise did you use to solve the use case?**
To solve this use case, we used our knowledge of structural engineering, engineering mechanics and mathematics. We also used our knowledge of Python and BlenderBIM to develop a script to calculate the load bearing capacity of structural elements, in this case the beams, in an IFC file.

**What IFC concepts did you use in your script (or would you use in the rest of the tool)?**
The IFC concepts that we used in our script include:

IfcBeam
IfcColumn
IfcSlab
IfcProfileDefinition
IfcStructuralActivity

**What disciplinary analysis does it require?**
Structural analysis which includes assessing beam dimensions (length, width, and height) and determining the maximum bending stress. Knowledge of structural analysis, as well as the use of appropriate structural formulas, is essential.

Material analysis: The analysis of material properties is essential. This includes determining material strength, elasticity, and material behavior under different stress conditions.

Load-Bearing Analysis: Expertise in load-bearing principles is necessary to calculate and evaluate the effect of external loads on beams. It involves understanding statics, dynamics, and the effects of forces and moments on structural elements.

**What building elements are you interested in**
In this use case we are primarely focused on 'IfcBeam' elements. The script is designed to extract data and assess these specific structural elements and further calculating the structural properties .

**What (use cases) need to be done before you can start your use case?**
Availability of a valid IFC model and familiarity with the IFC file structure and the specific representation of beams within the model.
 
**What is the input data for your use case (quantities information)?**
The primary input data for this use case is the path to the IFC file that contains the building information, including the beams. The script also requires the specification of load information (e.g., applied force) and material properties (e.g., material strength).

**What other use cases are waiting for your use case to complete?**
For our use case we need use cases that require the load bearing capacity of the structural elements in the IFC file. It is also a possibility to have structural design optimization and reporting on the safety and integrity of the building structure.
We also need a use case that can give us a detailed overview of the requirements for the diffrent structural elements. 