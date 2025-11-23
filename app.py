import streamlit as st

st.set_page_config(
    page_title="Master Streamlit Hub",
    layout="centered"
)

st.title("📂 Master Streamlit Project Hub")
st.write("Welcome! Click any project below to open it in a new tab.")

# Add your Streamlit project URL entries here:
projects = [
    {
        "name": "Postal Code Lookup Tool",
        "desc": Postal Code Lookup Tool",
        "url": "https://postallooker-qnpcrwdwsaunhlvu3symrm.streamlit.app/"
    },
    {
        "name": "📦 TechSHIP Bulk Rate Estimators",
        "desc": "TechSHIP Bulk Rate Estimators",
        "url": "https://techship-app-5xasvw43cp8uotjnznoyek.streamlit.app/"
    },
    {
        "name": "📦 18 Wheels Utility Toolkit",
        "desc": "18 Wheels Utility Toolkit.",
        "url": https://airport-bomuudpwln3j4ujavvy8zx.streamlit.app/"
    },
]

for p in projects:
    st.markdown(f"### {p['name']}")
    st.write(p["desc"])
    st.markdown(f"[▶ Open App]({p['url']})")
    st.markdown("---")
