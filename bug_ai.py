import sys
import pandas as pd

# Import thuật toán Cây quyết định (Decision Tree) từ thư viện Scikit-learn
from sklearn.tree import DecisionTreeClassifier
# Import hàm chia bộ dữ liệu thành tập huấn luyện (Train) và tập kiểm tra (Test)
from sklearn.model_selection import train_test_split
# Import hàm tính toán độ chính xác của mô hình dự đoán
from sklearn.metrics import accuracy_score

# Cấu hình đầu ra console (stdout) sử dụng định dạng UTF-8 để tránh lỗi font Tiếng Việt trên Windows
if sys.version_info >= (3, 7):
    sys.stdout.reconfigure(encoding='utf-8')

# BƯỚC 1: ĐỌC DỮ LIỆU TỪ FILE CSV
# Sử dụng thư viện Pandas để đọc file "bugs.csv" lưu lịch sử các lỗi và chuyển thành DataFrame (bảng dữ liệu)
df = pd.read_csv("bugs.csv")

print("Dữ liệu lỗi lịch sử dùng để huấn luyện AI:")
print(df)

# BƯỚC 2: CHỌN DỮ LIỆU ĐẦU VÀO VÀ ĐẦU RA MONG MUỐN
# X (Dữ liệu đầu vào / Thuộc tính quyết định): Lựa chọn cột 'Bug_Count' (số lượng lỗi) và 'Crash' (có sập hệ thống không)
X = df[['Bug_Count', 'Crash']]

# y (Đầu ra / Nhãn kết quả mong muốn): Cột 'Severity' (mức độ nghiêm trọng của lỗi: Minor, Major, Critical)
y = df['Severity']

# BƯỚC 3: CHIA DỮ LIỆU THÀNH TẬP HUẤN LUYỆN (TRAIN) VÀ TẬP KIỂM TRA (TEST)
# train_test_split chia ngẫu nhiên dữ liệu theo tỷ lệ:
# - test_size=0.2 (20% dữ liệu dùng để kiểm định mô hình, tương đương 4 mẫu)
# - 80% còn lại dùng để huấn luyện mô hình (tương đương 12 mẫu)
# - random_state=42: Cố định cách chia ngẫu nhiên để mọi lần chạy code đều ra kết quả giống nhau
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# BƯỚC 4: KHỞI TẠO VÀ HUẤN LUYỆN MÔ HÌNH MACHINE LEARNING
# Khởi tạo mô hình AI dựa trên thuật toán Cây quyết định (Decision Tree Classifier)
model = DecisionTreeClassifier()

# Tiến hành huấn luyện mô hình bằng cách cho Cây quyết định học quy luật từ tập Train (X_train và y_train)
model.fit(X_train, y_train)

# BƯỚC 5: ĐÁNH GIÁ ĐỘ CHÍNH XÁC CỦA MÔ HÌNH AI
# Sử dụng mô hình đã huấn luyện để dự đoán kết quả cho tập kiểm tra X_test (4 mẫu lỗi)
y_pred = model.predict(X_test)

# So sánh kết quả dự đoán (y_pred) với kết quả thực tế (y_test) để tính tỷ lệ chính xác (Accuracy Score)
acc = accuracy_score(y_test, y_pred)

print("\n--- ĐÁNH GIÁ MÔ HÌNH AI ---")
print("Độ chính xác của mô hình trên tập Test:", round(acc * 100, 2), "%")

# BƯỚC 6: THỬ NGHIỆM DỰ ĐOÁN VỚI MẪU LỖI MỚI PHÁT SINH
# Giả định một lỗi mới được phát hiện trong phần mềm có:
# - Bug_Count = 8 (số lượng lỗi trong module này tích lũy lên tới 8 lỗi)
# - Crash = 1 (lỗi này làm sập toàn bộ hệ thống)
new_bug = pd.DataFrame([[8, 1]], columns=['Bug_Count', 'Crash'])

# Yêu cầu mô hình AI dự đoán mức độ nghiêm trọng cho lỗi mới này
result = model.predict(new_bug)

print("\n--- DỰ ĐOÁN LỖI MỚI PHÁT SINH ---")
print("Thông số lỗi mới nhập vào:")
print(" - Số lượng lỗi (Bug_Count) = 8")
print(" - Làm sập hệ thống (Crash) = Có (1)")

# Xuất kết quả dự đoán từ AI
print("\nKết quả AI dự đoán mức độ nghiêm trọng:")
if result[0] == "Minor":
    print("AI dự đoán: Minor - Lỗi nhẹ (Không ảnh hưởng nhiều tới hệ thống)")
elif result[0] == "Major":
    print("AI dự đoán: Major - Lỗi trung bình (Ảnh hưởng chức năng nhưng chưa gây sập)")
else:
    print("AI dự đoán: Critical - Lỗi nghiêm trọng (Làm sập hệ thống, cần xử lý ngay lập tức!)")