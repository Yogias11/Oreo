import shapefile #import library yang digunakan
w=shapefile.Writer() #untuk membuat file 
w.shapeType #untuk mengecek type file yang dibuat

w.field("kolom1","C") #untuk membuat kolom di database
w.field("kolom2","C") 

w.record("ngek","satu") #untuk membuat record / isi dari kolom yang dibuat pd db
 
w.poly(parts=[[[1,3],[5,3],[1,2],[5,2]]], shapeType=shapefile.POLYLINE) #untuk membuat garis bertipe polyline

w.save("soal7") #untuk save