# BIM Execution Plan - Structural Capacity Calculation

## Overview

This BIM Execution Plan outlines the process for analyzing an IFC file to calculate the load-bearing capacity of structural elements in a building. The use case is intended for structural engineers, architects, and other professionals involved in structural analysis.

## Use Case Description

The primary objective of this use case is to develop a script that can analyze an IFC file to extract data from various structural elements in the building, with focus on 'IfcBeam' in our script, and calculate their load-bearing capacity. The script will utilize concepts from ISO 19650 and the IFC schema to achieve this. The following are key aspects of the use case:

### Use Case Audience

This use case is designed for a diverse set of professionals involved in building analysis and design, including:

**Structural Engineers:** Responsible for ensuring the safety and stability of the building structure.

**Architects:** Tasked with creating the initial building design and ensuring its alignment with structural requirements.

**Construction Managers:** Involved in managing construction activities while adhering to the structural design.

**Building Contractors:** Executing construction work with attention to structural specifications.

**Building Inspectors and Regulatory Authorities:** Responsible for ensuring compliance with safety and construction standards.

**Facility Managers:** Managing ongoing maintenance and operation of the building, including monitoring structural integrity.

**Building Owners and Investors:** Interested in the long-term safety and performance of the structure.

**BIM Specialists:** Dealing with the digital representation of the building and enhancing the quality of BIM data.

**Regulatory and Standards Organizations:** Setting and enforcing building standards and codes.

**Software Developers and IT Teams:** Involved in creating and maintaining the software or workflow if applicable.

**Project Managers and Team Leads:** Responsible for implementing the tool within their organizations.

### Disciplinary Expertise

To address this use case, the following disciplinary expertise is required:

- **Structural Analysis:** This involves assessing the dimensions of beams (length, width, height) and determining maximum bending stress. Knowledge of structural analysis and relevant formulas is essential.

- **Material Analysis:** Material properties such as strength, elasticity, and behavior under stress need to be considered.

- **Load-Bearing Analysis:** Understanding of load-bearing principles is crucial for calculating the effects of external loads on structural elements.

### Building Elements of Interest

The focus of the code for this use case is primarily on 'IfcBeam' elements. The script will extract data from these structural elements and perform calculations on their load-bearing properties. However, it can potentially be extended to cover other structural elements as well and give more detailed calculations.

### Prerequisites

Before executing this use case, the following prerequisites should be met:

1. Availability of a valid IFC model that includes 'IfcBeam' elements. The model should be representative of the building structure.

2. Familiarity with the structure and representation of beams within the IFC model to ensure accurate data extraction and analysis.

### Input Data

The primary input data for this use case includes:

- **Path to the IFC file:** The IFC file that contains the structural information of the building, including IfcBeams, etc.

- **Load information:** This may include information about applied forces, loads, and external stresses that affect the structural elements.

- **Material properties:** Data related to material properties, such as material strength, elasticity, and other relevant material characteristics, is necessary for structural calculations.

### Quality Assurance

The following quality assurance measures will be implemented to ensure the accuracy and reliability of the structural capacity calculation script and its outputs:

## Unit Testing

Unit tests will be written to verify the individual functions of the script, including:

- Reading and parsing IFC files
- Extracting data from IFC files, such as the dimensions, material properties, and applied loads for the different elements
- Conducting structural analysis for elements, including calculating maximum bending stress and load-bearing 
  capacity
- Aggregating the results to provide a comprehensive overview of the load-bearing capacity of all the structural elements 
  in the building, and in our case the beams
  

## Integration Testing

Integration tests will be performed to ensure that the script works correctly with other BIM software, such as structural analysis softwares. This will involve testing the script with a variety of IFC files and comparing the calculated load-bearing capacity values to those obtained from the structural analysis software.

## Acceptance Testing

Users will be involved in the acceptance testing process to ensure that the script meets their needs and requirements.

In addition to the above measures, the following steps will be taken to ensure the quality of the script:

- **Comprehensive Documentation:** The script will be well-documented, including detailed instructions on how to use it, 
  example input data and output results, and a description of the assumptions and limitations of the script.
- **Peer review:** The script will undergo review by other experienced professionals, including structural engineers and 
  architects, to identify potential errors, inaccuracies, or omissions.
- **Continuous Maintenance and Updates:** The script will be maintained and updated regularly to reflect changes in the IFC 
  schema and address any user feedback or bug reports.

By implementing these quality assurance measures, we can ensure that the structural capacity calculation script is a reliable and accurate tool for structural engineers and other professionals involved in building analysis and design.

### Interdependent Use Cases

Completion of this use case can enable other related use cases, including:

1. **Structural Design Optimization:** This use case can serve as a foundation for optimizing the design of structural elements based on their load-bearing capacity. It enables the exploration of design alternatives to enhance structural performance.

2. **Safety and Integrity Reporting:** The output of this use case can be used to assess the safety and integrity of the building structure. It provides the basis for creating safety reports and identifying potential risks.

3. **Detailed Structural Element Requirements:** A use case can be developed to define specific requirements for different structural elements based on their load-bearing capacity.

## Execution Steps

To achieve the use case objectives, the following steps will be taken:

1. Load the IFC file and extract 'IfcBeam' elements from the model.

2. For each 'IfcBeam' element, the script will gather data such as dimensions (length, width, height), material properties, and applied loads.

3. The script will conduct structural analysis for each 'IfcBeam' element, including calculating maximum bending stress, shear force, load-bearing capacity and E-module based on the gathered data.

4. The script will aggregate the results to provide a comprehensive overview of the load-bearing capacity of all 'IfcBeam' elements in the building.

## Conclusion

This BIM Execution Plan provides a roadmap for developing a script that can analyze an IFC file, calculate the load-bearing capacity of different structural elements, and support related use cases in structural engineering and building design. The successful completion of this use case will empower professionals to make informed decisions regarding structural integrity and safety.











 # Report
### 3A: Analyze Use Case

**Goal:** To develop a tool or workflow that enables users to calculate the different structural elements of a project from a BIM model.

**Model Use (BIM Uses):** Structural analysis is a critical process in all construction projects. By calculating the strength and stiffness of structural elements, engineers can ensure that the structure will be able to safely support the loads that it will be subjected to. BIM models provide a rich source of data for structural analysis, including information about the geometry, materials, and loading conditions of structural elements.

### 3B: Propose a (Design for a) Tool / Workflow

**Process Diagram:** The BPMN diagram illustrates the proposed workflow for calculating the structural elements of a project from a BIM model.

![diagram (5)](https://github.com/andreasfloan/Group-42/assets/149388813/7a04414f-1f72-4152-a0e1-85addc15f6de)

**Description of the process:**

- The user opens the BIM model in the tool.
- By checking the model for quality and requirements to further perform the calculations.
- The tool extracts the relevant data from the BIM model, such as the geometry, materials, and loading conditions of 
  structural elements.
- Utilizing the extracted data, the tool performs structural analysis calculations, determining properties like internal 
  forces, moments, stresses, and strains within the structural elements.
- The tool generates a report that summarizes the results of the structural analysis, including the calculated internal 
  forces and moments, as well as the stresses and strains in the structural elements.

### 3C: Requirements

**Functional requirements:** The tool or workflow shall be able to:

- Extract the relevant data from a BIM model, including the geometry, materials, and loading conditions of structural 
  elements.
- Perform structural analysis calculations using the extracted data.
- Generate a report that summarizes the results of the structural analysis.

**Non-functional requirements:** The tool or workflow shall be:

- User-friendly, ensuring ease of use for various professionals.
- Efficient, capable of handling calculations quickly.
- Accurate, providing precise structural analysis results.
- Scalable to accommodate large BIM models with complex structural elements.

### 3D: Value

**Business value:** The proposed tool or workflow can create significant value for businesses by helping them to:

- Reduce the risk of structural failure by providing accurate and up-to-date structural analysis results.
- The tool assists in making well-informed choices about structural design and construction methods, enhancing project 
  outcomes.
- Streamlining the structural analysis process enhances overall project efficiency, saving time and resources.

**Societal value:** The proposed tool or workflow can also contribute to societal value by helping to:

- Improve the safety of construction projects.
- Reduce the environmental impact of construction projects by optimizing the design of structural elements.
- Increase the affordability of construction projects by making them more cost-effective.

### Conclusion

The proposed tool or workflow has the potential to offer significant value to both businesses and society by helping to improve the safety, efficiency, and sustainability of construction projects.

In addition to the functional and non-functional requirements listed above, it is also important to consider the following requirements when developing a tool or workflow for calculating the different structural elements in a BIM model:

**Interoperability:** The tool or workflow should be interoperable with different BIM software applications. This will allow users to use the tool or workflow with their preferred BIM software, as well as it works as a safety measure to compare different data.

**Security:** The tool or workflow should be secure to protect users' data from unauthorized access and modification.

**Customization:** The tool or workflow should be customizable to meet the specific needs of different users and organizations.

By meeting these requirements, a tool or workflow for calculating the different structural elements in a BIM model can be a valuable asset for businesses and organizations involved in the design, construction, and operation of buildings and other infrastructure.

### 3E: Delivery
**IDM diagrams**
Updated: ![BPMN diagram new](https://github.com/andreasfloan/Group-42/assets/149388813/e7921bb1-071e-400f-8eaf-e3d98dc6ba74)

Previous: ![BPMN without path](https://github.com/andreasfloan/Group-42/assets/149388813/75f06e1e-6e2f-43bf-a462-e7a785e3769f)

