import geopandas as gpd
import matplotlib.pyplot as plt

plt.rcParams['font.family'] ='Malgun Gothic'
plt.rcParams['axes.unicode_minus'] =False

shapefile = gpd.read_file("D:\python\geopan\LARD_ADM_SECT_SGG_11_202405.shp")
ax = shapefile.plot(column = "SGG_NM" , legend = True )

plt.show()
