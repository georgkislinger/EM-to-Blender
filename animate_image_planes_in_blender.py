import bpy

# Helper function to clear all keyframes and reset visibility
def clear_and_reset_visibility(collection):
    for obj in collection.objects:
        if obj.animation_data:  # Clear any existing keyframes
            obj.animation_data_clear()
        obj.hide_render = True  # Hide in render
        obj.keyframe_insert(data_path="hide_render", frame=0)  # Ensure hidden at frame 0

# Helper function to animate visibility (render only)
def animate_visibility(obj, frame_start, hide=True):
    obj.hide_render = hide
    obj.keyframe_insert(data_path="hide_render", frame=frame_start)

# Specify collections
em_collection = bpy.data.collections.get("EM-Data")
cbd_collection = bpy.data.collections.get("CbD-Data")

# Reset and clear keyframes for both collections
if em_collection:
    clear_and_reset_visibility(em_collection)
if cbd_collection:
    clear_and_reset_visibility(cbd_collection)

# Animate `EM-Data`
frame = 0  # Start frame
if em_collection:
    planes_em = sorted(em_collection.objects, key=lambda o: o.name, reverse=True)  # Sort in reverse order
    for obj in planes_em:
        animate_visibility(obj, frame, hide=False)  # Show plane
        frame += 10
    # Hide all planes after the last one is shown
    for obj in planes_em:
        animate_visibility(obj, frame, hide=True)
    frame += 10  # Add buffer for hiding all planes

# Animate `CbD-Data`
if cbd_collection:
    planes_cbd = sorted(cbd_collection.objects, key=lambda o: o.name)  # Sort in ascending order
    # Show all planes at once
    for obj in planes_cbd:
        animate_visibility(obj, frame, hide=False)
    # Sequentially hide planes
    for obj in planes_cbd:
        frame += 5
        animate_visibility(obj, frame, hide=True)

print("Animation complete.")
