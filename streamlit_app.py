import streamlit as st
import requests

st.set_page_config(page_title="LUS Status")
st.title("Level Up Subs System Status")

url = "https://www.psacard.com"
st.write(f"Checking status of: **{url}**")

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
                  "AppleWebKit/537.36 (KHTML, like Gecko) "
                  "Chrome/120.0.0.0 Safari/537.36"
}

try:
    response = requests.get(url, headers=headers, timeout=5)
    if response.status_code == 200:
        st.success(f"✅ The PSA website is UP! (Status Code: {response.status_code})")
    else:
        st.warning(f"⚠️ The PSA website responded, but with status code: {response.status_code}")
except requests.exceptions.RequestException as e:
    st.error(f"❌ The PSA website appears to be DOWN.\n\nError: {e}")
