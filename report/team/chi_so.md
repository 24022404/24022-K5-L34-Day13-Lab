# Đặc tả chỉ số, event và rủi ro kinh tế · Nhiệm vụ E1, E2

Số tính bằng `src/lab13.py` (mục E1). Số dựa trên cột `_simulated` hoặc giả định của lab ghi nhãn `simulated`.

## E1 · Đặc tả chỉ số

| Loại | Chỉ số | Công thức | Tính thử trên 1.200 yêu cầu |
| --- | --- | --- | --- |
| Chính (kết quả) | % yêu cầu đóng trong 24 giờ và không mở lại trong 7 ngày | `dong_trong_24h` bằng 1 và `mo_lai_trong_7_ngay` bằng 0, chia tổng số yêu cầu | 82,83% (994/1.200) |
| Dùng | Tỉ lệ bỏ qua gợi ý | `quyet_dinh_xem_lai` là `sua` hoặc `bo`, chia số yêu cầu được xem lại | 27,12% (48/177) |
| An toàn | Tỉ lệ lỗi lọt đến khách | `mo_lai_trong_7_ngay` bằng 1, chia tổng số yêu cầu | 4,25% (51/1.200) |
| Dùng | Nhóm tự đề xuất: % yêu cầu của nhân viên nhóm trợ lý được mở bằng trợ lý | số `agent_suggestion_shown` chia số `refund_request_created` của nhóm trợ lý, theo tuần | Không cần tính |
| An toàn | Nhóm tự đề xuất: % đơn hoàn sai tiền qua kiểm tra mẫu hằng tuần | `so_tien_da_hoan` khác `so_tien_dung` trong 100 đơn mẫu mỗi tuần, chia 100 (bắt lỗi ngầm mà khách chưa phát hiện) | Không cần tính |

Viết "chỉ số trong đợt chạy thử là 82,83%", không viết "trợ lý đã nâng chỉ số": đợt chạy thử không có nhóm đối chứng.

## Danh sách event

Mười event, mỗi event có `trace_id` để nối với trace của agent.

| Event | Ai tạo | Thuộc tính chính | Thời điểm |
| --- | --- | --- | --- |
| `refund_request_created` | Ứng dụng của khách | request_id, loai, so_tien, arm (trợ lý hoặc đối chứng), trace_id | Khi khách gửi yêu cầu |
| `agent_run_completed` | Agent | attempt, tokens_in, tokens_out, tool_calls, status, trace_id | Sau mỗi lần chạy, kể cả lần lỗi |
| `agent_suggestion_shown` | Giao diện nhân viên | staff_id, so_tien_de_xuat, trace_id | Khi gợi ý hiện ra |
| `staff_review_decision` | Nhân viên | giu / sua / bo, phut_xem_lai (đo thật), trace_id | Khi nhân viên bấm gửi, sửa hoặc bỏ |
| `staff_rework_completed` | Nhân viên | phut_lam_lai, ly_do, trace_id | Khi làm lại xong |
| `refund_ledger_write` | Dịch vụ sổ cái | idempotency_key, so_tien, ket_qua, trace_id | Khi ghi sổ |
| `handoff_to_staff` | Agent | reason, tom_tat, trace_id | Khi chuyển nhân viên |
| `ticket_closed` | Hệ thống ticket | closed_at, trace_id | Khi đóng yêu cầu |
| `ticket_reopened` | Khách | reopened_at, reason, trace_id | Khi khách mở lại |
| `audit_sample_checked` | Kế toán | so_tien_da_hoan, so_tien_dung, trace_id | Hằng tuần, 100 đơn mẫu |

**Kiểm tra chéo:** mỗi chỉ số ở bảng E1 tính được từ event nào.

- Chỉ số chính: `ticket_closed` (closed_at trong 24 giờ kể từ `refund_request_created`) và không có `ticket_reopened` trong 7 ngày.
- Chỉ số dùng (bỏ qua gợi ý): `staff_review_decision` (sua hoặc bo) chia tổng `staff_review_decision`.
- Chỉ số dùng tự đề xuất: `agent_suggestion_shown` chia `refund_request_created` của nhóm trợ lý.
- Chỉ số an toàn: `ticket_reopened` chia `refund_request_created`.
- Chỉ số an toàn tự đề xuất: `audit_sample_checked`.
- Chi phí mỗi việc thành công (luật dừng thứ hai của pilot): `agent_run_completed` (token, tool), `staff_review_decision` (phút xem lại), `staff_rework_completed` (phút làm lại).

Cả sáu chỉ số và luật dừng đều tính được từ danh sách event này. Với đối chứng, trường `arm` ở `refund_request_created` cho phép so hai nhóm.

## E2 · Rủi ro kinh tế

Số lấy từ bảng độ nhạy (`bang_chi_phi.md`), đều là số [simulated].

| Rủi ro | Tác động đã tính | Dấu hiệu theo dõi | Hành động | Người phụ trách |
| --- | --- | --- | --- | --- |
| Số ca làm lại tăng gấp đôi | +51,8%, chi phí mỗi việc thành công lên 6.787 đ [simulated] | Tỉ lệ làm lại theo tuần vượt 7% (đợt chạy thử: 4,9% trong phạm vi, 48/982) | Thu hẹp về noi_dia, rà 20 trace làm lại | PM trợ lý hoàn phí |
| Phải xem lại 100% kéo dài | 11.743 đ = 0,98x của 12.000 đ; 12.415 đ = 1,03x nếu làm lại 15,3 phút như dữ liệu [simulated] | Tỉ lệ yêu cầu được xem lại còn trên 50% khi hết bước 0.25 | Giảm xem lại theo bậc khi tỉ lệ sửa cộng bỏ dưới 15% | Trưởng nhóm CSKH |
| Khối lượng thấp hơn dự kiến | Chi phí cố định 40 triệu đ mỗi tháng: +1.185 đ mỗi việc ở 45.000 yêu cầu mỗi tháng, +2.370 đ mỗi việc nếu còn một nửa [simulated] | Số việc thành công theo tuần dưới 50% kế hoạch | Không mở rộng pilot, xem lại hợp đồng chi phí cố định | PM trợ lý hoàn phí |
| Giới hạn chạy lại 1 lần đẩy việc sang nhân viên | Chi phí cả hệ thống 7.449.781 đ so với 6.901.220 đ ở giới hạn 2 lần; thêm 85 yêu cầu sang nhân viên [simulated] | Số yêu cầu chuyển nhân viên theo tuần | Giữ giới hạn 2 lần chạy | Kỹ sư trưởng agent |
