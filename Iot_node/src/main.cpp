#include <Arduino.h>
#include "DHT.h"

// Define the pin and sensor type
#define DHTPIN 4       // GPIO 4 (D4) on the ESP32
#define DHTTYPE DHT22  // We are using the DHT22

// Initialize the sensor
DHT dht(DHTPIN, DHTTYPE);

void setup() {
  // Start the serial connection to your computer
  Serial.begin(115200);
  Serial.println("🌱 AgriResQ Sensor Test Starting...");
  
  // Start the DHT sensor
  dht.begin();
}

void loop() {
  // Wait 2 seconds between readings (DHT22 is a slow sensor)
  delay(2000);

  // Read humidity and temperature
  float h = dht.readHumidity();
  float t = dht.readTemperature();

  // Check if the sensor is failing to read
  if (isnan(h) || isnan(t)) {
    Serial.println("⚠️ ERROR: Failed to read from DHT sensor! Check your wiring.");
    return;
  }

  // Print the results to the terminal
  Serial.print("Humidity: ");
  Serial.print(h);
  Serial.print("%  |  Temperature: ");
  Serial.print(t);
  Serial.println("°C");
}