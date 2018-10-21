import shapefile #import library yang digunakan 
w=shapefile.Writer(shapeType=1) #untuk membuat file bertipe shapefile dengan shapetype 1
w.shapeType #untuk mengecek type file yang dibuat
w.shapeType=3
w.shapeType #untuk mengecek type file yang dibuat

w.field("kolom1","C") #untuk membuat kolom di database
w.field("kolom2","C")

w.record("ngek","satu") #untuk membuat record / isi dari kolom yang dibuat pd db
w.record("ngok","dua")

w.point(1,1) #untuk membuat titik dengan koordinat 1,1
w.point(2,2) #untuk membuat titik dengan koordinat 2,2

w.save("soal3") #untuk save file