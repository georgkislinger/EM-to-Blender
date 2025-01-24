# EM-to-Blender
Upload image data to blender DISCLAIMER: Please note that this README was AI-created and may contain errors
# README: Blender Scripts for EM Data Visualization and Animation

This repository contains three Blender scripts designed for importing EM images as planes, handling transparency for black borders, and animating the planes for video creation. Below is a comprehensive guide to setting up and using these scripts effectively in Blender.

---

## Table of Contents
1. [Overview](#overview)
2. [Environment Setup](#environment-setup)
3. [Script Descriptions](#script-descriptions)
4. [How to Use](#how-to-use)
    - [Script 1: Import Planes and Adjust Placement](#import-planes-and-adjust-placement)
    - [Script 2: Render Black as Transparent](#render-black-as-transparent)
    - [Script 3: Animate Planes for Video Creation](#animate-planes-for-video-creation)
5. [Troubleshooting](#troubleshooting)

---

## Overview
The repository includes:
- **`import_planes_to_blender_and_place_correctly_adjust_shift_if_reused.py`**: Imports EM images as planes and places them correctly in Blender.
- **`Black_as_transparent_on_EM-Data_collection.py`**: Updates materials to render black as transparent for all planes in a collection.
- **`animate_image_planes_in_blender.py`**: Animates the planes for sequential visibility, creating a video effect.

These tools are tailored for visualizing large stacks of EM data in Blender and producing smooth animations.

---

## Environment Setup

### Prerequisites
- Blender 4.3 or higher.

### Setting Up Blender
1. Open Blender and create a new project.
2. Set Blender's unit system to metric for consistent scaling:
   - Go to **Scene Properties** > **Units** > Set **Unit System** to **Metric** and **Unit Scale** to `1.0`.

3. Ensure your EM images are organized in a folder and named sequentially (e.g., `image_0001.png`, `image_0002.png`, etc.).

---

## Script Descriptions

### 1. `import_planes_to_blender_and_place_correctly_adjust_shift_if_reused.py`
This script imports a stack of EM images as planes into Blender and places them in the correct orientation and spacing.

**Parameters to Update:**
- `image_folder`: Path to the folder containing the EM images.
- `file_pattern`: Naming pattern for the images (e.g., `image_%04d.png`).
- `num_images`: Total number of images in the stack.
- `pixel_size`: Physical size of a pixel in meters.
- `image_width_px` and `image_height_px`: Dimensions of the images in pixels.

**Steps:**
1. Update the parameters in the script to match your dataset.
2. Run the script in Blender's Scripting tab.
3. The images will be imported as planes and placed sequentially.

### 2. `Black_as_transparent_on_EM-Data_collection.py`
This script modifies materials for all planes in a specified collection to render black as transparent.

**Parameters to Update:**
- `collection_name`: Name of the collection containing the planes (default: `EM-Data`).

**Steps:**
1. Ensure all imported planes are in the specified collection.
2. Run the script in Blender's Scripting tab.
3. Black areas in the images will now be rendered as transparent.

### 3. `animate_image_planes_in_blender.py`
This script animates the visibility of planes, creating a sequential video effect.

**Parameters to Update:**
- `em_collection`: Name of the collection for the EM planes (default: `EM-Data`).
- `cbd_collection`: (Optional) Name of a second collection for additional animations (default: `CbD-Data`).

**Steps:**
1. Organize your planes into collections (`EM-Data`, `CbD-Data`).
2. Run the script in Blender's Scripting tab.
3. Planes will be animated for sequential visibility.

---

## How to Use

### Import Planes and Adjust Placement
1. Open Blender and load your project.
2. Open the Scripting tab and load the script `import_planes_to_blender_and_place_correctly_adjust_shift_if_reused.py`.
3. Update the parameters for your dataset.
4. Click **Run Script**. The planes will be imported and placed automatically.

### Render Black as Transparent
1. Ensure all planes are organized in the collection `EM-Data`.
2. Open the Scripting tab and load the script `Black_as_transparent_on_EM-Data_collection.py`.
3. Click **Run Script**. Black borders in the planes will now render as transparent.

### Animate Planes for Video Creation
1. Open the Scripting tab and load the script `animate_image_planes_in_blender.py`.
2. Organize the planes into the collections `EM-Data` and `CbD-Data`.
3. Click **Run Script**. The planes will be animated sequentially.

---

## Troubleshooting

### Common Issues
1. **Planes not appearing correctly:**
   - Check the `image_folder` and `file_pattern` parameters in the import script.
   - Verify the images are named and formatted correctly.

2. **Transparency not applied:**
   - Ensure the collection name matches the script's `collection_name` parameter.

3. **Animation not working:**
   - Verify the planes are organized in the correct collections (`EM-Data`, `CbD-Data`).

### Debugging
Use Blender's Console or add `print()` statements in the scripts to debug issues.

---

This README provides step-by-step instructions for using the Blender scripts to visualize and animate EM data. If you encounter issues or need additional features, feel free to reach out.


