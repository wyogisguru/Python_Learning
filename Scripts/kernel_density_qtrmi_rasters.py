import arcpy
from arcpy import env
from arcpy.sa import *

arcpy.env.extent = 'W:\\ArcView Projects\\GIS_Asset_Management\\CriticalityAssessment\\' \
                   '20170817_sde_bopu2_coopsde_water_system_criticality\\' \
                   '20171002_Sensitivity_Analysis_Outputs.gdb\WATER_PRESSURE_ZONES\\' \
                   'north_range_business_park'

env.workspace = 'W:\\ArcView Projects\\GIS_Asset_Management\\CriticalityAssessment\\' \
                '20170817_sde_bopu2_coopsde_water_system_criticality\\' \
                '20171002_Sensitivity_Analysis_Outputs.gdb'


# Set local variables...
inFeatures = "W:\\ArcView Projects\GIS_Asset_Management\\CriticalityAssessment\\" \
             "20170817_sde_bopu2_coopsde_water_system_criticality\\20171002_Sensitivity_Analysis_Outputs.gdb\\" \
             "MAIN_BREAKS\\beam_break"
cellSize = 20.5148198626637
populationField = "NONE"
searchRadius = 1320
outWorkspace = 'W:\\ArcView Projects\\GIS_Asset_Management\\CriticalityAssessment\\' \
               '20170817_sde_bopu2_coopsde_water_system_criticality\\20171002_Sensitivity_Analysis_Outputs.gdb\\'

outRaster = outWorkspace + 'northrangebusinessparkpz_krnl_dnsty_qtrmi_beambreaks'

outKernelDensity = KernelDensity(inFeatures, populationField, cellSize, search_radius=searchRadius,
                                 area_unit_scale_factor="SQUARE_MILES", method="PLANAR")

outKernelDensity.save(outRaster)

