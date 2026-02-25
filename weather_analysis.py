import statistics

# Last 10 days weather data for Gandhinagar (sample data)
temperature = [30, 31, 29, 32, 33, 34, 31, 30, 29, 28]
humidity = [60, 58, 65, 63, 59, 57, 62, 64, 61, 60]
aqi = [110, 105, 115, 120, 100, 98, 130, 125, 108, 112]

# Function to analyze data
def analyze(data, label):
    avg = sum(data) / len(data)
    median = statistics.median(data)
    print(f"\n{label} Analysis")
    print("Average:", avg)
    print("Median:", median)
    return avg, median

# Perform analysis
temp_avg, temp_median = analyze(temperature, "Temperature")
hum_avg, hum_median = analyze(humidity, "Humidity")
aqi_avg, aqi_median = analyze(aqi, "AQI")

# Store results in file
with open("results.txt", "w") as f:
    f.write("Weather Analysis for Gandhinagar (Last 10 Days)\n\n")
    f.write(f"Temperature - Avg: {temp_avg}, Median: {temp_median}\n")
    f.write(f"Humidity - Avg: {hum_avg}, Median: {hum_median}\n")
    f.write(f"AQI - Avg: {aqi_avg}, Median: {aqi_median}\n")
