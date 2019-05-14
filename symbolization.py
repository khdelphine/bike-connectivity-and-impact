# ***************************************
# ***Overview***
# Script name: symbolization.py
# Purpose: This Arcpy module applies chosen symbolizations to a list of vectors and rasters.
# Project: Connectivity and community impact analysis in Arcpy for potential bicycle infrastructure improvements.
# Extent: 4 PA Counties in Philadelphia suburbs.
# Last updated: May 14, 2019
# Author: Delphine Khanna
# Organization: Bicycle Coalition of Greater Philadelphia
# Note: This Arcpy script is meant to run in ArcGIS Desktop. It is NOT optimized for complete unsupervised automation.
# ***************************************

# Import Arcpy module
import arcpy

# Import local modules
from config import *

# *****************************************
# Functions

# Apply the chosen symbolization to each vector layer
def symbolize_vectors(vectors_to_symbolize, lyr_file_param=""):
    mxd = arcpy.mapping.MapDocument("CURRENT")
    df = arcpy.mapping.ListDataFrames(mxd)[0]

    # Loop through every layer in the mxd document
    for lyr in arcpy.mapping.ListLayers(mxd, "", df):
        # Check if it is in the list of vector layers:
        if lyr.name in vectors_to_symbolize:
            # Get the chosen Lyr template used
            if len(lyr_file_param) > 0:
                lyr_file = arcpy.mapping.Layer(base_path + "\\Lyr\\" + lyr_file_param + ".lyr")
            else:
                lyr_file = arcpy.mapping.Layer(base_path + "\\Lyr\\" + lyr.name + ".lyr")
            print("Symbolize:" + lyr.name)
            # Apply the Lyr template to it
            arcpy.mapping.UpdateLayer(df, lyr, lyr_file, True)
    # Refresh the display of the mxd
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

# Recalculate the statistics for every rasters -- This is necessary for the step
# lyr.symbology.reclassify() to work properly later on
def recalculate_raster_statistics(rasters_to_symbolize):
    for ras in rasters_to_symbolize:
        # First some cleanup (we need to remove the previously displayed layer):
        remove_intermediary_layers([ras + "1"])

        # Now build the pyramids, and calculate the statistics on each rasters
        # on the drive. The Calculate_Statistics will also show the raster as a layer:
        print("Calculate Stats:" + ras)
        arcpy.BatchBuildPyramids_management(gdb_output + "\\" + ras)
        arcpy.CalculateStatistics_management(gdb_output + "\\" + ras)

# Apply the chosen symbolization to each raster
def apply_raster_symbolization(rasters_to_symbolize):
    mxd = arcpy.mapping.MapDocument("CURRENT")
    df = arcpy.mapping.ListDataFrames(mxd)[0]
    # Get the chosen Lyr template used
    lyr_file = arcpy.mapping.Layer(base_path + "\\Lyr\\cii_overall_score_ras1e.lyr")

    # Loop through every layer in the mxd document
    for lyr in arcpy.mapping.ListLayers(mxd, "", df):
        # Check if it is in the list of rasters
        if lyr.name in rasters_to_symbolize:
            print("Symbolize:" + lyr.name)
            # If so, apply the Lyr template to it
            arcpy.mapping.UpdateLayer(df, lyr, lyr_file, True)
            # And reclassify, so that the classification breaks are adapted #
            # the current raster
            lyr.symbology.reclassify()
            #print(lyr.symbology.classBreakValues)
    # Refresh the display of the mxd
    arcpy.RefreshActiveView()
    arcpy.RefreshTOC()

def symbolize_rasters(rasters_to_symbolize, recalc_stats):
    if recalc_stats == "yes":
        recalculate_raster_statistics(rasters_to_symbolize)
    apply_raster_symbolization(rasters_to_symbolize)
