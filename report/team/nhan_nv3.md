# Bộ nhãn độc lập của Người 3

## Cam kết thực hiện độc lập

- Người gắn nhãn: Đàm Tuấn Linh (2A202603624)
- Thời điểm bắt đầu: 14h30 21/11/2026
- Thời điểm chốt bộ nhãn: 15h 21/11/2026
- Tôi chỉ đọc 20 ca lỗi trong `docs/Ngay13_Lab13_De_bai_hoc_vien.docx` và định nghĩa năm loại lỗi.
- Tôi chưa xem `report/team/nhan_nv2.md`, chưa trao đổi nhãn với Người 2 và chưa đọc tài liệu có đáp án trước khi chốt bảng này.
- Sau khi chốt, tôi không sửa bộ nhãn độc lập; các ca bất đồng sẽ được ghi riêng trong `bang_loi.md`.

## Quy tắc gắn nhãn

Gắn theo nguyên nhân gốc, không theo vị trí cần sửa. Mỗi ca chỉ chọn một trong năm nhãn: `Do người dùng`, `Hệ thống`, `Ngữ cảnh`, `Giới hạn hệ thống`, `Ngầm`.

## Hai mươi ca lỗi

| Ca | Nhãn độc lập | Lý do theo nguyên nhân gốc |
| ---: | --- | --- |
| 1 | Do người dùng | Khách nhập thiếu số tài khoản. |
| 2 | Hệ thống | Gọi tool sai tham số (hàng thường thay vì hàng nặng). |
| 3 | Ngữ cảnh | Đúng thiết kế (ví LogiX), nhưng khách hiểu là về ngân hàng. |
| 4 | Giới hạn hệ thống | Không có dữ liệu chặng hãng nước ngoài, đã báo rõ và chuyển nhân viên. |
| 5 | Ngầm | Hoàn theo giá trước giảm, không khách nào báo, không cảnh báo nào kích. |
| 6 | Do người dùng | Khách chọn sai mục “giao trễ”. |
| 7 | Hệ thống | Hoàn tiền thất bại nhưng vẫn báo “thành công”. |
| 8 | Ngầm | Dẫn điều khoản không tồn tại nhưng số tiền đúng, nên không ai nhận ra. |
| 9 | Do người dùng | Khách nhập mã đơn của sàn thay vì mã vận đơn. |
| 10 | Ngữ cảnh | Đúng chính sách bất khả kháng, nhưng app vẫn hiện “cam kết 24 giờ”. |
| 11 | Giới hạn hệ thống | Không xử lý được âm thanh. |
| 12 | Ngầm | Token D05 gấp 3 lần suốt 3 tuần mà không ai thấy. |
| 13 | Hệ thống | Ngoài phạm vi nhưng trả lời chung chung, không nói rõ là không xử lý. |
| 14 | Do người dùng | Khách bấm nhầm “Xác nhận đã nhận tiền”. |
| 15 | Hệ thống | Tính 100% thay vì 50%, nhân viên bắt được trước khi gửi. |
| 16 | Ngữ cảnh | Đúng thiết kế “gửi ngay”, nhưng khách bị làm phiền lúc 2:14 sáng. |
| 17 | Ngầm | Cache bảng giá cũ làm lệch 212 đơn trong 9 ngày, không ai mở lại. |
| 18 | Ngữ cảnh | Tính đúng, nhưng tin nhắn thiếu cách tính nên khách hiểu là hoàn thiếu. |
| 19 | Giới hạn hệ thống | Dữ liệu chỉ có 12 tháng, đã nói rõ và chuyển nhân viên. |
| 20 | Hệ thống | Lệnh hoàn thứ hai không có khoá chống trùng. |

## Kiểm tra trước khi chốt

- [x] Đã gắn đủ 20 ca, không để trống.
- [x] Mỗi ca chỉ có một nhãn thuộc đúng năm loại cho phép.
- [x] Lý do dựa trên nguyên nhân gốc, không chỉ nêu cách khắc phục.
- [ ] Chưa xem hoặc trao đổi bộ nhãn của Người 2.
- [x] Đã commit bộ nhãn trước khi đối chiếu (commit `499c9f3`).
