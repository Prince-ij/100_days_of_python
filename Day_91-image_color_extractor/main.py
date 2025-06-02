from flask import Flask, render_template, request, jsonify
import json
from PIL import Image
import extcolors
import plotly.express as px
import plotly
import pandas as pd
from webcolors import rgb_to_hex


app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/get-image', methods=['POST', 'GET'])
def get_and_process_image():
    if request.method == 'POST':
        file = request.files.get('image')


        # Resize Image
        pic = Image.open(file)
        pic = pic.resize((300, 300))

        # Extract Colors

        colors = extcolors.extract_from_image(pic)
        colors_rgb = [color[0] for color in colors[0]]
        hex_colors = [rgb_to_hex(color) for color in colors_rgb]

        # plotting colors on sunburst

        df = pd.DataFrame({
            'parent': [''] * len(hex_colors),
            'labels': hex_colors,
            'color': hex_colors
        })

        fig = px.sunburst(
            df,
            names='labels',
            parents='parent',
            color='color',
            color_discrete_map={c: c for c in hex_colors}
        )

        graph_html = fig.to_html(full_html=False)


    return render_template('colors.html', graph_html=graph_html)
