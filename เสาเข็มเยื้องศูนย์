import streamlit as st
import pandas as pd
import numpy as np

# ---------------------------
# 🎨 Custom CSS
# ---------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    font-size: 32px;
    font-weight: bold;
    color: #2c3e50;
}
.card {
    background-color: white;
    padding: 20px;
    border-radius: 15px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
}
</style>
""", unsafe_allow_html=True)

# ---------------------------
# 🏗️ Title
# ---------------------------
st.markdown('<div class="title">Pile Reaction Calculator (Eccentric Load)</div>', unsafe_allow_html=True)

st.markdown("---")

# ---------------------------
# 📥 Input Section
# ---------------------------
with st.container():
    st.markdown('<div class="card">', unsafe_allow_html=True)
    
    col1, col2 = st.columns(2)
    
    with col1:
        P = st.number_input("Total Load P (tons)", value=150.0)
        ex = st.number_input("Eccentricity ex (cm)", value=0.0)
        ey = st.number_input("Eccentricity ey (cm)", value=0.0)
    
    with col2:
        n = st.number_input("Number of piles", value=4, step=1)
    
    st.markdown("### 📍 Pile Coordinates (cm)")
    
    df = pd.DataFrame({
        "x": [ -60, 60, -60, 60 ],
        "y": [ 95, 95, -95, -95 ]
    })
    
    pile_df = st.data_editor(df, num_rows="dynamic")
    
    st.markdown('</div>', unsafe_allow_html=True)

# ---------------------------
# 🧮 Calculation
# ---------------------------
if st.button("Calculate Reactions"):
    
    x = pile_df["x"].values
    y = pile_df["y"].values
    
    # Moments
    Mx = P * ey
    My = P * ex
    
    sum_x2 = np.sum(x**2)
    sum_y2 = np.sum(y**2)
    
    reactions = []
    
    for i in range(len(x)):
        Ri = (P / n) + (Mx * y[i] / sum_y2) + (My * x[i] / sum_x2)
        reactions.append(Ri)
    
    result_df = pile_df.copy()
    result_df["Reaction (tons)"] = reactions
    
    # ---------------------------
    # 📊 Output Section
    # ---------------------------
    st.markdown("---")
    st.markdown("## 📊 Results")
    
    st.dataframe(result_df)
    
    st.success(f"Maximum Reaction = {max(reactions):.2f} tons")
    st.warning(f"Minimum Reaction = {min(reactions):.2f} tons")
