"""Lab 13 · Định giá agent và lập kế hoạch pilot (Gate 2a) — bài làm của nhóm (file nộp).
Chạy trong thư mục src/: python3 lab13.py   (cần pandas; Nhiệm vụ D cần thêm statsmodels)
Không cần khoá API. Dữ liệu trong hai file CSV là giả lập. Bản gốc chưa sửa nằm ở lab13_starter.py.
"""
import math
import pandas as pd

# Bảng giá GIẢ ĐỊNH của lab (không phải giá thật của nhà cung cấp nào)
GIA_VAO = 26        # đồng cho 1.000 token đầu vào
GIA_RA = 130        # đồng cho 1.000 token đầu ra
GIA_TOOL = 15       # đồng cho 1 lần gọi tool
LUONG_PHUT = 2000   # đồng cho 1 phút của nhân viên (đã gồm bảo hiểm, văn phòng)
BASELINE = 12000    # đồng cho 1 yêu cầu khi nhân viên tự làm (6 phút)
CO_DINH_THANG = 40_000_000   # chi phí cố định của trợ lý mỗi tháng
YC_THANG = 45_000            # số yêu cầu hoàn phí mỗi tháng


# ---------- Nhiệm vụ A1 · Kinh tế của việc chạy lại ----------
def so_lan_chay_ky_vong(p, k=None):
    """Số lần chạy trung bình cho 1 yêu cầu khi mỗi lần đúng với xác suất p.
    k = số lần chạy tối đa; k=None nghĩa là chạy lại đến khi đúng."""
    if k is None:
        return 1 / p
    return (1 - (1 - p) ** k) / p


def ti_le_thanh_cong(p, k=None):
    """Xác suất yêu cầu thành công sau tối đa k lần chạy."""
    if k is None:
        return 1.0
    return 1 - (1 - p) ** k


def he_so_chi_phi_moi_viec_thanh_cong(p, k=None):
    """Chi phí mỗi việc thành công, tính bằng bội số của giá một lần chạy."""
    return so_lan_chay_ky_vong(p, k) / ti_le_thanh_cong(p, k)


def kiem_tra_dap_an_biet_truoc():
    """Ba phép thử bắt buộc đạt 100% trước khi tính trên dữ liệu."""
    assert abs(so_lan_chay_ky_vong(0.8, 2) - 1.20) < 1e-9, 'p=0,8, tối đa 2 lần → 1,20 lần chạy'
    assert abs(so_lan_chay_ky_vong(0.8) - 1.25) < 1e-9, 'p=0,8, chạy đến khi đúng → 1,25 lần chạy'
    assert abs(he_so_chi_phi_moi_viec_thanh_cong(0.8, 3) - 1.25) < 1e-9, 'p=0,8, tối đa 3 lần → 1,25 lần giá một lần chạy'
    print('Ba phép thử đáp án biết trước: ĐẠT')


# ---------- Nhiệm vụ A2 · Mô hình chi phí từ trace ----------
def mo_hinh(runs, reqs, gia_vao=26, gia_ra=130, gia_tool=15, luong_phut=2000,
            he_so_xem_lai=1.0, he_so_lam_lai=1.0, max_lan_chay=None):
    """Trả về dict: token, tool, chay_lai, xem_lai, lam_lai, tong, thanh_cong, cps, hoa_don_moi_yc.
    - token, tool: cộng trên MỌI lần chạy trong runs, kể cả lần lỗi.
    - xem_lai, lam_lai: số phút (cột *_simulated) × luong_phut. Đây là số GIẢ LẬP (simulated).
    - thanh_cong: số yêu cầu có ket_qua == 'thanh_cong'.
    - max_lan_chay: giới hạn số lần chạy (B1, B3); yêu cầu chạy quá giới hạn chuyển nhân viên, 0 phút simulated.
    """
    reqs = reqs.copy()
    runs = runs[runs['request_id'].isin(reqs['request_id'])]
    if max_lan_chay is not None:
        runs = runs[runs['attempt'] <= max_lan_chay]
        vuot = reqs['so_lan_chay'] > max_lan_chay
        reqs.loc[vuot, 'ket_qua'] = 'chuyen_nhan_vien'
        reqs.loc[vuot, ['phut_xem_lai_simulated', 'phut_lam_lai_simulated']] = 0
    tien_token = runs['tokens_in'] / 1000 * gia_vao + runs['tokens_out'] / 1000 * gia_ra
    tien_tool = runs['tool_calls'] * gia_tool
    xem_lai = reqs['phut_xem_lai_simulated'].sum() * luong_phut * he_so_xem_lai
    lam_lai = reqs['phut_lam_lai_simulated'].sum() * luong_phut * he_so_lam_lai
    tong = tien_token.sum() + tien_tool.sum() + xem_lai + lam_lai
    thanh_cong = (reqs['ket_qua'] == 'thanh_cong').sum()
    return dict(token=tien_token.sum(), tool=tien_tool.sum(),
                chay_lai=(tien_token + tien_tool)[runs['attempt'] > 1].sum(),
                xem_lai=xem_lai, lam_lai=lam_lai, tong=tong,
                thanh_cong=thanh_cong, cps=tong / thanh_cong,
                hoa_don_moi_yc=(tien_token.sum() + tien_tool.sum()) / len(reqs))


if __name__ == '__main__':
    runs = pd.read_csv('logix_runs.csv')
    reqs = pd.read_csv('logix_requests.csv', keep_default_na=False)
    kiem_tra_dap_an_biet_truoc()

    print('\n=== A2 · Toàn mẫu (xem_lai, lam_lai, tong, cps là simulated) ===')
    ket_qua = mo_hinh(runs, reqs)
    for ten, gia_tri in ket_qua.items():
        print(f'{ten:16s} {gia_tri:>14,.1f}')
    print(f"cps gấp {ket_qua['cps'] / ket_qua['hoa_don_moi_yc']:.1f} lần hoá đơn token+tool chia số yêu cầu")
    print(f"giờ nhân viên chiếm {(ket_qua['xem_lai'] + ket_qua['lam_lai']) / ket_qua['tong']:.1%} tổng chi phí [simulated]")
    # cả hệ thống: nhân viên làm thay MỌI yêu cầu không thành công (222 = 1.200 − 978)
    he_thong = (ket_qua['tong'] + (len(reqs) - ket_qua['thanh_cong']) * BASELINE) / len(reqs)
    print(f'chi phí cả hệ thống / yêu cầu = {he_thong:,.0f} đ = {he_thong / BASELINE:.2f}x của {BASELINE:,} đ [simulated]')

    print('\n=== A3 · Theo loại yêu cầu [simulated] ===')
    print(f"{'loai':10s} {'so_yc':>6s} {'ti_le_tc':>9s} {'lan/yc':>7s} {'cps':>9s} {'so_voi_12k':>11s}")
    for loai in ['noi_dia', 'hang_nang', 'quoc_te', 'doi_tac']:
        sub = reqs[reqs['loai'] == loai]
        r = mo_hinh(runs, sub)
        so_run = runs['request_id'].isin(sub['request_id']).sum()
        print(f"{loai:10s} {len(sub):>6d} {r['thanh_cong'] / len(sub):>9.1%} {so_run / len(sub):>7.2f} "
              f"{r['cps']:>9,.0f} {r['cps'] / BASELINE:>10.2f}x")

    print('\n=== A4 · Cộng chi phí cố định, phạm vi noi_dia + hang_nang [simulated] ===')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    r = mo_hinh(runs, pv)
    ti_le = r['thanh_cong'] / len(reqs)  # 900 / 1200
    tc_thang = YC_THANG * ti_le
    co_dinh = CO_DINH_THANG / tc_thang
    print(f"thành công trong phạm vi: {r['thanh_cong']} / {len(reqs)}; thành công mỗi tháng ở quy mô đầy đủ: {tc_thang:,.0f}")
    print(f"cps phạm vi: {r['cps']:,.0f}; cố định mỗi việc: {co_dinh:,.0f}; cộng lại: {r['cps'] + co_dinh:,.0f} = {(r['cps'] + co_dinh) / BASELINE:.2f}x")
    co_dinh_nua = CO_DINH_THANG / (tc_thang / 2)
    print(f"khối lượng giảm một nửa: cố định {co_dinh_nua:,.0f}; cộng lại: {r['cps'] + co_dinh_nua:,.0f} = {(r['cps'] + co_dinh_nua) / BASELINE:.2f}x")

    # ---------- Nhiệm vụ B · Bảng độ nhạy ----------
    print('\n=== B1 · Đổi từng yếu tố [simulated] ===')
    kich_ban = {
        'Giá token gấp đôi':        dict(gia_vao=52, gia_ra=260),
        'Giá token giảm một nửa':   dict(gia_vao=13, gia_ra=65),
        'Xem lại gấp đôi':          dict(he_so_xem_lai=2),
        'Xem lại giảm một nửa':     dict(he_so_xem_lai=0.5),
        'Làm lại gấp đôi':          dict(he_so_lam_lai=2),
        'Làm lại giảm một nửa':     dict(he_so_lam_lai=0.5),
        'Lương tăng 25%':           dict(luong_phut=2500),
        'Tối đa 2 lần chạy':        dict(max_lan_chay=2),
        'Chỉ 1 lần chạy':           dict(max_lan_chay=1),
    }
    goc = mo_hinh(runs, reqs)['cps']
    thay_doi = {}
    print(f"{'Gốc':25s} {goc:8,.0f}")
    for ten, kw in kich_ban.items():
        cps = mo_hinh(runs, reqs, **kw)['cps']
        thay_doi[ten] = (cps / goc - 1) * 100
        print(f'{ten:25s} {cps:8,.0f} {thay_doi[ten]:+6.1f}%')

    print('\n=== B2 · Một cặp: giá token gấp đôi + xem lại gấp đôi [simulated] ===')
    cap = mo_hinh(runs, reqs, gia_vao=52, gia_ra=260, he_so_xem_lai=2)['cps']
    tong_rieng = thay_doi['Giá token gấp đôi'] + thay_doi['Xem lại gấp đôi']
    print(f'cặp: {cap:,.0f} đ ({(cap / goc - 1) * 100:+.1f}%); tổng hai tác động riêng: {tong_rieng:+.1f}%')
    print('Xếp hạng (mức tăng khi gấp đôi): làm lại > xem lại > lương nhân viên > giá token')

    print('\n=== B3 · Giới hạn số lần chạy: chi phí cả hệ thống [simulated] ===')
    print(f"{'Giới hạn':>9s} {'Tổng trợ lý':>13s} {'Không TC':>9s} {'Cả hệ thống':>13s} {'cps':>8s}")
    for k in (1, 2, 3):
        r = mo_hinh(runs, reqs, max_lan_chay=k)
        khong_tc = len(reqs) - r['thanh_cong']
        he_thong_k = r['tong'] + khong_tc * BASELINE
        print(f"{k:>7d} lần {r['tong']:>13,.0f} {khong_tc:>9d} {he_thong_k:>13,.0f} {r['cps']:>8,.0f}")

    print('\n=== B4 · Xem lại 100% cho noi_dia + hang_nang [simulated] ===')
    pv = reqs[reqs['loai'].isin(['noi_dia', 'hang_nang'])]
    runs_pv = runs[runs['request_id'].isin(pv['request_id'])]
    co_ok = runs_pv[runs_pv['status'] == 'ok']['request_id'].nunique()   # yêu cầu có ít nhất 1 lần chạy ok
    n_lam_lai = (pv['ket_qua'] == 'lam_lai').sum()
    hoa_don_pv = (runs_pv['tokens_in'] / 1000 * GIA_VAO + runs_pv['tokens_out'] / 1000 * GIA_RA
                  + runs_pv['tool_calls'] * GIA_TOOL).sum()
    tc_pv = (pv['ket_qua'] == 'thanh_cong').sum()
    phut_lam_lai_tb = reqs.loc[reqs['ket_qua'] == 'lam_lai', 'phut_lam_lai_simulated'].mean()
    for ten, phut_ll in (('đề cho 9 phút/ca', 9), (f'thực tế {phut_lam_lai_tb:.1f} phút/ca', phut_lam_lai_tb)):
        tong4 = co_ok * 5 * LUONG_PHUT + n_lam_lai * phut_ll * LUONG_PHUT + hoa_don_pv
        cps4 = tong4 / tc_pv
        hoa_von = (BASELINE * tc_pv - n_lam_lai * phut_ll * LUONG_PHUT - hoa_don_pv) / (co_ok * LUONG_PHUT)
        print(f'làm lại {ten}: {co_ok} yc xem lại, {n_lam_lai} ca làm lại, tổng {tong4:,.0f} đ, '
              f'cps {cps4:,.0f} đ = {cps4 / BASELINE:.2f}x; hoà vốn nếu mỗi lần xem lại ≤ {hoa_von:.1f} phút')

    # ---------- Nhiệm vụ D1 · Cỡ mẫu theo các cách chia ----------
    from statistics import NormalDist
    ICC = 0.02

    def co_mau(p1, p2, alpha=0.05, power=0.8):
        za, zb = NormalDist().inv_cdf(1 - alpha / 2), NormalDist().inv_cdf(power)
        pb = (p1 + p2) / 2
        return math.ceil((za * math.sqrt(2 * pb * (1 - pb))
                          + zb * math.sqrt(p1 * (1 - p1) + p2 * (1 - p2))) ** 2 / (p2 - p1) ** 2)

    print('\n=== D1 · Cỡ mẫu (baseline 0,70; ICC 0,02; alpha 0,05; power 0,8) ===')
    n5 = co_mau(0.70, 0.75)
    print(f'a) chia theo yêu cầu, +5 điểm: {n5} yêu cầu mỗi nhóm')
    m = 75
    de = 1 + (m - 1) * ICC
    n_b = math.ceil(n5 * de)
    nguoi = math.ceil(n_b / m)
    print(f'b) theo nhân viên, m = {m}: DE = {de:.2f}; {n_b} yêu cầu mỗi nhóm = {nguoi} nhân viên mỗi nhóm, tổng {2 * nguoi} > 40: không đủ người')
    print(f'c) 20 nhân viên mỗi nhóm: tối đa {20 / ICC:,.0f} < {n5}: không đạt mức chênh 5 điểm')
    print(f'd) 6 depot mỗi nhóm: tối đa {6 / ICC:,.0f}')
    n6 = co_mau(0.70, 0.76)
    m6 = math.ceil(n6 * (1 - ICC) / (20 - n6 * ICC))
    print(f'e) mức chênh 6 điểm: {n6} mỗi nhóm; 20 nhân viên mỗi nhóm cần m ≥ {m6} yêu cầu mỗi người (DE {1 + (m6 - 1) * ICC:.2f})')
    try:
        from statsmodels.stats.proportion import proportion_effectsize
        from statsmodels.stats.power import NormalIndPower
        pw = NormalIndPower().power(proportion_effectsize(0.75, 0.70), nobs1=n6, alpha=0.05, ratio=1)
    except ImportError:
        pw = NormalDist().cdf(0.05 / math.sqrt(0.7 * 0.3 / n6 + 0.75 * 0.25 / n6) - NormalDist().inv_cdf(0.975))
    print(f'power còn lại nếu cỡ mẫu {n6} mỗi nhóm nhưng tác động thật chỉ 5 điểm: {pw:.2f}')

    # ---------- Nhiệm vụ D3/E1 · Chỉ số tính thử ----------
    print('\n=== E1 · Chỉ số tính thử trên 1.200 yêu cầu ===')
    chinh = ((reqs['dong_trong_24h'] == 1) & (reqs['mo_lai_trong_7_ngay'] == 0)).sum()
    xem = reqs[reqs['duoc_xem_lai'] == 1]
    bo_qua = xem['quyet_dinh_xem_lai'].isin(['sua', 'bo']).sum()
    mo_lai = (reqs['mo_lai_trong_7_ngay'] == 1).sum()
    print(f'chính: {chinh}/{len(reqs)} = {chinh / len(reqs):.2%}')
    print(f'dùng (bỏ qua gợi ý): {bo_qua}/{len(xem)} = {bo_qua / len(xem):.2%}')
    print(f'an toàn (mở lại 7 ngày): {mo_lai}/{len(reqs)} = {mo_lai / len(reqs):.2%}')
    pv_mo_lai = (pv['mo_lai_trong_7_ngay'] == 1).mean()
    lam_lai_pv = (pv['ket_qua'] == 'lam_lai').mean()
    print(f'trong phạm vi noi_dia + hang_nang: mở lại {pv_mo_lai:.2%}; làm lại {lam_lai_pv:.2%}')
