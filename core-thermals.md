# Quadcopter Weatherproofing & Thermal Engineering Specification

## 1. High-Level Strategy: The "Breathing Labyrinth"
This design optimizes for **maximum reworkability** and **survivability in heavy weather/coastal environments** (IP54/IP55 equivalent). It avoids the permanent "glue trap" and thermal throttling of fully sealed (IP67) potting methods. 

* **Core Philosophy:** Deflect heavy liquid water mechanically, allow internal hot air to vent, and protect internal electronics chemically against the inevitable condensation.
* **Environment:** Designed for thunderstorms, high humidity, hot weather (up to 50°C), and coastal/salt-spray environments. Not designed for submersion.

---

## 2. Enclosure Design (Mechanical Defense)
The 3D-printed or custom-milled enclosure is the primary defense against liquid water kinetic energy.

* **Labyrinth Seals:** All wire ingress/egress points must use a tortuous maze path. This kills the momentum of splashing water and rain without requiring rigid cable glands.
* **The Weep Hole:** A tiny, tortuous exit hole placed at the absolute lowest point of gravity in the enclosure. Because the box "breathes" (inhaling humid air when cooling), this allows pooled condensation to safely drain out.

---

## 3. PCB & Connector Protection (Chemical & Gasket Defense)
Because the box is not hermetically sealed, Tier 2 defenses protect the raw electronics from condensation and salt-fog.

* **Main PCBA:** Coated with a high-build **Silicone Conformal Coating** (e.g., MG Chemicals 422B). Silicone is highly resistant to corrosive coastal salt spray and high heat. 
* **Micro-Connectors (e.g., 0.10mm pitch coax):** Mated dry. A small square of **closed-cell silicone foam** is placed over the joint. A physical rib designed into the enclosure lid compresses this foam when screwed down, creating a custom moisture gasket and shock absorber.
* **Stacked B2B Connectors:** Mated dry. A die-cut **"picture frame" gasket** made of closed-cell silicone foam is placed around the connector perimeter. Corner standoffs compress the boards, squishing the foam to seal the microscopic gap against capillary action.
* **Barometer:** **NEVER conformal coat the sensor hole.** Protect it by applying an adhesive **ePTFE (Gore-Tex) patch** over the hole. This allows air pressure to pass through for altitude readings but physically blocks salt crystals and water molecules.
* **Exposed External Metal:** Motor bearings, screw heads, and USB ports treated with a Q-tip application of **ACF-50** or **CorrosionX** to prevent saltwater rust.

---

## 4. Thermal Management Specification
The quadcopter utilizes a custom AZ31 Magnesium "H-Block" heatsink to manage 20W of heat generation in a 50°C (122°F) ambient environment, balancing natural convection (ground idling) and forced convection (13" propeller wash).

### Heatsink Geometry
* **Material:** AZ31 Magnesium (Aerospace grade, ~35% lighter than 6061 Aluminum).
* **Overall Dimensions:** 44mm (W) x 85mm (H) x 30mm (D).
* **Architecture:** Solid "H-Block" consisting of two 2mm front/back base plates bridged by vertical fins.
* **Fin Details:** 10 vertical fins, each 1.5mm thick, creating 3.2mm air gaps (critical to prevent boundary-layer stall on the ground).
* **PCB Interface:** 1.0mm - 1.5mm ultra-soft silicone thermal pads (≥ 6.0 W/m·K) bridging the gap between the bare chips and the magnesium base plates.

### Thermal Performance Summary (50°C Ambient)

| Parameter | Specification / Result |
| :--- | :--- |
| **Total Mass** | ~85.2 grams |
| **Total Surface Area** | 491 cm² |
| **Scenario 1: Ground (Idling)** | **10W Total** (5W per board), Natural Convection |
| *Ground Heating Rate* | Temp rises at ~6.8°C per minute |
| *Ground Temp Rise (ΔT)* | +27.1°C over ambient |
| *Max Ground Temp* | **77.1°C** (Safe, allows ~5-7 minutes of GPS lock wait time) |
| **Scenario 2: Flight (Active)** | **20W Total** (10W per board), Forced Convection (13" props) |
| *Flight Temp Rise (ΔT)* | +11.6°C over ambient |
| *Max Flight Temp* | **61.6°C** (Extremely safe, massive airflow wipes away heat) |