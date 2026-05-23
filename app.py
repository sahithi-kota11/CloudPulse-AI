import streamlit as st
import random
import pandas as pd
import plotly.express as px
import pydeck as pdk


from sklearn.ensemble import IsolationForest
from streamlit_autorefresh import st_autorefresh

st.set_page_config(
    page_title="CloudPulse AI",
    page_icon="⚡",
    layout="wide"
)

st_autorefresh(interval=5000, key="datarefresh")

st.markdown(
    """
    <style>
    .stApp {
        background-color: #0E1117;
        color: white;
    }
    </style>
    """,
    unsafe_allow_html=True
)

st.sidebar.title("⚙️ CloudPulse AI")

page = st.sidebar.radio(
    "Navigation",
    [
        "Dashboard",
        "Threat Analytics",
        "Incident Reports"
    ]
)

if page == "Dashboard":

    st.title("⚡ CloudPulse AI")

    st.subheader("AI-Powered Incident Intelligence Platform")

    st.write("Real-time monitoring dashboard for intelligent IT operations.")

    st.divider()

    # Fake live metrics
    cpu_usage = random.randint(40, 95)
    memory_usage = random.randint(35, 90)
    api_latency = random.randint(100, 700)
    failed_logins = random.randint(0, 30)

    # Metric cards
    col1, col2, col3, col4 = st.columns(4)

    col1.metric("CPU Usage", f"{cpu_usage}%")
    col2.metric("Memory Usage", f"{memory_usage}%")
    col3.metric("API Latency", f"{api_latency} ms")
    col4.metric("Failed Logins", failed_logins)



    st.divider()

    def predict_severity(cpu, memory, latency, failed_logins):
        risk_score = 0

        if cpu > 85:
            risk_score += 30
        elif cpu > 70:
            risk_score += 15

        if memory > 80:
            risk_score += 25
        elif memory > 65:
            risk_score += 10

        if latency > 500:
            risk_score += 30
        elif latency > 350:
            risk_score += 15

        if failed_logins > 20:
            risk_score += 15
        elif failed_logins > 10:
            risk_score += 5

        if risk_score >= 60:
            return "Critical", risk_score
        elif risk_score >= 30:
            return "Medium", risk_score
        else:
            return "Low", risk_score


    severity, risk_score = predict_severity(
        cpu_usage,
        memory_usage,
        api_latency,
        failed_logins
    )
    # Incident Alerts
    st.header("🚨 Incident Alerts")

    st.divider()

st.header("🖥️ Real-Time System Logs")

logs = pd.DataFrame({
    "Time": pd.date_range(start="2026-05-22 10:00", periods=8, freq="min"),
    "Service": [
        "Auth Service", "API Gateway", "Database", "Web Server",
        "Auth Service", "Payment API", "Cloud Storage", "Firewall"
    ],
    "Log Message": [
        "User login successful",
        "High API response time detected",
        "Database connection stable",
        "CPU usage spike observed",
        "Multiple failed login attempts",
        "Request timeout warning",
        "Backup completed successfully",
        "Suspicious IP blocked"
    ],
    "Severity": [
        "Low", "Medium", "Low", "High",
        "High", "Medium", "Low", "Critical"
    ]
})

st.dataframe(logs, use_container_width=True)

severity_score = random.randint(1, 100)

if severity_score > 80:
    severity = "Critical"
elif severity_score > 60:
    severity = "High"
elif severity_score > 40:
    severity = "Medium"
else:
    severity = "Low"

st.metric("Threat Severity Score", f"{severity_score}/100", severity)
if cpu_usage > 85:
st.error("Critical CPU spike detected!")

if memory_usage > 80:
st.warning("High memory usage detected!")

if api_latency > 500:
st.error("API latency is unusually high!")

if failed_logins > 20:
st.warning("Multiple failed login attempts detected!")

    st.divider()

    # Generate fake chart data
    data = {
        "Time": list(range(1, 11)),
        "CPU": [random.randint(40, 95) for _ in range(10)],
        "Memory": [random.randint(35, 90) for _ in range(10)],
        "Latency": [random.randint(100, 700) for _ in range(10)]
    }

    df = pd.DataFrame(data)

    # AI anomaly detection
    model = IsolationForest(contamination=0.2)

    features = df[["CPU", "Memory", "Latency"]]

    model.fit(features)

    df["Anomaly"] = model.predict(features)

    df["Anomaly"] = df["Anomaly"].map({
        1: "Normal",
        -1: "Anomaly"
    })
    # Charts section
    st.header("📊 System Performance Trends")

    fig_cpu = px.line(df, x="Time", y="CPU", title="CPU Usage Trend")
    st.plotly_chart(fig_cpu, use_container_width=True)

    fig_memory = px.line(df, x="Time", y="Memory", title="Memory Usage Trend")
    st.plotly_chart(fig_memory, use_container_width=True)

    fig_latency = px.line(df, x="Time", y="Latency", title="API Latency Trend")
    st.plotly_chart(fig_latency, use_container_width=True)
    st.divider()

    st.header("🤖 AI Anomaly Detection")

    st.dataframe(
        df[["CPU", "Memory", "Latency", "Anomaly"]],
        use_container_width=True
    )

    st.divider()

    # AI Insights
    st.header("🧠 AI Insights")

    st.info(
        "Possible root cause: Increased server load may be impacting API response times. "
        "Recommended action: Investigate background services and review authentication logs."
    )
    st.divider()

    st.header("📋 Incident Log Table")

    incident_data = {
        "Incident": [
            "CPU Spike",
            "Memory Overflow",
            "API Delay",
            "Failed Login Attempts"
        ],
        "Severity": [
            "Critical",
            "Medium",
            "Critical",
            "Warning"
        ],
        "Status": [
            "Investigating",
            "Monitoring",
            "Action Required",
            "Resolved"
        ]
    }

    incident_df = pd.DataFrame(incident_data)
    st.dataframe(incident_df, use_container_width=True)
    st.divider()

    st.header("🌍 Live Attack Source Map")

    attack_data = pd.DataFrame({
        "country": ["United States", "India", "Germany", "United Kingdom", "Singapore"],
        "lat": [37.0902, 20.5937, 51.1657, 55.3781, 1.3521],
        "lon": [-95.7129, 78.9629, 10.4515, -3.4360, 103.8198],
        "attack_count": [
            random.randint(10, 90),
            random.randint(10, 90),
            random.randint(10, 90),
            random.randint(10, 90),
            random.randint(10, 90)
        ]
    })

    st.pydeck_chart(
        pdk.Deck(
            map_style=None,
            initial_view_state=pdk.ViewState(
                latitude=20,
                longitude=0,
                zoom=1,
                pitch=30,
            ),
            layers=[
                pdk.Layer(
                    "ScatterplotLayer",
                    data=attack_data,
                    get_position="[lon, lat]",
                    get_radius="attack_count * 50000",
                    get_fill_color="[255, 80, 80, 160]",
                    pickable=True,
                )
            ],
            tooltip={
                "html": "<b>Country:</b> {country}<br/><b>Attacks:</b> {attack_count}",
                "style": {"color": "white"}
            }
        )
    )

    st.dataframe(attack_data, use_container_width=True)

    st.divider()

    st.header("📄 Download Incident Report")

    report = f"""
    CloudPulse AI - Incident Report

    CPU Usage: {cpu_usage}%
    Memory Usage: {memory_usage}%
    API Latency: {api_latency} ms
    Failed Logins: {failed_logins}
    Threat Severity Score: {severity_score}/100
    Threat Level: {severity}

    AI Summary:
    Possible root cause is increased server load, high latency, or suspicious login activity.
    Recommended action is to review server performance, background jobs, and authentication logs.
    """

    st.download_button(
        label="Download Report",
        data=report,
        file_name="cloudpulse_incident_report.txt",
        mime="text/plain"
    )

    st.divider()

    st.header("🏢 Business Impact Summary")

    st.success(
        "CloudPulse AI helps IT teams detect incidents early, reduce downtime, "
        "prioritize high-risk threats, and generate quick incident reports for decision-making."
    )

    if page == "Threat Analytics":

        st.title("📊 Threat Analytics")

        st.subheader("AI Threat Analysis Dashboard")

        st.metric("Detected Threats", random.randint(15, 60))

        st.metric("Critical Threats", random.randint(1, 10))

        threat_data = pd.DataFrame({
            "Threat Type": ["DDoS", "Brute Force", "Phishing", "Malware"],
            "Count": [
                random.randint(5, 20),
                random.randint(2, 15),
                random.randint(1, 10),
                random.randint(3, 18)
            ]
        })

        st.bar_chart(threat_data.set_index("Threat Type"))

if page == "Incident Reports":

    st.title("📄 Incident Reports")

    st.subheader("Generated Security Incident Logs")

    report_df = pd.DataFrame({
        "Incident ID": [101, 102, 103, 104],
        "Severity": ["Critical", "Medium", "High", "Low"],
        "Status": ["Investigating", "Resolved", "Monitoring", "Closed"]
    })
        


    st.dataframe(report_df, use_container_width=True)

    if page == "Incident Reports":

        st.title("📄 Incident Reports")

        st.subheader("Generated Security Incident Logs")

        report_df = pd.DataFrame({
            "Incident ID": [101, 102, 103, 104],
            "Severity": ["Critical", "Medium", "High", "Low"],
            "Status": ["Investigating", "Resolved", "Monitoring", "Closed"]
        })
        


    st.dataframe(report_df, use_container_width=True)

    st.success("AI-generated reports updated successfully.")

    

    st.success("AI-generated reports updated successfully.")

    