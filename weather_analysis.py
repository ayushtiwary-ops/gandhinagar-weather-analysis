import statistics

# Last 10 days weather data for Gandhinagar (sample data)
temperature = [30, 31, 29, 32, 33, 34, 31, 30, 29, 28]
humidity = [60, 58, 65, 63, 59, 57, 62, 64, 61, 60]

# Average
avg_temp = sum(temperature) / len(temperature)
avg_humidity = sum(humidity) / len(humidity)

# Median
median_temp = statistics.median(temperature)
median_humidity = statistics.median(humidity)

print("Temperature Analysis")
print("Average:", avg_temp)
print("Median:", median_temp)

print("\nHumidity Analysis")
print("Average:", avg_humidity)
print("Median:", median_humidity)
