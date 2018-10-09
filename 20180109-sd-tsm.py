fo = open("D:\\01-Working\\2017\\20171204-IDL_Average\\temp\\sd_stats.txt", "w+")
for r in rs:
    ro = arcpy.Raster(r)
    fo.writelines(ro.name + "\n")
    tm = ro.maximum
    sd_max = 8.64012 - 14.84545*math.log10(tm) + 10.54793*pow(math.log10(tm), 2) - 3.45375 * pow(math.log10(tm), 3) + 0.4254 * pow(math.log10(tm), 4)
    fo.writelines("MAX: " + str(round(sd_max, 2)) + "\n")
    tm = ro.minimum
    sd_min = 8.64012 - 14.84545*math.log10(tm) + 10.54793*pow(math.log10(tm), 2) - 3.45375 * pow(math.log10(tm), 3) + 0.4254 * pow(math.log10(tm), 4)
    fo.writelines("MIN: " + str(round(sd_min, 2)) + "\n")
    tm = ro.mean
    sd_mean = 8.64012 - 14.84545*math.log10(tm) + 10.54793*pow(math.log10(tm), 2) - 3.45375 * pow(math.log10(tm), 3) + 0.4254 * pow(math.log10(tm), 4)
    fo.writelines("MEAN: " + str(round(sd_mean, 2)) + "\n\n")
    
fo.close()

