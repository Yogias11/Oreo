import shapefile #mengimpor library shape pada python
w=shapefile.Writer() #menulis shape file
w.shapeType #menentukan jenis shape yang akan dibuat

w.field("Nama Bidang","C") #membuat file dengan nama "nama bidang" dengan type character
w.field("Bidang Ke-","C") #membuat file dengan nama "bidang ke" dengan type character

w.record("jajargenjang_1","satu") #menyimpan koordinat yang sudah dibuat dengan nama jajargenjang1 dengan garis y diberikan nama satu
w.record("jajargenjang_2","dua") #menyimpan koordinat yang sudah dibuat dengan nama jajargenjang2 dengan garis y diberikan nama dua
w.record("jajargenjang_3","tiga") #menyimpan koordinat yang sudah dibuat dengan nama jajargenjang3 dengan garis y diberikan nama dua
w.record("jajargenjang_4","empat") #menyimpan koordinat yang sudah dibuat dengan nama jajargenjang4 dengan garis y diberikan nama dua
w.record("jajargenjang_5","lima") #menyimpan koordinat yang sudah dibuat dengan nama jajargenjang5 dengan garis y diberikan nama dua
w.record("jajargenjang_6","enam") #menyimpan koordinat yang sudah dibuat dengan nama jajargenjang6 dengan garis y diberikan nama dua
w.record("jajargenjang_7","tigtujuh") #menyimpan koordinat yang sudah dibuat dengan nama jajargenjang7 dengan garis y diberikan nama dua
w.record("jajargenjang_8","delapan") #menyimpan koordinat yang sudah dibuat dengan nama jajargenjang8 dengan garis y diberikan nama dua
w.record("jajargenjang_9","sembilan") #menyimpan koordinat yang sudah dibuat dengan nama jajargenjang9 dengan garis y diberikan nama dua

w.poly(parts=[[[-5,8],[-1,8],[-3,6],[-7,6],[-5,8]]],shapeType=shapefile.POLYGON) #membuat polygon berbentuk jajargenjang dengan menggunakan 5 koordinat
w.poly(parts=[[[-5,4],[-1,4],[-3,2],[-7,2],[-5,4]]],shapeType=shapefile.POLYGON) #membuat polygon berbentuk jajargenjang dengan menggunakan 5 koordinat
w.poly(parts=[[[-5,-2],[-1,-2],[-3,-4],[-7,-4],[-5,-2]]],shapeType=shapefile.POLYGON) #membuat polygon berbentuk jajargenjang dengan menggunakan 5 koordinat
w.poly(parts=[[[-5,-6],[-1,-6],[-3,-8],[-7,-8],[-5,-6]]],shapeType=shapefile.POLYGON) #membuat polygon berbentuk jajargenjang dengan menggunakan 5 koordinat
 
w.poly(parts=[[[-1,-10],[3,-10],[1,-12],[-3,-12],[-1,-10]]],shapeType=shapefile.POLYGON) #membuat polygon berbentuk jajargenjang dengan menggunakan 5 koordinat

w.poly(parts=[[[3,-6],[7,-6],[5,-8],[1,-8],[3,-6]]],shapeType=shapefile.POLYGON) #membuat polygon berbentuk jajargenjang dengan menggunakan 5 koordinat
w.poly(parts=[[[3,-2],[7,-2],[5,-4],[1,-4],[3,-2]]],shapeType=shapefile.POLYGON) #membuat polygon berbentuk jajargenjang dengan menggunakan 5 koordinat
w.poly(parts=[[[3,4],[7,4],[5,2],[1,2],[3,4]]],shapeType=shapefile.POLYGON) #membuat polygon berbentuk jajargenjang dengan menggunakan 5 koordinat
w.poly(parts=[[[3,8],[7,8],[5,6],[1,6],[3,8]]],shapeType=shapefile.POLYGON) #membuat polygon berbentuk jajargenjang dengan menggunakan 5 koordinat

w.save("Soal10") #menyimpan file dengna nama "soal10"