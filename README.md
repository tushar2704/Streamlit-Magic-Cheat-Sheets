# Streamlit Magical Cheat Sheets 




![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B.svg?style=for-the-badge&logo=Streamlit&logoColor=white)
![CSS](https://img.shields.io/badge/CSS3-1572B6.svg?style=for-the-badge&logo=CSS3&logoColor=white)
![HTML](https://img.shields.io/badge/HTML5-E34F26.svg?style=for-the-badge&logo=HTML5&logoColor=white)
![Markdown](https://img.shields.io/badge/markdown-%23000000.svg?style=for-the-badge&logo=markdown&logoColor=white)
![Visual Studio Code](https://img.shields.io/badge/Visual%20Studio%20Code-0078d7.svg?style=for-the-badge&logo=visual-studio-code&logoColor=white)
## Deployment  [![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://cheat-sheets.streamlit.app/)

`Streamlit Magic Cheat Sheets` encapsulates the Streamlit documentation version 1.28.0, providing concise summaries along with exemplar implementations of Streamlit code snippets.

**Version**`October, 2023 v1.1.1`

The development and maintenance of this application are solely undertaken by [Tushar Aggarwal](https://www.linkedin.com/in/tusharaggarwalinseec/)

![2](https://github.com/tushar2704/Streamlit-Magic-Cheat-Sheets/assets/66141195/dec7cf04-e0cc-45d7-8c8c-bec90d92a91a)

![Untitled design](https://github.com/tushar2704/Streamlit-Magic-Cheat-Sheets/assets/66141195/087cb3d6-b042-4f98-a07a-f66c1fd4c564)

## Author
- [<ins><b>©2023 Tushar Aggarwal. All rights reserved</b></ins>](https://www.tushar-aggarwal.com/)
- <b>[LinkedIn](https://www.linkedin.com/in/tusharaggarwalinseec/)</b>
- <b>[Medium](https://medium.com/@tushar_aggarwal)</b>
- <b>[Tushar-Aggarwal.com](https://www.tushar-aggarwal.com/)</b>
- <b>[X](https://twitter.com/TaggData)</b>
- <b>[Data Unboxed Newsletter](https://tadata.substack.com/)</b>
- <b>[HuggingFace](https://huggingface.co/tushar27)</b>
- <b>[DagsHub](https://dagshub.com/tushar27)</b>
- <b>[Hashnode](https://hashnode.com/@TAGG)</b>
- <b>[NovyPro](https://www.novypro.com/profile_projects/tusharagg)</b>
- <b>[New Kaggle](https://www.kaggle.com/tagg27)</b>

## Table of Contents

1. [Introduction to Streamlit](#introduction-to-streamlit)
2. [Getting Started with Streamlit](#getting-started-with-streamlit)
   - [Installation](#installation)
   - [Running a Streamlit App](#running-a-streamlit-app)
   - [Streamlit Hello World](#streamlit-hello-world)
3. [Streamlit Magic](#streamlit-magic)
   - [Streamlit Write](#streamlit-write)
   - [Streamlit Markdown](#streamlit-markdown)
   - [Streamlit Titles](#streamlit-titles)
   - [Streamlit Headers](#streamlit-headers)
   - [Streamlit Subheaders](#streamlit-subheaders)
   - [Streamlit Text](#streamlit-text)
   - [Streamlit Code](#streamlit-code)
   - [Streamlit LaTeX](#streamlit-latex)
   - [Streamlit JSON](#streamlit-json)
4. [Streamlit Widgets](#streamlit-widgets)
   - [Streamlit Button](#streamlit-button)
   - [Streamlit Checkbox](#streamlit-checkbox)
   - [Streamlit Radio](#streamlit-radio)
   - [Streamlit Selectbox](#streamlit-selectbox)
   - [Streamlit Multiselect](#streamlit-multiselect)
   - [Streamlit Slider](#streamlit-slider)
   - [Streamlit Text Input](#streamlit-text-input)
   - [Streamlit Text Area](#streamlit-text-area)
   - [Streamlit Date Input](#streamlit-date-input)
   - [Streamlit Time Input](#streamlit-time-input)
   - [Streamlit File Uploader](#streamlit-file-uploader)
   - [Streamlit Color Picker](#streamlit-color-picker)
5. [Streamlit Data Display](#streamlit-data-display)
   - [Streamlit Data Frame](#streamlit-data-frame)
   - [Streamlit Metric](#streamlit-metric)
   - [Streamlit JSON](#streamlit-json-1)
   - [Streamlit Table](#streamlit-table)
6. [Streamlit Charts](#streamlit-charts)
   - [Streamlit Line Chart](#streamlit-line-chart)
   - [Streamlit Area Chart](#streamlit-area-chart)
   - [Streamlit Bar Chart](#streamlit-bar-chart)
   - [Streamlit Pie Chart](#streamlit-pie-chart)
   - [Streamlit Altair Chart](#streamlit-altair-chart)
   - [Streamlit Plotly Chart](#streamlit-plotly-chart)
   - [Streamlit Bokeh Chart](#streamlit-bokeh-chart)
   - [Streamlit Deck GL Chart](#streamlit-deck-gl-chart)
   - [Streamlit Graphviz Chart](#streamlit-graphviz-chart)
   - [Streamlit Pyplot Chart](#streamlit-pyplot-chart)
7. [Streamlit Media](#streamlit-media)
   - [Streamlit Image](#streamlit-image)
   - [Streamlit Audio](#streamlit-audio)
   - [Streamlit Video](#streamlit-video)
8. [Streamlit Layout](#streamlit-layout)
   - [Streamlit Columns](#streamlit-columns)
   - [Streamlit Expander](#streamlit-expander)
   - [Streamlit Container](#streamlit-container)
   - [Streamlit Sidebar](#streamlit-sidebar)
9. [Streamlit State Management](#streamlit-state-management)
   - [Streamlit Session State](#streamlit-session-state)
   - [Streamlit State](#streamlit-state)
10. [Streamlit Caching](#streamlit-caching)
    - [Streamlit Memo](#streamlit-memo)
    - [Streamlit Cache Data](#streamlit-cache-data)
    - [Streamlit Cache Resource](#streamlit-cache-resource)
11. [Streamlit Theming](#streamlit-theming)
    - [Streamlit Config](#streamlit-config)
    - [Streamlit Themes](#streamlit-themes)
12. [Streamlit Deployment](#streamlit-deployment)
    - [Streamlit Sharing](#streamlit-sharing)
    - [Streamlit Cloud](#streamlit-cloud)
    - [Streamlit Heroku](#streamlit-heroku)
    - [Streamlit AWS](#streamlit-aws)
    - [Streamlit Azure](#streamlit-azure)
    - [Streamlit GCP](#streamlit-gcp)
13. [Streamlit Components](#streamlit-components)
    - [Streamlit Custom Components](#streamlit-custom-components)
    - [Streamlit Community Components](#streamlit-community-components)
14. [Streamlit Best Practices](#streamlit-best-practices)
    - [Streamlit Performance](#streamlit-performance)
    - [Streamlit Debugging](#streamlit-debugging)
    - [Streamlit Testing](#streamlit-testing)
15. [Streamlit Resources](#streamlit-resources)
    - [Streamlit Documentation](#streamlit-documentation)
    - [Streamlit Tutorials](#streamlit-tutorials)
    - [Streamlit Books](#streamlit-books)
    - [Streamlit Courses](#streamlit-courses)
    - [Streamlit Community](#streamlit-community)
16. [Streamlit Examples](#streamlit-examples)
    - [Streamlit Data Science Examples](#streamlit-data-science-examples)
    - [Streamlit Machine Learning Examples](#streamlit-machine-learning-examples)
    - [Streamlit NLP Examples](#streamlit-nlp-examples)
    - [Streamlit Computer Vision Examples](#streamlit-computer-vision-examples)
    - [Streamlit Recommender Systems Examples](#streamlit-recommender-systems-examples)
    - [Streamlit Finance Examples](#streamlit-finance-examples)
    - [Streamlit Healthcare Examples](#streamlit-healthcare-examples)
    - [Streamlit Retail Examples](#streamlit-retail-examples)
    - [Streamlit Cybersecurity Examples](#streamlit-cybersecurity-examples)
    - [Streamlit IoT Examples](#streamlit-iot-examples)
17. [Streamlit Alternatives](#streamlit-alternatives)
    - [Streamlit vs. Dash](#streamlit-vs-dash)
    - [Streamlit vs. Voila](#streamlit-vs-voila)
    - [Streamlit vs. Panel](#streamlit-vs-panel)
    - [Streamlit vs. Bokeh](#streamlit-vs-bokeh)
    - [Streamlit vs. Plotly Dash](#streamlit-vs-plotly-dash)
18. [Streamlit Integrations](#streamlit-integrations)
    - [Streamlit with Pandas](#streamlit-with-pandas)
    - [Streamlit with NumPy](#streamlit-with-numpy)
    - [Streamlit with Scikit-Learn](#streamlit-with-scikit-learn)
    - [Streamlit with TensorFlow](#streamlit-with-tensorflow)
    - [Streamlit with PyTorch](#streamlit-with-pytorch)
    - [Streamlit with Hugging Face](#streamlit-with-hugging-face)
    - [Streamlit with LangChain](#streamlit-with-langchain)
    - [Streamlit with OpenAI](#streamlit-with-openai)
19. [Streamlit Contributions](#streamlit-contributions)
    - [Streamlit GitHub](#streamlit-github)
    - [Streamlit Issues](#streamlit-issues)
    - [Streamlit Pull Requests](#streamlit-pull-requests)
    - [Streamlit Code of Conduct](#streamlit-code-of-conduct)
20. [Streamlit FAQ](#streamlit-faq)
21. [Streamlit Glossary](#streamlit-glossary)
22. [Streamlit Cheat Sheet](#streamlit-cheat-sheet)
23. [Streamlit Tips and Tricks](#streamlit-tips-and-tricks)
24. [Streamlit Roadmap](#streamlit-roadmap)
25. [Streamlit Changelog](#streamlit-changelog)
26. [Streamlit License](#streamlit-license)
27. [Streamlit Contributing](#streamlit-contributing)
28. [Streamlit Code of Conduct](#streamlit-code-of-conduct-1)
29. [Streamlit Security](#streamlit-security)
30. [Streamlit Feedback](#streamlit-feedback)

## Introduction to Streamlit

Streamlit is an open-source Python library that allows you to create interactive web applications for data science and machine learning projects with minimal effort. It provides a simple and intuitive way to build user interfaces, visualize data, and deploy models without the need for extensive web development knowledge.

Streamlit's main goal is to bridge the gap between data scientists and web development, enabling them to share their work and insights with others in a user-friendly and interactive manner. With Streamlit, you can create interactive dashboards, data explorers, and model visualizations using pure Python code.

Some key features of Streamlit include:

- **Easy to Learn**: Streamlit has a simple and intuitive API, making it easy for data scientists and developers to get started with building web applications.
- **Interactive Widgets**: Streamlit provides a wide range of interactive widgets, such as sliders, dropdowns, and text inputs, allowing users to interact with your application and explore data.
- **Data Visualization**: Streamlit supports various data visualization libraries, including Matplotlib, Plotly, Altair, and more, enabling you to create beautiful and interactive visualizations.
- **Caching and State Management**: Streamlit provides built-in caching and state management capabilities, allowing you to create stateful applications and improve performance.
- **Deployment**: Streamlit applications can be easily deployed to various platforms, including Streamlit Sharing, Heroku, AWS, and more.

Streamlit has gained significant popularity in the data science and machine learning communities due to its simplicity and ease of use. It allows data scientists to focus on their core tasks, such as data analysis and model development, while providing a seamless way to share their work with others.

## Getting Started with Streamlit

### Installation

To get started with Streamlit, you need to have Python installed on your system. You can install Streamlit using pip, the Python package installer:

```bash
pip install streamlit
```

Alternatively, you can install Streamlit in a virtual environment to keep your project dependencies isolated:

```bash
python -m venv myenv
source myenv/bin/activate  # On Windows, use `myenv\Scripts\activate`
pip install streamlit
```

### Running a Streamlit App

To run a Streamlit app, create a Python file (e.g., `app.py`) and add your Streamlit code. Then, run the following command in your terminal or command prompt:

```bash
streamlit run app.py
```

This will start the Streamlit server and open your app in a new browser window.

### Streamlit Hello World

Here's a simple "Hello, World!" example to get you started with Streamlit:

```python
import streamlit as st

st.title("Hello, World!")
st.write("This is a Streamlit app.")
```

When you run this code with `streamlit run app.py`, you should see a web page with the title "Hello, World!" and the text "This is a Streamlit app."

## Streamlit Magic

Streamlit provides a variety of functions and widgets to create interactive web applications. Here are some of the most commonly used Streamlit features:

### Streamlit Write

The `st.write()` function is used to display text, data, and other objects in your Streamlit app. It can handle various data types, including strings, numbers, Pandas DataFrames, and more.

```python
import streamlit as st

st.write("Hello, World!")
st.write(42)
st.write([1][2][3])
```

### Streamlit Markdown

Streamlit supports Markdown formatting, allowing you to style your text with headings, lists, links, and more. You can use the `st.markdown()` function to render Markdown content.

```python
import streamlit as st

st.markdown("# This is a Heading")
st.markdown("- This is a bullet point")
st.markdown("[This is a link](https://streamlit.io/)")
```

### Streamlit Titles

You can add titles to your Streamlit app using the `st.title()` function.

```python
import streamlit as st

st.title("My Streamlit App")
```

### Streamlit Headers

Streamlit provides functions to add headers of different levels to your app.

```python
import streamlit as st

st.header("This is a Header")
st.subheader("This is a Subheader")
```

### Streamlit Text
```python
import streamlit as st

st.text("This is some text.")
```

### Streamlit Code

Streamlit allows you to display code snippets in your app using the `st.code()` function.

```python
import streamlit as st

code = """
def hello():
    print("Hello, World!")
"""

st.code(code, language="python")
```

### Streamlit LaTeX

Streamlit supports rendering LaTeX equations using the `st.latex()` function.

```python
import streamlit as st

st.latex(r'''
    a + ar + a r^2 + a r^3 + \cdots + a r^n =
    \sum_{k=0}^n ar^k =
    a \left(\frac{1-r^{n+1}}{1-r}\right)
''')
```

### Streamlit JSON

You can display JSON data in your Streamlit app using the `st.json()` function.

```python
import streamlit as st

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

st.json(data)
```

## Streamlit Widgets

Streamlit provides a variety of interactive widgets that allow users to input data and control the behavior of your app.

### Streamlit Button

The `st.button()` function creates a button that can be clicked to trigger an action.

```python
import streamlit as st

if st.button("Click me"):
    st.write("Button clicked!")
```

### Streamlit Checkbox

The `st.checkbox()` function creates a checkbox that can be used to toggle a boolean value.

```python
import streamlit as st

agree = st.checkbox("I agree to the terms and conditions")

if agree:
    st.write("Thank you for agreeing!")
```

### Streamlit Radio

The `st.radio()` function creates a group of radio buttons, allowing the user to select one option from a list.

```python
import streamlit as st

option = st.radio(
    "Select an option",
    ("Option 1", "Option 2", "Option 3")
)

st.write(f"You selected: {option}")
```

### Streamlit Selectbox

The `st.selectbox()` function creates a dropdown menu, allowing the user to select one option from a list.

```python
import streamlit as st

option = st.selectbox(
    "Select an option",
    ("Option 1", "Option 2", "Option 3")
)

st.write(f"You selected: {option}")
```

### Streamlit Multiselect

The `st.multiselect()` function creates a multi-select widget, allowing the user to select multiple options from a list.

```python
import streamlit as st

options = st.multiselect(
    "Select options",
    ("Option 1", "Option 2", "Option 3")
)

st.write(f"You selected: {', '.join(options)}")
```

### Streamlit Slider

The `st.slider()` function creates a slider widget, allowing the user to select a value within a specified range.

```python
import streamlit as st

value = st.slider("Select a value", 0, 100, 50)

st.write(f"You selected: {value}")
```

### Streamlit Text Input

The `st.text_input()` function creates a text input field, allowing the user to enter text.

```python
import streamlit as st

name = st.text_input("Enter your name", "Type here...")

st.write(f"Hello, {name}!")
```

### Streamlit Text Area

The `st.text_area()` function creates a multi-line text input area, allowing the user to enter longer text.

```python
import streamlit as st

message = st.text_area("Enter a message")

st.write(f"You entered: {message}")
```

### Streamlit Date Input

The `st.date_input()` function creates a date input widget, allowing the user to select a date.

```python
import streamlit as st

date = st.date_input("Select a date")

st.write(f"You selected: {date}")
```

### Streamlit Time Input

The `st.time_input()` function creates a time input widget, allowing the user to select a time.

```python
import streamlit as st

time = st.time_input("Select a time")

st.write(f"You selected: {time}")
```

### Streamlit File Uploader

The `st.file_uploader()` function creates a file uploader widget, allowing the user to upload files to your app.

```python
import streamlit as st

file = st.file_uploader("Upload a file")

if file is not None:
    st.write(f"File name: {file.name}")
    st.write(f"File type: {file.type}")
    st.write(f"File size: {file.size} bytes")
```

### Streamlit Color Picker

The `st.color_picker()` function creates a color picker widget, allowing the user to select a color.

```python
import streamlit as st

color = st.color_picker("Select a color")

st.write(f"You selected: {color}")
```

## Streamlit Data Display

Streamlit provides several functions to display data in your app, including DataFrames, metrics, JSON, and tables.

### Streamlit Data Frame

The `st.dataframe()` function displays a Pandas DataFrame in your Streamlit app.

```python
import streamlit as st
import pandas as pd

data = {
    "name": ["John", "Jane", "Bob"],
    "age": [25, 30, 35]
}

df = pd.DataFrame(data)

st.dataframe(df)
```

### Streamlit Metric

The `st.metric()` function displays a metric value with an optional label and optional delta value.

```python
import streamlit as st

st.metric("Temperature", "25°C", "1.2°C")
```

### Streamlit JSON

The `st.json()` function displays JSON data in your Streamlit app.

```python
import streamlit as st

data = {
    "name": "John Doe",
    "age": 30,
    "city": "New York"
}

st.json(data)
```

### Streamlit Table

The `st.table()` function displays a table in your Streamlit app.

```python
import streamlit as st
import pandas as pd

data = {
    "name": ["John", "Jane", "Bob"],
    "age": [25, 30, 35]
}

df = pd.DataFrame(data)

st.table(df)
```

## Streamlit Charts

Streamlit supports various charting libraries, allowing you to create interactive visualizations in your app.

### Streamlit Line Chart

The `st.line_chart()` function creates a line chart using Matplotlib or Altair.

```python
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.line_chart(chart_data)
```

### Streamlit Area Chart

The `st.area_chart()` function creates an area chart using Matplotlib or Altair.

```python
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(20, 3),
    columns=["a", "b", "c"]
)

st.area_chart(chart_data)
```

### Streamlit Bar Chart

The `st.bar_chart()` function creates a bar chart using Matplotlib or Altair.

```python
import streamlit as st
import pandas as pd
import numpy as np

chart_data = pd.DataFrame(
    np.random.randn(5, 3), columns=["a", "b", "c"]
)

st.bar_chart(chart_data)
```

### Streamlit Pie Chart

The `st.pie_chart()` function creates a pie chart using Matplotlib.

```python
import streamlit as st
import pandas as pd

data = pd.DataFrame({
    "category": ["A", "B", "C"],
    "values": [30, 40, 30]
})

st.pie_chart(data["values"])
```

### Streamlit Altair Chart

The `st.altair_chart()` function creates an Altair chart in your Streamlit app.

```python
import streamlit as st
import altair as alt
import pandas as pd

data = pd.DataFrame({
    "a": [1, 2, 3, 4, 5],
    "b": [1, 3, 2, 5, 4]
})

chart = alt.Chart(data).mark_line().encode(
    x="a",
    y="b"
)

st.altair_chart(chart, use_container_width=True)
```

### Streamlit Plotly Chart

The `st.plotly_chart()` function creates a Plotly chart in your Streamlit app.

```python
import streamlit as st
import plotly.express as px

df = px.data.iris()
fig = px.scatter(df, x="sepal_width", y="sepal_length", color="species")

st.plotly_chart(fig)
```

### Streamlit Bokeh Chart

The `st.bokeh_chart()` function creates a Bokeh chart in your Streamlit app.

```python
import streamlit as st
from bokeh.plotting import figure

x = [1, 2, 3, 4, 5]
y = [6, 7, 2, 4, 5]

p = figure(
    title="Simple line example",
    x_axis_label="x",
    y_axis_label="y"
)

p.line(x, y, line_width=2)

st.bokeh_chart(p, use_container_width=True)
```

### Streamlit Deck GL Chart

The `st.deck_gl_chart()` function creates a Deck.gl chart in your Streamlit app.

```python
import streamlit as st
import pandas as pd
import pydeck as pdk

data = pd.DataFrame({
    "lat": [37.76, 37.77, 37.78],
    "lon": [-122.4, -122.41, -122.42]
})

layer = pdk.Layer(
    "HexagonLayer",
    data=data,
    get_position=["lon", "lat"],
    auto_highlight=True,
    elevation_scale=50,
    pickable=True,
    elevation_range=[0, 3000],
    extruded=True,
)

st.deck_gl_chart(
    viewport={
        "latitude": 37.76,
        "longitude": -122.4,
        "zoom": 11,
        "pitch": 50,
    },
    layers=[layer],
)
```

### Streamlit Graphviz Chart

The `st.graphviz_chart()` function creates a Graphviz chart in your Streamlit app.

```python
import streamlit as st
import graphviz as graphviz

graph = graphviz.Digraph()
graph.edge("run", "intr")
graph.edge("intr", "kernel")
graph.edge("kernel", "zombie")
graph.edge("kernel", "sleep")
graph.edge("kernel", "runnable")
graph.edge("sleep", "runnable")
graph.edge("runnable", "run")
graph.edge("runnable", "kernel")

st.graphviz_chart(graph)
```

### Streamlit Pyplot Chart

The `st.pyplot()` function creates a Matplotlib chart in your Streamlit app.

```python
import streamlit as st
import matplotlib.pyplot as plt
import numpy as np

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
```

## Streamlit Media

Streamlit allows you to display various media types in your app, including images, audio, and video.

### Streamlit Image

The `st.image()` function displays an image in your Streamlit app.

```python
import streamlit as st

st.image("https://example.com/image.jpg")
```

### Streamlit Audio

The `st.audio()` function plays an audio file in your Streamlit app.

```python
import streamlit as st

st.audio("https://example.com/audio.mp3")
```

### Streamlit Video

The `st.video()` function plays a video file in your Streamlit app.

```python
import streamlit as st

st.video("https://example.com/video.mp4")
```

## Streamlit Layout

Streamlit provides several layout options to organize and structure your app's content.

### Streamlit Columns

The `st.columns()` function creates multiple columns in your Streamlit app.

```python
import streamlit as st

col1, col2 = st.columns(2)

with col1:
    st.write("Column 1")

with col2:
    st.write("Column 2")
```

### Streamlit Expander

The `st.expander()` function creates an expandable section in your Streamlit app.

```python
import streamlit as st

with st.expander("Click to expand"):
    st.write("This content is hidden by default.")
```

### Streamlit Container

The `st.container()` function creates a container in your Streamlit app, allowing you to group elements together.

```python
import streamlit as st

with st.container():
    st.write("This content is inside a container.")
```

### Streamlit Sidebar

The `st.sidebar` object allows you to create a sidebar in your Streamlit app.

```python
import streamlit as st

with st.sidebar:
    st.write("This content is in the sidebar.")
```

## Streamlit State Management

Streamlit provides state management capabilities to handle user interactions and maintain application state.

### Streamlit Session State

The `st.session_state` object allows you to store and retrieve data across multiple sessions.

```python
import streamlit as st

if "count" not in st.session_state:
    st.session_state.count = 0

st.button("Increment", on_click=increment_count)

def increment_count():
    st.session_state.count += 1
    st.write(f"Count: {st.session_state.count}")
```

### Streamlit State

The `st.state` object allows you to store and retrieve data within the same session.

```python
import streamlit as st

if "count" not in st.state:
    st.state.count = 0

st.button("Increment", on_click=increment_count)

def increment_count():
    st.state.count += 1
    st.write(f"Count: {st.state.count}")
```

## Streamlit Caching

Streamlit provides caching mechanisms to improve performance and reduce computation time.

### Streamlit Memo

The `@st.memo` decorator caches the result of a function based on its input parameters.

```python
import streamlit as st

@st.memo
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

n = st.number_input("Enter a number", value=10)
result = fibonacci(n)
st.write(f"The {n}th Fibonacci number is {result}")
```

### Streamlit Cache Data

The `@st.cache_data` decorator caches the result of a function based on its input parameters and persists the cache across sessions.

```python
import streamlit as st
import pandas as pd

@st.cache_data
def load_data(path):
    return pd.read_csv(path)

path = st.text_input("Enter the file path")
data = load_data(path)
st.write(data)
```

### Streamlit Cache Resource

The `@st.cache_resource` decorator caches the result of a function and persists the cache across sessions, even if the function has no input parameters.

```python
import streamlit as st
import
