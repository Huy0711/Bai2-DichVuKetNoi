import firebase_admin
from firebase_admin import credentials, db
from datetime import datetime

# Kết nối Firebase
cred = credentials.Certificate("firebase_config.json")
firebase_admin.initialize_app(cred, {
    'databaseURL': 'https://bai-2-a52bf-default-rtdb.firebaseio.com/'
})

# Nhập dữ liệu
station_id = input("Nhập mã trạm: ")
temperature = float(input("Nhiệt độ (°C): "))
humidity = float(input("Độ ẩm (%): "))
wind = float(input("Gió (m/s): "))
pressure = float(input("Áp suất (hPa): "))

data = {
    "ID": station_id,
    "Name": f"Weather Station {station_id}",
    "Time": datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
    "Temperature": temperature,
    "Humidity": humidity,
    "Wind": wind,
    "Pressure": pressure
}

# Gửi lên Firebase
ref = db.reference(f"stations/{station_id}")
ref.set(data)

print("✅ Dữ liệu đã được gửi lên Firebase")
