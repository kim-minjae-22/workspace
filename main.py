import streamlit as st
import pandas as pd
import numpy as np

st.title('Uber pickups in NYC')

import streamlit as st
import pandas as pd

st.write("Here's our first attempt at using data to create a table:")
st.write(pd.DataFrame({
    'first column': [1, 2, 3, 4],
    'second column': [10, 20, 30, 40]
}))

# 라인차트 그리기
import streamlit as st
import numpy as np
import pandas as pd

chart_data = pd.DataFrame(
     np.random.randn(20, 3),
     columns=['a', 'b', 'c'])

st.line_chart(chart_data)

# 지도그리기
import streamlit as st
import numpy as np
import pandas as pd

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [50, 50] + [37.514575, 127.0495556],
    columns=['lat', 'lon'])

st.map(map_data)

# 위젯 슬라이드바
import streamlit as st
x = st.slider('x')  # 👈 this is a widget
st.write(x, 'squared is', x * x)

# 체크박스을 사용하여 데이터 표시/숨기기
import streamlit as st
import numpy as np
import pandas as pd

if st.checkbox('Show dataframe'):
    chart_data = pd.DataFrame(
       np.random.randn(20, 3),
       columns=['a', 'b', 'c'])

    chart_data
    
# option을 위해 select box 사용
import streamlit as st
import pandas as pd

option = st.selectbox(
    'Which number do you like best?',
     [1, 2, 3, 4, 5])

'You selected: ', option

# Layout
import streamlit as st

# Add a selectbox to the sidebar:
add_selectbox = st.sidebar.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Home phone', 'Mobile phone')
)

# Add a slider to the sidebar:
add_slider = st.sidebar.slider(
    'Select a range of values',
    0.0, 100.0, (25.0, 75.0)
)

# `st.columns`를 사용하면 위젯을 나란히 배치할 수 있음.
import streamlit as st

left_column, right_column = st.columns(2)
# You can use a column just like st.sidebar:
left_column.button('Press me!')

# Or even better, call Streamlit functions inside a "with" block:
with right_column:
    chosen = st.radio(
        'Sorting hat',
        ("Gryffindor", "Ravenclaw", "Hufflepuff", "Slytherin"))
    st.write(f"You are in {chosen} house!")


# def some_func(input):
#     with open("./xgboost_feature3.pkl",'rb') as f :
#         loaded_model = pickle.load(f)
        
#     result = loaded_model.predict(input)
    



# Store the initial value of widgets in session state
if "visibility" not in st.session_state:
    st.session_state.visibility = "visible"
    st.session_state.disabled = False

col1,col2 = st.columns(2)

with col1:
    text_input = st.text_input(
        "거실 크기를 입력해주세요! 👇",
        # label_visibility=st.session_state.visibility,
        # disabled=st.session_state.disabled,
        placeholder="거실 크기를 입력 해 주세요.",
    )

    if text_input:
        st.write("You entered: ", text_input)
    

# textbox 

import streamlit as st

txt = st.text_area(
    "Text to analyze",
    "It was the best of times, it was the worst of times, it was the age of "
    "wisdom, it was the age of foolishness, it was the epoch of belief, it "
    "was the epoch of incredulity, it was the season of Light, it was the "
    "season of Darkness, it was the spring of hope, it was the winter of "
    "despair, (...)",
)

st.write(f"You wrote {len(txt)} characters.")