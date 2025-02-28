# Virtunexa Internship - Week 1 Tasks  

Welcome to **Week 1** of the Virtunexa Internship! 🚀  
- **Web Scraper** 🕵️‍♂️  
- **GUI Calculator** 🧮
- **Console Calculator** 🔢  
- **Text-Based Adventure Game** 🎮  

## **📂 Project Overview**  

### **1️⃣ Web Scraper (Web_Scraper.ipynb)**
**Goal:** Extract relevant data (e.g., headlines, links, product details) from a website and store it in CSV/JSON format.  

🔹 **Features:**  
- Takes **user-input URL** for flexibility.  
- Uses **BeautifulSoup** & **requests** for web scraping.  
- Saves results in **CSV & JSON** for analysis.  

📌 **How to Run:**  
```bash
pip install requests beautifulsoup4
```
🔹 Run the file.
🔹 **Enter a website URL**, and the script will scrape data and save it!  

---

### **2️⃣ GUI Calculator (GUI_Calculator.py)**
**Goal:** Create an interactive calculator with a **Tkinter-based GUI** and a **calculation history feature**.  

🔹 **Features:**  
- Supports **basic operations** (+, -, ×, ÷).  
- Stores **calculation history** in an **SQLite database**.  
- Allows users to **view past calculations**.  

📌 **How to Run:**  
```bash
python GUI_Calculator.py
```
🔹 Enter an expression, hit **Calculate**, and check the **history**!  

---

### **3️⃣ Console Calculator (Console_Calculator.py)**
**Goal:** Develop a simple, text-based calculator for performing basic arithmetic operations.  

🔹 **Features:**  
- Supports **addition, subtraction, multiplication, and division**.  
- Handles **invalid inputs** (e.g., non-numeric values, division by zero).  
- Allows **continuous calculations** until the user decides to exit.  

📌 **How to Run:**  
```bash
python Console_Calculator.py
```
🔹 Follow the on-screen prompts to enter numbers and operators!  

---

### **4️⃣ Text-Based Adventure Game (Text_Adventure.ipynb)**
**Goal:** Develop an interactive **dungeon escape game** with **multiple choices & inventory management**.  

🔹 **Features:**  
- **Multiple endings** based on choices.  
- **Inventory management** (collect and use items).  
- **Story-driven adventure** with text-based interaction.  

📌 **How to Play:**  
🔹 Run the file. 
🔹 Make choices (1 or 2) and **try to escape the dungeon**!  

---

## **📌 Technologies Used**
- **Python** 🐍 – Core programming language.  
- **BeautifulSoup & Requests** 🌐 – Web scraping.  
- **Tkinter** 🖥️ – GUI for the calculator.  
- **SQLite** 🗄️ – Storing calculation history.  
- **CSV & JSON** 📄 – Data storage formats.  

---
# Virtunexa Internship - Week 2  Tasks    

Welcome to **Week 2** of the Virtunexa Internship! 🚀  
- **Automated Email Sender** 📧  

---
## **📂 Project Overview**  

### **1️⃣ Automated Email Sender (send_email.py)**
**Goal:** Write a Python script that sends automated emails with attachments using SMTP, personalized with user details from a CSV file.  

🔹 **Features:**  
   - Reads recipient details (name, email) from a CSV file.
   - Uses SMTP to send emails with attachments.
   - Supports personalized messages for each recipient.  

📌 **How to Run:**  
```bash
python send_email.py
```
---
## **📌 Technologies Used**
- **Python** 🐍 – Core programming language.  
- **SMPT & Pandas** 🌐 - To send emails. 
- **CSV & JSON** 📄 – Data storage formats.
---
# Virtunexa Internship - Week 3  Tasks    

Welcome to **Week 3** of the Virtunexa Internship! 🚀  
- **voice-activated virtual assistant** 📧  
---

## Project Overview
This is a simple **voice-activated virtual assistant** built with Python. It can:
- ✅ **Set reminders** ⏰
- ✅ **Answer simple questions** 🗣️
- ✅ **Provide weather updates** 🌦️ (using OpenWeather API)

## Features
- **Voice Command Recognition** 🎤 (Uses `speech_recognition`)
- **Text-to-Speech Output** 🗣️ (Uses `pyttsx3`)
- **Weather API Integration** 🌍 (Uses OpenWeather API)
- **Reminder System** ⏰ (Uses `time.sleep`)
- **Exit Command** 🏁 (Say "exit" to quit)
---
## Installation
### 1️⃣ Install Dependencies
Ensure you have Python installed, then run:
```bash
pip install requests pyttsx3 speechrecognition
```

### 2️⃣ Get an OpenWeather API Key
- Sign up at [OpenWeather](https://openweathermap.org/api)
- Get your API key and replace it in `API_KEY` inside the script.

### 3️⃣ Run the Script
```bash
python virtual_assistant.py
```
---
## How It Works
1️⃣ Run the script, and the assistant will greet you.  
2️⃣ Say **"weather"** → It will ask for the city and give the weather report.  
3️⃣ Say **"reminder"** → It will ask what to remind you about and in how many seconds.  
4️⃣ Say **"exit"** → To stop the assistant.  

## Example Usage
```
You: Weather
Assistant: Which city?
You: New York
Assistant: The weather in New York is clear with a temperature of 15°C.
```
---
## **📌 Technologies Used**
- **Python** 🐍 – Core programming language
- **SpeechRecognition** 🎙️ – Recognizing user voice commands
- **pyttsx3** 🗣️ – Converting text to speech
- **Requests** 🌍 – Fetching weather data from OpenWeather API
- **Time** ⏰ – Handling reminders

---
🔹 **Enjoy exploring the projects!** 🚀🔥

