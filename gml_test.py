import owslib.wps
import owslib.etree
from gdal import ogr

gml = owslib.wps.GMLMultiPolygonFeatureCollection([[(-102.8184, 39.5273),
                                                    (-102.8184, 37.418),
                                                    (-101.2363, 37.418),
                                                    (-101.2363, 39.5273),
                                                    (-102.8184, 39.5273)]])

tmp = open("/tmp/gml", 'wb')
tmp.write(owslib.etree.etree.tostring(gml.getXml()))
tmp.close()
        
drv = ogr.GetDriverByName("GML")
ds = drv.Open(tmp.name ,0)

lyr = ds.GetLayer()

for f in lyr:
    print (f.GetGeometryRef())

ds.Destroy()


