# Nhãn độc lập · Người gắn nhãn 2

Người gắn nhãn: Bùi Xuân Thành (2A202603521) · Bắt đầu: 15:01 · Kết thúc: 15:09 (8 phút, không trao đổi, không xem nhãn người 3 hay file hướng dẫn chi tiết)

Năm loại (Google PAIR), gắn theo **nguyên nhân gốc**, không theo chỗ cần sửa:

- **Do người dùng**: người dùng nhập sai hoặc chọn sai
- **Hệ thống**: hệ thống trả lời/làm sai so với thiết kế và chính sách
- **Ngữ cảnh**: hệ thống làm đúng thiết kế nhưng người dùng thấy sai, vì giả định không khớp hoàn cảnh của họ
- **Giới hạn hệ thống**: hệ thống không thể trả lời (thiếu dữ liệu, ngoài phạm vi, đầu vào không xử lý được)
- **Ngầm**: có sai nhưng cả người dùng lẫn hệ thống đều không nhận ra

| Ca | Mô tả ngắn | Nhãn |
| --: | --- | --- |
| 1 | Khách nhập số tài khoản thiếu 2 chữ số, ngân hàng trả lỗi | Do người dùng |
| 2 | Kiện 28 kg, tool tra giá theo hàng thường, hoàn thiếu 45.000 đ, khách mở lại | Hệ thống |
| 3 | Thiết kế hoàn về ví LogiX, khách chờ tiền về ngân hàng, báo "chưa được hoàn" | Ngữ cảnh |
| 4 | Chặng do hãng nước ngoài giao, không có dữ liệu, trợ lý chuyển nhân viên | Giới hạn hệ thống |
| 5 | 14 đơn có mã giảm giá hoàn theo giá trước giảm, không ai báo, không cảnh báo | Ngầm |
| 6 | Khách chọn "giao trễ" nhưng mô tả hàng vỡ, trợ lý xử lý luồng giao trễ và từ chối | Do người dùng |
| 7 | API sổ cái 503, thử lại 3 lần vẫn báo khách "đã hoàn thành công" | Hệ thống |
| 8 | Trợ lý dẫn "Điều 7.2" không tồn tại, số tiền vẫn đúng | Hệ thống |
| 9 | Khách nhập mã đơn sàn TMĐT thay mã vận đơn, trợ lý báo không hợp lệ rồi dừng | Do người dùng |
| 10 | Trễ do bão, từ chối đúng chính sách, khách thấy vô lý vì app hiện "cam kết 24 giờ" | Ngữ cảnh |
| 11 | Tin nhắn thoại 40 giây, trợ lý không xử lý được âm thanh | Giới hạn hệ thống |
| 12 | Tool depot D05 thiếu trường, gọi nhiều lần, token D05 gấp 3 lần suốt 3 tuần không ai thấy | Ngầm |
| 13 | Hỏi hoàn phí bảo hiểm (ngoài phạm vi), trợ lý trả lời chung chung, không nói rõ | Giới hạn hệ thống |
| 14 | Khách bấm nhầm "Xác nhận đã nhận tiền", yêu cầu bị đóng | Do người dùng |
| 15 | Trễ 26 giờ, chính sách hoàn 50%, trợ lý tính 100%, nhân viên bắt được | Hệ thống |
| 16 | Thiết kế "gửi ngay", trợ lý gửi Zalo lúc 2:14 sáng, khách bị làm phiền | Ngữ cảnh |
| 17 | Bảng giá cũ trong cache cho đơn < 2 kg, lệch 1.000–2.000 đ, 212 đơn/9 ngày, không ai mở lại | Ngầm |
| 18 | Tính đúng hoàn 15.000 đ nhưng không kèm cách tính, khách tưởng thiếu và mở lại | Ngữ cảnh |
| 19 | Đơn 14 tháng trước, trợ lý chỉ có dữ liệu 12 tháng, nói rõ và chuyển nhân viên | Giới hạn hệ thống |
| 20 | Khách gửi lại sau 10 phút, trợ lý hoàn 2 lần vì không có khoá chống trùng | Hệ thống |