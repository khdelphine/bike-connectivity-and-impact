
# ***************************************
# ***Overview***
# Script name: config.py
# Purpose: This Python module defines the global varialbles for all the scripts of the project.
# Project: Connectivity and community impact analysis in Arcpy for potential bicycle infrastructure improvements.
# Extent: 4 PA Counties in Philadelphia suburbs.
# Last updated: May 12, 2019
# Author: Delphine Khanna
# Organization: Bicycle Coalition of Greater Philadelphia
# Note: This Arcpy script is meant to run in ArcGIS Desktop. It is NOT optimized for complete unsupervised automation.
# ***************************************

# *********
# Option switches
# Should we remove from the mxd document all intermediary layers generated by the process?
REMOVE_INTERMEDIARY_LAYERS_OPTION = "yes" # or "no"
# We have the option of computing everything from scratch or only recompute the final scores
# (Note: only applies to roads.py and trails.py)
COMPUTE_FROM_SCRATCH_OPTION = "no" # or "yes"

# *********
# Set up global variables used in all scripts
base_path = "C:\\Users\\delph\\Desktop\\GIS\\BCGP\\Connectivity_and_impact"
data_path = base_path + "\\Data"
common_util_path = data_path + "\\common_util.gdb"
orig_datasets_path = data_path + "\\Orig_datasets"
county_list = ["Delaware", "Montgomery", "Bucks", "Chester"]
county_list1 = ["Delaware"]

# Set up global variables used in the CII script
gdb_output_CII_name = "\\script_output_CII3.gdb"
gdb_output_CII = data_path + gdb_output_CII_name

# Set up global variables used in roads.py script
gdb_output_roads_name = "\\script_output_roads3.gdb"
gdb_output_roads = data_path + gdb_output_roads_name
cii_overall_score_ras = common_util_path + "\\cii_overall_score_ras"
lts3_orig =  orig_datasets_path + "\\Road_analysis\\DVRPC_Bike_Stress_Suburban_LTS_3_Connections\\DVRPC_Bike_Stress_Suburban_LTS_3_Connections.shp"

# Set up global variables used in trails.py script
gdb_output_trails_name = "\\script_output_trails3.gdb"
gdb_output_trails = data_path + gdb_output_trails_name
islands_orig =  orig_datasets_path + "\\Trail_analysis\\DVRPC_Bike_Stress_LTS_1__2_Islands\\DVRPC_Bike_Stress_LTS_1__2_Islands.shp"
trails_orig = orig_datasets_path + "\\Trail_analysis\\Non_Circuit_Trails\\Non_Circuit_Trails.kml"
trails_converted_path = orig_datasets_path + "\\Trail_analysis\\Non_Circuit_Trails"