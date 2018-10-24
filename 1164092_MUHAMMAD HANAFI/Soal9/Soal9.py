import shapefile #mengimpor library shape pada python
w=shapefile.Writer() #menulis shape file
w.shapeType #menentukan type shape
w.field("kolom1","C") #membuat field dengan nama kolom 1 dengan type character
w.field("kolom2","C") #membuat field dengan nama kolom 2 dengan type character
w.record("ngek","satu") #membuat record dengan isi kolom 1 "ngek" dan kolom dua "satu"
w.record("crot","dua") #membuat record dengan isi kolom 2 "crot" dan kolom dua "satu"
w.poly(parts=[[[1,3],[5,3], [5,2],[1,2],[1,3]]],shapeType=shapefile.POLYLINE) #membuat polygon dengan 5 koordinat dengan type polyline
w.poly(parts=[[[1,6],[5,6], [5,9],[1,9],[1,6]]],shapeType=shapefile.POLYLINE) #membuat polygon dengan 5 koordinat dengan type polyline
w.save("soal9") #menyimpan file dengan nama "soal9"