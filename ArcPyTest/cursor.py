import arcpy

arcpy.env.workspace="E:\ArcGISFiles\DataFiles\feature.gdb"
cursor=arcpy.SearchCursor("roads","'TYPE'<>4")
for row in cursor:
    print(row)