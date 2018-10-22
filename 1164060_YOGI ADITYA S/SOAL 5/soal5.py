import shapefile #import library yang digunakan
w=shapefile.Writer() #untuk membuat file 
w.shapeType #untuk mengecek type file yang dibuat

w.field("kolom1","C") #untuk membuat kolom di database
w.field("kolom2","C") 

w.record("ngek","satu") #untuk membuat record / isi dari kolom yang dibuat pd db
 
w.line(parts=[[[1,5],[5,5],[5,1],[3,3],[1,1]]])  #untuk membuat kumpulan titik

w.save("soal5") #untuk save 