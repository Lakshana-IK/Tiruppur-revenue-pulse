# 🧵 Tiruppur Textile Revenue Pulse

A real-time **Sales Command Center Dashboard** built using Streamlit to simulate live textile sales and analyze the impact of weather conditions on business performance.

---

## 📌 Project Overview

This project was developed as part of a 3-day sprint to build a **live operational monitoring system**.
It replicates a **War Room UI**, enabling real-time tracking of sales, identifying trends, and supporting quick decision-making.

---

## 🎯 Objectives

* Simulate real-time sales data
* Build a live dashboard with auto-refresh
* Track key business KPIs
* Integrate weather data to analyze external impact
* Design a War Room-style command center UI

---

## 🚀 Features

* 🔄 Real-time auto-refresh dashboard
* 💰 Total Revenue tracking
* 📦 Order Volume monitoring
* 📊 Average Order Value calculation
* 🧵 Product Performance insights
* 🌍 Revenue breakdown by city
* 🌦️ Weather integration (Rain / Heat / Cloud)
* 📈 Real-time revenue trend (interactive chart)
* 📊 Revenue by product (bar chart)
* 📋 Live sales feed with weather impact
* 🚨 Alert system (High / Low / Normal sales activity)
* 🟢 System Status indicator (LIVE)

---

## 🔧 Technical Summary

This project is built using Streamlit for the frontend and Python for backend logic.
Sales data is dynamically generated within the application to simulate real-time updates.
Pandas is used for data processing, Plotly for visualization, and OpenWeatherMap API is used to fetch live weather conditions.

---

## ▶️ Dashboard Walkthrough

* KPI cards display total revenue, order volume, average order value, top product, and top city
* Revenue by city shows geographic performance along with weather conditions
* Product performance highlights best-selling textile items
* Real-time charts visualize revenue trends and product-wise distribution
* Live sales feed displays recent transactions with weather-based impact

---

## 🗂️ Project Structure

tiruppur-revenue-pulse/
│
├── app.py                # Main Streamlit dashboard
├── requirements.txt     # Python dependencies
├── README.md            # Project documentation

---

## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Plotly
* Requests
* OpenWeatherMap API

---

## ⚙️ How to Run Locally

### Step 1: Install dependencies

pip install -r requirements.txt

### Step 2: Run the dashboard

python -m streamlit run app.py

### Step 3: Open in browser

http://localhost:8501

---

## 🌐 Live Demo

🔗 https://tiruppur-revenue-pulse-kh2zhzfj5l2cfels9vjhg9.streamlit.app/

---

## 🌦️ Weather Integration

| Condition        | Indicator | Impact             |
| ---------------- | --------- | ------------------ |
| Rain / Storm     | 🌧️       | Sales may decrease |
| High Temperature | 🔥        | Increased sales    |
| Normal Weather   | ☁️        | Stable activity    |

---

## 📊 Key Insights

* Weather conditions influence sales patterns
* Certain products perform better in specific conditions
* City-level analysis helps identify high-performing regions
* Real-time monitoring enables faster business decisions

---

## 👩‍💻 Developed By

**Lakshana**

---

## 📅 Submission Details

Project: Live Revenue Pulse
---

## 📬 Notes

* This project simulates real-time data for demonstration purposes
* Designed to mimic a real-world business command center dashboard
* Built with a focus on clarity, usability, and decision-making
