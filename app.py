import streamlit as st
import pandas as pd
import plotly.express as px

# ---- Mock Data ----
platform_data = {
    'Facebook': {
        'privacy_risk': 9,
        'data_collected': ['Location', 'Contacts', 'Search History', 'Interests'],
        'advice': 'Adjust your ad preferences and turn off location history.'
    },
    'Instagram': {
        'privacy_risk': 8,
        'data_collected': ['Photos', 'Search History', 'Device Info'],
        'advice': 'Be careful with photo metadata and third-party app access.'
    },
    'LinkedIn': {
        'privacy_risk': 6,
        'data_collected': ['Work History', 'Connections', 'Activity'],
        'advice': 'Limit public visibility and turn off profile viewing notifications.'
    },
    'Twitter': {
        'privacy_risk': 7,
        'data_collected': ['Tweets', 'Location (if enabled)', 'Interests'],
        'advice': 'Use private mode and avoid tagging location.'
    },
    'WhatsApp': {
        'privacy_risk': 5,
        'data_collected': ['Contacts', 'Chats (metadata)', 'Phone Number'],
        'advice': 'Disable cloud backup for end-to-end encryption.'
    },
    'Google': {
        'privacy_risk': 10,
        'data_collected': ['Search History', 'Location', 'Email Content', 'Browsing Data'],
        'advice': 'Review and pause activity tracking from Google Account settings.'
    },
    'TikTok': {
        'privacy_risk': 9,
        'data_collected': ['Usage Data', 'Location', 'Device Info'],
        'advice': 'Limit permissions and consider using the browser instead of app.'
    }
}

# ---- Streamlit App ----
st.set_page_config(page_title="Digital Footprint Visualizer", layout="wide")
st.title("🔍 Digital Footprint Visualizer")
st.markdown("Select the platforms you use to see what data they collect and the privacy risks.")

# ---- Sidebar Selection ----
platforms = list(platform_data.keys())
selected = st.multiselect("Choose your platforms:", platforms)

if selected:
    # ---- Radar Chart ----
    risk_data = pd.DataFrame({
        'Platform': selected,
        'Privacy Risk': [platform_data[p]['privacy_risk'] for p in selected]
    })

    fig = px.line_polar(risk_data, r='Privacy Risk', theta='Platform',
                        line_close=True, range_r=[0, 10],
                        title='Privacy Risk Radar Chart', markers=True)
    st.plotly_chart(fig, use_container_width=True)

    # ---- Data Collected Table ----
    st.subheader("📦 Data Collected")
    for p in selected:
        st.markdown(f"**{p}** collects: {', '.join(platform_data[p]['data_collected'])}")

    # ---- Advice Cards ----
    st.subheader("💡 Advice to Reduce Risk")
    for p in selected:
        with st.expander(f"Advice for {p}"):
            st.info(platform_data[p]['advice'])

else:
    st.warning("Please select at least one platform to visualize your digital footprint.")
