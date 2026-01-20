"""
M.Tech Course Project: Social Media Privacy Dashboard
Minimal working version for Streamlit Cloud
"""

import streamlit as st
import pandas as pd
import numpy as np
import json
import random
from datetime import datetime
import streamlit.components.v1 as components

# Page config - MUST BE FIRST
st.set_page_config(
    page_title="Social Media Privacy Dashboard",
    page_icon="📊",
    layout="wide"
)

# Simple header
st.title("📊 Social Media Privacy & Security Dashboard")
st.markdown("**M.Tech Course Project | Ethical Issues in IT | Module 5: Highcharts**")

with st.expander("Course Connection"):
    st.write("""
    **Modules Covered:**
    - Module 3: Privacy in Online Social Networks
    - Module 4: Phishing & Network Analysis
    - Module 5: Case Studies & Highcharts Visualization
    """)

# Sidebar
with st.sidebar:
    st.title("Controls")
    chart_type = st.selectbox(
        "Select Chart Type:",
        ["Network Graph", "Heatmap", "Bubble Chart", "Timeline"]
    )
    st.divider()
    st.caption(f"Updated: {datetime.now().strftime('%H:%M:%S')}")

# Network Graph
if chart_type == "Network Graph":
    st.subheader("🔗 Social Network Analysis")
    
    # Generate simple network data
    nodes = []
    for i in range(10):
        nodes.append({
            'id': f'user_{i}',
            'name': f'User_{1000+i}',
            'community': random.choice(['A', 'B', 'C'])
        })
    
    links = []
    for _ in range(15):
        links.append([
            f'user_{random.randint(0, 9)}',
            f'user_{random.randint(0, 9)}'
        ])
    
    # Highcharts network graph
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://code.highcharts.com/highcharts.js"></script>
        <script src="https://code.highcharts.com/modules/networkgraph.js"></script>
    </head>
    <body>
        <div id="container" style="width:100%; height:500px;"></div>
        <script>
            Highcharts.chart('container', {{
                chart: {{ type: 'networkgraph' }},
                title: {{ text: 'Social Network Connections' }},
                series: [{{
                    data: {json.dumps(links)},
                    nodes: {json.dumps(nodes)}
                }}]
            }});
        </script>
    </body>
    </html>
    '''
    
    components.html(html, height=550)
    st.metric("Nodes", len(nodes))
    st.metric("Connections", len(links))

# Heatmap
elif chart_type == "Heatmap":
    st.subheader("📍 Location Privacy Heatmap")
    
    days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
    hours = ['8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00']
    
    data = []
    for i, day in enumerate(days):
        for j, hour in enumerate(hours):
            risk = random.randint(20, 90)
            data.append([i, j, risk])
    
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://code.highcharts.com/highcharts.js"></script>
        <script src="https://code.highcharts.com/modules/heatmap.js"></script>
    </head>
    <body>
        <div id="heatmap" style="width:100%; height:450px;"></div>
        <script>
            Highcharts.chart('heatmap', {{
                chart: {{ type: 'heatmap' }},
                title: {{ text: 'Privacy Risk Heatmap' }},
                xAxis: {{ categories: {json.dumps(days)} }},
                yAxis: {{ categories: {json.dumps(hours)}, reversed: true }},
                colorAxis: {{ min: 0, max: 100 }},
                series: [{{
                    data: {json.dumps(data)}
                }}]
            }});
        </script>
    </body>
    </html>
    '''
    
    components.html(html, height=500)

# Bubble Chart
elif chart_type == "Bubble Chart":
    st.subheader("🫧 Platform Comparison")
    
    data = [
        {'x': 2910, 'y': 45, 'z': 85, 'name': 'Facebook'},
        {'x': 2000, 'y': 50, 'z': 75, 'name': 'Instagram'},
        {'x': 450, 'y': 60, 'z': 50, 'name': 'Twitter'},
        {'x': 930, 'y': 70, 'z': 40, 'name': 'LinkedIn'}
    ]
    
    html = f'''
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://code.highcharts.com/highcharts.js"></script>
    </head>
    <body>
        <div id="bubble" style="width:100%; height:450px;"></div>
        <script>
            Highcharts.chart('bubble', {{
                chart: {{ type: 'bubble' }},
                title: {{ text: 'Platform Comparison' }},
                xAxis: {{ title: {{ text: 'Users (M)' }} }},
                yAxis: {{ title: {{ text: 'Privacy Score' }} }},
                series: [{{
                    data: {json.dumps(data)}
                }}]
            }});
        </script>
    </body>
    </html>
    '''
    
    components.html(html, height=500)

# Timeline
elif chart_type == "Timeline":
    st.subheader("📅 Security Incidents")
    
    html = '''
    <!DOCTYPE html>
    <html>
    <head>
        <script src="https://code.highcharts.com/highcharts.js"></script>
    </head>
    <body>
        <div id="timeline" style="width:100%; height:450px;"></div>
        <script>
            Highcharts.chart('timeline', {
                chart: { type: 'line' },
                title: { text: 'Security Incidents' },
                xAxis: { categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun'] },
                series: [{
                    name: 'Phishing',
                    data: [45, 52, 38, 60, 55, 48]
                }, {
                    name: 'Data Breaches',
                    data: [12, 15, 10, 18, 20, 15]
                }]
            });
        </script>
    </body>
    </html>
    '''
    
    components.html(html, height=500)

# Course connection
st.divider()
st.markdown("""
### 🎓 Course Outcomes Demonstrated
- **CO3**: Analyze ethical dilemmas in social media privacy
- **CO4**: Apply visualization to real-world scenarios
- **Module 5**: Highcharts visualization implementation

### ⚖️ Ethical Considerations
- All data is simulated for educational purposes
- No real user data collected
- Privacy-preserving analysis methods
""")
