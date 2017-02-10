import glob, os, shapefile

fileList = glob.glob('~/Desktop/Reseaux/*.shp')
print fileList

w = shapefile.Writer()
print w

for f in fileList:
    print f
    r = shapefile.Reader(f)
    w._shapes.extend(r.shapes())
    w.records.extend(r.records())

w.fields = list(r.fields)
w.save('~/Desktop/Reseau_ALL.shp')
