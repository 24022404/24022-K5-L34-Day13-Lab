# Bảng lỗi và cách khắc phục · Nhiệm vụ C

20 ca lỗi nằm trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx`. Năm loại theo Google PAIR: **Do người dùng · Hệ thống · Ngữ cảnh · Giới hạn hệ thống · Ngầm**. Gắn nhãn theo nguyên nhân gốc, không theo chỗ cần sửa.

## Hai bộ nhãn độc lập

Người gắn nhãn 1: ... · Người gắn nhãn 2: Bùi Xuân Thành (2A202603521) (gắn trong 8 phút, không trao đổi)

| Ca | Nhãn người 1 | Nhãn người 2 | Trùng? | Nhãn thống nhất |
| --: | --- | --- | --- | --- |
| 1 | ... | ... | ... | ... |
| 2 | ... | ... | ... | ... |
| 3 | ... | ... | ... | ... |
| 4 | ... | ... | ... | ... |
| 5 | ... | ... | ... | ... |
| 6 | ... | ... | ... | ... |
| 7 | ... | ... | ... | ... |
| 8 | ... | ... | ... | ... |
| 9 | ... | ... | ... | ... |
| 10 | ... | ... | ... | ... |
| 11 | ... | ... | ... | ... |
| 12 | ... | ... | ... | ... |
| 13 | ... | ... | ... | ... |
| 14 | ... | ... | ... | ... |
| 15 | ... | ... | ... | ... |
| 16 | ... | ... | ... | ... |
| 17 | ... | ... | ... | ... |
| 18 | ... | ... | ... | ... |
| 19 | ... | ... | ... | ... |
| 20 | ... | ... | ... | ... |

**Tỉ lệ đồng thuận:** ... / 20 = ...%

## Quy tắc phân biệt cho các ca không trùng

Mỗi ca không trùng một câu. Đồng thuận dưới 80% thì ghi định nghĩa đã viết lại.

- ...

## Bảng khắc phục cho 5 ca, mỗi loại một ca

Cách phát hiện phải đo được (event, ngưỡng, tần suất). Người phụ trách là một vai trò, không ghi "cả đội".

| Ca | Loại lỗi | Phát hiện bằng gì | Khắc phục thế nào | Ai phụ trách |
| --: | --- | --- | --- | --- |
| 1 | Do người dùng | Event `hoan_tien_ngan_hang_loi` (kèm `trace_id`, mã lỗi ngân hàng "sai số tài khoản"); theo dõi hằng ngày, cảnh báo khi > 1% lệnh hoàn trong ngày | Kiểm tra định dạng số tài khoản (độ dài, checksum theo ngân hàng) ngay lúc nhập và bắt khách xác nhận lại tên chủ tài khoản trước khi tạo lệnh hoàn | Product owner trợ lý hoàn phí |
| 20 | Hệ thống | Đối soát hằng giờ: đếm `request_id` có ≥ 2 event `hoan_tien_da_ghi`; ngưỡng > 0 ca là cảnh báo ngay | Thêm khoá chống trùng (idempotency key = mã vận đơn + loại hoàn) ở bước ghi sổ cái; lệnh thứ hai trả về kết quả của lệnh đầu thay vì hoàn lần nữa | Trưởng nhóm kỹ thuật tích hợp |
| 18 | Ngữ cảnh | Tỉ lệ `mo_lai_trong_7_ngay` của các yêu cầu hoàn một phần, đo theo tuần; cảnh báo khi cao hơn nhóm hoàn đủ 5 điểm % trở lên | Tin nhắn hoàn tiền luôn kèm cách tính: phí gốc, điều khoản áp dụng, tỉ lệ hoàn, số tiền (vd "30.000 đ × 50% theo mục trễ 24–48 giờ = 15.000 đ") | Trưởng nhóm CSKH |
| 13 | Giới hạn hệ thống | Event `ngoai_pham_vi` (có `trace_id`) do bộ phân loại ý định gắn; mỗi tuần lấy mẫu 50 hội thoại có từ khoá "bảo hiểm" mà không có event này, ngưỡng > 5% bị bỏ sót là phải sửa | Khi phát hiện yêu cầu ngoài phạm vi: nói rõ "trợ lý không xử lý phí bảo hiểm", đưa đầu mối công ty bảo hiểm đối tác và chuyển nhân viên kèm tóm tắt | Product owner trợ lý hoàn phí |
| 17 | Ngầm | Đối soát hằng ngày số tiền hoàn của trợ lý với bảng giá hiện hành, lấy mẫu ngẫu nhiên 2% đơn; cảnh báo khi > 0,5% đơn lệch; thêm event `bang_gia_version` ghi phiên bản bảng giá dùng cho mỗi lần tính | Xoá bộ nhớ đệm bảng giá mỗi khi có bản mới (theo ngày hiệu lực), chặn tính hoàn nếu phiên bản bảng giá cũ hơn bản hiện hành; tính lại và bù 212 đơn đã lệch | Kế toán trưởng phụ trách đối soát |
