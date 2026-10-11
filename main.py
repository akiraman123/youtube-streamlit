import streamlit as st
import time

st.title('Streamlit 超入門')

st.write('プログレスバーの表示')
'Start!!'

latest_iteration = st.empty()
bar = st.progress(0)

for i in range(100):
    latest_iteration.text(f'Iteration{i+1}')
    bar.progress(i + 1)
    time.sleep(0.1)

'Done!!!!!'

left_column, right_column = st.columns(2)
button = left_column.button('右カラムに文字を表示')
if button:
    right_column.write('ここは右カラム')

expander = st.expander('問い合わせ1')
expander.write('問い合わせ内容回答1')
expander = st.expander('問い合わせ2')
expander.write('問い合わせ内容回答2')
expander = st.expander('問い合わせ3')
expander.write('問い合わせ内容回答3')

# text = st.text_input('あなたの趣味を教えて下さい。 ')
# condition = st.slider('あなたの今の調子は？', 0, 100, 50)

# 'あなたの趣味： ', text
# 'コンディション: ', condition

# if st.checkbox('Show Image'):
#     img = Image.open('test.jpg')
#     st.image(img, caption='Akira Kagiwada', width="content")
