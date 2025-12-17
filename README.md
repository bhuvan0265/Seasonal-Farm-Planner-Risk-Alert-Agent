# 🌾 Seasonal Farm Planner & Risk Alert Agent

An **Agentic AI–powered web application** that helps small and marginal farmers plan an entire agricultural season, manage **multi-crop farms**, optimize budgets, and receive **weather risk alerts**. The system dynamically updates farm plans based on changing conditions, acting as a **virtual seasonal farm advisor**.

Built as part of an **Agentic AI Hackathon** with a focus on ethical, explainable, and adaptable AI for real-world agriculture.

---

## 🎯 Problem Statement

Small farmers often struggle to:

* Plan crops across an entire season
* Coordinate tasks like sowing, irrigation, and harvesting
* Anticipate weather risks (rain, heat, frost)
* Manage budgets and farm inputs efficiently

Lack of integrated planning tools leads to crop losses, wasted resources, and reduced income.

---

## 💡 Solution Overview

The **Seasonal Farm Planner & Risk Alert Agent** uses an **agentic AI workflow** to:

* Generate **month-by-month crop plans** using public crop calendars
* Suggest **intercropping combinations**
* Create detailed **task schedules** (sowing, irrigation, weeding, fertilization, harvest)
* Monitor weather forecasts (API or mock data)
* Trigger **risk alerts** and **dynamically update plans** when conditions change

The system shows **what changed, why it changed, and how the plan adapts**, making the AI transparent and explainable.

---

## 🤖 Agentic AI Workflow

1. **Planning Agent** – Builds a seasonal plan using crop calendars
2. **Task Generator** – Creates date-wise farm activities
3. **Risk Monitor** – Analyzes weather data for risks
4. **Plan Update Agent** – Adjusts schedules based on detected risks
5. **Memory & Logs** – Stores farm context and maintains plan update history

---

## 🧾 Key Features

* 🌱 Multi-crop seasonal planning
* 📅 Month-by-month task calendar with dates
* 🚨 Weather risk alerts (heat, frost, heavy rain)
* 🔁 Automatic plan updates with change logs
* 💰 Budget estimation and input checklist
* 🌐 Mobile-friendly, responsive web interface
* 📄 Structured outputs (JSON/CSV ready)

---

## 📥 Inputs

* Location (district-level)
* Season (Kharif / Rabi)
* Crop selection (multi-crop)
* Field list (Field A, Field B, etc.)
* Budget constraints
* Weather forecast (API or mock data)

---

## 📤 Outputs

* Planner view (calendar and task tables)
* Weather risk alerts with explanations
* Updated plan history logs
* Budget and resource checklist

---

## ⚠️ Safety, Ethics & Privacy

* Advisory-only system based on **public agricultural guidelines**
* No medical or chemical prescriptions beyond standard references
* Uses **synthetic/demo data only**
* No personal farmer data collected or shared
* Encourages consultation with local agricultural experts for high-risk scenarios

---

## 📚 Data Sources

* FAO Crop Calendars
* ICAR Agricultural Guidelines
* IMD / OpenWeather (API or mock data)
* Local agricultural extension references

---

## 🛠️ Tech Stack

* **Frontend**: HTML, CSS, JavaScript (Bootstrap)
* **Backend**: Python (Flask)
* **AI**: Prompt-based Large Language Model integration
* **Data**: JSON files and mock APIs

---

## 🚀 Getting Started

### Prerequisites

* Python 3.9+
* Git

### Installation

```bash
git clone https://github.com/your-username/seasonal-farm-planner.git
cd seasonal-farm-planner
pip install -r requirements.txt
python app.py
```

Open your browser and go to:

```
http://127.0.0.1:5000
```

---

## 🏆 Hackathon Context

This project was developed for an **Agentic AI Hackathon**, emphasizing:

* Explainable AI decision-making
* Ethical and safe AI usage
* Practical agricultural impact
* Adaptability to real-world conditions

---

## 🔮 Future Scope

* Mobile application
* Offline / low-bandwidth mode
* SMS or WhatsApp alert integration
* IoT sensor integration (soil moisture, temperature)
* Expanded multilingual support (Tamil and other regional languages)

---

## 📜 Disclaimer

This application provides advisory guidance based on publicly available agricultural information. It is **not a replacement for professional agricultural consultation**.

---

## 👨‍💻 Team

Developed by **[Your Name / Team Name]** as part of a hackathon project.

---

⭐ If you find this project useful, please consider starring the repository!
