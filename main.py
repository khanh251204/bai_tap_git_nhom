def tinh_thue_thu_nhap(thu_nhap):
    # Dev A áp dụng giảm trừ 4tr và thuế 10%
    thu_nhap_tinh_thue = thu_nhap - 4000000
    return max(0, thu_nhap_tinh_thue * 0.1)  
print("Thuế thu nhập phải nộp:", tinh_thue_thu_nhap(10000000))
  
