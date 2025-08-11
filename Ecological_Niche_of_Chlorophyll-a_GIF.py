import xarray as xr
import pandas as pd
import numpy as np
import plotly.express as px
import os
import imageio.v2 as imageio

# --- Import files for processing ---

data_folder = "/Users/Zhuanz/Documents/VsCode/hot-phytoplankton-analysis/Phytoplankton_Data"  # Local folder that contains all the files with data

files_to_process = [  # Bottle Extraction data file from different stations of HOT-DOGS
    "(2) ALOHA.nc",
    "(8) HALE-ALOHA.nc",
    "(6) Kaena.nc",
    "(1) Kahe Point.nc",
    "(50) WHOTS.nc",
    "(52) WHOTS.nc",
]

list_of_dataframes = (
    []
)  # Empty list as a blanket for later loop to put all the cleaned data in

# --- Data cleaning and editing ---

for filename in files_to_process:

    file_path = os.path.join(
        data_folder, filename
    )  # Join the folder path and file for the absolute path

    try:
        ds = xr.open_dataset(
            file_path
        )  # Transfer netCDF to Pandas Dataframe for better editing
        data_dict = {
            "pressure": ds["press"].values,
            "temperature": ds["temp"].values,
            "salinity": ds["bsal"].values,
            "phosphate": ds["phos"].values,
            "nitrate": ds["nit"].values,
            "silicate": ds["sil"].values,
            "chlorophyll": ds["chl"].values,
        }
        df_file = pd.DataFrame(data_dict)

        df_file.replace(-9.0, np.nan, inplace=True)  # Replace all the -9.0 with NaN

        list_of_dataframes.append(df_file)  # Add the cleaned data values to the list

    except (
        Exception
    ) as e:  # Double check for any potential mistakes when processing specific file
        print(f"Error: {e} occurs when processing {filename}")

final_df = pd.concat(list_of_dataframes, ignore_index=True)

final_df.info()  # Review of the final data collection

# --- 3D Scatter Plot: Determining the combination effects of temperature, pressure, and nutrient salt such as nitrate ---

df_3d = final_df.dropna(
    subset=["temperature", "nitrate", "pressure", "chlorophyll"]
)  # Sort out four core values
df_3d = df_3d[df_3d["pressure"] <= 400]

fig = px.scatter_3d(  # Create the 3-d graph with plotly built-in function
    df_3d,
    x="temperature",
    y="nitrate",
    z="pressure",
    color="chlorophyll",
    size="chlorophyll",
    size_max=40,
    color_continuous_scale=px.colors.sequential.Viridis,
    title="3D View: The Ecological Niche for Chlorophyll-a",
    labels={
        "temperature": "Temperature (°C)",
        "nitrate": "Nitrate (umol/kg)",
        "pressure": "Depth (m)",
        "chlorophyll": "Chlorophyll-a",
    },
)

fig.update_layout(  # Decorative effects
    margin=dict(l=0, r=0, b=0, t=40),
    scene=dict(
        zaxis=dict(autorange="reversed"),
        xaxis_showbackground=True,
        yaxis_showbackground=True,
        zaxis_showbackground=True,
    ),
)

# --- Generating GIF from this 3-d plot ---

frames_folder = "gif_frames"

if not os.path.exists(
    frames_folder
):  # Create a folder that stores all the photos to create gif
    os.makedirs(frames_folder)

n_frames = 100  # GIF total frames
rotation_speed = (
    2 * np.pi / n_frames
)  # Calculate the angle to rotate for every single frame

list_of_frame_files = []

for i in range(n_frames):  # Loop to generate every frame of photos
    # Get the location of the camera
    # Let it rotates in a circle around the z-axis
    eye_x = 2.5 * np.cos(i * rotation_speed)
    eye_y = 2.5 * np.sin(i * rotation_speed)

    # Update the location of the camera
    fig.update_layout(scene_camera=dict(eye=dict(x=eye_x, y=eye_y, z=0.8)))

    frame_filename = os.path.join(
        frames_folder, f"frame_{i:03d}.png"
    )  # Save the current view as a png photo
    fig.write_image(frame_filename)

    list_of_frame_files.append(frame_filename)  # Add the filename to the list

    print(
        f"Generating Frame {i+1}/{n_frames}"
    )  # Clearly demonstrating which frame is processing right now

output_gif_path = "The Ecological Niche for Chlorophyll-a.gif"
with imageio.get_writer(output_gif_path, mode="I", duration=50, loop=0) as writer:
    for filename in list_of_frame_files:
        image = imageio.imread(filename)
        writer.append_data(image)

for filename in list_of_frame_files:  #  Clean the temporary photos in the frame file
    os.remove(filename)
os.rmdir(frames_folder)
