cursor = arcpy.da.UpdateCursor("new2", "ID")
for row in cursor:
    if row[0] == 19:
        row[0] = 234
        cursor.updateRow(row)
        

