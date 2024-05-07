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
