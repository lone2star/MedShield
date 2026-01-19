import streamlit as st
import pickle

# Load your saved files
model = pickle.load(open('model.pkl', 'rb'))
vector = pickle.load(open('vectorizer.pkl', 'rb'))

st.set_page_config(page_title="MedShield", page_icon="🛡️")
st.title("MedShield")
st.write("Check medical news for accuracy. Paste your text below to verify.")
st.warning("Disclaimer: This tool analyzes text patterns. It does not verify scientific truth. Consult medical professionals for health advice.")

user_input = st.text_area("Medical News Text")

if st.button("Verify"):
    if user_input:
        data = vector.transform([user_input])
        prediction = model.predict(data)
        # In your code: 1 is Misleading, 0 is Verified
        if prediction[0] == 1:
            st.error("Result: Misleading")
        else:
            st.success("Result: Verified")
    else:

        st.warning("Enter text before clicking verify.")
