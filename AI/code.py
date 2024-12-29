#Đầu tiên, nhập tất cả các thư viện có liên quan sẽ sử dụng cũng như dữ liệu của chính nó.
import os
import numpy as np
import pandas as pd
import matplotlib as plt
import seaborn as sns
import plotly.express as px

file_path = "winequality-red.csv"
#Đọc dữ liệu từ file dữ liệu
df = pd.read_csv(file_path)

#Hiển thị ra số dòng và số cột có trong bộ dữ liệu
df.shape

#In ra thông tin các thuộc tính có trong bộ dữ liệu
df.info()

#Đổi tên các thuộc tính để dễ theo dõi
df.columns = ['DoChua','AxBayHoi','AxCitric', 'Duong', 'Clo', 'SO2', 'SumSO2', 'TiTrong', 'pH', 'SO4', 'Ruou', 'KQ']

#Chuẩn hóa bảng dữ liệu theo từng đoạn nhỏ

for i in range(0, len(df.DoChua)):
    if 4.6 <= df.DoChua[i] < 5.73:
        df.DoChua[i] = 0
    elif df.DoChua[i] < 6.86:
        df.DoChua[i] = 1
    elif df.DoChua[i] < 7.99:
        df.DoChua[i] = 2
    elif df.DoChua[i] < 9.12:
        df.DoChua[i] = 3
    elif df.DoChua[i] < 10.25:
        df.DoChua[i] = 4
    elif df.DoChua[i] < 11.38:
        df.DoChua[i] = 5
    elif df.DoChua[i] < 12.51:
        df.DoChua[i] = 6
    elif df.DoChua[i] < 13.64:
        df.DoChua[i] = 7
    elif df.DoChua[i] <= 15.9:
        df.DoChua[i] = 8
    df.DoChua[i] += 1

for i in range(0, len(df.AxBayHoi)):
    if 0.12 <= df.AxBayHoi[i] < 0.27:
        df.AxBayHoi[i]  = 0
    elif df.AxBayHoi[i] < 0.41:
        df.AxBayHoi[i] = 1
    elif df.AxBayHoi[i] < 0.56:
        df.AxBayHoi[i] = 2
    elif df.AxBayHoi[i] < 0.7:
        df.AxBayHoi[i] = 3
    elif df.AxBayHoi[i] < 0.85:
        df.AxBayHoi[i] = 4
    elif df.AxBayHoi[i] < 1.0:
        df.AxBayHoi[i] = 5
    elif df.AxBayHoi[i] < 1.14:
        df.AxBayHoi[i] = 6
    elif df.AxBayHoi[i] <= 1.58:
        df.AxBayHoi[i] = 7
    df.AxBayHoi[i] += 1

for i in range(0, len(df.AxCitric)):
    if 0 <= df.AxCitric[i] < 0.1:
        df.AxCitric[i]  = 0
    elif df.AxCitric[i] < 0.2:
        df.AxCitric[i] = 1
    elif df.AxCitric[i] < 0.3:
        df.AxCitric[i] = 2
    elif df.AxCitric[i] < 0.4:
        df.AxCitric[i] = 3
    elif df.AxCitric[i] < 0.5:
        df.AxCitric[i] = 4
    elif df.AxCitric[i] < 0.6:
        df.AxCitric[i] = 5
    elif df.AxCitric[i] < 0.7:
        df.AxCitric[i] = 6
    elif df.AxCitric[i] < 0.8:
        df.AxCitric[i] = 7
    elif df.AxCitric[i] <= 1:
        df.AxCitric[i] = 8
    df.AxCitric[i] += 1

for i in range(0, len(df.Duong)):
    if 0.9 <= df.Duong[i] < 2.36:
        df.Duong[i]  = 0
    elif df.Duong[i] < 3.82:
        df.Duong[i] = 1
    elif df.Duong[i] < 5.28:
        df.Duong[i] = 2
    elif df.Duong[i] < 6.74:
        df.Duong[i] = 3
    elif df.Duong[i] < 8.99:
        df.Duong[i] = 4
    elif df.Duong[i] <= 15.5:
        df.Duong[i] = 5
    df.Duong[i] += 1

for i in range(0, len(df.Clo)):
    if 0.01 < df.Clo[i] < 0.07:
        df.Clo[i] = 0
    elif df.Clo[i] < 0.13:
        df.Clo[i] = 1
    elif df.Clo[i] < 0.19:
        df.Clo[i] = 2
    elif df.Clo[i] < 0.27:
        df.Clo[i] = 3
    elif df.Clo[i] <= 0.611:
        df.Clo[i] = 4
    df.Clo[i] += 1

for i in range(0, len(df.SO2)):
    if 1 <= df.SO2[i] < 8.1:
        df.SO2[i]  = 0
    elif df.SO2[i] < 15.2:
        df.SO2[i] = 1
    elif df.SO2[i] < 22.3:
        df.SO2[i] = 2
    elif df.SO2[i] < 29.4:
        df.SO2[i] = 3
    elif df.SO2[i] < 36.5:
        df.SO2[i] = 4
    elif df.SO2[i] < 43.6:
        df.SO2[i] = 5
    elif df.SO2[i] < 50.7:
        df.SO2[i] = 6
    elif df.SO2[i] < 57.8:
        df.SO2[i] = 7
    elif df.SO2[i] <= 72:
        df.SO2[i] = 8
    df.SO2[i] += 1

for i in range(0, len(df.SumSO2)):
    if 6 <= df.SumSO2[i] < 34.3:
        df.SumSO2[i]  = 0
    elif df.SumSO2[i] < 62.6:
        df.SumSO2[i] = 1
    elif df.SumSO2[i] < 90.9:
        df.SumSO2[i] = 2
    elif df.SumSO2[i] < 119.2:
        df.SumSO2[i] = 3
    elif df.SumSO2[i] < 147.5:
        df.SumSO2[i] = 4
    elif df.SumSO2[i] <= 289:
        df.SumSO2[i] = 5
    df.SumSO2[i] += 1

for i in range(0, len(df.TiTrong)):
    if 0.99 < df.TiTrong[i] < 0.994:
        df.TiTrong[i]  = 0
    elif df.TiTrong[i] < 0.995:
        df.TiTrong[i] = 1
    elif df.TiTrong[i] < 0.996:
        df.TiTrong[i] = 2
    elif df.TiTrong[i] < 0.997:
        df.TiTrong[i] = 3
    elif df.TiTrong[i] < 0.998:
        df.TiTrong[i] = 4
    elif df.TiTrong[i] < 0.999:
        df.TiTrong[i] = 5
    elif df.TiTrong[i] < 1:
        df.TiTrong[i] = 6
    elif df.TiTrong[i] < 1.0002:
        df.TiTrong[i] = 7
    elif df.TiTrong[i] < 1.0006:
        df.TiTrong[i] = 8
    elif df.TiTrong[i] < 1.001:
        df.TiTrong[i] = 9
    elif df.TiTrong[i] < 1.0021:
        df.TiTrong[i] = 10
    elif df.TiTrong[i] < 1.004:
        df.TiTrong[i] = 11
    df.TiTrong[i] += 1

for i in range(0, len(df.pH)):
    if 2.74 <= df.pH[i] < 2.87:
        df.pH[i] = 0
    elif df.pH[i] < 2.99:
        df.pH[i] = 1
    elif df.pH[i] < 3.12:
        df.pH[i] = 2
    elif df.pH[i] < 3.25:
        df.pH[i] = 3
    elif df.pH[i] < 3.38:
        df.pH[i] = 4
    elif df.pH[i] < 3.50:
        df.pH[i] = 5
    elif df.pH[i] < 3.63:
        df.pH[i] = 6
    elif df.pH[i] < 3.76:
       df.pH[i] = 7
    elif df.pH[i] <= 4.01:
        df.pH[i] = 8
    df.pH[i] += 1

for i in range(0, len(df.SO4)):
    if 0.33 <= df.SO4[i] < 0.5:
        df.SO4[i] = 0
    elif df.SO4[i] < 0.66:
        df.SO4[i] = 1
    elif df.SO4[i] < 0.83:
        df.SO4[i] = 2
    elif df.SO4[i] < 1:
        df.SO4[i] = 3
    elif df.SO4[i] < 1.17:
        df.SO4[i] = 4
    elif df.SO4[i] < 1.35:
        df.SO4[i] = 5
    elif df.SO4[i] <= 2:
        df.SO4[i] = 6
    df.SO4[i] += 1


#Gán giá trị goodquality với 2 giá trị là '1' và '0' tương ứng với chất lượng rượu tốt hoặc không tốt
df['goodquality'] = [1 if x >= 7 else 0 for x in df['KQ']]

#In ra bảng dữ liệu sau khi chuẩn hóa với 20 dòng
df.head(20)

#Sử dụng hàm để chạy cây quyết định
cotdt = ['DoChua','AxBayHoi','AxCitric', 'Duong', 'Clo', 'SO2', 'SumSO2', 'TiTrong', 'pH', 'SO4','Ruou']
x = df[cotdt]
y = df['goodquality'].astype('float')
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(x, y, test_size=0.5, random_state = 26)

clf = DecisionTreeClassifier(criterion='entropy', max_depth=5)
clf = clf.fit(X_train, y_train)

predictions = clf.predict(X_test)


test1 = []


# Lặp qua từng thuộc tính và nhập giá trị từ bàn phím
for attribute in cotdt:
    value = float(input(f'Nhập giá trị cho {attribute}: '))
    test1.append(value)

# Chuyển danh sách thành mảng 2 chiều để đưa vào mô hình
test1 = [test1]

# Dự đoán bằng mô hình cây quyết định
prediction = clf.predict(test1)
print(f'Kết quả dự đoán: {prediction}')

# Kiểm tra kết quả dự đoán và in ra thông báo tương ứng
if prediction == 1:
    print('Chất lượng rượu tốt')
else:
    print('Chất lượng rượu không tốt')
    #0.58	0.02	2	0.073	9	18	0.9968	3.36	0.57	9.5


#Tính độ chính xác của thuật toán
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC

svc = SVC()
svc.fit(X_train, y_train)

def compute_accuracy(Y_true, Y_pred):
    correctly_predicted = 0
    # lặp lại nhãn và kiểm tra độ trính xác
    for true_label, predicted in zip(Y_true, Y_pred):
        if true_label == predicted:
            correctly_predicted += 1
    # Tính toán điểm chính xác của việc so sánh
    accuracy_score = correctly_predicted / len(Y_true)
    return accuracy_score

Y_pred = svc.predict(X_test)
score = compute_accuracy(y_test, Y_pred)
print(score)

#Vẽ cây quyết định
import sklearn.tree as tr
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split
cotdt = ['DoChua','AxBayHoi','AxCitric', 'Duong', 'Clo', 'SO2', 'SumSO2', 'TiTrong', 'pH', 'SO4', 'Ruou']
x = df[cotdt]
y = df['goodquality'].astype('float')
dtree = tr.DecisionTreeClassifier()
dtree = dtree.fit(x, y)
tr.plot_tree(dtree)
[...]
