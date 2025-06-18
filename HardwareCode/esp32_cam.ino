  #include <Arduino.h>
  #include <WiFi.h>
  #include <HTTPClient.h>
  #include <ESP32QRCodeReader.h>
  #include <ArduinoJson.h>
  // WiFi credentials
  const char* ssid = "Hidden Network";
  const char* password = "hcmute@lab";
  String NAME_QR_CODE = "";
  String before_NAME_QR_CODE = "_";
  int current_materialId = -1;
  // Server endpoint
  const char* serverUrl_name = "http://iea.ddns.net:8383/api/get-name/?id=";
  const char* serverURL = "http://iea.ddns.net:8383/api/material-transactions/";
  // Define UART pins for STM32 communication
  #define TXD2 1
  #define RXD2 3

  HardwareSerial stm32Serial(2);  // UART2: giao tiếp với STM32


  #define BUTTON1_PIN 14   // Nút 1: GPIO2
  #define BUTTON2_PIN 2  // Nút 2: GPIO16

  volatile bool button1Pressed = false;
  volatile bool button2Pressed = false;


  void IRAM_ATTR handleButton1Interrupt() {
    button1Pressed = true;
  }

  void IRAM_ATTR handleButton2Interrupt() {
    button2Pressed = true;
  }


  // QR reader object (AI Thinker model)
  ESP32QRCodeReader reader(CAMERA_MODEL_AI_THINKER);

  // Connect to WiFi
  void connectToWiFi() {
    Serial.printf("📡 Connecting to %s", ssid);
    WiFi.begin(ssid, password);
    while (WiFi.status() != WL_CONNECTED) {
      delay(500);
      Serial.print(".");
    }
    Serial.println("\n✅ WiFi connected");
    Serial.print("📍 IP Address: ");
    Serial.println(WiFi.localIP());
  }

  // Gửi GET request để lấy tên sản phẩm từ server
  String getProductName(int materialId) {
    HTTPClient http;
    String fullUrl = String(serverUrl_name) + String(materialId);
    http.begin(fullUrl);

    int httpCode = http.GET();
    if (httpCode == 200) {
      String payload = http.getString();
      http.end();

      // Parse JSON: {"name":"oc vit"} → trích chỉ phần "oc vit"
      int nameStart = payload.indexOf(":\"") + 2;
      int nameEnd = payload.indexOf("\"", nameStart);
      if (nameStart > 1 && nameEnd > nameStart) {
        return payload.substring(nameStart, nameEnd);  // Trả về chỉ tên sản phẩm
      } else {
        return "";  // Không parse được
      }
    } else {
      Serial.printf("❌ Failed to GET. HTTP code: %d\n", httpCode);
      http.end();
      return "";
    }
  }


  // Task đọc QR
  void onQrCodeTask(void* pvParameters) {
    struct QRCodeData qrCodeData;

    while (true) {
      if (reader.receiveQrCode(&qrCodeData, 500)) {
        Serial.println("🔍 Scanned new QRCode");

        if (qrCodeData.valid) {
          String payload = String((const char*)qrCodeData.payload);
          Serial.print("✅ Valid payload: ");
          Serial.println(payload);

          int materialId = payload.toInt();
          String productName = getProductName(materialId);
          current_materialId = materialId;
          if (productName.length() > 0) {
            Serial.print("📦 Product name: ");
            Serial.println(productName);
            // Gửi tên sản phẩm qua UART đến STM32 
            NAME_QR_CODE = productName;
            if (NAME_QR_CODE != before_NAME_QR_CODE){
              before_NAME_QR_CODE = NAME_QR_CODE;
              NAME_QR_CODE = "!" + productName; 
              while (NAME_QR_CODE.length() < 80) NAME_QR_CODE += " "; 
              stm32Serial.print(NAME_QR_CODE);
              delay(200);
            }else {
              Serial.print("QR trung lap!!");
          }

          }
        } else {
          Serial.print("⚠️ Invalid payload: ");
          Serial.println((const char*)qrCodeData.payload);
        }
      }
      vTaskDelay(100 / portTICK_PERIOD_MS);
    }
  }

  // Setup
  void setup() {
    Serial.begin(115200);                               // Debug Serial
    stm32Serial.begin(115200, SERIAL_8N1, RXD2, TXD2);  // UART2: TX = 14, RX = 13

    delay(1000);

    connectToWiFi();

    pinMode(BUTTON1_PIN, INPUT_PULLUP);
    pinMode(BUTTON2_PIN, INPUT_PULLUP);

    attachInterrupt(digitalPinToInterrupt(BUTTON1_PIN), handleButton1Interrupt, FALLING);
    attachInterrupt(digitalPinToInterrupt(BUTTON2_PIN), handleButton2Interrupt, FALLING);

    reader.setup();
    reader.beginOnCore(1);

    Serial.println("🚀 QR Code Reader Initialized");

    xTaskCreate(onQrCodeTask, "onQrCode", 4 * 1024, NULL, 4, NULL);
  }

  String lastWeight = ""; 
  String sendWeight = "";

  // Loop chính
  void loop() {
    
    
    //Nhan khoi luong tu can
    if (stm32Serial.available()) {
      String weight = stm32Serial.readStringUntil('\n');  // Đọc đến khi xuống dòng

      weight.trim();  // Xoá khoảng trắng hoặc newline dư

      if (weight.length() > 0 && weight != lastWeight) {
        Serial.print("⚖️  Khối lượng nhận được từ STM32: ");
        Serial.println(weight);
        lastWeight = weight;  // Cập nhật giá trị mới
        sendWeight = weight;
      }
    }

    if (button1Pressed) {
      button1Pressed = false;
      Serial.println("🔘 Nút 1 (GPIO2) được nhấn: Gửi EXPORT");
      sendExport();  // export
    }

      if (button2Pressed) {
      button2Pressed = false;
      Serial.println("🔘 Nút 2 (GPIO16) được nhấn: Gửi IMPORT");
      sendImport();  // import
    }

    delay(1000);
  }


  void sendImport() {
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(serverURL);
      http.addHeader("Content-Type", "application/json");

      // Gửi thông tin giả lập
      StaticJsonDocument<200> jsonDoc;
      jsonDoc["materialId"] = current_materialId;
       //current_materialId
      jsonDoc["unitId"] = 3;
      jsonDoc["quantity"] = sendWeight; //sendWeight
      jsonDoc["transaction_type"] = "import";

      String jsonPayload;
      serializeJson(jsonDoc, jsonPayload);

      int httpCode = http.POST(jsonPayload);
      Serial.print("📨 HTTP Response code: ");
      Serial.println(httpCode);

      if (httpCode > 0) {
        String response = http.getString();
        Serial.println("📥 Server Response:");
        Serial.println(response);

        // Parse JSON để lấy từng dòng
        StaticJsonDocument<256> doc;
        DeserializationError error = deserializeJson(doc, response);
        if (!error) {
          String m1 = doc["message"] | "";

          String fullMessage = m1;

          // Gửi 1 lần qua UART
          stm32Serial.print(fullMessage);
        } else {
            Serial.println("⚠️ Không parse được JSON.");
          }
      }


      http.end();
    } else {
      Serial.println("🚫 WiFi not connected");
    }
  }


  void sendExport() {
    if (WiFi.status() == WL_CONNECTED) {
      HTTPClient http;
      http.begin(serverURL);
      http.addHeader("Content-Type", "application/json");

      // Gửi thông tin giả lập
      StaticJsonDocument<200> jsonDoc;
      jsonDoc["materialId"] = current_materialId; //current_materialId
      jsonDoc["unitId"] = 3;
      jsonDoc["quantity"] = sendWeight; //sendWeight
      jsonDoc["transaction_type"] = "export";

      String jsonPayload;
      serializeJson(jsonDoc, jsonPayload);

      int httpCode = http.POST(jsonPayload);
      Serial.print("📨 HTTP Response code: ");
      Serial.println(httpCode);

      if (httpCode > 0) {
        String response = http.getString();
        Serial.println("📥 Server Response:");
        Serial.println(response);

        // Parse JSON để lấy từng dòng
        StaticJsonDocument<256> doc;
        DeserializationError error = deserializeJson(doc, response);
        if (!error) {
          String m1 = doc["message"] | "";

          String fullMessage = m1;

          // Gửi 1 lần qua UART
          stm32Serial.print(fullMessage);
        } else {
            Serial.println("⚠️ Không parse được JSON.");
          }
      }


      http.end();
    } else {
      Serial.println("🚫 WiFi not connected");
    }
  }
