"""
Social Media Privacy & Security Dashboard
Clean version for Streamlit Cloud - No Plotly
M.Tech Course Project - Module 5: Highcharts Visualization
"""

import pandas as pd
import numpy as np
import json
import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
import random

# Page configuration - MUST BE FIRST
st.set_page_config(
    page_title="Social Media Privacy Dashboard",
    page_icon="📊",
    layout="wide"
)

# ========== HIGCHARTS GENERATOR ==========
class HighchartsGenerator:
    """Generate Highcharts visualizations"""
    
    def create_network_graph(self, nodes_data, links_data):
        """Create social network graph"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/modules/networkgraph.js"></script>
        </head>
        <body>
            <div id="network-container" style="width:100%; height:500px;"></div>
            <script>
                Highcharts.chart('network-container', {{
                    chart: {{ 
                        type: 'networkgraph',
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{ 
                        text: 'Social Network Analysis',
                        align: 'left'
                    }},
                    plotOptions: {{
                        networkgraph: {{
                            keys: ['from', 'to']
                        }}
                    }},
                    series: [{{
                        data: {json.dumps(links_data)},
                        nodes: {json.dumps(nodes_data)},
                        color: '#2E93fA',
                        dataLabels: {{
                            enabled: true,
                            format: '{{point.name}}'
                        }}
                    }}]
                }});
            </script>
        </body>
        </html>
        '''
        return html
    
    def create_heatmap_chart(self, categories_x, categories_y, data):
        """Create heatmap for location privacy"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/modules/heatmap.js"></script>
        </head>
        <body>
            <div id="heatmap-container" style="width:100%; height:450px;"></div>
            <script>
                Highcharts.chart('heatmap-container', {{
                    chart: {{ 
                        type: 'heatmap',
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{ 
                        text: 'Location Privacy Risk Heatmap',
                        align: 'left'
                    }},
                    xAxis: {{
                        categories: {json.dumps(categories_x)}
                    }},
                    yAxis: {{
                        categories: {json.dumps(categories_y)},
                        reversed: true
                    }},
                    colorAxis: {{
                        min: 0,
                        minColor: '#FFFFFF',
                        maxColor: '#FF4560'
                    }},
                    series: [{{
                        name: 'Privacy Risk',
                        data: {json.dumps(data)}
                    }}],
                    tooltip: {{
                        formatter: function() {{
                            return '<b>Day:</b> ' + this.point.x + '<br>' +
                                   '<b>Time:</b> ' + this.point.y + '<br>' +
                                   '<b>Risk:</b> ' + this.point.value + '/100';
                        }}
                    }}
                }});
            </script>
        </body>
        </html>
        '''
        return html
    
    def create_bubble_chart(self, data):
        """Create bubble chart for platform comparison"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
        </head>
        <body>
            <div id="bubble-container" style="width:100%; height:450px;"></div>
            <script>
                Highcharts.chart('bubble-container', {{
                    chart: {{ 
                        type: 'bubble',
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{ 
                        text: 'Social Media Platform Comparison',
                        align: 'left'
                    }},
                    xAxis: {{
                        title: {{ text: 'Monthly Active Users (Millions)' }}
                    }},
                    yAxis: {{
                        title: {{ text: 'Privacy Score (0-100)' }}
                    }},
                    series: [{{
                        name: 'Platforms',
                        data: {json.dumps(data)}
                    }}],
                    tooltip: {{
                        pointFormat: '<b>{{point.name}}</b><br>Users: {{point.x}}M<br>Privacy: {{point.y}}<br>Data: {{point.z}}TB/month'
                    }}
                }});
            </script>
        </body>
        </html>
        '''
        return html
    
    def create_timeline_chart(self, series_data):
        """Create timeline for security incidents"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
        </head>
        <body>
            <div id="timeline-container" style="width:100%; height:450px;"></div>
            <script>
                Highcharts.chart('timeline-container', {{
                    chart: {{ 
                        type: 'line',
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{ 
                        text: 'Security Incidents Timeline',
                        align: 'left'
                    }},
                    xAxis: {{
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                    }},
                    yAxis: {{
                        title: {{ text: 'Number of Incidents' }}
                    }},
                    series: {json.dumps(series_data)}
                }});
            </script>
        </body>
        </html>
        '''
        return html

# ========== DATA SIMULATOR ==========
class DataSimulator:
    """Generate simulated data for visualization"""
    
    @staticmethod
    def generate_network_data():
        """Generate network data"""
        nodes = []
        for i in range(12):
            nodes.append({
                'id': f'user_{i}',
                'name': f'User_{1000 + i}',
                'value': random.uniform(0.5, 5.0)
            })
        
        links = []
        for _ in range(20):
            source = f'user_{random.randint(0, 11)}'
            target = f'user_{random.randint(0, 11)}'
            if source != target:
                links.append([source, target])
        
        return nodes, links
    
    @staticmethod
    def generate_heatmap_data():
        """Generate heatmap data"""
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        hours = ['8:00', '10:00', '12:00', '14:00', '16:00', '18:00', '20:00']
        
        data = []
        for i, day in enumerate(days):
            for j, hour in enumerate(hours):
                # Base risk
                risk = 40
                # Higher on weekends
                if day in ['Sat', 'Sun']:
                    risk += 20
                # Higher in evening
                if '18:00' in hour or '20:00' in hour:
                    risk += 15
                # Add some randomness
                risk += random.randint(-10, 10)
                risk = max(0, min(100, risk))
                
                data.append([i, j, risk])
        
        return days, hours, data
    
    @staticmethod
    def generate_bubble_data():
        """Generate bubble chart data"""
        platforms = [
            {'name': 'Facebook', 'users': 2910, 'privacy': 45, 'data': 85},
            {'name': 'Instagram', 'users': 2000, 'privacy': 50, 'data': 75},
            {'name': 'Twitter', 'users': 450, 'privacy': 60, 'data': 50},
            {'name': 'LinkedIn', 'users': 930, 'privacy': 70, 'data': 40},
            {'name': 'TikTok', 'users': 1500, 'privacy': 40, 'data': 90}
        ]
        
        data = []
        for p in platforms:
            data.append({
                'x': p['users'],
                'y': p['privacy'],
                'z': p['data'],
                'name': p['name']
            })
        
        return data
    
    @staticmethod
    def generate_timeline_data():
        """Generate timeline data"""
        return [
            {
                'name': 'Phishing Attacks',
                'data': [45, 52, 38, 60, 55, 48, 65, 70, 58, 62, 75, 80],
                'color': '#FF4560'
            },
            {
                'name': 'Data Breaches',
                'data': [12, 15, 10, 18, 20, 15, 22, 25, 18, 20, 28, 30],
                'color': '#8B5CF6'
            }
        ]

# ========== MAIN DASHBOARD ==========
def main():
    """Main dashboard function"""
    
    # Initialize generators
    hc = HighchartsGenerator()
    data_sim = DataSimulator()
    
    # Header
    st.title("📊 Social Media Privacy & Security Dashboard")
    st.markdown("**M.Tech Course Project | Ethical Issues in IT | Module 5: Highcharts Visualization**")
    
    # Course info
    with st.expander("📚 Course Connection", expanded=False):
        st.write("""
        **Modules Covered:**
        - Module 3: Privacy & Security in OSNs
        - Module 4: Phishing & Network Analysis  
        - Module 5: Case Studies & Highcharts
        
        **Course Outcomes:**
        - CO3: Analyze ethical dilemmas
        - CO4: Analyze real-world case studies
        """)
    
    # Sidebar
    with st.sidebar:
        st.title("Controls")
        chart_type = st.selectbox(
            "Select Chart:",
            ["Network Graph", "Heatmap", "Bubble Chart", "Timeline", "All"]
        )
        st.divider()
        st.caption(f"Updated: {datetime.now().strftime('%H:%M:%S')}")
    
    # NETWORK GRAPH
    if chart_type in ["Network Graph", "All"]:
        st.subheader("🔗 Social Network Analysis")
        
        col1, col2 = st.columns([3, 1])
        with col1:
            nodes, links = data_sim.generate_network_data()
            html = hc.create_network_graph(nodes, links)
            components.html(html, height=550)
        
        with col2:
            st.metric("Total Nodes", len(nodes))
            st.metric("Connections", len(links))
            st.info("""
            **Ethical Note:**
            - Simulated data only
            - No real user information
            """)
    
    # HEATMAP
    if chart_type in ["Heatmap", "All"]:
        st.subheader("📍 Location Privacy Heatmap")
        
        days, hours, heat_data = data_sim.generate_heatmap_data()
        
        # Calculate stats
        risks = [d[2] for d in heat_data]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Average Risk", f"{np.mean(risks):.1f}/100")
        with col2:
            st.metric("Peak Risk", f"{max(risks)}/100")
        with col3:
            high = len([r for r in risks if r > 70])
            st.metric("High Risk Slots", high)
        
        # Display heatmap
        html = hc.create_heatmap_chart(days, hours, heat_data)
        components.html(html, height=500)
    
    # BUBBLE CHART
    if chart_type in ["Bubble Chart", "All"]:
        st.subheader("🫧 Platform Comparison")
        
        bubble_data = data_sim.generate_bubble_data()
        
        # Find best privacy and most users
        platforms = [
            {'name': 'Facebook', 'users': 2910, 'privacy': 45},
            {'name': 'Instagram', 'users': 2000, 'privacy': 50},
            {'name': 'Twitter', 'users': 450, 'privacy': 60},
            {'name': 'LinkedIn', 'users': 930, 'privacy': 70},
            {'name': 'TikTok', 'users': 1500, 'privacy': 40}
        ]
        
        # Convert to DataFrame for easy analysis
        df = pd.DataFrame(platforms)
        best_privacy = df.loc[df['privacy'].idxmax()]
        most_users = df.loc[df['users'].idxmax()]
        
        # Display metrics
        col1, col2 = st.columns(2)
        with col1:
            st.metric(
                "Best Privacy", 
                best_privacy['name'], 
                f"{best_privacy['privacy']}/100"
            )
        with col2:
            st.metric(
                "Most Users", 
                most_users['name'], 
                f"{most_users['users']}M"
            )
        
        # Display bubble chart
        html = hc.create_bubble_chart(bubble_data)
        components.html(html, height=500)
        
        # Show data table
        with st.expander("📊 View Platform Data"):
            st.dataframe(df)
    
    # TIMELINE
    if chart_type in ["Timeline", "All"]:
        st.subheader("📅 Security Incidents Timeline")
        
        timeline_data = data_sim.generate_timeline_data()
        
        # Calculate totals
        phishing_total = sum(timeline_data[0]['data'])
        breaches_total = sum(timeline_data[1]['data'])
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Phishing", phishing_total)
        with col2:
            st.metric("Total Data Breaches", breaches_total)
        
        # Display timeline
        html = hc.create_timeline_chart(timeline_data)
        components.html(html, height=500)
    
    # Course outcomes summary
    st.divider()
    st.subheader("🎓 Course Outcomes Demonstrated")
    
    col1, col2, col3 = st.columns(3)
    with col1:
        st.markdown("**CO1 & CO2**")
        st.write("Identify ethical issues & apply concepts")
    with col2:
        st.markdown("**CO3**")
        st.write("Analyze ethical dilemmas")
    with col3:
        st.markdown("**CO4**")
        st.write("Real-world case study analysis")
    
    # Ethical considerations
    with st.expander("⚖️ Ethical Implementation"):
        st.write("""
        1. **Data Privacy**: All data is simulated
        2. **No Real Users**: No personal information used
        3. **Educational Purpose**: Academic project only
        4. **Transparency**: Clear about data sources
        """)
    
    # Footer
    st.caption("M.Tech in Information Technology | Ethical Issues Course | 2024")

# Run the app
if __name__ == "__main__":
    main()
