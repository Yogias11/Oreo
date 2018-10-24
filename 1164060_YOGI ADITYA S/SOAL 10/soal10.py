import shapefile #import library yang digunakan
w=shapefile.Writer() #untuk membuat file 
w.shapeType #untuk mengecek type file yang dibuat

w.field("kolom1","C") #untuk membuat kolom di database
w.field("kolom2","C") 

w.record("ngek","satu") #untuk membuat record / isi dari kolom yang dibuat pd db
w.record("crot","dua")
w.record("ngok","tiga")
w.record("ngAk","4")
w.record("ngo","5")
w.record("ngokkk","6") 
 
w.poly(parts=[[[-6,-2],[3,-2], [5,3],[-4,3], [-6,-2]]],shapeType=shapefile.POLYLINE) #untuk membuat garis bertipe polyline
w.poly(parts=[[[-2,-1],[1,-1], [3,2],[0,2], [-2,-1]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-12,-4],[6,-4], [10,6],[-8,6], [-12,-4]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-8,-3],[4,-3], [7,4],[-5,4], [-8,-3]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-24,-8],[12,-8], [20,12],[-16,12], [-24,-8]]],shapeType=shapefile.POLYLINE)
w.poly(parts=[[[-48,-16],[24,-16], [40,24],[-32,24], [-48,-16]]],shapeType=shapefile.POLYLINE)

w.save("soal10") #untuk save