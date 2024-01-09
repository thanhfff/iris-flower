import csv
with open(file="D:/AI Engineer/vietnguyen/Iris.csv",mode= "r") as csv_file:
    data = csv_file.readlines()
    for row in data:
        print(row)

#tinh trung binh cong chieu dai va chieu rong dai hoa cua tung loai
print('1a:')
#setosa
x_setosa = []
y_setosa = []
tbcd_setosa = 0
tbcr_setosa = 0
for setosa in data[1:51]:
    loai_setosa = str(setosa).split(sep=',')
    chieudaidaihoa = loai_setosa[1]
    chieurongdaihoa = loai_setosa[2]
    #them phan tu vao list va dong thoi ep kieu du lieu so thuc
    try:
        x_setosa.append(float(chieudaidaihoa))
        y_setosa.append(float(chieurongdaihoa))
    except ValueError:
        pass
#tinh trung binh cong
for a in x_setosa:
    tbcd_setosa+=a
print('Trung binh cong chieu dai dai hoa setosa: ',tbcd_setosa/50)
for b in y_setosa:
    tbcr_setosa+=b
print('Trung binh cong chieu rong dai hoa setosa: ',tbcr_setosa/50)

#versicolor
x_versicolor = []
y_versicolor = []
tbcd_versicolor = 0
tbcr_versicolor = 0
for versicolor in data[51:101]:
    loai_versicolor = str(versicolor).split(sep=',')
    chieudaidaihoa = loai_versicolor[1]
    chieurongdaihoa = loai_versicolor[2]
    #them phan tu vao list va dong thoi ep kieu du lieu so thuc
    try:
        x_versicolor.append(float(chieudaidaihoa))
        y_versicolor.append(float(chieurongdaihoa))
    except ValueError:
        pass
#tinh trung binh cong
for c in x_versicolor:
    tbcd_versicolor+=c
print('Trung binh cong chieu dai dai hoa versicolor: ',tbcd_versicolor/50)
for d in y_versicolor:
    tbcr_versicolor+=d
print('Trung binh cong chieu rong dai hoa versicolor: ',tbcr_versicolor/50)

#virginica
x_virginica = []
y_virginica = []
tbcd_virginica = 0
tbcr_virginica = 0
for virginica in data[101:151]:
    loai_virginica = str(virginica).split(sep=',')
    chieudaidaihoa = loai_virginica[1]
    chieurongdaihoa = loai_virginica[2]
    #them phan tu vao list va dong thoi ep kieu du lieu so thuc
    try:
        x_virginica.append(float(chieudaidaihoa))
        y_virginica.append(float(chieurongdaihoa))
    except ValueError:
        pass
#tinh trung binh cong
for e in x_virginica:
    tbcd_virginica+=e
print('Trung binh cong chieu dai dai hoa virginica: ',tbcd_virginica/50)
for f in y_virginica:
    tbcr_virginica+=f
print('Trung binh cong chieu rong dai hoa virginica: ',tbcr_virginica/50)



#xac dinh chieu dai va chieu rong dai hoa lon nhat cua tung loai
print('1b:')
#setosa
max_length_setosa = 0
for row in data[1:51]:
    text = str(row).split(sep=',')
    if max_length_setosa < float(text[1]):
        max_length_setosa = float(text[1])
print("Setosa's length max:", max_length_setosa)

#versicolor
max_length_versicolor = 0
for row in data[51:101]:
    text = str(row).split(sep=',')
    if max_length_versicolor < float(text[1]):
        max_length_versicolor = float(text[1])
print("versicolor's length max:", max_length_versicolor)

#virginica
max_length_virginica = 0
for row in data[101:151]:
    text = str(row).split(sep=',')
    if max_length_virginica < float(text[1]):
        max_length_virginica = float(text[1])
print("virginica's length max:", max_length_virginica)

