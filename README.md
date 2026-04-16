# 🧵 Tiruppur Textile Revenue Pulse

A real-time sales dashboard built using Streamlit that simulates live textile sales and integrates weather data to analyze its impact on business performance.


## 📌 Project Overview

This project was developed as part of a 3-day sprint to build a **live operational monitoring dashboard**.
It simulates real-time sales and displays insights in a **war-room style interface** for quick decision-making.


## 🚀 Features

* 🔄 Auto-refreshing dashboard (no manual reload)
* 💰 Total Revenue tracking
* 📦 Order Volume monitoring
* 📊 Average Order Value calculation
* 🧵 Product Performance analysis
* 🌍 Revenue breakdown by city
* 🌦️ Weather integration (Rain / Heat / Cloud)
* 📈 Real-time revenue trend (interactive chart)
* 📊 Revenue by product (bar chart)
* 📋 Live sales feed with weather impact
* 🚨 Alert system (High / Low / Normal sales)


## 🗂️ Project Structure

tiruppur-revenue-pulse/
│
├── app.py                # Main Streamlit dashboard
├── requirements.txt     # Required Python libraries
├── README.md            # Project documentation


## 🛠️ Tech Stack

* Python
* Streamlit
* Pandas
* Plotly
* Requests (Weather API)
* OpenWeatherMap API


## ⚙️ How to Run Locally

### Step 1: Install dependencies

pip install -r requirements.txt

### Step 2: Run the dashboard

python -m streamlit run app.py

### Step 3: Open in browser

http://localhost:8501


## 🌦️ Weather Integration

This dashboard uses the OpenWeatherMap API to fetch live weather data for each city.

| Weather Condition | Indicator | Impact             |
| ----------------- | --------- | ------------------ |
| Rain / Storm      | 🌧️       | Sales may decrease |
| High Temperature  | 🔥        | Increased sales    |
| Normal Weather    | ☁️        | Stable activity    |



## 📊 Dashboard Sections

1. KPI Cards (Revenue, Orders, Avg Value, Top Product, Top City)
2. Alert System
3. Revenue by City + Weather
4. Product Performance
5. Real-Time Revenue Trend
6. Revenue by Product
7. Live Sales Feed
   

## 📁 Data Fields

| Field   | Description             |
| ------- | ----------------------- |
| Time    | Timestamp of sale       |
| Product | Textile item sold       |
| Price   | Sale value              |
| City    | Location of sale        |
| Weather | Current weather         |
| Impact  | Weather impact on sales |


## 👩‍💻 Developed By

Lakshana

## 📅 Submission

Project: Live Revenue Pulse

## 📬 Notes

* This project simulates live data for demonstration purposes
* Designed to resemble a real-world business command center dashboard

