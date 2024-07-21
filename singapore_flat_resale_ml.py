import numpy as np
import pickle
import streamlit as st
import time


# Streamlit page custom design

def streamlit_config():

    # page configuration
    st.set_page_config(page_title='Singapore Flat Resale Price Predicition')

    # page header transparent color
    page_background_color = """
    <style>

    [data-testid="stHeader"] 
    {
    background: rgba(0,0,0,0);
    }

    </style>
    """
    st.markdown(page_background_color, unsafe_allow_html=True)

    # title and position
    st.markdown(f'<h2 style="text-align: center;">SINGAPORE FLAT RESALE PREDICTION</h2>',
                unsafe_allow_html=True)



# custom style for submit button - color and width

def style_submit_button():

    st.markdown("""
                    <style>
                    div.stButton > button:first-child {
                                                        background-color: #367F89;
                                                        color: white;
                                                        width: 30%}
                    </style>
                """, unsafe_allow_html=True)



# custom style for prediction result text - color and position

def style_prediction():

    st.markdown(
            """
            <style>
            .center-text {
                text-align: center;
                color: #20CA0C
            }
            </style>
            """,
            unsafe_allow_html=True
        )



# user input options

class options:


    town_values = ['ANG MO KIO', 'BEDOK', 'BISHAN', 'BUKIT BATOK', 'BUKIT MERAH',
       'BUKIT TIMAH', 'CENTRAL AREA', 'CHOA CHU KANG', 'CLEMENTI',
       'GEYLANG', 'HOUGANG', 'JURONG EAST', 'JURONG WEST',
       'KALLANG/WHAMPOA', 'MARINE PARADE', 'QUEENSTOWN', 'SENGKANG',
       'SERANGOON', 'TAMPINES', 'TOA PAYOH', 'WOODLANDS', 'YISHUN',
       'LIM CHU KANG', 'SEMBAWANG', 'BUKIT PANJANG', 'PASIR RIS',
       'PUNGGOL']
    town_dict = {'ANG MO KIO':0, 'BEDOK':1, 'BISHAN':2, 'BUKIT BATOK':3, 'BUKIT MERAH':4,
       'BUKIT TIMAH':5, 'CENTRAL AREA':6, 'CHOA CHU KANG':7, 'CLEMENTI':8,
       'GEYLANG':9, 'HOUGANG':10, 'JURONG EAST':11, 'JURONG WEST':12,
       'KALLANG/WHAMPOA':13, 'MARINE PARADE':14, 'QUEENSTOWN':15, 'SENGKANG':16,
       'SERANGOON':17, 'TAMPINES':18, 'TOA PAYOH':19, 'WOODLANDS':20, 'YISHUN':21,
       'LIM CHU KANG':22, 'SEMBAWANG':23, 'BUKIT PANJANG':24, 'PASIR RIS':25,
       'PUNGGOL':26}

    storey_range_values = ['10 TO 12', '04 TO 06', '07 TO 09', '01 TO 03', '13 TO 15',
       '19 TO 21', '16 TO 18', '25 TO 27', '22 TO 24', '28 TO 30',
       '31 TO 33', '40 TO 42', '37 TO 39', '34 TO 36', '06 TO 10',
       '01 TO 05', '11 TO 15', '16 TO 20', '21 TO 25', '26 TO 30',
       '36 TO 40', '31 TO 35', '46 TO 48', '43 TO 45', '49 TO 51']
    storey_range_dict = {'10 TO 12':0, '04 TO 06':1, '07 TO 09':2, '01 TO 03':3, '13 TO 15':4,
       '19 TO 21':5, '16 TO 18':6, '25 TO 27':7, '22 TO 24':8, '28 TO 30':9,
       '31 TO 33':10, '40 TO 42':11, '37 TO 39':12, '34 TO 36':13, '06 TO 10':14,
       '01 TO 05':15, '11 TO 15':16, '16 TO 20':17, '21 TO 25':18, '26 TO 30':19,
       '36 TO 40':20, '31 TO 35':21, '46 TO 48':22, '43 TO 45':23, '49 TO 51':24}
    
    flat_model_values = ['IMPROVED', 'NEW GENERATION', 'MODEL A', 'STANDARD', 'SIMPLIFIED',
       'MODEL A-MAISONETTE', 'APARTMENT', 'MAISONETTE', 'TERRACE',
       '2-ROOM', 'IMPROVED-MAISONETTE', 'MULTI GENERATION',
       'PREMIUM APARTMENT', 'ADJOINED FLAT', 'PREMIUM MAISONETTE',
       'MODEL A2', 'DBSS', 'TYPE S1', 'TYPE S2', 'PREMIUM APARTMENT LOFT',
       '3GEN']
    flat_model_dict = {'IMPROVED':0 , 'NEW GENERATION':1, 'MODEL A':2, 'STANDARD':3, 'SIMPLIFIED':4,
       'MODEL A-MAISONETTE':5, 'APARTMENT':6, 'MAISONETTE':7, 'TERRACE':8,
       '2-ROOM':9, 'IMPROVED-MAISONETTE':10, 'MULTI GENERATION':11,
       'PREMIUM APARTMENT':12, 'ADJOINED FLAT':13, 'PREMIUM MAISONETTE':14,
       'MODEL A2':15, 'DBSS':16, 'TYPE S1':17, 'TYPE S2':18, 'PREMIUM APARTMENT LOFT':19,
       '3GEN':20}
    
    
# Get input data from users both regression and classification methods

class prediction:

    def regression():

        # get input from users
        with st.form('Regression'):

                town = st.selectbox(label='Town', options=options.town_values)

                storey_range = st.selectbox(label='Storey Range', options=options.storey_range_values)

                floor_area_sqm = st.number_input(label='Floor area (Sq m)', min_value=1.0, max_value=10000.0, value=50.0)

                flat_model = st.selectbox(label='Flat Model', options=options.flat_model_values)

                lease_commence_date = st.number_input(label='Lease Commence Year', min_value=1950, max_value=2024, value = 1990 )

                remaining_lease_1 = (lease_commence_date + 99) - 2024

                remaining_lease = st.number_input("Remaining Lease", value=remaining_lease_1, step=1, disabled=True)

                Year = st.number_input("Year", min_value=1950, max_value=2100, value=2024, step=1)

                Month = st.number_input("Month", min_value=1, max_value=12, value=1, step=1)

                
                st.write('')
                st.write('')
                button = st.form_submit_button(label='SUBMIT')
                style_submit_button()



        # user entered the all input values and click the button
        if button:
            
            # load the regression pickle model
            with open(r'C:\Users\91916\GUVI_DS\singapore_resale_price_regression_model.pkl', 'rb') as g:
                model_1 = pickle.load(g)
            
            # make array for all user input values in required order for model prediction
            user_data = np.array([[options.town_dict[town],
                                   options.storey_range_dict[storey_range],
                                   floor_area_sqm,
                                   options.flat_model_dict[flat_model],
                                   lease_commence_date,
                                   remaining_lease,
                                   Year,
                                   Month]])
            
            # model predict the selling price based on user input
            y_pred = model_1.predict(user_data)

            return y_pred

streamlit_config()
        
header = st.subheader('Predict Flat Resale Price')
        
y_pred = prediction.regression()

if y_pred:
    # apply custom css style for prediction text
    progress_text = "Prediction in progress. Please wait."
    my_bar = st.progress(0, text=progress_text)

    for percent_complete in range(100):
        time.sleep(0.01)
        my_bar.progress(percent_complete + 1, text=progress_text)
    time.sleep(1)
    my_bar.empty()
    style_prediction()

    for val in y_pred:
        st.markdown(f"<h4>Predicted Resale Price = {val:.0f}<h4>", unsafe_allow_html=True)



