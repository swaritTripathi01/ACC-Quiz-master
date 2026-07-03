import streamlit as st

st.title("ACC केमिस्ट्री क्विज़ मास्टर")

st.header("नियम और निर्देश:")
st.write("1. सभी प्रश्न अनिवार्य हैं।")
st.write("2. अपना नाम और रोल नंबर दर्ज करें।")
st.write("3. अंत में 'Submit' बटन दबाएं।")

name = st.text_input("अपना नाम लिखें:")

st.subheader("प्रश्न 1: हैलोऐल्केन में SN2 अभिक्रिया की क्रियाविधि क्या है?")
q1 = st.radio("विकल्प चुनें:", ["एक चरण (Single step)", "दो चरण (Two steps)"])

if st.button("Submit"):
    st.write(f"धन्यवाद {name}! आपका उत्तर रिकॉर्ड कर लिया गया है।")
