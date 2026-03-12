#!/usr/bin/env python3
"""
Wraith Vehicle Performance Model
Recreated from spreadsheet estimator.
"""

import math


# ============================================================
# INPUTS
# ============================================================

# -- Product --
prop_diameter_in = 12.5                 # propeller diameter [in]
thrust_to_weight = 3.0                  # T:W at sea level EOL
feature_power_w = 20.0                  # avionics, compute, payload [W]
target_cell_mass_pct = 0.398            # target cell mass as % of AUW
total_vehicle_weight_g = 2250           # total vehicle weight [g]

# -- Propeller / Vehicle --
Ct = 0.016156213                        # thrust coefficient (non-dimensional, from thrust stand)
Cq = 0.002200587                        # torque/power coefficient (non-dimensional, from thrust stand)
motor_efficiency_hover = 0.75           # motor efficiency at hover
air_density = 1.2                       # kg/m³ (test conditions, hardcoded in spreadsheet)

# -- Battery Cells --
grav_energy_density_j_per_g = 1116      # gravimetric energy density [J/g]
vol_energy_density_wh_per_cm3 = 0.5745  # volumetric energy density [Wh/cm³]
cell_nominal_v = 3.60                   # nominal cell voltage [V]
cell_min_v = 2.90                       # minimum cell voltage [V]
cells_in_series = 8                     # cells in series

# -- Cell Geometry --
cell_thickness_mm = 10                  # pouch cell thickness [mm]
cell_length_width_ratio = 2             # length:width ratio

# -- KV Estimator --
sag_compensator = 1.2                   # voltage sag factor under max load

# -- Flight Time Bonuses --
bonus_reduced_compute_min = 2.0         # time saved reducing compute by 15W [min]
bonus_forward_flight_min = 1.5          # time gained at 8 m/s forward flight [min]


# ============================================================
# DERIVED — PRODUCT
# ============================================================

prop_diameter_m = prop_diameter_in * 0.0254
prop_radius_m = prop_diameter_m / 2
rotor_area_m2 = math.pi * prop_radius_m ** 2

vehicle_mass_kg = total_vehicle_weight_g / 1000
n_motors = 4
g = 9.81

cell_mass_total_g = target_cell_mass_pct * total_vehicle_weight_g
cell_mass_each_g = cell_mass_total_g / cells_in_series
non_cell_mass_g = total_vehicle_weight_g - cell_mass_total_g

disc_loading_g_per_cm2 = total_vehicle_weight_g / (n_motors * rotor_area_m2 * 1e4)


# ============================================================
# DERIVED — VEHICLE
# ============================================================

# Thrust per motor
thrust_hover_n = (total_vehicle_weight_g / n_motors) * 0.00980665
thrust_max_n = thrust_hover_n * thrust_to_weight

# Mechanical power: P = (Cq/Ct) * T * sqrt(T / (rho * A * Ct))
# From spreadsheet: =(F31/F30)*F35*SQRT(F35/(1.2*F34*F30))
mech_power_hover = (Cq / Ct) * thrust_hover_n * math.sqrt(thrust_hover_n / (air_density * rotor_area_m2 * Ct))
mech_power_max = (Cq / Ct) * thrust_max_n * math.sqrt(thrust_max_n / (air_density * rotor_area_m2 * Ct))

# Vehicle power (electrical)
vehicle_power_hover = n_motors * (mech_power_hover / motor_efficiency_hover) + feature_power_w
vehicle_power_max = n_motors * (mech_power_max / motor_efficiency_hover) + feature_power_w


# ============================================================
# DERIVED — BATTERY
# ============================================================

# Energy
energy_per_cell_wh = cell_mass_each_g * grav_energy_density_j_per_g / 3600
capacity_per_cell_mah = energy_per_cell_wh / cell_nominal_v * 1000
pack_wh = cells_in_series * energy_per_cell_wh

# Voltages
pack_nominal_v = cells_in_series * cell_nominal_v
pack_min_v = cells_in_series * cell_min_v

# Currents
hover_current_nom_v = vehicle_power_hover / pack_nominal_v
hover_current_min_v = vehicle_power_hover / pack_min_v
max_current_nom_v = vehicle_power_max / pack_nominal_v
max_current_min_v = vehicle_power_max / pack_min_v

# C rating
c_rating_required = max_current_min_v / (capacity_per_cell_mah / 1000)

# Cell geometry
cell_volume_cm3 = energy_per_cell_wh / vol_energy_density_wh_per_cm3
cell_width_mm = math.sqrt(cell_volume_cm3 * 1000 / (cell_thickness_mm * cell_length_width_ratio))
cell_length_mm = cell_width_mm * cell_length_width_ratio
cells_volume_cm3 = cells_in_series * cell_volume_cm3
cells_total_thickness_mm = cells_in_series * cell_thickness_mm


# ============================================================
# KV ESTIMATOR
# ============================================================

vtip_max = math.sqrt(thrust_max_n / (air_density * rotor_area_m2 * Ct))
max_rotor_rate_rad_s = vtip_max / prop_radius_m
max_rotor_rate_rpm = max_rotor_rate_rad_s * 60 / (2 * math.pi)
max_rotor_rate_hz = max_rotor_rate_rpm / 60
lowest_pack_v = pack_min_v
estimated_kv = max_rotor_rate_rpm / (lowest_pack_v / sag_compensator)


# ============================================================
# FLIGHT TIME
# ============================================================

flight_time_min = pack_wh / vehicle_power_hover * 60
total_time_with_bonuses = flight_time_min + bonus_reduced_compute_min + bonus_forward_flight_min


# ============================================================
# SENSITIVITIES
# ============================================================

def hover_time_sec(mass_g):
    """Compute hover time in seconds for a given vehicle mass."""
    t = (mass_g / n_motors) * 0.00980665
    p_mech = (Cq / Ct) * t * math.sqrt(t / (air_density * rotor_area_m2 * Ct))
    p_total = n_motors * (p_mech / motor_efficiency_hover) + feature_power_w
    return pack_wh / p_total * 3600

hover_time_s = hover_time_sec(total_vehicle_weight_g)
sensitivity_sec_per_g = hover_time_sec(total_vehicle_weight_g - 1) - hover_time_s
sensitivity_sec_per_w = pack_wh / vehicle_power_hover ** 2 * 3600  # d(t)/d(P) = -E/P²


# ============================================================
# OUTPUT
# ============================================================

def print_section(title):
    print(f"\n{'=' * 50}")
    print(f"  {title}")
    print(f"{'=' * 50}")

def row(label, value, unit=""):
    if isinstance(value, float):
        print(f"  {label:<40} {value:>10.2f}  {unit}")
    else:
        print(f"  {label:<40} {value:>10}  {unit}")


print_section("PRODUCT")
row("propeller diameter", prop_diameter_in, "in")
row("propeller diameter", prop_diameter_m, "m")
row("thrust:weight (EoL @ sea lvl)", thrust_to_weight)
row("feature power", feature_power_w, "W")
row("target cell mass %", target_cell_mass_pct * 100, "%")
row("non cell mass", non_cell_mass_g, "g")
row("total vehicle weight", total_vehicle_weight_g, "g")
row("per cell weight", cell_mass_each_g, "g")
row("total cell weight", cell_mass_total_g, "g")
row("flight time", flight_time_min, "min")
row("disc loading", disc_loading_g_per_cm2, "g/cm²")
row("bonus time, reduced compute (-15W)", bonus_reduced_compute_min, "min")
row("bonus time, 8 m/s forward flight", bonus_forward_flight_min, "min")
row("total time accounting for bonuses", total_time_with_bonuses, "min")

print_section("VEHICLE")
row("thrust coefficient", Ct)
row("torque coefficient", Cq)
row("motor efficiency (hover)", motor_efficiency_hover)
row("rotor area", rotor_area_m2, "m²")
row("thrust/motor (hover)", thrust_hover_n, "N")
row("mech. power/motor (hover)", mech_power_hover, "W")
row("thrust/motor (max)", thrust_max_n, "N")
row("mech. power/motor (max)", mech_power_max, "W")
row("vehicle power (hover)", vehicle_power_hover, "W")
row("vehicle power (max)", vehicle_power_max, "W")

print_section("BATTERY")
row("gravimetric energy density", grav_energy_density_j_per_g, "J/g")
row("volumetric energy density", vol_energy_density_wh_per_cm3, "Wh/cm³")
row("nominal voltage", cell_nominal_v, "V")
row("minimum voltage", cell_min_v, "V")
row("cells in series", cells_in_series)
row("hover current @ nominal V", hover_current_nom_v, "A")
row("hover current @ minimum V", hover_current_min_v, "A")
row("max current @ nominal V", max_current_nom_v, "A")
row("max current @ minimum V", max_current_min_v, "A")
row("capacity required per cell", capacity_per_cell_mah, "mAh")
row("C rating required", c_rating_required)
row("pack wattage - hour", pack_wh, "Wh")
row("cell thickness", cell_thickness_mm, "mm")
row("length:width ratio", cell_length_width_ratio)
row("cell width", cell_width_mm, "mm")
row("cell length", cell_length_mm, "mm")
row("cells volume", cells_volume_cm3, "cm³")
row("cells total thickness", cells_total_thickness_mm, "mm")

print_section("KV ESTIMATOR")
row("max required rotor rate", max_rotor_rate_rad_s, "rad/s")
row("max required rotor rate", max_rotor_rate_rpm, "RPM")
row("max required rotor rate", max_rotor_rate_hz, "Hz")
row("lowest pack voltage", lowest_pack_v, "V")
row("sag compensator", sag_compensator)
row("estimated KV", estimated_kv)

print_section("SENSITIVITIES")
row("hover time / weight", sensitivity_sec_per_g, "sec/g")
row("hover time / power", sensitivity_sec_per_w, "sec/W")
