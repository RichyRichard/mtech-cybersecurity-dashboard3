"""
Enhanced Social Media Privacy Dashboard with Platform Comparison
M.Tech Course Project - Module 5: Highcharts Visualization
"""

import pandas as pd
import numpy as np
import json
import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
import random

# Page configuration
st.set_page_config(
    page_title="Social Media Privacy Dashboard",
    page_icon="📊",
    layout="wide"
)

class HighchartsGenerator:
    """Generate Highcharts visualizations"""
    
    def __init__(self):
        self.color_palette = {
            'facebook': '#1877F2',
            'instagram': '#E4405F', 
            'twitter': '#1DA1F2',
            'linkedin': '#0A66C2',
            'tiktok': '#000000',
            'primary': '#2E93fA',
            'success': '#00E396',
            'danger': '#FF4560',
            'warning': '#FF9800'
        }
    
    def create_platform_bar_chart(self, platform_data):
        """Create comprehensive platform comparison bar chart"""
        platforms = [p['name'] for p in platform_data]
        users = [p['users'] for p in platform_data]
        privacy_scores = [p['privacy'] for p in platform_data]
        data_collection = [p['data'] for p in platform_data]
        
        html = f'''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
        </head>
        <body>
            <div id="platform-bar" style="width:100%; height:500px;"></div>
            <script>
                Highcharts.chart('platform-bar', {{
                    chart: {{ 
                        type: 'column',
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{ 
                        text: 'Social Media Platform Comparison - Multi-Metric Analysis',
                        align: 'left',
                        style: {{ fontSize: '16px', fontWeight: 'bold' }}
                    }},
                    subtitle: {{ 
                        text: 'Comparing user base size, privacy protection scores, and estimated data collection volumes',
                        align: 'left'
                    }},
                    xAxis: {{
                        categories: {json.dumps(platforms)},
                        crosshair: true
                    }},
                    yAxis: [{{
                        title: {{ 
                            text: 'Monthly Active Users (Millions)'
                        }},
                        labels: {{
                            format: '{{value}}M'
                        }}
                    }}, {{
                        title: {{ 
                            text: 'Privacy Score (0-100)'
                        }},
                        opposite: true,
                        max: 100
                    }}],
                    tooltip: {{
                        shared: true,
                        useHTML: true,
                        headerFormat: '<table><tr><th colspan="2">{{point.key}}</th></tr>',
                        pointFormat: '<tr><td style="color:{{series.color}}">● {{series.name}}: </td>' +
                                   '<td style="text-align:right"><b>{{point.y}}</b></td></tr>',
                        footerFormat: '</table>'
                    }},
                    plotOptions: {{
                        column: {{
                            pointPadding: 0.1,
                            groupPadding: 0.15,
                            borderWidth: 0
                        }}
                    }},
                    series: [{{
                        name: 'Monthly Active Users',
                        data: {json.dumps(users)},
                        color: '{self.color_palette["primary"]}',
                        yAxis: 0,
                        tooltip: {{
                            valueSuffix: 'M'
                        }}
                    }}, {{
                        name: 'Privacy Score',
                        type: 'spline',
                        data: {json.dumps(privacy_scores)},
                        color: '{self.color_palette["success"]}',
                        yAxis: 1,
                        marker: {{
                            enabled: true,
                            radius: 4
                        }},
                        tooltip: {{
                            valueSuffix: '/100'
                        }}
                    }}, {{
                        name: 'Data Collection',
                        data: {json.dumps(data_collection)},
                        color: '{self.color_palette["danger"]}',
                        yAxis: 0,
                        tooltip: {{
                            valueSuffix: 'TB/month'
                        }}
                    }}],
                    legend: {{
                        layout: 'horizontal',
                        align: 'center',
                        verticalAlign: 'bottom'
                    }}
                }});
            </script>
        </body>
        </html>
        '''
        return html
    
    def create_platform_radar_chart(self):
        """Create radar chart for multi-dimensional comparison"""
        html = '''
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/highcharts-more.js"></script>
        </head>
        <body>
            <div id="platform-radar" style="width:100%; height:500px;"></div>
            <script>
                Highcharts.chart('platform-radar', {
                    chart: {
                        polar: true,
                        type: 'line',
                        backgroundColor: '#FFFFFF'
                    },
                    title: {
                        text: 'Platform Security & Privacy Radar Analysis',
                        align: 'left'
                    },
                    pane: {
                        size: '80%'
                    },
                    xAxis: {
                        categories: ['Data Encryption', 'Privacy Controls', 
                                   'Transparency', 'Security Features', 'User Education',
                                   'Compliance', 'Incident Response', 'Third-Party Security'],
                        tickmarkPlacement: 'on',
                        lineWidth: 0
                    },
                    yAxis: {
                        gridLineInterpolation: 'polygon',
                        lineWidth: 0,
                        min: 0,
                        max: 10,
                        tickInterval: 2
                    },
                    series: [{
                        name: 'Facebook',
                        data: [7, 5, 4, 6, 5, 7, 6, 5],
                        pointPlacement: 'on',
                        color: '#1877F2'
                    }, {
                        name: 'Instagram',
                        data: [6, 4, 3, 5, 4, 6, 5, 4],
                        pointPlacement: 'on',
                        color: '#E4405F'
                    }, {
                        name: 'Twitter',
                        data: [8, 7, 8, 7, 6, 8, 7, 7],
                        pointPlacement: 'on',
                        color: '#1DA1F2'
                    }, {
                        name: 'LinkedIn',
                        data: [9, 8, 7, 8, 7, 9, 8, 8],
                        pointPlacement: 'on',
                        color: '#0A66C2'
                    }],
                    legend: {
                        align: 'center',
                        verticalAlign: 'bottom'
                    }
                });
            </script>
        </body>
        </html>
        '''
        return html
    
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
            <div id="network" style="width:100%; height:500px;"></div>
            <script>
                Highcharts.chart('network', {{
                    chart: {{ 
                        type: 'networkgraph',
                        backgroundColor: '#FFFFFF'
                    }},
                    title: {{ 
                        text: 'Social Network Analysis',
                        align: 'left'
                    }},
                    series: [{{
                        data: {json.dumps(links_data)},
                        nodes: {json.dumps(nodes_data)}
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
            <div id="heatmap" style="width:100%; height:450px;"></div>
            <script>
                Highcharts.chart('heatmap', {{
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
                    }}]
                }});
            </script>
        </body>
        </html>
        '''
        return html

class DataSimulator:
    """Generate simulated data for visualization"""
    
    @staticmethod
    def generate_platform_data():
        """Generate comprehensive platform comparison data"""
        return [
            {
                'name': 'Facebook',
                'users': 2910,
                'privacy': 45,
                'data': 85,
                'security': 7,
                'transparency': 5,
                'compliance': 7,
                'color': '#1877F2'
            },
            {
                'name': 'Instagram', 
                'users': 2000,
                'privacy': 50,
                'data': 75,
                'security': 6,
                'transparency': 4,
                'compliance': 6,
                'color': '#E4405F'
            },
            {
                'name': 'Twitter',
                'users': 450,
                'privacy': 60,
                'data': 50,
                'security': 8,
                'transparency': 8,
                'compliance': 8,
                'color': '#1DA1F2'
            },
            {
                'name': 'LinkedIn',
                'users': 930,
                'privacy': 70,
                'data': 40,
                'security': 9,
                'transparency': 7,
                'compliance': 9,
                'color': '#0A66C2'
            },
            {
                'name': 'TikTok',
                'users': 1500,
                'privacy': 40,
                'data': 90,
                'security': 5,
                'transparency': 3,
                'compliance': 5,
                'color': '#000000'
            }
        ]
    
    @staticmethod
    def generate_network_data():
        """Generate network data"""
        nodes = []
        for i in range(12):
            nodes.append({
                'id': f'user_{i}',
                'name': f'User_{1000 + i}'
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
                risk = 40
                if day in ['Sat', 'Sun']:
                    risk += 20
                if '18:00' in hour or '20:00' in hour:
                    risk += 15
                risk += random.randint(-10, 10)
                risk = max(0, min(100, risk))
                
                data.append([i, j, risk])
        
        return days, hours, data

def main():
    """Main dashboard function"""
    
    # Initialize
    hc = HighchartsGenerator()
    data_sim = DataSimulator()
    
    # Header
    st.title("📊 Social Media Privacy & Security Dashboard")
    st.markdown("**M.Tech Course Project | Ethical Issues in IT | Module 5: Highcharts Visualization**")
    
    # Course info
    with st.expander("📚 Course Connection", expanded=False):
        col1, col2 = st.columns(2)
        with col1:
            st.markdown("**Modules Covered:**")
            st.write("- Module 3: Privacy in OSNs")
            st.write("- Module 4: Phishing & Network Analysis")
            st.write("- Module 5: Case Studies & Highcharts")
        with col2:
            st.markdown("**Course Outcomes:**")
            st.write("- CO1: Identify ethical issues")
            st.write("- CO2: Apply ethical concepts")
            st.write("- CO3: Analyze dilemmas")
            st.write("- CO4: Real-world case studies")
    
    # Sidebar
    with st.sidebar:
        st.title("Dashboard Controls")
        
        # Visualization selection
        viz_type = st.radio(
            "Select Visualization:",
            ["Platform Comparison", "Network Analysis", "Location Privacy", "All"]
        )
        
        # Platform filters
        if viz_type == "Platform Comparison":
            platforms = st.multiselect(
                "Select Platforms:",
                ["Facebook", "Instagram", "Twitter", "LinkedIn", "TikTok"],
                default=["Facebook", "Instagram", "Twitter", "LinkedIn"]
            )
        
        st.divider()
        
        # Real-time metrics
        st.metric("Overall Privacy Risk", f"{random.randint(35, 75)}/100")
        st.metric("Data Points Analyzed", f"{random.randint(1000, 5000):,}")
        
        st.caption(f"Last update: {datetime.now().strftime('%H:%M:%S')}")
    
    # PLATFORM COMPARISON SECTION
    if viz_type in ["Platform Comparison", "All"]:
        st.subheader("🆚 Social Media Platform Comparison Analysis")
        
        # Get platform data
        all_platforms = data_sim.generate_platform_data()
        
        # Display key metrics
        col1, col2, col3, col4 = st.columns(4)
        
        # Find best privacy platform
        best_privacy = max(all_platforms, key=lambda x: x['privacy'])
        with col1:
            st.metric(
                "Best Privacy", 
                best_privacy['name'],
                f"{best_privacy['privacy']}/100",
                delta=f"↑ {best_privacy['privacy'] - 50}",
                delta_color="normal"
            )
        
        # Find most users
        most_users = max(all_platforms, key=lambda x: x['users'])
        with col2:
            st.metric(
                "Most Users",
                most_users['name'],
                f"{most_users['users']}M",
                delta=f"↑ {most_users['users'] - 1000}M",
                delta_color="normal"
            )
        
        # Find least data collection
        least_data = min(all_platforms, key=lambda x: x['data'])
        with col3:
            st.metric(
                "Least Data Collection",
                least_data['name'],
                f"{least_data['data']}TB/month",
                delta=f"↓ {90 - least_data['data']}",
                delta_color="inverse"
            )
        
        # Average privacy score
        avg_privacy = np.mean([p['privacy'] for p in all_platforms])
        with col4:
            st.metric(
                "Industry Average Privacy",
                f"{avg_privacy:.1f}/100",
                delta=f"{avg_privacy - 50:+.1f}",
                delta_color="off" if avg_privacy == 50 else ("normal" if avg_privacy > 50 else "inverse")
            )
        
        # Bar chart visualization
        st.markdown("#### 📈 Multi-Metric Platform Comparison")
        bar_html = hc.create_platform_bar_chart(all_platforms)
        components.html(bar_html, height=550)
        
        # Data table
        with st.expander("📊 View Detailed Platform Data"):
            df = pd.DataFrame(all_platforms)
            st.dataframe(
                df[['name', 'users', 'privacy', 'data', 'security', 'transparency', 'compliance']].rename(
                    columns={
                        'name': 'Platform',
                        'users': 'Users (M)',
                        'privacy': 'Privacy Score',
                        'data': 'Data Collection',
                        'security': 'Security Score',
                        'transparency': 'Transparency',
                        'compliance': 'Compliance'
                    }
                ),
                use_container_width=True
            )
        
        # Radar chart
        st.markdown("#### 🎯 Multi-Dimensional Security Analysis")
        radar_html = hc.create_platform_radar_chart()
        components.html(radar_html, height=550)
        
        # Ethical insights
        with st.expander("⚖️ Ethical Insights from Platform Analysis"):
            st.write("""
            **Key Ethical Findings:**
            
            1. **Privacy-Tradeoff**: Platforms with larger user bases tend to have lower privacy scores
            2. **Transparency Gap**: Many platforms lack clear data usage transparency
            3. **Data Collection**: Social media platforms collect 40-90TB of user data monthly
            4. **Security Standards**: Professional platforms (LinkedIn) score higher on security
            
            **Recommendations:**
            - Users should review privacy settings regularly
            - Consider platform privacy scores when choosing services
            - Support platforms with better transparency practices
            - Advocate for stronger data protection regulations
            """)
    
    # NETWORK ANALYSIS
    if viz_type in ["Network Analysis", "All"]:
        st.subheader("🔗 Social Network Analysis")
        
        nodes, links = data_sim.generate_network_data()
        network_html = hc.create_network_graph(nodes, links)
        components.html(network_html, height=550)
        
        col1, col2 = st.columns(2)
        with col1:
            st.metric("Total Nodes", len(nodes))
        with col2:
            st.metric("Total Connections", len(links))
    
    # LOCATION PRIVACY
    if viz_type in ["Location Privacy", "All"]:
        st.subheader("📍 Location Privacy Analysis")
        
        days, hours, heat_data = data_sim.generate_heatmap_data()
        heat_html = hc.create_heatmap_chart(days, hours, heat_data)
        components.html(heat_html, height=500)
        
        # Calculate and display stats
        risks = [d[2] for d in heat_data]
        col1, col2, col3 = st.columns(3)
        with col1:
            st.metric("Average Risk", f"{np.mean(risks):.1f}/100")
        with col2:
            st.metric("Peak Risk Time", "Weekend Evenings")
        with col3:
            high_risk = len([r for r in risks if r > 70])
            st.metric("High Risk Periods", high_risk)
    
    # Course outcomes summary
    st.divider()
    st.subheader("🎓 Course Outcomes Demonstrated")
    
    cols = st.columns(4)
    outcomes = [
        ("CO1", "Identify ethical issues in social media platforms"),
        ("CO2", "Apply ethical frameworks to platform analysis"),
        ("CO3", "Analyze privacy vs utility trade-offs"),
        ("CO4", "Real-world case study of platform ethics")
    ]
    
    for col, (co, desc) in zip(cols, outcomes):
        with col:
            st.metric(co, desc)
    
    # Footer
    st.caption("""
    **M.Tech in Information Technology | Ethical Issues Course Project | 2024**  
    *Note: All data is simulated for educational purposes. No real user data was used.*
    """)

if __name__ == "__main__":
    main()
