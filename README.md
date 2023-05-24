![image](https://github.com/Thefuckingdead/Student_Classification_Project/assets/95278548/491be18f-a227-4b5f-8200-57a8677b1a21)
# Trên đây là dự án giữa kì đối với môn học "Nhập môn trí tuệ nhân tạo". Trong dự án này, chúng em thực hiện nhiệm vụ xem xét một ảnh xem đó là ai bằng cách sử dụng mô hình đã được lưu dưới dạng file có đuôi '.pkl'
___

## Thành viên nhóm:

Khuất Đăng Sơn 20002159 <b>(C)</b> ([github_link](https://github.com/Thefuckingdead))

Nguyễn Thị Thanh 20002164 ([github_link])

Trần Thiên Cường 20002109 ([github_link](https://github.com/TranThienCuong))
___

## Cấu trúc các thư mục:

* UI: Đây là thư mục chứa các file code html, css, javascript dùng để tạo nên giao diện người dùng cũng như liên kết với server được viết bằng Flask 
* Model: Đây là thư mục chứa các python notebook cho việc xây dựng nên mô hình cũng như chứa các tập dữ liệu dùng để huấn luyện
* Server: Thư mục chứa file server.py và các file liên quan để tạo nên webserver cũng như chứa model và file json đã được tạo ra từ folder Model
___

## Công nghệ được sử dụng:
<p align='center'>
  <a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" height="30" width="30">
  </a>
  
  <a>
    <img src="https://cdn.icon-icons.com/icons2/2148/PNG/512/flask_icon_132389.png" height="30" width="30">
  </a>
  
  <a>
    <img src="https://user-images.githubusercontent.com/67586773/105040771-43887300-5a88-11eb-9f01-bee100b9ef22.png" height="30" width="30">
  </a>
  
  <a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/e/ed/Pandas_logo.svg/2560px-Pandas_logo.svg.png" height="30" width="50">
  </a>
  
  <a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/3/32/OpenCV_Logo_with_text_svg_version.svg/831px-OpenCV_Logo_with_text_svg_version.svg.png" height="30" width="30">
  </a>
  
  <a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/d/d0/Google_Colaboratory_SVG_Logo.svg/2560px-Google_Colaboratory_SVG_Logo.svg.png" height="30" width="50">
  </a>
  
  <a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/8/84/Matplotlib_icon.svg/1200px-Matplotlib_icon.svg.png" height="30" width="30">
  </a>
  
  <a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/0/05/Scikit_learn_logo_small.svg/1200px-Scikit_learn_logo_small.svg.png" height="30" width="50">
  </a>
  
  <a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/1/1d/PyCharm_Icon.svg/1024px-PyCharm_Icon.svg.png" height="30" width="30">
  </a>
  
  <a>
    <img src="https://upload.wikimedia.org/wikipedia/commons/thumb/9/9a/Visual_Studio_Code_1.35_icon.svg/2048px-Visual_Studio_Code_1.35_icon.svg.png" height="30" width="30">
  </a>
</p>

* Python: Sử dụng version 3.9
* Numpy: Dùng để thao tác với mảng và các con số
* Pandas: Dùng để visualize các loại bảng cũng như thao tác với các file
* Matplotlib + Opencv: Sử dụng để hiển thị hình ảnh cũng như cắt ghép ảnh vào các folder khác nhau
* sklearn: Phục vụ việc xây dựng mô hình học máy cũng như tìm ra mô hình tốt nhất
* Google Colab: Sử dụng để tiện hơn trong việc xây dựng mô hình
* Vscode: Dùng trong việc code html, css, javascript
___

## Lưu đồ
1. Lưu đồ tổng quan
![General_Model](https://github.com/Thefuckingdead/Student_Classification_Project/assets/95278548/05866d57-a2e6-4b8a-b9cb-c8d8d3286edb)
------
2. Lưu đồ xây dựng mô hình machine learning
![Machine Learning Process](https://github.com/Thefuckingdead/Student_Classification_Project/assets/95278548/040dca91-de76-40eb-97d5-87b946d98128)
------
3. Mô hình chuẩn dựa trên CRISP-DM ([Reference_Link](https://en.wikipedia.org/wiki/Cross-industry_standard_process_for_data_mining))

![standard machine learning model](https://github.com/Thefuckingdead/Student_Classification_Project/assets/95278548/42f4f8a1-fa14-4ca0-bf2e-02e0d1b99a9c)
___

## Quy trình phát triển
- Bước 1: Data Collecting (Thu thập dữ liệu)
- Bước 2: Data Cleaning (Áp dụng kỹ thuật lọc ảnh haarcascade để nhận diện được khuôn mặt trong từng bức ảnh)
- Bước 3: Feature Engineering (Trích chọn đặc trưng - Áp dụng Wavelet Transform để lọc ra những đặc trưng có ý nghĩa quan trọng để đưa vào việc huần luyện mô hình học máy)
- Bước 4: Build Model (Đầu tiên, thử với svm(Support Vector Machine) sau đó sử dụng GridSearchCV áp dụng với 4 thuật toán học máy (KNN, Random Forest, SVM và Logistic Regression) với các tham số khác nhau để chọn ra được mô hình có điểm số tốt nhất (đáp ứng cả tập train và tập test))
- Bước 5: Build Flask Server (Viết 1 server sử dụng thư viện Flask và đưa mô hình học máy đã được huấn luyện ở trên vào Server đó)
- Bước 6: Build UI (Viết code html, css, javascript để tạo ra giao diện người dùng cũng như là phần front-end để giao tiếp với back-end (Webser đã được tạo ra từ bước trước đó) --> Tạo ra được 1 web hoạt động được ổn định)

___

## Cách thức cài đặt và hoạt động của web app
### 1. Cách thức cài đặt
1.1. Các gói phần mềm cần cài

- Để có thể chạy được dự án trước hết chúng ta cần cài python version 3.9 thông qua đường link sau : https://www.python.org/ 
- Sau đó đi vào thư mục Model. Ở đó mở git bash ([Có thể cài tại đây](https://git-scm.com/)) lên và gõ câu lệnh sau:
```python
pip install -r requirements.txt
```
- Sau khi cài đặt các gói thư viện thành công. Truy cập vào thư mục Server chạy file server.py thông qua câu lệnh sau:
```python
python server.py
```
Kết quả chạy được:
```
Starting Python Flask Server for Student Image Classification
loading server artifacts...start
Loading server artifacts...done
 * Serving Flask app 'server'
 * Debug mode: off
WARNING: This is a development server. Do not use it in a production deployment. Use a production WSGI server instead.
 * Running on http://127.0.0.1:5000
Press CTRL+C to quit
```
1.2 Chạy chương trình

- Sau khi thực hiện các bước như trên thì chúng ta truy cập vào folder UI mở file app.html lên sẽ được kết quả như sau

![image](https://github.com/Thefuckingdead/Student_Classification_Project/assets/95278548/a0d190d7-15bd-483b-aa9e-2e5c2558b344)

- Sau khi kéo ảnh vào ô "Drop File here or click to upload" và ấn vào nút classify chúng ta sẽ được kết quả như sau

![image](https://github.com/Thefuckingdead/Student_Classification_Project/assets/95278548/4da6a928-b502-4731-b91c-c7a59eebab00)
___

## Kết luận
-> Như vậy trong dự án trên nhóm chúng em đã làm được một ứng dụng khá thú vị khi có sự kết hợp giữa việc kết hợp học máy và tích hợp được vào 1 web app. Mặc dù web app phía trên của chúng em vẫn chưa được hoàn chỉnh, việc nhận diện nhiều lúc vẫn còn nhầm lẫn mặc dù mô hình đưa ra có thể thấy có độ chính xác khá cao nhưng mà đối với việc đưa vào thực tế vẫn chưa được ổn. Thông qua dự án trên chúng em đã có cái nhìn tổng thể hơn về quy trình để từ một mô hình học máy đưa đến tay người dùng khó khăn như thế nào. Không chỉ là việc biết về machine learning cũng như các thuật toán của chúng mà chúng ta còn phải biết tích hợp các công nghệ đưa ra sản phẩm cuối cùng đến tay người dùng.
- Trong tương lai sau khi đã tinh chỉnh xong mọi thứ, trang web đã hoạt động được hoàn hảo thì chúng em cũng tính đến bước cuối cùng đó là đẩy lên cloud, tạo ra 1 web chính thức và đưa được đến tay người dùng.
___

## Tài liệu tham khảo

1. Sport Celebrity Image Classification Playlist (author: Code Basic) (https://www.youtube.com/playlist?list=PLeo1K3hjS3uvaRHZLl-jLovIjBP14QTXc)
2. Link github (https://github.com/codebasics/py/tree/master/DataScience/CelebrityFaceRecognition)
3. What is Fourier Transform (author: 3Blue1Brown) (https://www.youtube.com/watch?v=spUNpyF58BY&t=423s)
4. Feature Engineering là gì? (https://viblo.asia/p/feature-engineering-phan-1-vai-tro-cua-feature-engineering-voi-viec-xay-dung-mo-hinh-hoc-may-co-ban-ve-dac-trung-cua-du-lieu-1Je5E420lnL)
