#!/usr/bin/env python3
"""
Wraith Vehicle Performance Model — Interactive
Run: streamlit run vehicle_model_app.py
"""

import math
import streamlit as st

st.set_page_config(page_title="Wraith Vehicle Model", layout="wide")
st.title("Wraith Vehicle Model")

# ============================================================
# INPUTS (sidebar)
# ============================================================

st.sidebar.header("Product")
prop_diameter_in = st.sidebar.number_input("Propeller diameter [in]", value=12.5, step=0.5)
thrust_to_weight = st.sidebar.number_input("T:W (sea level EOL)", value=3.0, step=0.1)
feature_power_w = st.sidebar.number_input("Feature power [W]", value=20.0, step=1.0)
cell_mass_each_g = st.sidebar.number_input("Cell weight [g]", value=112, step=1)
non_cell_mass_g = st.sidebar.number_input("Non-battery-cell weight [g]", value=1354, step=10)

st.sidebar.header("Propeller (from thrust stand)")
Ct = st.sidebar.number_input("Thrust coefficient Ct", value=0.016156213, format="%.9f")
Cq = st.sidebar.number_input("Torque coefficient Cq", value=0.002200587, format="%.9f")
motor_efficiency_hover = st.sidebar.slider("Motor efficiency (hover)", 0.50, 0.95, 0.75, 0.01)
air_density = st.sidebar.number_input("Air density [kg/m³]", value=1.2, step=0.01, format="%.3f")

st.sidebar.header("Battery Cells")
grav_energy_density_j_per_g = st.sidebar.number_input("Gravimetric energy density [J/g]", value=1116, step=10)
vol_energy_density_wh_per_cm3 = st.sidebar.number_input("Volumetric energy density [Wh/cm³]", value=0.5745, step=0.01, format="%.4f")
cell_nominal_v = st.sidebar.number_input("Nominal voltage [V]", value=3.60, step=0.01, format="%.2f")
cell_min_v = st.sidebar.number_input("Minimum voltage [V]", value=2.90, step=0.01, format="%.2f")
cells_in_series = st.sidebar.number_input("Cells in series", value=8, step=1)

st.sidebar.header("Cell Geometry")
cell_thickness_mm = st.sidebar.number_input("Cell thickness [mm]", value=10, step=1)
cell_length_width_ratio = st.sidebar.number_input("Length:width ratio", value=2, step=1)

st.sidebar.header("KV Estimator")
sag_compensator = st.sidebar.number_input("Sag compensator", value=1.2, step=0.1, format="%.1f")

st.sidebar.header("Flight Time Bonuses")
bonus_reduced_compute_min = st.sidebar.number_input("Reduced compute bonus [min]", value=2.0, step=0.5)
bonus_forward_flight_min = st.sidebar.number_input("Forward flight bonus [min]", value=1.5, step=0.5)


# ============================================================
# CALCULATIONS
# ============================================================

prop_diameter_m = prop_diameter_in * 0.0254
prop_radius_m = prop_diameter_m / 2
rotor_area_m2 = math.pi * prop_radius_m ** 2

n_motors = 4
g = 9.81

cell_mass_total_g = cell_mass_each_g * cells_in_series
total_vehicle_weight_g = cell_mass_total_g + non_cell_mass_g
target_cell_mass_pct = cell_mass_total_g / total_vehicle_weight_g
vehicle_mass_kg = total_vehicle_weight_g / 1000

disc_loading_g_per_cm2 = total_vehicle_weight_g / (n_motors * rotor_area_m2 * 1e4)

# Thrust
thrust_hover_n = (total_vehicle_weight_g / n_motors) * 0.00980665
thrust_max_n = thrust_hover_n * thrust_to_weight

# Mechanical power: P = (Cq/Ct) * T * sqrt(T / (rho * A * Ct))
mech_power_hover = (Cq / Ct) * thrust_hover_n * math.sqrt(thrust_hover_n / (air_density * rotor_area_m2 * Ct))
mech_power_max = (Cq / Ct) * thrust_max_n * math.sqrt(thrust_max_n / (air_density * rotor_area_m2 * Ct))

# Vehicle power (electrical)
vehicle_power_hover = n_motors * (mech_power_hover / motor_efficiency_hover) + feature_power_w
vehicle_power_max = n_motors * (mech_power_max / motor_efficiency_hover) + feature_power_w

# Battery
energy_per_cell_wh = cell_mass_each_g * grav_energy_density_j_per_g / 3600
capacity_per_cell_mah = energy_per_cell_wh / cell_nominal_v * 1000
pack_wh = cells_in_series * energy_per_cell_wh

pack_nominal_v = cells_in_series * cell_nominal_v
pack_min_v = cells_in_series * cell_min_v

hover_current_nom_v = vehicle_power_hover / pack_nominal_v
hover_current_min_v = vehicle_power_hover / pack_min_v
max_current_nom_v = vehicle_power_max / pack_nominal_v
max_current_min_v = vehicle_power_max / pack_min_v

c_rating_required = max_current_min_v / (capacity_per_cell_mah / 1000)

# Cell geometry
cell_volume_cm3 = energy_per_cell_wh / vol_energy_density_wh_per_cm3
cell_width_mm = math.sqrt(cell_volume_cm3 * 1000 / (cell_thickness_mm * cell_length_width_ratio))
cell_length_mm = cell_width_mm * cell_length_width_ratio
cells_volume_cm3 = cells_in_series * cell_volume_cm3
cells_total_thickness_mm = cells_in_series * cell_thickness_mm

# KV estimator
vtip_max = math.sqrt(thrust_max_n / (air_density * rotor_area_m2 * Ct))
max_rotor_rate_rad_s = vtip_max / prop_radius_m
max_rotor_rate_rpm = max_rotor_rate_rad_s * 60 / (2 * math.pi)
max_rotor_rate_hz = max_rotor_rate_rpm / 60
lowest_pack_v = pack_min_v
estimated_kv = max_rotor_rate_rpm / (lowest_pack_v / sag_compensator)

# Flight time
flight_time_min = pack_wh / vehicle_power_hover * 60
total_time_with_bonuses = flight_time_min + bonus_reduced_compute_min + bonus_forward_flight_min

# Sensitivities
def hover_time_sec(mass_g):
    t = (mass_g / n_motors) * 0.00980665
    p_mech = (Cq / Ct) * t * math.sqrt(t / (air_density * rotor_area_m2 * Ct))
    p_total = n_motors * (p_mech / motor_efficiency_hover) + feature_power_w
    return pack_wh / p_total * 3600

hover_time_s = hover_time_sec(total_vehicle_weight_g)
sensitivity_sec_per_g = hover_time_sec(total_vehicle_weight_g - 1) - hover_time_s
sensitivity_sec_per_w = pack_wh / vehicle_power_hover ** 2 * 3600


# ============================================================
# DISPLAY
# ============================================================

col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Total Vehicle Weight", f"{total_vehicle_weight_g:.0f} g")
    st.metric("Flight Time", f"{flight_time_min:.1f} min")
    st.metric("w/ Bonuses", f"{total_time_with_bonuses:.1f} min")

with col2:
    st.metric("Hover Power", f"{vehicle_power_hover:.0f} W")
    st.metric("Max Power", f"{vehicle_power_max:.0f} W")
    st.metric("Cell Mass %", f"{target_cell_mass_pct*100:.1f}%")

with col3:
    st.metric("Estimated KV", f"{estimated_kv:.0f}")
    st.metric("Disc Loading", f"{disc_loading_g_per_cm2:.3f} g/cm²")
    st.metric("Sensitivity", f"{sensitivity_sec_per_g:.1f} sec/g")

st.divider()

col_left, col_right = st.columns(2)

with col_left:
    st.subheader("Product")
    st.markdown(f"""
| | |
|---|---|
| Propeller diameter | {prop_diameter_in}" / {prop_diameter_m:.4f} m |
| T:W (sea level EOL) | {thrust_to_weight} |
| Feature power | {feature_power_w} W |
| Target cell mass | {target_cell_mass_pct*100:.1f}% |
| Non-cell mass | {non_cell_mass_g:.0f} g |
| Total vehicle weight | {total_vehicle_weight_g} g |
| Per cell weight | {cell_mass_each_g:.0f} g |
| Total cell weight | {cell_mass_total_g:.0f} g |
| Disc loading | {disc_loading_g_per_cm2:.3f} g/cm² |
""")

    st.subheader("Vehicle")
    st.markdown(f"""
| | |
|---|---|
| Thrust coefficient | {Ct:.9f} |
| Torque coefficient | {Cq:.9f} |
| Motor efficiency (hover) | {motor_efficiency_hover} |
| Rotor area | {rotor_area_m2:.5f} m² |
| Thrust/motor (hover) | {thrust_hover_n:.2f} N |
| Mech. power/motor (hover) | {mech_power_hover:.2f} W |
| Thrust/motor (max) | {thrust_max_n:.2f} N |
| Mech. power/motor (max) | {mech_power_max:.2f} W |
| Vehicle power (hover) | {vehicle_power_hover:.2f} W |
| Vehicle power (max) | {vehicle_power_max:.2f} W |
""")

    st.subheader("Sensitivities")
    st.markdown(f"""
| | |
|---|---|
| Hover time / weight | {sensitivity_sec_per_g:.1f} sec/g |
| Hover time / power | {sensitivity_sec_per_w:.1f} sec/W |
""")

with col_right:
    st.subheader("Battery")
    st.markdown(f"""
| | |
|---|---|
| Gravimetric energy density | {grav_energy_density_j_per_g} J/g |
| Volumetric energy density | {vol_energy_density_wh_per_cm3} Wh/cm³ |
| Nominal voltage | {cell_nominal_v} V |
| Minimum voltage | {cell_min_v} V |
| Cells in series | {cells_in_series} |
| Hover current @ nominal V | {hover_current_nom_v:.2f} A |
| Hover current @ minimum V | {hover_current_min_v:.2f} A |
| Max current @ nominal V | {max_current_nom_v:.2f} A |
| Max current @ minimum V | {max_current_min_v:.2f} A |
| Capacity per cell | {capacity_per_cell_mah:.0f} mAh |
| C rating required | {c_rating_required:.1f} |
| Pack energy | {pack_wh:.2f} Wh |
| Cell thickness | {cell_thickness_mm} mm |
| Cell width | {cell_width_mm:.1f} mm |
| Cell length | {cell_length_mm:.1f} mm |
| Cells volume | {cells_volume_cm3:.2f} cm³ |
| Cells total thickness | {cells_total_thickness_mm} mm |
""")

    st.subheader("KV Estimator")
    st.markdown(f"""
| | |
|---|---|
| Max rotor rate | {max_rotor_rate_rad_s:.0f} rad/s |
| Max rotor rate | {max_rotor_rate_rpm:.0f} RPM |
| Max rotor rate | {max_rotor_rate_hz:.0f} Hz |
| Lowest pack voltage | {lowest_pack_v:.1f} V |
| Sag compensator | {sag_compensator} |
| Estimated KV | {estimated_kv:.0f} |
""")
