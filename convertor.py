# import streamlit as st

# st.markdown(
#     """
#     <style>
#     body {
#         background-color: #e1e12f;
#         color: white;
#     }
#     .stApp {
#         background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
#         padding: 30px;
#         border-radius: 15px;
#         box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
#     }
#     h1 {
#         text-align: center;
#         font-size: 36px;
#         color: white;
#     }
#     .stButton > button {
#         background: linear-gradient(45deg, #0b5394, #351c75);
#         color: white;
#         font-size: 18px;
#         padding: 10px 20px;
#         border-radius: 10px;
#         transition: 0.3s;
#         box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
#     }
#     .stButton > button:hover {
#         transform: scale(1.05);
#         background: linear-gradient(45deg, #92fe9d, #00c9ff);
#         color: black;
#     }
#     .result-box {
#         font-size: 20px;
#         font-weight: bold;
#         text-align: center;
#         background: rgba(255, 255, 255, 0.1);
#         padding: 25px;
#         border-radius: 10px;
#         margin-top: 20px;
#         box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
#     }
#     .footer {
#         text-align: center;
#         margin-top: 50px;
#         font-size: 14px;
#         color: black;
#     }
#     </style>
#     """,
#     unsafe_allow_html=True
# )


# #title and description

# st.markdown("<h1> Unit Convertor Using Python And Stresmlit </h1>", unsafe_allow_html=True)
# st.write("Easily Convert Between Different Units Of Length , Weight , And Temperature")

# #sidebar menu 

# conversion_type = st.sidebar.selectionbox("Choose Conversion Type", ["Length", "Weight", "Temperature"])
# value = st.number_input("Enter Value", value=0.0, min_value=0.0, step=0.1)


import streamlit as st

# Custom Styling
st.markdown(
    """
    <style>
    body {
        background-color: #e1e12f;
        color: white;
    }
    .stApp {
        background: linear-gradient(135deg, #bcbcbc, #cfe2f3);
        padding: 30px;
        border-radius: 15px;
        box-shadow: 0px 10px 30px rgba(0, 0, 0, 0.3);
    }
    h1 {
        text-align: center;
        font-size: 36px;
        color: white;
    }
    .stButton > button {
        background: linear-gradient(45deg, #0b5394, #351c75);
        color: white;
        font-size: 18px;
        padding: 10px 20px;
        border-radius: 10px;
        transition: 0.3s;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.4);
    }
    .stButton > button:hover {
        transform: scale(1.05);
        background: linear-gradient(45deg, #92fe9d, #00c9ff);
        color: black;
    }
    .result-box {
        font-size: 20px;
        font-weight: bold;
        text-align: center;
        background: rgba(255, 255, 255, 0.1);
        padding: 25px;
        border-radius: 10px;
        margin-top: 20px;
        box-shadow: 0px 5px 15px rgba(0, 201, 255, 0.3);
    }
    .footer {
        text-align: center;
        margin-top: 50px;
        font-size: 14px;
        color: black;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# App Title
st.title("Unit Converter")

# Unit Categories
unit_categories = {
    "Length": {"Meter": 1, "Kilometer": 0.001, "Centimeter": 100, "Millimeter": 1000, "Inch": 39.3701, "Feet": 3.28084},
    "Weight": {"Kilogram": 1, "Gram": 1000, "Pound": 2.20462, "Ounce": 35.274},
    "Temperature": {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}
}

# User Input - Select Category
category = st.selectbox("Select Category", list(unit_categories.keys()))

# Select Units for Conversion
from_unit = st.selectbox("From", list(unit_categories[category].keys()))
to_unit = st.selectbox("To", list(unit_categories[category].keys()))

# Input Field
value = st.number_input("Enter Value", min_value=0.0, step=0.01, format="%.2f")

# Conversion Function
def convert(value, from_unit, to_unit, category):
    if category == "Temperature":
        if from_unit == "Celsius" and to_unit == "Fahrenheit":
            return (value * 9/5) + 32
        elif from_unit == "Celsius" and to_unit == "Kelvin":
            return value + 273.15
        elif from_unit == "Fahrenheit" and to_unit == "Celsius":
            return (value - 32) * 5/9
        elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
            return (value - 32) * 5/9 + 273.15
        elif from_unit == "Kelvin" and to_unit == "Celsius":
            return value - 273.15
        elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
            return (value - 273.15) * 9/5 + 32
        else:
            return value  # Same unit
    else:
        return value * (unit_categories[category][to_unit] / unit_categories[category][from_unit])

# Convert Button
if st.button("Convert"):
    result = convert(value, from_unit, to_unit, category)
    st.success(f"Converted Value: {result:.2f} {to_unit}")
