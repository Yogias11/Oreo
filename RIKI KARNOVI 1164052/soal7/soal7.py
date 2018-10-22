import shapefile #mengimpor library shape pada python
w=shapefile.Writer() #menulis shape file
w.shapeType #menggunakan tipe apa shape di buat
w.field("kolom1","C") #membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C") #membuat file dengan nama kolom 2 dengan type character
w.record("ngek","satu") #membuat record dengan isi kolom 1 "ngek" dan kolom dua "satu"

w.poly(parts=[[[1,3],[5,3],[1,2],[5,2]]],shapeType=shapefile.POLYLINE) #membuat polyline denegan parameter 4 koordinat
w.save("soal7") #menyimpan data dengan nama soal7