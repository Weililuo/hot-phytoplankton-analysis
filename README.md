# Exploratory Analysis of Phytoplankton's Ecological Niche in Hawaii Ocean Time-series (HOT) Data

![Python Version](https://img.shields.io/badge/Python-3.12+-blue.svg)
![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)

This is a data analysis project in Python aimed at exploring the key environmental factors that influence phytoplankton biomass (measured as Chlorophyll-a) within the Hawaii Ocean Time-series (HOT) dataset. The project leverages a series of visualizations to uncover the complex interplay between temperature, depth, and nutrient concentrations.

---

## Table of Contents
1.  [Project Goal](#project-goal)
2.  [Data Source](#data-source)
3.  [Analysis Workflow](#analysis-workflow)
4.  [Key Findings & Visualizations](#key-findings--visualizations)
5.  [How to Run](#how-to-run)
6.  [Libraries Used](#libraries-used)

---

### Project Goal
The primary scientific objective of this project is to identify the "optimal ecological niche" for phytoplankton growth by analyzing a real-world oceanographic dataset. Specifically, it aims to answer the following questions:
* Which environmental factors (e.g., temperature, nutrients) show the strongest correlation with phytoplankton biomass?
* What are the classic vertical distribution patterns of these key variables in the ocean water column?
* Under what specific combination of temperature, nutrient concentration, and depth does high chlorophyll concentration occur?

---

### Data Source
The data used in this analysis is publicly available bottle data from the **Hawaii Ocean Time-series (HOT) program**.
* **Data Portal**: [HOT-DOGS (Hawaii Ocean Time-series Data Organization & Graphical System)](https://hahana.soest.hawaii.edu/hot/hot-dogs/bextraction.html)
* **Sampling Stations**: This analysis aggregates `.nc` (NetCDF) data files from several key stations, including:
    * `ALOHA`
    * `HALE-ALOHA`
    * `Kaena`
    * `Kahe Point`
    * `WHOTS`

---

### Analysis Workflow
The project follows a standard data science workflow:
1.  **Data Loading and Cleaning**: Multiple `.nc` files are read using the `xarray` library and then merged into a single, unified DataFrame using `pandas`. Invalid values (`-9.0`) are handled and replaced with `NaN`.
2.  **Data Preprocessing**: To generate smooth depth profiles, the data is binned by depth (in 10-meter intervals), and the mean value for each variable within every bin is calculated.
3.  **Exploratory Data Analysis and Visualization**:
    * **Figure 1**: A correlation heatmap is plotted to get a high-level overview of the linear relationships between all variables.
    * **Figure 2**: A multi-panel depth profile plot is created to visualize how each key variable changes with depth and to identify critical oceanographic phenomena.
    * **Figure 3**: An interactive 3D scatter plot is generated, using depth, temperature, and nitrate as the three axes, with chlorophyll concentration represented by color and size to visually pinpoint the "optimal ecological niche."

---

### Key Findings & Visualizations

#### 1. The Grand Overview: Variable Correlations
The heatmap displays the Pearson correlation coefficients between all environmental variables. A key finding is the strong **negative correlation** between chlorophyll concentration and the three primary nutrients (**nitrate, phosphate, and silicate**). This aligns with established oceanographic principles, where phytoplankton growth consumes available nutrients in the water.

![Correlation Heatmap](Preview_graph_of_data_analysis/Correlation%20Heatmap%20Between%20Environmental%20Factors%20and%20Chlorophyll-a.png)

#### 2. The Scientific Context: Ocean Vertical Structure
The multi-panel depth profile plot clearly illustrates classic vertical stratification phenomena:
* **Thermocline**: A sharp decrease in temperature from the warm surface layer to the cold deep water.
* **Nutricline**: Nutrients are depleted at the surface and begin to increase sharply at a depth of approximately 100-150 meters.
* **Deep Chlorophyll Maximum (DCM)**: The peak chlorophyll concentration is found not at the surface, but at a depth of around 100-125 meters. This layer represents the optimal balance point between light availability from above and nutrient supply from below.

![Vertical Profiles of Key Oceanographic Parameters (0-400m)](Preview_graph_of_data_analysis/Vertical%20Profiles%20of%20Key%20Oceanographic%20Parameters%20(0-400m).png)

#### 3. The Insightful Discovery: The Phytoplankton Niche
This interactive 3D scatter plot is the central insight of the analysis. Each point represents a water sample, with its color and size determined by chlorophyll concentration.
By rotating and observing the plot, it becomes clear that the largest, brightest points (high chlorophyll) are highly concentrated in a specific 3D "cloud." This provides strong evidence that phytoplankton blooms are the result of a delicate trade-off, requiring a combination of **suitable temperature (approx. 20-25°C)**, **nascent nutrient availability (Nitrate > 0)**, and **sufficient light (depth of approx. 50-125m)**.

![The Ecological Niche for Chlorophyll-a.gif](Preview_graph_of_data_analysis/The%20Ecological%20Niche%20for%20Chlorophyll-a.gif)

---

### How to Run
1.  Ensure all required libraries are installed in your Python environment.
2.  Place all `.nc` data files into a folder named `Phytoplankton_Data` in the same directory as the `Phytoplankton_Analysis.ipynb` notebook.
3.  Open the `Phytoplankton_Analysis.ipynb` file in VS Code and run the cells in order.

### Libraries Used
* `pandas`
* `numpy`
* `xarray`
* `matplotlib`
* `seaborn`
* `plotly`
* `imageio` (for GIF generation)

---

### License
This project is licensed under the MIT License.
