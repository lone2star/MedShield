import streamlit as st
import pickle

model = pickle.load(open('model.pkl', 'rb'))
vector = pickle.load(open('vectorizer.pkl', 'rb'))

st.set_page_config(page_title="MedShield", page_icon="🛡️")
st.title("MedShield")
st.write("Check medical news for patterns of misinformation. Paste your text below.")

# Add the professional disclaimer immediately
st.warning("DISCLAIMER: This tool identifies text patterns found in known misinformation. It does not verify scientific truth. Always consult a doctor for health decisions.")

user_input = st.text_area("Medical Text Input")

if st.button("Verify"):
    if user_input:
        data = vector.transform([user_input])
        prediction = model.predict(data)
        if prediction[0] == 1:
            st.error("Result: Misleading Patterns Detected")
        else:
            st.success("Result: Verified Pattern")
            st.info("Note: Model verifies text structure, not scientific facts.")
    else:
        st.warning("Enter text before clicking verify.")
