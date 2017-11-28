# ----------------------------------------------------------------------------------------------------------------------
# Authors: Chris Brink
# ----------------------------------------------------------------------------------------------------------------------
# main_break_date_temps.py
# Created on: 11-27-2017
# Last edited on: 11-27-2017 (CGB)
# Description: Read in temperature table and assign min, max, and average temperature values to main breaks layer.
# ----------------------------------------------------------------------------------------------------------------------
import grumpy
import datetime
import arcpy
import os
import sys
import gc
import time
from arcpy import env
count = 0
# ----------------------------------------------------------------------------------------------------------------------
# Pylogger setup..
iLog = r'D:\python\logs\DSU_2.0_Info.log'
eLog = r'D:\python\logs\DSU_2.0_Error.log'
wLog = r'D:\python\logs\DSU_2.0_QAQC_(Warning).log'
pylogger = grumpy.pylogger_setup(iLog, eLog, wLog)
# ----------------------------------------------------------------------------------------------------------------------
# Set time variables; QA/QC time is set between 5:00PM and 5:10PM...
current_time = datetime.datetime.now()
compare_time2yr = current_time - datetime.timedelta(days=730)
format_current_time = current_time.strftime("%Y-%m-%d %H:%M:%S %p")
qaqc_time_start = current_time.strftime("%Y-%m-%d 17:00:00 PM")

# Set workspace....
workspace = r'W:\ArcView Projects\GIS_Asset_Management\CriticalityAssessment\Sensitivity Analysis\20171122_GIS_Sensitivity_Analysis\20171122_GIS_Sensitivity_Analysis.gdb'
temps_table = r'W:\ArcView Projects\GIS_Asset_Management\CriticalityAssessment\Sensitivity Analysis\20171122_GIS_Sensitivity_Analysis\20171122_GIS_Sensitivity_Analysis.gdb\TempsDaily_98_17'
temps_table_ids = r'W:\ArcView Projects\GIS_Asset_Management\CriticalityAssessment\Sensitivity Analysis\20171122_GIS_Sensitivity_Analysis\20171122_GIS_Sensitivity_Analysis.gdb\temps_ids'
water_leak = r'W:\ArcView Projects\GIS_Asset_Management\CriticalityAssessment\Sensitivity Analysis\20171122_GIS_Sensitivity_Analysis\20171122_GIS_Sensitivity_Analysis.gdb\active_leaks_join_copy'


# ----------------------------------------------------------------------------------------------------------------------
def get_temps_objids():
    """
    Get temperature objectids based on dates corresponding to water leak dates...
    """
    try:
        pylogger.debug('|BEGIN - ' + os.path.basename(os.path.realpath(__file__)) +
                       ' @ ' + sys._getframe().f_code.co_name + '|\n')

        water_leak_fields = [
            'OBJECTID',
            'break_date',
            'temp_avg_14day_prior',
            'temp_max_14day_prior',
            'temp_min_14day_prior',
            'temp_range_14day_prior'
            ]

        temps_fields = [
            'DATE',
            'OBJECTID'
            ]

        # Search water leak layer for break dates...
        with arcpy.da.SearchCursor(water_leak, water_leak_fields) as cursor1:

            for row1 in cursor1:

                leak_objid = row1[0]
                leak_date = row1[1]

                # Search temps table for matching records based on water leak dates...
                expression = "DATE = date '%s'" % leak_date
                with arcpy.da.SearchCursor(temps_table, temps_fields, where_clause=expression) as cursor2:

                    for row2 in cursor2:

                        temps_date = row2[0]
                        temps_id = row2[1]

                        # Create 14 day prior temperature objectid list...
                        obj_id_start = int(temps_id) - 14
                        obj_id_end = int(temps_id) + 1
                        obj_id_14day_list = [id for id in range(obj_id_start, obj_id_end)]

                        print(temps_id, obj_id_14day_list)
                        # temp_calculations(leak_objid, temps_obj_ids)

    except RuntimeError:
        # Log error message and send alert text message...
        pylogger.exception('|FAIL - ' + os.path.basename(os.path.realpath(__file__)) +
                           ' @ ' + sys._getframe().f_code.co_name + '|\n')

    finally:
        cursor1 = None
        row1 = None
        cursor2 = None
        row2 = None

        del cursor1
        del row1
        del cursor2
        del row2


# ----------------------------------------------------------------------------------------------------------------------
def temp_calculations(leak_id=None,
                      obj_id_list=None):
    """
        Read temperature table and retain values.
        """
    try:
        pylogger.debug('|BEGIN - ' + os.path.basename(os.path.realpath(__file__)) +
                       ' @ ' + sys._getframe().f_code.co_name + '|\n')

        temps_fields = [
            'OBJECTID',
            'DATE',
            'TAVG',
            'TMIN',
            'TMAX'
            ]

        # Create 14 day prior average_temps, min_temps, max_temps lists...
        average_temps = []
        min_temps = []
        max_temps = []

        for id_14 in obj_id_14day_list:

            # Search temps table for matching records based on water leak dates...
            expression = "OBJECTID = %s" % id_14
            with arcpy.da.SearchCursor(temps_table, temps_fields, where_clause=expression) as cursor1:

                for row1 in cursor1:

                    temps_id = row1[0]
                    temps_date = row1[1]
                    temps_tavg = row1[2]
                    temps_tmin = row1[3]
                    temps_tmax = row1[4]

                    # Populate 14 prior various temp lists...
                    average_temps.append(temps_tavg)
                    min_temps.append(temps_tmin)
                    max_temps.append(temps_tmax)

        print(average_temps, min_temps, max_temps)

            # Temp values to add to water leak dataset...
            # min_temps.sort()
            # min_temp = min_temps[0]
            # max_temp_index = len(max_temps) - 1
            # max_temp = max_temps[max_temp_index]
            # range_temp = max_temp - min_temp

    except RuntimeError:
        # Log error message and send alert text message...
        pylogger.exception('|FAIL - ' + os.path.basename(os.path.realpath(__file__)) +
                           ' @ ' + sys._getframe().f_code.co_name + '|\n')


# ----------------------------------------------------------------------------------------------------------------------
def main():
    """
    Makes function calls.

    """
    try:
        # Set edit session workspace...
        arcpy.env.workspace = workspace

        # Set environment to overwrite outputs...
        env.overwriteOutput = True

        # Declare edit session workspace...
        edit = arcpy.da.Editor(arcpy.env.workspace)

        # Check for active edit session before starting edit session...
        while edit.isEditing is True:
            time.sleep(5)

        # Edit session is started without undo/redo stack for versioned data
        # (for second argument, use False for unversioned data)
        edit.startEditing(True, False)

        # Nested 'try' statement that handles occasional system error
        # in starting an edit operation.
        try:
            # Start an edit operation...
            edit.startOperation()

        except:
            # Log to console; log info message...
            pylogger.debug('Failed at "startOperation". Ending program...')
            pylogger.exception('FAIL - @ main - edit.startOperation()')

        # Function calls...
        get_temps_objids()

        # Stop the edit operation...
        edit.stopOperation()

        # Nested 'try' statement handles scenario where fielbopu version is
        # being edited simulataneously by 2 or more users and
        # saving edits fails...
        try:
            # Try to stop edit session and save edits...
            edit.stopEditing(True)

        except:
            # Log to console; log info message...
            pylogger.debug('Failed at "stopEditing". Ending program...')
            pylogger.exception('FAIL - WaterLeakDSU_da_Cursor_Arcpy.py @ main - ' +
                               'edit.stopEditing()')
            # Abort operation and stop edit session without saving edits...
            edit.abortOperation()
            edit.stopEditing(False)

        pylogger.debug('|SUCCESS - main_break_date_temps.py|\n')

    except RuntimeError:
        # Log error message and send alert text message...
        pylogger.exception('|FAIL - ' + os.path.basename(os.path.realpath(__file__)) +
                           ' @ ' + sys._getframe().f_code.co_name + '|\n')

    finally:
        gc.collect()


# ----------------------------------------------------------------------------------------------------------------------
# Call main function if condition met...
if __name__ == '__main__':
    main()