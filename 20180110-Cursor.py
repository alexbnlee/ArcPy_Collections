import arcpy
mxd = arcpy.mapping.MapDocument("CURRENT")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyr = arcpy.mapping.ListLayers(mxd)[0]
cursor = arcpy.UpdateCursor(lyr, "NAME" = "辽宁省")
cursor = arcpy.UpdateCursor(lyr, '"NAME" = "辽宁省"')
print '"NAME" = "辽宁省"'
cursor = arcpy.UpdateCursor(lyr, "NAME")
cursor = arcpy.SearchCursor(lyr)
for row in cursor:
    print row.getValue("NAME")
    
cursor = arcpy.UpdateCursor(lyr)
for row in cursor:
    row.setValue("AREA", 200)
    
for row in cursor:
    row.setValue("AREA", 200)
    cursor.updateRow(row)
    
del cursor, row
for row in cursor:
    row.setValue("AREA", '200')
    cursor.updateRow(row)
    
for row in cursor:
    row.setValue("AREA", '200')
    cursor.updateRow(row)
    
for row in cursor:
    row.setValue("AREA", 200)
    cursor.updateRow(row)
    
cursor = arcpy.UpdateCursor(lyr)
for row in cursor:
    row.setValue("AREA", 200)
    cursor.updateRow(row)
    
del cursor, row
cursor = arcpy.UpdateCursor(lyr)
for row in cursor:
    row.setValue("AREA", 300)
    cursor.updateRow(row)
    
cursor = arcpy.SearchCursor(lyr)
for row in cursor:
    name = row.getValue("NAME")
    print name
    
cursor = arcpy.InsertCursor(lyr)
for i in range(1, 10):
    row = cursor.newRow()
    row.setValue("NAME", "阿拉斯加")
    row.setValue("ID", i)
    cursor.insertRow(row)
    

