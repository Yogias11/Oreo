import shapefile #mengimpor modul shapefile
w=shapefile.Writer() #untuk membuat shapefile baru
w.shapeType #menyeting menggunakan jenis shape apa (point,polygon)

#membuat dbs dengan 2 field, berupa kolom
w.field("kolom1","C") #dengan type character
w.field("kolom2","C") #dengan type character


w.record("ngek","satu") #baris pertama kolom 1 berisi "ngek", kolom kedua berisi "satu"
w.record("ngok","dua") #baris pertama kolom 1 berisi "ngok", kolom kedua berisi "dua"

#membuat 2 row karena menggunakan 2 record
w.point(1,1) #mengisi .shp dengan titik point (=x1 , x=1)
w.point(2,2) #mengisi .shp dengan titik point (=x2 , x=2)

w.save("soal1") #melakukan save dengan nama (soal1)