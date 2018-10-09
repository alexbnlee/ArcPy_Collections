import arcpy
arcpy.env.workspace = r"D:\01-Working\2018\20180411-HAD_FREQ\tmp"
arcpy.Merge_management(["New_Shapefile", "New_ShapefileCopy", "New_ShapefileCopy2"], "merge")
arcpy.Union_analysis(["New_Shapefile", "New_ShapefileCopy", "New_ShapefileCopy2"], "union")
mxd = arcpy.mapping.MapDocument("current")
df = arcpy.mapping.ListDataFrames(mxd)[0]
lyrs = arcpy.mapping.ListLayers(df)
lyrs[0]
lyrs
for i in range(0, 3):
    print str(i)
    
for i in range(0, 3):
    for j in range(0, 3):
        if i <> j:
            print(str(i)+":"+str(j))
            
for i in range(0, 3):
    for j in range(0, 3):
        if i <> j:
            arcpy.Intersect_analysis([lyrs[i], lyrs[j]], "inter_" + lyrs[i].name + "_" + lyrs[j].name)
            
for i in range(0, 3):
    for j in range(0, 3):
        if i < j:
            print(str(i)+":"+str(j))
            
for i in range(0, 3):
    for j in range(0, 3):
        if i < j:
            arcpy.Intersect_analysis([lyrs[i], lyrs[j]], "inter_" + lyrs[i].name + "_" + lyrs[j].name)
            
for i in range(0, 3):
    for j in range(0, 3):
        if i < j:
            arcpy.Intersect_analysis([lyrs[i], lyrs[j]], "inter_" + lyrs[i].name + "_" + lyrs[j].name)
            
for i in range(0, 3):
    for j in range(0, 3):
        if i < j:
            arcpy.Intersect_analysis([lyrs[i], lyrs[j]], "inter_" + str(i).zfill(2) + "_" + str(j).zfill(2))
            
lyrs = arcpy.mapping.ListLayers(df)
for i in range(0, 3):
    for j in range(0, 3):
        if i < j:
            arcpy.Intersect_analysis([lyrs[i], lyrs[j]], "2_inter_" + str(i).zfill(2) + "_" + str(j).zfill(2))
            
arcpy.Union_analysis(["New_Shapefile", "New_ShapefileCopy", "New_ShapefileCopy2"], "union")
# arcpy.Select_analysis('union', r'D:\McDelfino\Documents\ArcGIS\Default.gdb\union_Select', '"FID" = 0')
for i in range(0, 6):
    arcpy.Select_analysis("union", "uniq_"+str(i).zfill(2), '"FID" = ' + str(i))
    
geo1 = arcpy.CopyFeatures_management("uniq_00", arcpy.Geometry())
g1 = geo1[0]
geo2 = arcpy.CopyFeatures_management("New_Shapefile", arcpy.Geometry())
g2 = geo2[0]
g2.contains(g1)
cursor = arcpy.da.SearchCursor("uniq_00", "Id")
cursor[0]
for row in cursor:
    print row[0]
    
cursor.reset()
for row in cursor:
    row[0]++
    
for row in cursor:
    row[0] = row[0] + 1
    
cursor[0][0]
for row in cursor:
    tmp = row[0]
    
print tmp
tmp
cursor.reset()
for row in cursor:
    tmp = row[0]
    
tmp
cursor = arcpy.da.UpdateCursor("uniq_00", "Id")
for row in cursor:
    print row[0]
    
cursor.reset()
for row in cursor:
    row[0] = row[0] + 1
    
cursor.reset()
for row in cursor:
    row[0] = row[0] + 1
    cursor.updateRow(row)
    
lyrs = arcpy.mapping.ListLayers(df)
lyrs
for i range(0, 5):
for i in range(0, 5):
    for j in range(8, 11):
        
for i in range(0, 5):
    for j in range(8, 11):
        print(str(i)+"_"+str(j)
        
for i in range(0, 5):
    for j in range(8, 11):
        print(str(i)+"_"+str(j))
        
for i in range(0, 5):
    geo1 = arcpy.CopyFeatures_management(lyrs[i], arcpy.Geometry())
    g1 = geo1[0]
    for j in range(8, 11):
        geo2 = arcpy.CopyFeatures_management(lyrs[j], arcpy.Geometry())
        
for i in range(0, 5):
    geo1 = arcpy.CopyFeatures_management(lyrs[i], arcpy.Geometry())
    g1 = geo1[0]
    for j in range(8, 11):
        geo2 = arcpy.CopyFeatures_management(lyrs[j], arcpy.Geometry())
        g2 = geo2[0]
        if g2.contains(g1):
            cursor = arcpy.da.UpdateCursor(lyrs[i], "Id")
            for row in cursor:
                row[0] = row[0] + 1
                cursor.updateRow(row)
                
len(lyrs)
for i in range(0, 5):
    for j in range(8, 11):
        print(lyrs[i], lyrs[j])
        
geoms = arcpy.CopyFeatures_management("union", arcpy.Geometry())
len(geoms)
for i in range(0, len(geoms))
cursor = arcpy.da.UpdateCursor("union", "Id")
i = 0
for row in cursor:
    geom = geoms[i]
    for j in range(8, 11):
        geo2 = arcpy.CopyFeatures_management(lyrs[j], arcpy.Geometry())
        g2 = geo2[0]
        if g2.contains(geom):
            row[i] = row[i] + 1
            cursor.updateRow(row)
    i = i + 1
    
for row in cursor:
    geom = geoms[i]
    for j in range(8, 11):
        geo2 = arcpy.CopyFeatures_management(lyrs[j], arcpy.Geometry())
        g2 = geo2[0]
        if g2.contains(geom):
            row[0] = row[0] + 1
            cursor.updateRow(row)
    i = i + 1
    
lyrs = arcpy.mapping.ListLayers(df)
lyrs
cursor = arcpy.da.UpdateCursor("union", "Id")
i = 0
geoms = arcpy.CopyFeatures_management("union", arcpy.Geometry())
for row in cursor:
    geom = geoms[i]
    print("row", str(i))
    for j in range(1, 4):
        geo2 = arcpy.CopyFeatures_management(lyrs[j], arcpy.Geometry())
        g2 = geo2[0]
        if g2.contains(geom):
            row[0] = row[0] + 1
            cursor.updateRow(row)
            print("   :"+lyrs[i].name)
    i = i + 1
    
cursor = arcpy.da.UpdateCursor("union", "Id")
i = 0
geoms = arcpy.CopyFeatures_management("union", arcpy.Geometry())
for row in cursor:
    geom = geoms[i]
    print("row", str(i))
    for j in range(1, 4):
        geo2 = arcpy.CopyFeatures_management(lyrs[j], arcpy.Geometry())
        g2 = geo2[0]
        if g2.contains(geom):
            row[0] = row[0] + 1
            cursor.updateRow(row)
            print("   :"+lyrs[j].name)
    i = i + 1
    

