import streamlit as st
import pandas as pd
import requests
import datetime
import plotly.express as px
from streamlit_autorefresh import st_autorefresh

# ------------------ CONFIG ------------------
st.set_page_config(page_title="Tiruppur Textile Revenue Pulse", layout="wide")

API_KEY = "28d3ab76827107d3e0ace23ab8c8bc0a"

# ------------------ AUTO REFRESH ------------------
speed = st.radio("Speed", ["Fast (5s)", "Medium (15s)", "Slow (30s)"], horizontal=True)
refresh_rate = 5 if "Fast" in speed else 15 if "Medium" in speed else 30
st_autorefresh(interval=refresh_rate * 1000, key="refresh")

# ------------------ CUSTOM CSS ------------------
st.markdown("""
<style>
[data-testid="stAppViewContainer"] {
    background-color: #0a0f1e;
    color: white;
}
.metric-box {
    background: #0d1f3c;
    padding: 15px;
    border-radius: 12px;
    text-align: center;
    border: 1px solid #1e3a5f;
}
.tag {
    padding: 4px 10px;
    border-radius: 8px;
    font-size: 12px;
    color: white;
}
.rain { background-color: #1d4ed8; }
.heat { background-color: #c2410c; }
.cloud { background-color: #4b5563; }
</style>
""", unsafe_allow_html=True)

# ------------------ WEATHER FUNCTION ------------------
@st.cache_data(ttl=600)
def get_weather(city):
    try:
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city},IN&appid={API_KEY}&units=metric"
        res = requests.get(url, timeout=5).json()
        weather = res["weather"][0]["main"]
        temp = res["main"]["temp"]
        return weather, temp
    except:
        return "Clear", 32

def weather_tag(weather, temp):
    if weather in ["Rain", "Thunderstorm", "Drizzle"]:
        return "🌧 Rain"
    elif temp > 35:
        return f"🔥 Heat ({temp}°C)"
    else:
        return f"☁ {weather}"

# ------------------ HEADER ------------------
st.title("🧵 Tiruppur Textile Revenue Pulse")
st.caption("Textile Sales Command Center — Tiruppur Region")
st.caption(f"Last updated: {datetime.datetime.now().strftime('%H:%M:%S')}")

# ------------------ LOAD DATA ------------------
df = pd.read_csv("sales_data.csv")

required_cols = {"Time", "Product", "City", "Price"}
if not required_cols.issubset(df.columns):
    st.error("CSV must contain: Time, Product, City, Price")
    st.stop()

# ------------------ KPI CALCULATIONS ------------------
total_revenue = df["Price"].sum()
total_orders = len(df)
avg_order = int(total_revenue / total_orders) if total_orders else 0
top_product = df["Product"].value_counts().idxmax()
top_city = df.groupby("City")["Price"].sum().idxmax()

# ------------------ KPI CARDS ------------------
c1, c2, c3, c4, c5 = st.columns(5)

c1.markdown(f"""
<div class="metric-box">
<h4>Total Revenue</h4>
<h2>₹{total_revenue:,}</h2>
</div>
""", unsafe_allow_html=True)

c2.markdown(f"""
<div class="metric-box">
<h4>Order Volume</h4>
<h2>{total_orders}</h2>
</div>
""", unsafe_allow_html=True)

c3.markdown(f"""
<div class="metric-box">
<h4>Avg Order Value</h4>
<h2>₹{avg_order:,}</h2>
</div>
""", unsafe_allow_html=True)

c4.markdown(f"""
<div class="metric-box">
<h4>Top Product</h4>
<h2>{top_product}</h2>
</div>
""", unsafe_allow_html=True)

c5.markdown(f"""
<div class="metric-box">
<h4>Top City</h4>
<h2>{top_city}</h2>
</div>
""", unsafe_allow_html=True)

# ------------------ ALERT SYSTEM ------------------
if total_orders > 10:
    st.success("🔥 High Textile Sales Activity Detected!")
elif total_orders < 5:
    st.error("🚨 Low Sales Alert — Check Inventory!")
else:
    st.info("⚖ Normal Sales Activity")

st.markdown("---")

# ------------------ WEATHER DATA ------------------
cities = df["City"].unique()
city_weather = {}
city_temp = {}
for city in cities:
    w, t = get_weather(city)
    city_weather[city] = w
    city_temp[city] = t

# ------------------ MIDDLE SECTION ------------------
left, right = st.columns([2, 1])

# -------- LEFT: CITY REVENUE --------
with left:
    st.subheader("📊 Revenue by City + Weather")
    city_data = df.groupby("City")["Price"].sum().sort_values(ascending=False)

    for city, revenue in city_data.items():
        weather = city_weather.get(city, "Clear")
        temp = city_temp.get(city, 32)
        tag = weather_tag(weather, temp)

        col1, col2 = st.columns([4, 1])
        col1.markdown(f"**{city}** — ₹{revenue:,}")
        col2.markdown(tag)
        st.progress(float(revenue / city_data.max()))

# -------- RIGHT: PRODUCT PERFORMANCE --------
with right:
    st.subheader("🧵 Product Performance")
    product_data = df["Product"].value_counts()

    for product, count in product_data.items():
        st.write(f"{product} ({count})")
        st.progress(float(count / product_data.max()))

st.markdown("---")

# ------------------ GRAPH ------------------
st.subheader("📈 Real-Time Revenue Trend")
st.caption("Live revenue fluctuation based on incoming textile sales")

fig = px.line(df, y="Price", markers=True,
              title="Tiruppur Textile Sales Trend",
              color_discrete_sequence=["#3b82f6"])
fig.update_layout(
    plot_bgcolor="#0a0f1e",
    paper_bgcolor="#0a0f1e",
    font=dict(color="white"),
    title_font=dict(color="white")
)
st.plotly_chart(fig, use_container_width=True)

# ------------------ BAR CHART ------------------
st.subheader("📊 Revenue by Product")
product_revenue = df.groupby("Product")["Price"].sum().reset_index()
fig2 = px.bar(product_revenue, x="Product", y="Price",
              color="Product",
              color_discrete_sequence=px.colors.qualitative.Bold)
fig2.update_layout(
    plot_bgcolor="#0a0f1e",
    paper_bgcolor="#0a0f1e",
    font=dict(color="white")
)
st.plotly_chart(fig2, use_container_width=True)

# ------------------ TABLE ------------------
st.subheader("🧾 Live Textile Sales Feed")

def impact_label(weather):
    if weather in ["Rain", "Thunderstorm"]:
        return "🌧 Wet Day — Sales May Drop"
    elif weather == "Clear":
        return "🔥 Hot Day — High Sales"
    else:
        return "✅ Normal"

df["Weather"] = df["City"].map(city_weather)
df["Impact"] = df["Weather"].apply(impact_label)

df_display = df.tail(15).sort_values(by="Price", ascending=False)
st.dataframe(df_display, use_container_width=True, height=300)