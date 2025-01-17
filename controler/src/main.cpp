#include <WiFi.h>
#include <AsyncMqttClient.h>
#include <ArduinoJson.h>


// WiFi Credentials
const char* ssid = "The Bronk";
const char* password = "abidanumi";

// MQTT Broker
const char* mqttServer = "broker.emqx.io";
const uint16_t mqttPort = 1883;

// MQTT Client
AsyncMqttClient mqttClient;
TimerHandle_t mqttReconnectTimer;
TimerHandle_t wifiReconnectTimer;
TimerHandle_t myTimer;



// Menghubungkan WiFi
void connectToWiFi() {
  Serial.println("Connecting to WiFi...");
  WiFi.begin(ssid, password);
}

// Menghubungkan MQTT
void connectToMqtt() {
  Serial.println("Connecting to MQTT...");
  mqttClient.connect();
}

// Saat MQTT berhasil terhubung
void onMqttConnect(bool sessionPresent) {
  Serial.println("Connected to MQTT.");
  Serial.print("Session present: ");
  Serial.println(sessionPresent);

  // Subscribe to topic
  mqttClient.subscribe("sensor/tanaman2", 1);

  // Publish initial message
  mqttClient.publish("sensor/tanaman", 0, false, "ESP32 Connected!");
}

// Saat MQTT terputus 
void onMqttDisconnect(AsyncMqttClientDisconnectReason reason) {
  Serial.println("Disconnected from MQTT.");

  if (WiFi.isConnected()) {
    xTimerStart(mqttReconnectTimer, 0);
  }
}
// Saat berhasil subscribe
void onMqttSubscribe(uint16_t packetId, uint8_t qos) {
  Serial.print("Subscribed to topic. : ");
  Serial.println(packetId);
  
}

// Saat pesan masuk
void onMqttMessage(char* topic, char* payload, AsyncMqttClientMessageProperties properties, size_t len, size_t index, size_t total) {
  unsigned long currentTime;
  unsigned long previousTime;
  const long delayTime = 3000;
  JsonDocument doc;

  Serial.print("Received message on topic: ");
  Serial.println(topic);

  // Convert payload ke string
  String message = String(payload).substring(0, len);
  Serial.print("Message: ");
  Serial.println(message);


  // message == siram
  deserializeJson(doc, message);
  if (doc["message"] == "Siram" || doc["message"] == "Isi Air"){
    currentTime = millis();
    previousTime= millis(); 
    while(true){
      digitalWrite(18, HIGH);
      
      if(currentTime-previousTime >= delayTime){
        digitalWrite(18, LOW);
        previousTime = currentTime;
        break;
      }
      currentTime = millis();
      
    }
  }

}
// Mengirim pesan
void sendSensorData(TimerHandle_t xTimer){
  // Nilai Sensor
  int sensorKelembapan  = random(40, 100);    // Random humidity between 40-60%
  int suhuTanah         = random(40, 100);    // Random humidity between 40-60%
  int Ph                = random(1, 20);      // Menghasilkan angka acak dari 1 hingga 100
  int nutrisiTanah      = random(40, 100);    // Random humidity between 40-60%

  // JSON objects
  JsonDocument doc; 

  doc["kelembapanTanah"]  = sensorKelembapan;
  doc["suhuTanah"]        = suhuTanah;
  doc["Ph"]               = Ph;
  doc["nutrisiTanah"]     = nutrisiTanah;
  

  // Ubah JSON ke String
  char jsonBuffer[512];
  serializeJson(doc, jsonBuffer);
  Serial.println("Mengirim data....");
  mqttClient.publish("sensor/tanaman", 1, true, jsonBuffer);  

}

  


void setup() {
  // Aktifkan serial dan pin ESP32
  Serial.begin(115200);
  pinMode(18, OUTPUT);

  // Set up WiFi connection
  WiFi.onEvent([](WiFiEvent_t event, arduino_event_info_t info) {
    if (event == ARDUINO_EVENT_WIFI_STA_GOT_IP) {
      Serial.println("WiFi Connected!");
      connectToMqtt();
    } else if (event == ARDUINO_EVENT_WIFI_STA_DISCONNECTED) {
      Serial.println("WiFi Disconnected.");
      xTimerStart(wifiReconnectTimer, 0);
    }
  });

  connectToWiFi();

  // Set up MQTT client
  mqttClient.onConnect(onMqttConnect);
  mqttClient.onDisconnect(onMqttDisconnect);
  mqttClient.onMessage(onMqttMessage);
  mqttClient.onSubscribe(onMqttSubscribe);
  mqttClient.setServer(mqttServer, mqttPort);
  

  // Initialize timers
  mqttReconnectTimer = xTimerCreate("mqttTimer", pdMS_TO_TICKS(2000), pdFALSE, (void*)0, reinterpret_cast<TimerCallbackFunction_t>(connectToMqtt));

  wifiReconnectTimer = xTimerCreate("wifiTimer", pdMS_TO_TICKS(2000), pdFALSE, (void*)0, reinterpret_cast<TimerCallbackFunction_t>(connectToWiFi));
  
  myTimer = xTimerCreate("MyTimer", pdMS_TO_TICKS(1000), pdTRUE, (void*)0, sendSensorData);
  if (myTimer != NULL){
    xTimerStart(myTimer, 0);
  }

}

void loop() {
  // Tidak perlu kode di loop karena semuanya asynchronous
}
