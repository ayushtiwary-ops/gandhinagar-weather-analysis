import statistics
temperature = [30, 31, 29, 32, 33, 34, 31, 30, 29, 28]
humidity = [60, 58, 65, 63, 59, 57, 62, 64, 61, 60]
aqi = [110, 105, 115, 120, 100, 98, 130, 125, 108, 112]

def analyze(data, label):
    average = sum(data) / len(data)
    median = statistics.median(data)

    print(f"\n{label} Analysis")
    print("Average:", average)
    print("Median:", median)

    return average, median

temp_avg, temp_median = analyze(temperature, "Temperature")
hum_avg, hum_median = analyze(humidity, "Humidity")
aqi_avg, aqi_median = analyze(aqi, "AQI")


with open("results.txt", "w") as file:
    file.write("Weather Analysis for Gandhinagar (Last 10 Days)\n\n")
    file.write(f"Temperature - Average: {temp_avg}, Median: {temp_median}\n")
    file.write(f"Humidity - Average: {hum_avg}, Median: {hum_median}\n")
    file.write(f"AQI - Average: {aqi_avg}, Median: {aqi_median}\n")
