import streamlit as st
import math

# --------------------------
# CSS Styling
# --------------------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}
.title {
    font-size: 36px;
    font-weight: bold;
    color: #1f4e79;
    text-align: center;
}
.section {
    background-color: white;
    padding: 20px;
    border-radius: 12px;
    box-shadow: 0px 4px 10px rgba(0,0,0,0.1);
    margin-bottom: 20px;
}
.result {
    font-size: 20px;
    font-weight: bold;
    color: #0a7d5e;
}
</style>
""", unsafe_allow_html=True)

# --------------------------
# Title
# --------------------------
st.markdown('<div class="title">Terzaghi Bearing Capacity Calculator</div>', unsafe_allow_html=True)

# --------------------------
# Input Section
# --------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)

st.subheader("📥 Input Parameters")

c = st.number_input("Cohesion, c (kPa)", value=25.0)
phi = st.number_input("Friction angle, φ (degrees)", value=30.0)
gamma = st.number_input("Unit weight, γ (kN/m³)", value=18.0)
Df = st.number_input("Foundation depth, Df (m)", value=1.5)
B = st.number_input("Footing width, B (m)", value=2.0)
FS = st.number_input("Factor of Safety", value=3.0)

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# Bearing Capacity Factors
# --------------------------
def bearing_capacity_factors(phi):
    phi_rad = math.radians(phi)

    if phi == 0:
        Nc = 5.7
        Nq = 1
        Ngamma = 0
    else:
        Nq = math.exp(math.pi * math.tan(phi_rad)) * (math.tan(math.radians(45) + phi_rad/2))**2
        Nc = (Nq - 1) / math.tan(phi_rad)
        Ngamma = 2 * (Nq + 1) * math.tan(phi_rad)

    return Nc, Nq, Ngamma

Nc, Nq, Ngamma = bearing_capacity_factors(phi)

# --------------------------
# Calculation
# --------------------------
qu = c * Nc + gamma * Df * Nq + 0.5 * gamma * B * Ngamma
q_allow = qu / FS

# --------------------------
# Output Section
# --------------------------
st.markdown('<div class="section">', unsafe_allow_html=True)

st.subheader("📊 Results")

st.markdown(f'<div class="result">Ultimate Bearing Capacity (qu): {qu:,.2f} kPa</div>', unsafe_allow_html=True)
st.markdown(f'<div class="result">Allowable Bearing Capacity (q_allow): {q_allow:,.2f} kPa</div>', unsafe_allow_html=True)

st.markdown("### 🔢 Bearing Capacity Factors")
st.write(f"Nc = {Nc:.2f}")
st.write(f"Nq = {Nq:.2f}")
st.write(f"Nγ = {Ngamma:.2f}")

st.markdown('</div>', unsafe_allow_html=True)

# --------------------------
# Footer
# --------------------------
st.markdown("""
---
👷 Developed for Geotechnical Engineers | Terzaghi Theory
""")
