import firebase_admin
from firebase_admin import credentials, db

# Kết nối Firebase
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bai-2-a52bf-default-rtdb.firebaseio.com/'
})

print("=== Ứng dụng xem dữ liệu thời tiết ===")
print("1. Xem thông tin 1 trạm")
print("2. Xem toàn bộ danh sách trạm")

choice = input("Chọn chế độ (1/2): ").strip()

if choice == "1":
    station_id = input("Nhập mã trạm cần xem: ").strip()
    ref = db.reference(f"stations/{station_id}")
    data = ref.get()

    if isinstance(data, dict):
        print("\n--- Thông tin thời tiết ---")
        for k, v in data.items():
            print(f"{k}: {v}")
    else:
        print("❌ Không tìm thấy dữ liệu trạm này.")

elif choice == "2":
    ref = db.reference("stations")
    stations = ref.get()

    if stations:
        print("\n=== Danh sách tất cả các trạm ===")
        
        # Nếu Firebase trả về dict
        if isinstance(stations, dict):
            for sid, info in stations.items():
                print(f"\n📍 Trạm {sid}:")
                if isinstance(info, dict):
                    for k, v in info.items():
                        print(f"   {k}: {v}")
        
        # Nếu Firebase trả về list
        elif isinstance(stations, list):
            for idx, info in enumerate(stations, start=1):
                print(f"\n📍 Trạm {idx}:")
                if isinstance(info, dict):
                    for k, v in info.items():
                        print(f"   {k}: {v}")
    else:
        print("❌ Không có dữ liệu trạm nào.")

else:
    print("❌ Lựa chọn không hợp lệ.")
