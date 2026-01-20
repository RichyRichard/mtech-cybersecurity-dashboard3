"""
Enhanced Social Media Privacy & Security Analytics Dashboard
Fixed for Streamlit Cloud Deployment
M.Tech Mini Project - Module 5: Visualization - Highcharts
"""

import pandas as pd
import numpy as np
import json
import streamlit as st
from datetime import datetime, timedelta
import streamlit.components.v1 as components
import random
import warnings
warnings.filterwarnings('ignore')

# Try to import plotly with graceful fallback
try:
    import plotly.graph_objects as go
    import plotly.express as px
    PLOTLY_AVAILABLE = True
except ImportError:
    PLOTLY_AVAILABLE = False
    st.warning("Plotly not installed. Some visualizations will use alternative methods.")

# Page configuration
st.set_page_config(
    page_title="Advanced Highcharts Visualization Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

class HighchartsGenerator:
    """Class to generate various Highcharts visualizations"""
    
    def __init__(self):
        self.color_palette = [
            '#2E93fA', '#66DA26', '#546E7A', '#E91E63', '#FF9800',
            '#8B5CF6', '#00E396', '#FF4560', '#775DD0', '#3F51B5'
        ]
    
    def create_network_graph(self, nodes_data, links_data):
        """Create social network graph"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/modules/networkgraph.js"></script>
            <style>
                #container {{
                    min-width: 320px;
                    max-width: 1200px;
                    height: 600px;
                    margin: 0 auto;
                }}
            </style>
        </head>
        <body>
            <div id="container"></div>
            <script type="text/javascript">
                Highcharts.chart('container', {{
                    chart: {{
                        type: 'networkgraph',
                        height: 550,
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{
                        text: 'Social Network Analysis - Privacy Risk Propagation',
                        align: 'left'
                    }},
                    subtitle: {{
                        text: 'Visualizing user connections and community structures (Anonymized Ethical Data)',
                        align: 'left'
                    }},
                    plotOptions: {{
                        networkgraph: {{
                            keys: ['from', 'to'],
                            layoutAlgorithm: {{
                                enableSimulation: true,
                                friction: -0.9
                            }}
                        }}
                    }},
                    series: [{{
                        name: 'Social Network',
                        data: {json.dumps(links_data)},
                        nodes: {json.dumps(nodes_data)},
                        color: '#2E93fA',
                        dataLabels: {{
                            enabled: true,
                            format: '{{point.name}}'
                        }}
                    }}],
                    tooltip: {{
                        formatter: function() {{
                            return '<b>Node:</b> ' + this.point.name + '<br>' +
                                   '<b>Connections:</b> ' + this.point.links.length;
                        }}
                    }}
                }});
            </script>
        </body>
        </html>
        '''
        return html
    
    def create_sankey_diagram(self, nodes, links):
        """Create Sankey diagram for data flow analysis"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/modules/sankey.js"></script>
            <style>
                #sankey-container {{
                    min-width: 310px;
                    max-width: 1200px;
                    height: 600px;
                    margin: 0 auto;
                }}
            </style>
        </head>
        <body>
            <div id="sankey-container"></div>
            <script type="text/javascript">
                Highcharts.chart('sankey-container', {{
                    chart: {{
                        type: 'sankey',
                        height: 550,
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{
                        text: 'Data Flow in Social Media Ecosystem',
                        align: 'left'
                    }},
                    subtitle: {{
                        text: 'How user data flows through social media platforms (Ethical Analysis)',
                        align: 'left'
                    }},
                    series: [{{
                        name: 'Data Flow',
                        keys: ['from', 'to', 'weight'],
                        data: {json.dumps(links)},
                        nodes: {json.dumps(nodes)},
                        nodeWidth: 20,
                        nodePadding: 10
                    }}],
                    tooltip: {{
                        headerFormat: null,
                        pointFormat: '<b>{{point.fromNode.name}}</b> → <b>{{point.toNode.name}}</b><br/>'
                    }}
                }});
            </script>
        </body>
        </html>
        '''
        return html
    
    def create_heatmap_chart(self, categories_x, categories_y, data):
        """Create heatmap for location privacy analysis"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/modules/heatmap.js"></script>
            <style>
                #heatmap-container {{
                    min-width: 310px;
                    max-width: 1200px;
                    height: 500px;
                    margin: 0 auto;
                }}
            </style>
        </head>
        <body>
            <div id="heatmap-container"></div>
            <script type="text/javascript">
                Highcharts.chart('heatmap-container', {{
                    chart: {{
                        type: 'heatmap',
                        height: 450,
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{
                        text: 'Location Privacy Risk Heatmap',
                        align: 'left'
                    }},
                    subtitle: {{
                        text: 'Privacy risk scores across different locations and times',
                        align: 'left'
                    }},
                    xAxis: {{
                        categories: {json.dumps(categories_x)},
                        title: {{ text: 'Day of Week' }}
                    }},
                    yAxis: {{
                        categories: {json.dumps(categories_y)},
                        title: {{ text: 'Hour of Day' }},
                        reversed: true
                    }},
                    colorAxis: {{
                        min: 0,
                        minColor: '#FFFFFF',
                        maxColor: '#FF4560'
                    }},
                    series: [{{
                        name: 'Privacy Risk',
                        borderWidth: 1,
                        data: {json.dumps(data)},
                        dataLabels: {{
                            enabled: false
                        }}
                    }}],
                    tooltip: {{
                        formatter: function() {{
                            return '<b>Time:</b> ' + this.point.y + ':00<br>' +
                                   '<b>Day:</b> ' + this.point.x + '<br>' +
                                   '<b>Privacy Risk:</b> ' + this.point.value;
                        }}
                    }}
                }});
            </script>
        </body>
        </html>
        '''
        return html
    
    def create_bubble_chart(self, data):
        """Create bubble chart for social media metrics"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <style>
                #bubble-container {{
                    min-width: 310px;
                    max-width: 1200px;
                    height: 500px;
                    margin: 0 auto;
                }}
            </style>
        </head>
        <body>
            <div id="bubble-container"></div>
            <script type="text/javascript">
                Highcharts.chart('bubble-container', {{
                    chart: {{
                        type: 'bubble',
                        zoomType: 'xy',
                        height: 450,
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{
                        text: 'Social Media Platform Comparison',
                        align: 'left'
                    }},
                    subtitle: {{
                        text: 'Bubble size represents data collection volume',
                        align: 'left'
                    }},
                    xAxis: {{
                        title: {{
                            text: 'Monthly Active Users (Millions)'
                        }}
                    }},
                    yAxis: {{
                        title: {{
                            text: 'Privacy Protection Score (0-100)'
                        }}
                    }},
                    series: [{{
                        name: 'Platforms',
                        data: {json.dumps(data)}
                    }}],
                    tooltip: {{
                        headerFormat: '<b>{{point.name}}</b><br>',
                        pointFormat: 'Users: {{point.x}}M<br>Privacy Score: {{point.y}}<br>Data: {{point.z}}TB/month'
                    }}
                }});
            </script>
        </body>
        </html>
        '''
        return html
    
    def create_timeline_chart(self, series_data):
        """Create timeline chart for security incidents"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <style>
                #timeline-container {{
                    min-width: 310px;
                    max-width: 1200px;
                    height: 500px;
                    margin: 0 auto;
                }}
            </style>
        </head>
        <body>
            <div id="timeline-container"></div>
            <script type="text/javascript">
                Highcharts.chart('timeline-container', {{
                    chart: {{
                        type: 'line',
                        height: 450,
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{
                        text: 'Security Incidents Timeline - Last 12 Months',
                        align: 'left'
                    }},
                    subtitle: {{
                        text: 'Tracking phishing, data breaches, and malware incidents',
                        align: 'left'
                    }},
                    xAxis: {{
                        categories: ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 
                                    'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
                    }},
                    yAxis: {{
                        title: {{
                            text: 'Number of Incidents'
                        }}
                    }},
                    series: {json.dumps(series_data)},
                    tooltip: {{
                        shared: true
                    }}
                }});
            </script>
        </body>
        </html>
        '''
        return html
    
    def create_gauge_chart(self, value, max_value=100):
        """Create gauge chart for privacy risk score"""
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/highcharts-more.js"></script>
            <script src="https://code.highcharts.com/modules/solid-gauge.js"></script>
            <style>
                #gauge-container {{
                    min-width: 310px;
                    max-width: 600px;
                    height: 400px;
                    margin: 0 auto;
                }}
            </style>
        </head>
        <body>
            <div id="gauge-container"></div>
            <script type="text/javascript">
                Highcharts.chart('gauge-container', {{
                    chart: {{
                        type: 'solidgauge',
                        height: 350,
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{
                        text: 'Overall Privacy Risk Score'
                    }},
                    pane: {{
                        center: ['50%', '85%'],
                        size: '140%',
                        startAngle: -90,
                        endAngle: 90,
                        background: {{
                            backgroundColor: '#FFF',
                            innerRadius: '60%',
                            outerRadius: '100%',
                            shape: 'arc'
                        }}
                    }},
                    yAxis: {{
                        min: 0,
                        max: {max_value},
                        stops: [
                            [0.1, '#55BF3B'],
                            [0.5, '#DDDF0D'],
                            [0.9, '#DF5353']
                        ]
                    }},
                    series: [{{
                        name: 'Risk Score',
                        data: [{value}],
                        dataLabels: {{
                            format: '<div style="text-align:center">' +
                                   '<span style="font-size:25px">{{y}}</span><br/>' +
                                   '<span style="font-size:12px">OUT OF {max_value}</span></div>'
                        }}
                    }}]
                }});
            </script>
        </body>
        </html>
        '''
        return html

class DataSimulator:
    """Simulate data for ethical visualization"""
    
    @staticmethod
    def generate_network_data():
        """Generate social network data"""
        nodes = []
        for i in range(15):
            nodes.append({
                'id': f'user_{i}',
                'name': f'User_{1000 + i}',
                'value': random.uniform(0.5, 5.0),
                'community': random.choice(['A', 'B', 'C']),
                'color': random.choice(['#2E93fA', '#66DA26', '#E91E63'])
            })
        
        links = []
        for i in range(25):
            source = f'user_{random.randint(0, 14)}'
            target = f'user_{random.randint(0, 14)}'
            if source != target:
                links.append([source, target])
        
        return nodes, links
    
    @staticmethod
    def generate_sankey_data():
        """Generate data for Sankey diagram"""
        nodes = [
            {'id': 'User', 'name': 'User Profile'},
            {'id': 'Posts', 'name': 'User Posts'},
            {'id': 'Location', 'name': 'Location Data'},
            {'id': 'Platform', 'name': 'Social Platform'},
            {'id': 'Advertisers', 'name': 'Advertisers'},
            {'id': 'Analytics', 'name': 'Analytics Firms'}
        ]
        
        links = [
            ['User', 'Platform', 25],
            ['Posts', 'Platform', 40],
            ['Location', 'Platform', 15],
            ['Platform', 'Advertisers', 50],
            ['Platform', 'Analytics', 30]
        ]
        
        return nodes, links
    
    @staticmethod
    def generate_heatmap_data():
        """Generate heatmap data"""
        days = ['Mon', 'Tue', 'Wed', 'Thu', 'Fri', 'Sat', 'Sun']
        hours = [f'{h}:00' for h in range(8, 22, 2)]
        
        data = []
        for i, day in enumerate(days):
            for j, hour in enumerate(hours):
                base_risk = 30
                if day in ['Sat', 'Sun']:
                    base_risk += 20
                if 18 <= int(hour.split(':')[0]) <= 22:
                    base_risk += 25
                
                risk = base_risk + random.randint(-10, 10)
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
        for platform in platforms:
            data.append({
                'x': platform['users'],
                'y': platform['privacy'],
                'z': platform['data'],
                'name': platform['name']
            })
        
        return data
    
    @staticmethod
    def generate_timeline_data():
        """Generate timeline data"""
        series_data = [
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
        
        return series_data

class EnhancedPrivacyDashboard:
    """Main dashboard class"""
    
    def __init__(self):
        self.hc_generator = HighchartsGenerator()
        self.data_simulator = DataSimulator()
    
    def render_header(self):
        """Render dashboard header"""
        st.title("📊 Social Media Privacy & Security Dashboard")
        st.markdown("**M.Tech Mini Project | Ethical Issues in IT | Module 5: Highcharts Visualization**")
        
        with st.expander("Course Connection", expanded=False):
            st.write("""
            **Modules Covered:**
            - Module 3: Privacy & Security in OSNs
            - Module 4: Phishing & Network Visualization  
            - Module 5: Case Studies & Highcharts
            
            **Course Outcomes:**
            - CO3: Analyze ethical dilemmas
            - CO4: Real-world case studies
            """)
    
    def render_sidebar(self):
        """Render sidebar"""
        with st.sidebar:
            st.title("Controls")
            
            selected_charts = st.multiselect(
                "Chart Types:",
                ["Network Graph", "Sankey Diagram", "Heatmap", "Bubble Chart", "Timeline", "Gauge"],
                default=["Network Graph", "Sankey Diagram", "Heatmap"]
            )
            
            st.divider()
            st.caption(f"Last update: {datetime.now().strftime('%H:%M:%S')}")
            
            return selected_charts
    
    def render_network_section(self):
        """Render network graph"""
        st.subheader("🔗 Social Network Analysis")
        
        col1, col2 = st.columns([3, 1])
        
        with col1:
            nodes, links = self.data_simulator.generate_network_data()
            html = self.hc_generator.create_network_graph(nodes, links)
            components.html(html, height=600)
        
        with col2:
            st.metric("Nodes", len(nodes))
            st.metric("Connections", len(links))
            
            st.info("""
            **Ethical Note:**
            - All data anonymized
            - Simulated network
            - No real users
            """)
    
    def render_sankey_section(self):
        """Render Sankey diagram"""
        st.subheader("🌊 Data Flow Analysis")
        
        nodes, links = self.data_simulator.generate_sankey_data()
        
        col1, col2, col3 = st.columns(3)
        with col1:
            total_data = sum([link[2] for link in links])
            st.metric("Data Flow", f"{total_data} GB/month")
        with col2:
            st.metric("Entities", len(nodes))
        with col3:
            st.metric("Pathways", len(links))
        
        html = self.hc_generator.create_sankey_diagram(nodes, links)
        components.html(html, height=600)
    
    def render_heatmap_section(self):
        """Render heatmap"""
        st.subheader("📍 Location Privacy Heatmap")
        
        days, hours, data = self.data_simulator.generate_heatmap_data()
        
        risks = [point[2] for point in data]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Avg Risk", f"{np.mean(risks):.1f}/100")
        with col2:
            st.metric("Peak Risk", max(risks))
        with col3:
            high_risk = len([r for r in risks if r > 70])
            st.metric("High Risk", high_risk)
        
        html = self.hc_generator.create_heatmap_chart(days, hours, data)
        components.html(html, height=500)
    
    def render_bubble_section(self):
        """Render bubble chart"""
        st.subheader("🫧 Platform Comparison")
        
        data = self.data_simulator.generate_bubble_data()
        
        # Create summary table
        df = pd.DataFrame([
            {'Platform': d['name'], 'Users': d['x'], 'Privacy': d['y'], 'Data': d['z']}
            for d in data
        ])
        
        best_privacy = df.loc[df['Privacy'].idxmax()]
        most_users = df.loc[df['Users'].idxmax()]
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Best Privacy", best_privacy['Platform'], f"{best_privacy['Privacy']}/100")
        with col2:
            st.metric("Most Users", most_users['Platform'], f"{most_users['Users']}M")
        
        html = self.hc_generator.create_bubble_chart(data)
        components.html(html, height=500)
        
        with st.expander("Data Table"):
            st.dataframe(df)
    
    def render_timeline_section(self):
        """Render timeline"""
        st.subheader("📅 Security Incidents")
        
        data = self.data_simulator.generate_timeline_data()
        
        totals = {s['name']: sum(s['data']) for s in data}
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Phishing", totals['Phishing Attacks'])
        with col2:
            st.metric("Data Breaches", totals['Data Breaches'])
        
        html = self.hc_generator.create_timeline_chart(data)
        components.html(html, height=500)
    
    def render_gauge_section(self):
        """Render gauge"""
        st.subheader("⚠️ Risk Assessment")
        
        risk_score = random.randint(35, 75)
        
        col1, col2 = st.columns([2, 1])
        with col1:
            html = self.hc_generator.create_gauge_chart(risk_score)
            components.html(html, height=400)
        with col2:
            st.metric("Risk Score", f"{risk_score}/100")
            
            st.write("**Factors:**")
            factors = {
                "Location": random.randint(40, 90),
                "Data Sharing": random.randint(30, 80),
                "Network": random.randint(20, 70)
            }
            
            for factor, score in factors.items():
                st.progress(score/100, text=f"{factor}: {score}")
    
    def render_conclusion(self):
        """Render conclusion"""
        st.divider()
        
        col1, col2 = st.columns([2, 1])
        with col1:
            st.markdown("""
            ### Project Summary
            
            **Highcharts Visualizations Implemented:**
            1. Network Graph - Social connections
            2. Sankey Diagram - Data flow  
            3. Heatmap - Location patterns
            4. Bubble Chart - Platform comparison
            5. Timeline - Security incidents
            6. Gauge Chart - Risk assessment
            
            **Course Alignment:**
            - Module 3: OSN Privacy & Security
            - Module 4: Phishing & Network Analysis
            - Module 5: Case Studies & Visualization
            """)
        
        with col2:
            st.write("### Status")
            st.success("✅ Streamlit Cloud Ready")
            st.info("✅ Ethical Data Handling")
            st.warning("✅ Course Requirements Met")
        
        st.info("**Academic Submission Ready** - This project demonstrates practical Highcharts implementation for M.Tech course requirements.")
    
    def run(self):
        """Main run method"""
        self.render_header()
        selected = self.render_sidebar()
        
        # Only show selected charts
        if "Network Graph" in selected:
            self.render_network_section()
        
        if "Sankey Diagram" in selected:
            self.render_sankey_section()
        
        if "Heatmap" in selected:
            self.render_heatmap_section()
        
        if "Bubble Chart" in selected:
            self.render_bubble_section()
        
        if "Timeline" in selected:
            self.render_timeline_section()
        
        if "Gauge" in selected:
            self.render_gauge_section()
        
        self.render_conclusion()

# Run the app
if __name__ == "__main__":
    app = EnhancedPrivacyDashboard()
    app.run()
