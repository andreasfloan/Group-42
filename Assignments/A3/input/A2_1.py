from pathlib import Path
import ifcopenshell
import math
import collections

modelname = "LLYN_STRU"

try:
    dir_path = Path(__file__).parent
    model_url = Path.joinpath(dir_path, 'model', modelname).with_suffix('.ifc')
    model = ifcopenshell.open(model_url)
except OSError:
    try:
        import bpy
        model_url = Path.joinpath(Path(bpy.context.space_data.text.filepath).parent, 'model', modelname).with_suffix('.ifc')
        model = ifcopenshell.open(model_url)
    except OSError:
        print(f"ERROR: Please check your model folder: {model_url} does not exist")

# Test if everything works:
beams = model.by_type("IfcBeam")
if not beams:
    print("ERROR: Model does not contain any beams.") # If no error; the script identfies all the beam ID's in the file
    exit(1)

# Defining constants
q = 1000.0  # Load in Newtons per meter (N/m)
beam_material_strength = 25.0  # [MPa] Material strength in mega-Pascals

# Initializing an empty dictionary to store beam details
beam_details = {}

# Initialize a counter for similar beams
similar_beams_counter = collections.Counter()

if model:
    # Extract beams
    for beam in beams:
        # Check if the beam has 'ObjectPlacement' and 'Representation' properties
        if hasattr(beam, "ObjectPlacement") and hasattr(beam, "Representation"):
            # Extract coordinates (x1, y1, z1) and (x2, y2, z2) from the beam's ObjectPlacement
            placement = beam.ObjectPlacement
            if hasattr(placement, "Location"):
                location = placement.Location
                x1, y1, z1, x2, y2, z2 = location.Coordinates

                # Calculate the length of the beam using Pythagoras
                length = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2 + (z2 - z1) ** 2)

                # Assuming a simple supported beam, calculate the maximum moment
                # Max Moment = (q * L^2) / 8
                max_moment = (q * length ** 2) / 8.0 # load in N*m

                # Calculate the width and height of the beam
                width = getattr(beam, "Width", 0.0)
                height = getattr(beam, "Height", 0.0)

                if not width or not height:
                    obj_def = beam.ObjectDefinition
                    if obj_def and hasattr(obj_def, "Representation") and hasattr(obj_def.Representation, "Items"):
                        for item in obj_def.Representation.Items:
                            if hasattr(item, "Width"):
                                width = item.Width
                            if hasattr(item, "Height"):
                                height = item.Height

                # Calculate the bending stress
                # Doesn't take into account that it could be different types of cross-sections...
                # We have not been able to identify cross-sections
                c = height / 2  
                I = (width * height ** 3) / 12  # Calculate the second moment of area
                max_bending_stress = (max_moment * c) / I

                # Calculate the E-Module
                e_module = 200_000 * beam_material_strength

                # Calculate the shear force (Assuming simple supported beam)
                shear_force = (q * length) / 2

                # Calculate the first moment of area (Q)
                Q = (width * height ** 2) / 4

                # Calculate shear stress
                shear_stress = shear_force * (Q / I)

                # Store the beam details in the dictionary
                beam_details[beam.id()] = {
                    "Length": length,
                    "Width": width,
                    "Height": height,
                    "Max Moment": max_moment,
                    "Max Bending Stress": max_bending_stress,
                    "E-Module": e_module,
                    "Shear Force": shear_force,
                    "Shear Stress": shear_stress
                }

                # Count similar beams based on width and height
                # Benefitial to get similar beams to know how many different load-combinations there is
                similar_beams_counter[(width, height)] += 1
        else:
            print(f"Beam '{beam.Name}' does not have 'ObjectPlacement' and 'Representation' properties.")

# Now you can choose to print or process the data in beam_details as needed since it is in a dictionary
# Here we have chosen to try printing the following, but it seems like don't get the measurements...
for beam_id, details in beam_details.items():
    print(f"Beam ID: {beam_id}")
    print(f"- Length: {details['Length']} meters")
    print(f"- Width: {details['Width']} meters")
    print(f"- Height: {details['Height']} meters")
    print(f"- Maximum Moment: {details['Max Moment']} Nm")
    print(f"- Maximum Bending Stress: {details['Max Bending Stress']} Pa")
    print(f"- E-Module: {details['E-Module']} Pa")
    print(f"- Shear Force: {details['Shear Force']} N")
    print(f"- Shear Stress: {details['Shear Stress']} Pa")
    print()

# Print the count of similar beams
print("Count of Similar Beams:")
for (width, height), count in similar_beams_counter.items():
    print(f"- Width: {width} meters, Height: {height} meters, Count: {count}")

print()

