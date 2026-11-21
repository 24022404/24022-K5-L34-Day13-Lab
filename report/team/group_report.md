# Báo cáo nhóm

## 1. Thông tin nhóm

- Tên nhóm: 04552
- Lớp: L3A
- Thành viên: xem `TEAM.md`

## 2. Mục tiêu và cách tiếp cận

Nhóm xây dựng hồ sơ launch v0 cho trợ lý hoàn phí LogiX-VN để đánh giá chi phí, mức sử dụng, cơ chế xử lý lỗi và khả năng ra quyết định của pilot. Nhóm phân tích 1.200 yêu cầu và 1.624 lần chạy bằng `src/lab13.py`; các số từ cột `_simulated` được ghi nhãn `simulated`. Hai thành viên gắn nhãn lỗi độc lập trước khi đối chiếu.

## 3. Giải pháp

**A - Mô hình chi phí.** Nhóm cộng token và tool của mọi lần chạy, chi phí xem lại và làm lại, rồi chia cho số việc thành công. Mô hình được kiểm tra bằng ba phép thử, phân tách theo loại yêu cầu và bổ sung chi phí cố định. Chi tiết: [`bang_chi_phi.md`](bang_chi_phi.md).

**B - Độ nhạy.** Nhóm thay đổi giá token, mức xem lại, mức làm lại, lương và giới hạn số lần chạy; đồng thời tính phần việc chuyển cho nhân viên. Kết quả B1-B4: [`bang_chi_phi.md`](bang_chi_phi.md).

**C - Phân loại lỗi.** Hai người gắn nhãn riêng 20 ca theo Google PAIR, sau đó xử lý bất đồng theo nguyên nhân gốc. Mỗi loại lỗi có cách phát hiện đo được, biện pháp và vai trò phụ trách trong [`bang_loi.md`](bang_loi.md).

**D - Thiết kế pilot.** Nhóm tính cỡ mẫu hiệu dụng trước khi chọn cách chia. Kế hoạch có đối chứng, ngẫu nhiên hóa, rollback và ít nhất ba luật dừng đủ NẾU - TRONG - THÌ - KHÔNG THÌ. Chi tiết: [`pilot_plan.yaml`](pilot_plan.yaml).

**E - Chỉ số và quyết định.** Nhóm đặc tả ba nhóm chỉ số, liên kết chúng với event có `trace_id`, rồi tổng hợp rủi ro và bằng chứng bất lợi trước khi đề xuất. Chi tiết: [`chi_so.md`](chi_so.md), [`ho_so_launch_v0.md`](ho_so_launch_v0.md).


## 4. Kết quả

- Chi phí mỗi việc thành công và so sánh với nhân viên tự làm: **[CHỜ KẾT QUẢ ĐÃ KIỂM TRA TỪ NGƯỜI 1]**.
- Ba yếu tố nhạy nhất: **[CHỜ BẢNG B1-B2 ĐÃ KIỂM TRA]**.
- Phạm vi pilot, cách chia và đánh đổi về cỡ mẫu: **[CHỜ `pilot_plan.yaml` HOÀN THIỆN]**.
- Chỉ số chính, chỉ số sử dụng và chỉ số an toàn: **[CHỜ `chi_so.md` HOÀN THIỆN]**.
- Đồng thuận giữa hai bộ nhãn: **[CHỜ NGƯỜI 2 ĐỐI CHIẾU, YÊU CẦU TỐI THIỂU 16/20]**.
- Đề xuất cuối: **[CHỜ `ho_so_launch_v0.md`: Go / Go có điều kiện / No-go]**.
- Kết quả duyệt chéo nhận từ hội đồng: **[CHỜ PHIÊN GATE 2a]**.


## 5. Khó khăn và cách xử lý

- Ba thành viên kiêm nhiệm nhiều vai trò. Nhóm tách file và nhánh để giảm xung đột, đồng thời giữ hai bộ nhãn độc lập.
- Thời gian xem lại và làm lại là giả lập; nhóm ghi nhãn `simulated` và yêu cầu pilot đo thời gian thực.
- Số cụm hạn chế độ nhạy; nhóm tính cỡ mẫu hiệu dụng và ghi rõ đánh đổi trước khi chọn phương án.

## 6. Tổng hợp đóng góp

Phân công, đóng góp thực tế và bằng chứng file/commit của từng thành viên được ghi trong [`TEAM.md`](../../TEAM.md) và báo cáo cá nhân tương ứng.

## 7. Hạn chế và hướng cải thiện

- Dữ liệu giả lập và chưa có đối chứng nên chưa cho phép kết luận nhân quả.
- Pilot phải đo thời gian, khối lượng và chi phí thực tế; duy trì event có `trace_id`, đối soát và kiểm tra mẫu.
- Chỉ xem xét mở rộng sau khi đạt cỡ mẫu, luật dừng và tiêu chí quyết định đã viết trước.

## 8. Tài liệu tham khảo

- Đề bài và hướng dẫn Lab 13 trong thư mục `docs/`.
- Erol và cộng sự, *Cost-of-Pass: An Economic Framework for Evaluating Language Models*.
- Google PAIR, *People + AI Guidebook*, phần Errors and Graceful Failure.
- Tài liệu `statsmodels.stats.power.NormalIndPower`.
