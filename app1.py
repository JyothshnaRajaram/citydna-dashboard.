import streamlit as st
import numpy as np
import matplotlib.pyplot as plt
import pandas as pd

st.set_page_config(page_title="CityDNA Monitor", layout="wide")

st.title("🌍 CityDNA – Global Environment Monitoring")

st.write("Enter any location or click on the map to analyze the environment.")

# LOCATION INPUT
location = st.text_input("Type Location (Example: Chennai, Tokyo, New York)")

# WORLD MAP (Clickable)
st.subheader("Click on Map to Select Location")

map_data = pd.DataFrame({
    'lat':[20],
    'lon':[0]
})

st.map(map_data)

if location:

    st.subheader(f"Environment Analysis for: {location}")

    noise = np.random.randint(40,90)
    traffic = np.random.randint(10,100)

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("Noise Level (dB)", noise)

    with col2:
        st.metric("Traffic Activity", traffic)

    with col3:
        if noise > 70:
            st.error("⚠ High Noise Event Detected")
        else:
            st.success("Normal Environment")

    st.subheader("Event Statistics")

    noise_events = np.random.randint(80,150)
    accidents = np.random.randint(10,40)
    clashes = np.random.randint(5,20)
    distress = np.random.randint(3,10)

    st.write("Noise Spikes:",noise_events)
    st.write("Traffic Accidents:",accidents)
    st.write("Clashes:",clashes)
    st.write("Distress Signals:",distress)

    st.subheader("Urban Activity Graph")

    time = np.arange(0,24)
    activity = np.sin(time/3)+np.random.rand(24)

    fig, ax = plt.subplots()

    ax.plot(time,activity,color="red",linewidth=3)
    ax.set_xlabel("Time (Hours)")
    ax.set_ylabel("Activity Level")
    ax.set_title("Urban Event Activity Pattern")

    st.pyplot(fig)

    st.subheader("Environment Analysis")

    st.write("• Activity increases during peak hours.")
    st.write("• Noise spikes occur in dense traffic areas.")
    st.write("• Event probability increases in crowded zones.")