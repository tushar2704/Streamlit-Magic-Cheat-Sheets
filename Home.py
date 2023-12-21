##© 2023 Tushar Aggarwal. All rights reserved.
##Streamlit Magic Cheat Sheets
#######################################################################################################
# Full length is above 10000 lines and is avalibale on requests only. Follow me, I will realising that in my upcoming book too!
#######################################################################################################
#Importind required libraries
#######################################################################################################
import streamlit as st
from pathlib import Path
import base64
import sys
from pathlib import Path
script_dir = Path(__file__).resolve().parent
project_root = script_dir.parent
sys.path.append(str(project_root))
import warnings
warnings.filterwarnings("ignore")
import os
#######################################################################################################
#Importing from SRC
#######################################################################################################
from src.Streamlit_Magic_Cheat_Sheets.components.header import *
from src.Streamlit_Magic_Cheat_Sheets.components.body import *
from src.Streamlit_Magic_Cheat_Sheets.components.navigation import *
from src.Streamlit_Magic_Cheat_Sheets.components.siderbar import *
from src.Streamlit_Magic_Cheat_Sheets.components.metrics import *
from src.Streamlit_Magic_Cheat_Sheets.components.charts import *
from src.Streamlit_Magic_Cheat_Sheets.components.test import *
#######################################################################################################
#Header of Streamlit Magic Cheat Sheets by github.com/tushar2704
#######################################################################################################
main_header()
#######################################################################################################
#Page Config of Streamlit Magic Cheat Sheets by github.com/tushar2704
#######################################################################################################
custom_style()
#######################################################################################################
#Body of Streamlit Magic Cheat Sheets by github.com/tushar2704
#######################################################################################################
left_main_panel()







footer()
#######################################################################################################
#End of Streamlit Magic Cheat Sheets by github.com/tushar2704
#######################################################################################################
