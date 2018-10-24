import shapefile 
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)
w.field("kolom1","C") #membuat dbs dengan 2 field, berupa kolom
w.field("kolom2","C")
#membuat dbs dengan 2 field, berupa kolom
w.record("a","satu")
w.record("b","dua")
w.record("c","tiga")
w.record("d","empat")
w.record("e","lima")
#membuat 5 row karena menggunakan 5
w.poly(parts=[[[2,7],[5,7],[4,5],[1,5],[2,7]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[2,3],[5,3],[4,1],[1,1],[2,3]]],shapeType=shapefile.POLYGON)
w.poly(parts=[[[5,-1],[4,-3],[1,-3],[2,-1],[5,-1]]],shapeType=shapefile.POLYGON)
w.poly(parts=[[[-1,7],[-2,5],[-5,5],[-4,7],[-1,7]]],shapeType=shapefile.POLYGON)
w.poly(parts=[[[-2,1],[-5,1],[-4,3],[-1,3],[-2,1]]],shapeType=shapefile.POLYGON)


w.save("soal10")