import shapefile #mengimpor library shape pada python
w=shapefile.Writer() #menulis shape file
w.shapeType #menentukan jenis shape file
w.field("kolom1","C") #membuat file dengan nama kolom 1 dengan type character
w.field("kolom2","C") #membuat file dengan nama kolom 2 dengan type character
w.record("ngek","satu") #membuat record dengan kolom1 "ngek" dan kolom2 "satu"

w.poly(parts=[[[1,3],[5,3],[1,2],[5,2],[1,3]]],shapeType=shapefile.POLYLINE) #membuat polygon dengan tipe shapefile polyline
w.save("soal8") #menyimpan file dengna nama "soal18"