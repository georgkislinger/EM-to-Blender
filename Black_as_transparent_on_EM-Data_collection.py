import bpy

# Define the collection name
collection_name = "EM-Data"

# Ensure the collection exists
if collection_name not in bpy.data.collections:
    raise ValueError(f"Collection '{collection_name}' not found.")

# Get the collection
collection = bpy.data.collections[collection_name]

# Disable shadow casting for all objects in the collection
for obj in collection.objects:
    # Ensure the object is a mesh
    if obj.type == 'MESH':
        # Disable shadow casting
        obj.cycles.cast_shadow = False

        # Get the material of the object
        if len(obj.data.materials) == 0:
            print(f"Object '{obj.name}' has no materials. Skipping.")
            continue

        mat = obj.data.materials[0]

        # Ensure the material uses nodes
        mat.use_nodes = True
        nodes = mat.node_tree.nodes
        links = mat.node_tree.links

        # Check if a Principled BSDF node exists
        principled_node = None
        for node in nodes:
            if node.type == 'BSDF_PRINCIPLED':
                principled_node = node
                break

        if not principled_node:
            print(f"Object '{obj.name}' has no Principled BSDF node. Skipping.")
            continue

        # Adjust the roughness to 1.0
        principled_node.inputs['Roughness'].default_value = 1.0

        # Find the existing Image Texture node
        texture_node = None
        for node in nodes:
            if node.type == 'TEX_IMAGE':
                texture_node = node
                break

        if not texture_node:
            print(f"Object '{obj.name}' has no Image Texture node. Skipping.")
            continue

        # Add a Mix Shader node if it doesn't exist
        mix_shader = nodes.new(type='ShaderNodeMixShader')
        mix_shader.location = (200, 200)

        # Add a Transparent BSDF node
        transparent_node = nodes.new(type='ShaderNodeBsdfTransparent')
        transparent_node.location = (0, 200)

        # Add a Color Ramp node
        color_ramp_node = nodes.new(type='ShaderNodeValToRGB')
        color_ramp_node.location = (-200, 200)
        color_ramp_node.color_ramp.interpolation = 'LINEAR'
        color_ramp_node.color_ramp.elements[0].position = 0.0  # White fully left
        color_ramp_node.color_ramp.elements[0].color = (1, 1, 1, 1)  # White
        color_ramp_node.color_ramp.elements[1].position = 0.01  # Black close to white
        color_ramp_node.color_ramp.elements[1].color = (0, 0, 0, 1)  # Black

        # Link the new nodes
        links.new(texture_node.outputs['Color'], color_ramp_node.inputs['Fac'])
        links.new(color_ramp_node.outputs['Color'], mix_shader.inputs[0])
        links.new(principled_node.outputs[0], mix_shader.inputs[1])  # Principled BSDF to upper input
        links.new(transparent_node.outputs[0], mix_shader.inputs[2])  # Transparent BSDF to lower input

        # Connect the Mix Shader to the Material Output
        output_node = None
        for node in nodes:
            if node.type == 'OUTPUT_MATERIAL':
                output_node = node
                break

        if output_node:
            links.new(mix_shader.outputs[0], output_node.inputs['Surface'])

print("Shader nodes updated and shadow casting disabled for all planes in collection 'EM-Data'.")
