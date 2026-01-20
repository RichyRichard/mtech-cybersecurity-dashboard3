"""
Enhanced Social Media Privacy & Security Analytics Dashboard
Fixed for Streamlit Cloud Deployment
M.Tech Mini Project - Module 5: Visualization - Highcharts
"""

import pandas as pd
import numpy as np
import json
import streamlit as st
from datetime import datetime
import streamlit.components.v1 as components
import random
import warnings

warnings.filterwarnings("ignore")

# Page configuration
st.set_page_config(
    page_title="Advanced Highcharts Visualization Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)


class HighchartsGenerator:
    """Class to generate various Highcharts visualizations"""

    def create_network_graph(self, nodes_data, links_data):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/modules/networkgraph.js"></script>
        </head>
        <body>
        <div id="container" style="height:600px;"></div>
        <script>
        Highcharts.chart('container', {{
            chart: {{ type: 'networkgraph', height: 550 }},
            title: {{ text: 'Social Network Analysis - Privacy Risk Propagation' }},
            plotOptions: {{
                networkgraph: {{
                    keys: ['from', 'to'],
                    layoutAlgorithm: {{ enableSimulation: true }}
                }}
            }},
            series: [{{
                data: {json.dumps(links_data)},
                nodes: {json.dumps(nodes_data)},
                dataLabels: {{ enabled: true }}
            }}]
        }});
        </script>
        </body>
        </html>
        """
        return html

    def create_sankey_diagram(self, nodes, links):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/modules/sankey.js"></script>
        </head>
        <body>
        <div id="sankey" style="height:600px;"></div>
        <script>
        Highcharts.chart('sankey', {{
            series: [{{
                type: 'sankey',
                keys: ['from', 'to', 'weight'],
                data: {json.dumps(links)},
                nodes: {json.dumps(nodes)}
            }}],
            title: {{ text: 'Data Flow in Social Media Ecosystem' }}
        }});
        </script>
        </body>
        </html>
        """
        return html

    def create_heatmap_chart(self, x, y, data):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/modules/heatmap.js"></script>
        </head>
        <body>
        <div id="heatmap" style="height:500px;"></div>
        <script>
        Highcharts.chart('heatmap', {{
            chart: {{ type: 'heatmap' }},
            xAxis: {{ categories: {json.dumps(x)} }},
            yAxis: {{ categories: {json.dumps(y)}, reversed: true }},
            colorAxis: {{ min: 0, max: 100 }},
            series: [{{
                data: {json.dumps(data)},
                borderWidth: 1
            }}],
            title: {{ text: 'Location Privacy Risk Heatmap' }}
        }});
        </script>
        </body>
        </html>
        """
        return html

    def create_bubble_chart(self, data):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
        </head>
        <body>
        <div id="bubble" style="height:500px;"></div>
        <script>
        Highcharts.chart('bubble', {{
            chart: {{ type: 'bubble' }},
            series: [{{ data: {json.dumps(data)} }}],
            title: {{ text: 'Social Media Platform Comparison' }}
        }});
        </script>
        </body>
        </html>
        """
        return html

    def create_timeline_chart(self, series):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
        </head>
        <body>
        <div id="timeline" style="height:500px;"></div>
        <script>
        Highcharts.chart('timeline', {{
            xAxis: {{ categories: ['Jan','Feb','Mar','Apr','May','Jun','Jul','Aug','Sep','Oct','Nov','Dec'] }},
            series: {json.dumps(series)},
            title: {{ text: 'Security Incidents Timeline' }}
        }});
        </script>
        </body>
        </html>
        """
        return html

    def create_gauge_chart(self, value):
        html = f"""
        <!DOCTYPE html>
        <html>
        <head>
            <script src="https://code.highcharts.com/highcharts.js"></script>
            <script src="https://code.highcharts.com/highcharts-more.js"></script>
            <script src="https://code.highcharts.com/modules/solid-gauge.js"></script>
        </head>
        <body>
        <div id="gauge" style="height:400px;"></div>
        <script>
        Highcharts.chart('gauge', {{
            chart: {{ type: 'solidgauge' }},
            yAxis: {{ min: 0, max: 100 }},
            series: [{{ data: [{value}] }}],
            title: {{ text: 'Overall Privacy Risk Score' }}
        }});
        </script>
        </body>
        </html>
        """
        return html


class DataSimulator:
    @staticmethod
    def generate_network_data():
        nodes = [{'id': f'u{i}', 'name': f'User_{i}'} for i in range(15)]
        links = [[f'u{random.randint(0,14)}', f'u{random.randint(0,14)}'] for _ in range(25)]
        return nodes, links

    @staticmethod
    def generate_sankey_data():
        nodes = [{'id': 'User'}, {'id': 'Platform'}, {'id': 'Advertisers'}]
        links = [['User', 'Platform', 50], ['Platform', 'Advertisers', 40]]
        return nodes, links

    @staticmethod
    def generate_heatmap_data():
        days = ['Mon','Tue','Wed','Thu','Fri','Sat','Sun']
        hours = [f'{h}:00' for h in range(8,22,2)]
        data = [[i, j, random.randint(20,90)] for i in range(len(days)) for j in range(len(hours))]
        return days, hours, data

    @staticmethod
    def generate_bubble_data():
        return [
            {'x': 2900, 'y': 45, 'z': 80, 'name': 'Facebook'},
            {'x': 1500, 'y': 40, 'z': 90, 'name': 'TikTok'}
        ]

    @staticmethod
    def generate_timeline_data():
        return [
            {'name': 'Phishing', 'data': [random.randint(30,80) for _ in range(12)]},
            {'name': 'Breaches', 'data': [random.randint(10,40) for _ in range(12)]}
        ]


class EnhancedPrivacyDashboard:
    def __init__(self):
        self.hc = HighchartsGenerator()
        self.data = DataSimulator()

    def run(self):
        st.title("📊 Social Media Privacy & Security Dashboard")
        selected = st.sidebar.multiselect(
            "Select Charts",
            ["Network", "Sankey", "Heatmap", "Bubble", "Timeline", "Gauge"],
            default=["Network", "Sankey", "Heatmap"]
        )

        if "Network" in selected:
            nodes, links = self.data.generate_network_data()
            components.html(self.hc.create_network_graph(nodes, links), height=600)

        if "Sankey" in selected:
            nodes, links = self.data.generate_sankey_data()
            components.html(self.hc.create_sankey_diagram(nodes, links), height=600)

        if "Heatmap" in selected:
            d, h, data = self.data.generate_heatmap_data()
            components.html(self.hc.create_heatmap_chart(d, h, data), height=500)

        if "Bubble" in selected:
            components.html(self.hc.create_bubble_chart(self.data.generate_bubble_data()), height=500)

        if "Timeline" in selected:
            components.html(self.hc.create_timeline_chart(self.data.generate_timeline_data()), height=500)

        if "Gauge" in selected:
            components.html(self.hc.create_gauge_chart(random.randint(35,75)), height=400)


if __name__ == "__main__":
    EnhancedPrivacyDashboard().run()
