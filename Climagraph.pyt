import requests
import matplotlib.pyplot as plt
import datetime
import json

API_KEY = "masukkan_api_key_anda"
CITY = "Denpasar"
URL = f"http://api.openweathermap.org/data/2.5/forecast?q={CITY}&appid={API_KEY}&units=metric"

def fetch_weather_data():
    """Mengambil data cuaca dari API."""
    response = requests.get(URL)
    if response.status_code == 200:
        return response.json()
    else:
        print("Gagal mengambil data cuaca:", response.status_code)
        return None

def process_weather_data(data):
    """Mengolah data cuaca menjadi rata-rata suhu harian."""
    daily_temps = {}
    for entry in data["list"]:
        date = entry["dt_txt"].split(" ")[0]
        temp = entry["main"]["temp"]
        if date not in daily_temps:
            daily_temps[date] = []
        daily_temps[date].append(temp)
    
    daily_avg_temp = {date: sum(temps) / len(temps) for date, temps in daily_temps.items()}
    return daily_avg_temp

def plot_weather_data(daily_avg_temp):
    """Membuat grafik suhu harian."""
    dates = list(daily_avg_temp.keys())
    temps = list(daily_avg_temp.values())

    plt.figure(figsize=(10, 5))
    plt.plot(dates, temps, marker='o', color='b', label="Rata-rata Suhu (°C)")
    plt.title(f"Rata-rata Suhu Harian di {CITY}")
    plt.xlabel("Tanggal")
    plt.ylabel("Suhu (°C)")
    plt.xticks(rotation=45)
    plt.grid(True)
    plt.legend()
    plt.tight_layout()
    plt.savefig("weather_plot.png")
    plt.show()

if __name__ == "__main__":
    print(f"Mengambil data cuaca untuk kota {CITY}...")
    weather_data = fetch_weather_data()
    
    if weather_data:
        print("Memproses data cuaca...")
        daily_avg_temp = process_weather_data(weather_data)

        print("Membuat grafik suhu...")
        plot_weather_data(daily_avg_temp)

        print("Grafik berhasil disimpan sebagai 'weather_plot.png'.")
    else:
        print("Proses gagal. Periksa API key atau koneksi internet Anda.")
