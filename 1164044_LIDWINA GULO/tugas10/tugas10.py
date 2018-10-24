import shapefile #mengimpor modul shapefil
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)

#membuat dbs dengan 2 field, berupa kolom
w.field("Nama Bidang","Bidang ke ") 
w.field("Nama Bidang","Bidang ke") 
#membuat dbs dengan 2 field, berupa kolom
w.record("jajargenjang 1","satu") 
w.record("jajargenjang 2","dua") 
w.record("jajargenjang 3","tiga") 
 
#membuat 3 row karena menggunakan 3
w.poly(parts=[[[-4,3],[-1,3], [-2,1],[-5,1],[-4,3]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[2,3],[5,3], [4,1],[1,1], [2,3]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[-4,-1],[-1,-1], [-2,-3],[-5,-3], [-4,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point
w.poly(parts=[[[2,-1],[5,-1], [4,-3],[1,-3], [2,-1]]],shapeType=shapefile.POLYGON) #mengisi .shp dengan titik point

 
w.save("soal10")#melakukan save dengan nama (soal1)