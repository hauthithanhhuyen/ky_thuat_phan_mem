# BẢN TÓM TẮT CHUYÊN SÂU: CÁC LOẠI AI/ML VÀ KHẢ NĂNG ÁP DỤNG TRONG QA

Tài liệu này tóm tắt toàn bộ lý thuyết nền tảng về Trí tuệ nhân tạo (AI), Học máy (Machine Learning - ML), phân biệt các phương pháp học (Học có giám sát, Học không giám sát, Học tăng cường) và chi tiết khả năng áp dụng thực tế của chúng trong hoạt động Đảm bảo chất lượng phần mềm (QA) và Kiểm thử (Software Testing).

---

## I. TỔNG QUAN VỀ AI, MACHINE LEARNING VÀ DEEP LEARNING

Để trình bày tốt trước hội đồng, cần phân biệt rõ mối quan hệ bao hàm giữa ba khái niệm cốt lõi này:

* **Trí tuệ nhân tạo (AI - Artificial Intelligence):** Là ngành khoa học máy tính rộng lớn nhằm xây dựng các hệ thống thông minh có khả năng mô phỏng hành vi trí tuệ của con người (như suy luận, giải quyết vấn đề, tự học và hiểu ngôn ngữ).
* **Học máy (ML - Machine Learning):** Là một nhánh con của AI. Thay vì lập trình các quy tắc cứng (Hard-coded rules), ML tập trung vào phát triển các thuật toán giúp máy tính tự tìm ra các quy luật từ dữ liệu thực tế để đưa ra dự đoán hoặc quyết định.
* **Học sâu (DL - Deep Learning):** Là một nhánh con của ML, sử dụng các mạng nơ-ron nhân tạo nhiều lớp (Deep Neural Networks) để mô phỏng hoạt động của não bộ người nhằm xử lý dữ liệu phức tạp (như hình ảnh, âm thanh, video).

---

## II. PHÂN LOẠI CÁC PHƯƠNG PHÁP HỌC MÁY (ML) CHÍNH

### 1. Học có giám sát (Supervised Learning)
* **Nguyên lý hoạt động:** Mô hình học tập dựa trên dữ liệu đã được **gán nhãn sẵn (Labeled Data)**. Tức là với mỗi mẫu dữ liệu đầu vào (Input/Features $X$), ta đã biết trước kết quả đầu ra đúng (Output/Label $y$). Mô hình sẽ tìm hàm ánh xạ $f(X) = y$ để dự đoán nhãn cho dữ liệu mới.
* **Hai dạng bài toán chính:**
  * **Phân loại (Classification):** Dự đoán các nhãn rời rạc (ví dụ: lỗi này là *Minor*, *Major* hay *Critical*; email này là *Spam* hay *Not Spam*).
  * **Hồi quy (Regression):** Dự đoán các giá trị số liên tục (ví dụ: thời gian thực thi test case, số lượng lỗi phát sinh trong sprint tiếp theo).
* **Ưu điểm:** Độ chính xác cao, dễ đánh giá hiệu suất (qua các chỉ số như Accuracy, Precision, Recall).
* **Hạn chế:** Cực kỳ tốn kém công sức và thời gian để thu thập và gán nhãn dữ liệu ban đầu.

### 2. Học không giám sát (Unsupervised Learning)
* **Nguyên lý hoạt động:** Mô hình học từ dữ liệu **chưa được gán nhãn (Unlabeled Data)**. Thuật toán tự tìm kiếm các cấu trúc ẩn, mối liên hệ mật thiết hoặc các nhóm dữ liệu có đặc tính tương đồng nhau mà không cần sự hướng dẫn trước.
* **Hai dạng bài toán chính:**
  * **Gom nhóm (Clustering):** Chia tập dữ liệu thành các cụm sao cho các mẫu trong cùng một cụm tương đồng nhất, và khác biệt nhất với cụm khác.
  * **Giảm chiều dữ liệu / Phát hiện bất thường:** Loại bỏ các thuộc tính nhiễu, phát hiện các điểm dữ liệu dị biệt (Outliers) không tuân theo quy luật chung.
* **Ưu điểm:** Không cần tốn công gán nhãn dữ liệu, khám phá ra các quy luật tiềm ẩn mà con người chưa nhận ra.
* **Hạn chế:** Khó đánh giá chính xác chất lượng đầu ra, kết quả phụ thuộc lớn vào việc lựa chọn thuật toán và tham số.

### 3. Học tăng cường (Reinforcement Learning - RL)
* **Nguyên lý hoạt động:** Mô hình (Agent) tự học cách đưa ra các quyết định tối ưu thông qua quá trình liên tục tương tác với môi trường (Environment). Tại mỗi trạng thái (State), Agent thực hiện một hành động (Action) và nhận lại phản hồi thưởng (Reward) hoặc phạt (Penalty). Mục tiêu của Agent là tối đa hóa tổng điểm thưởng tích lũy theo thời gian.
* **Ứng dụng chính:** Chơi game (AlphaGo), điều khiển robot tự hành, tối ưu hóa các quy trình động.

---

## III. BẢNG SO SÁNH: HỌC CÓ GIÁM SÁT VS. HỌC KHÔNG GIÁM SÁT TRONG QA

| Tiêu chí | Học có giám sát (Supervised Learning) | Học không giám sát (Unsupervised Learning) |
| :--- | :--- | :--- |
| **Dữ liệu đầu vào** | Đã gán nhãn đầy đủ (ví dụ: Mô tả lỗi + Nhãn Severity). | Chưa gán nhãn (ví dụ: Chỉ có dòng Logs hệ thống thô). |
| **Mục tiêu chính** | Dự đoán nhãn hoặc giá trị cho mẫu dữ liệu mới. | Tìm kiếm cấu trúc ẩn hoặc gom cụm dữ liệu tương tự. |
| **Thuật toán phổ biến** | Decision Tree, Random Forest, SVM, Naive Bayes. | K-Means, PCA, DBSCAN, Isolation Forest. |
| **Ứng dụng cụ thể trong QA**| - Tự động phân loại mức độ lỗi (Severity).<br>- Dự đoán module nào dễ phát sinh lỗi nhất. | - Gom nhóm các báo cáo lỗi trùng lặp (Duplicate bugs).<br>- Phát hiện bất thường (Anomalies) trong Log file. |

---

## IV. KHẢ NĂNG ÁP DỤNG CỦA AI/ML TRONG HOẠT ĐỘNG QA & TESTING

Việc tích hợp AI/ML vào quy trình Đảm bảo chất lượng (QA) giúp chuyển dịch từ phương pháp **Kiểm thử thụ động (Reactive Testing)** sang **Kiểm thử chủ động & Thông minh (Predictive Testing)**.

### 1. Tự động sinh Kịch bản kiểm thử (Test Case Generation)
* **Giải pháp áp dụng:** Sử dụng Học có giám sát kết hợp với các mô hình xử lý ngôn ngữ tự nhiên (NLP) hoặc AI tạo sinh (Generative AI).
* **Cơ chế:** AI phân tích tài liệu đặc tả yêu cầu hệ thống (SRS) hoặc lịch sử thao tác của người dùng trên UI để tự động sinh ra các kịch bản kiểm thử (đường đi kiểm thử, dữ liệu kiểm thử biên) tự động.
* **Lợi ích:** Tăng độ bao phủ kiểm thử (Test coverage), tiết kiệm tới 70% thời gian thiết kế kịch bản thủ công.

### 2. Phân loại và Ưu tiên xử lý lỗi (Bug Classification & Triaging)
* **Giải pháp áp dụng:** Học có giám sát (Supervised Classification) - cụ thể như thuật toán **Decision Tree** trong bài thực nghiệm của đề tài.
* **Cơ chế:** Hệ thống phân tích thuộc tính của lỗi mới nhập vào (như module phát sinh, số lượng lỗi tích lũy, trạng thái sập hệ thống, hoặc từ khóa mô tả) để tự động xếp loại mức độ nghiêm trọng (Severity: Minor, Major, Critical).
* **Lợi ích:** Giúp phân phối nguồn lực phát triển sửa các lỗi nghiêm trọng trước, loại bỏ tính chủ quan/cảm tính của con người khi gán nhãn lỗi.

### 3. Phát hiện bất thường trong Logs (Log Anomaly Detection)
* **Giải pháp áp dụng:** Học không giám sát (Unsupervised Anomaly Detection).
* **Cơ chế:** Trong các hệ thống lớn, file Log có dung lượng hàng chục GB mỗi ngày, QA không thể đọc thủ công. AI sẽ tự động học các mẫu hành vi bình thường của hệ thống. Khi xuất hiện dòng Log dị biệt (ví dụ: thời gian phản hồi tăng vọt đột ngột, xuất hiện chuỗi lỗi lạ), AI sẽ ngay lập tức gắn cờ cảnh báo.
* **Lợi ích:** Rút ngắn thời gian debug và phát hiện lỗi ẩn trong hệ thống (Root Cause Analysis).

### 4. Kiểm thử giao diện tự động bằng Thị giác máy tính (Visual UI Testing)
* **Giải pháp áp dụng:** Học sâu (Deep Learning) và Thị giác máy tính (Computer Vision).
* **Cơ chế:** Mô hình AI chụp ảnh giao diện phần mềm qua các phiên bản, phân tích và so khớp mức độ sai lệch bố cục, font chữ, màu sắc, hoặc các nút bị đè lên nhau (Visual Diff) trên nhiều loại thiết bị khác nhau.
* **Lợi ích:** Thay thế kiểm thử giao diện thủ công, phát hiện nhanh các lỗi vỡ khung giao diện mà kiểm thử chức năng bằng code (như Selenium) khó quét ra được.

### 5. Tối ưu hóa bộ Test Suite (Test Suite Minimization & Prioritization)
* **Giải pháp áp dụng:** Học tăng cường (Reinforcement Learning) hoặc thuật toán Heuristics.
* **Cơ chế:** Khi code thay đổi, thay vì chạy lại toàn bộ hàng ngàn Test Case (Regression Testing) gây tốn thời gian, AI sẽ tính toán và chỉ ra nhóm Test Case nhỏ nhất có liên quan trực tiếp đến vùng code vừa sửa đổi và xếp thứ tự ưu tiên chạy các test case dễ tìm ra lỗi nhất trước.
* **Lợi ích:** Giảm thiểu thời gian chạy CI/CD, tối ưu hóa chi phí hạ tầng.

---

## V. KẾT LUẬN & ĐÁNH GIÁ THỰC TẾ
Mặc dù AI/ML mang lại nhiều đột phá cho hoạt động QA, việc triển khai vẫn tồn tại các rào cản cần lưu ý:
1. **Sự phụ thuộc vào dữ liệu:** Mô hình AI chỉ thông minh khi bộ dữ liệu huấn luyện lịch sử đủ lớn và sạch.
2. **Hiện tượng Overfitting (Quá khớp):** Mô hình học quá kỹ dữ liệu cũ dẫn đến dự đoán kém chính xác trên dữ liệu mới.
3. **Tính giải thích (Explainability):** Một số mô hình học sâu phức tạp hoạt động như "hộp đen", rất khó giải thích lý do tại sao AI đưa ra kết quả đó, gây khó khăn cho QA trong việc xác minh độ tin cậy. Do đó, việc lựa chọn thuật toán trực quan như **Decision Tree** trong đề tài là bước tiếp cận thực tế vô cùng phù hợp.
