
lyrs = arcpy.mapping.ListLayers(mxd)
lyrs[9]
lyrs[20]

# 注意写表达式的时候不能有字符串函数什么的，而且变量名需要用双引号
# 因此可以先print下效果
# SQL函数很无语

for i in range(9, 21):
    arcpy.gp.RasterCalculator_sa('8.64012 - 14.84545*Log10("' + lyrs[i].name + '") + 10.54793*Power(Log10("' + lyrs[i].name + '"), 2) - 3.45375 * Power(Log10("' + lyrs[i].name + '"), 3) + 0.4254 * Power(Log10("' + lyrs[i].name + '"), 4)', lyrs[i].name + "_sd.tif")
    

