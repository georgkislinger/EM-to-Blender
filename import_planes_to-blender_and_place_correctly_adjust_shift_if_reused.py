import bpy
import os

# Parameters
image_folder = r"D:\shared_drive\notch_50x50x200_final\seg\CbD_on_EM_2"
file_pattern = "CbD_EM_%04d.png"
num_images = 295
pixel_size = 0.2  # in meters
image_width_px = 2361
image_height_px = 2628

# Derived parameters
image_width = image_width_px * pixel_size  # in meters
image_height = image_height_px * pixel_size  # in meters
image_spacing = pixel_size  # Distance between planes

# Set Blender's unit scale to meters for consistency
bpy.context.scene.unit_settings.system = 'METRIC'
bpy.context.scene.unit_settings.scale_length = 1.0

# Function to create a plane with an image texture
def create_plane_with_image(image_path, location, width, height):
    # Load the image
    image_name = os.path.basename(image_path)
    if image_name not in bpy.data.images:
        bpy.data.images.load(image_path)
    image = bpy.data.images[image_name]

    # Create a new plane
    bpy.ops.mesh.primitive_plane_add(size=1)
    plane = bpy.context.object

    # Adjust the plane's origin to the top-left corner
    bpy.ops.object.mode_set(mode='EDIT')
    bpy.ops.mesh.select_all(action='SELECT')
    bpy.ops.transform.translate(value=(-0.5, -0.5, 0))  # Adjust to top-left corner and positive directions
    bpy.ops.object.mode_set(mode='OBJECT')

    # Scale the plane to match the image dimensions
    plane.scale.x = width
    plane.scale.y = height

    # Rotate the plane to align with the desired orientation
    plane.rotation_euler = (1.5708, -1.5708, 0)  # Rotate 90 degrees along X-axis and -90 along Y-axis

    # Move the plane to the desired location
    plane.location = (location[0], location[1], location[2] + (image_width_px * pixel_size)  # Adjust Z position by 472.2!!!!!!IMAGE_WIDTH*pixel_size

    # Create a new material
    mat = bpy.data.materials.new(name=f"Mat_{image_name}")
    mat.use_nodes = True
    bsdf = mat.node_tree.nodes["Principled BSDF"]

    # Add an image texture node
    tex_image = mat.node_tree.nodes.new('ShaderNodeTexImage')
    tex_image.image = image
    mat.node_tree.links.new(bsdf.inputs['Base Color'], tex_image.outputs['Color'])

    # Assign the material to the plane
    plane.data.materials.append(mat)

    return plane

# Import all images as planes
for i in range(num_images):
    # Construct file path
    file_name = file_pattern % i
    file_path = os.path.join(image_folder, file_name)

    # Check if file exists
    if not os.path.exists(file_path):
        print(f"File not found: {file_path}")
        continue

    # Calculate the location of the plane
    x = 0.0  # Original Y -> Blender X
    y = i * image_spacing  # Stack planes along Blender Y
    z = 0.0  # Original X -> Blender Z

    # Bounding box calculation
    bbox_min_x = x
    bbox_min_y = y
    bbox_min_z = z
    bbox_max_x = x + image_width
    bbox_max_y = y + image_height
    bbox_max_z = z + image_spacing

    print(f"Plane {i}: Bounding Box Min=({bbox_min_x}, {bbox_min_y}, {bbox_min_z}), Max=({bbox_max_x}, {bbox_max_y}, {bbox_max_z})")

    # Create the plane with the image
    create_plane_with_image(file_path, location=(x, y, z), width=image_width, height=image_height)

print("Finished importing images as planes.")
