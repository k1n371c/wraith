# Wraith — Project Overview

## Product
Folding quadcopter drone. 2kg AUW. 12.5" three-blade props. Four folding arms — two front (200mm), two rear (275mm). Arms fold horizontally via coaxial vertical hinge axes (one hinge per side, front + rear arms share axis).

## Intended Use
Military / defense. Designed for field abuse — branch strikes, hard landings, rough handling. Arms fold for transport, snap open for deployment. Tactile feel and build quality matter (M4 charging handle is the UX benchmark).

## Customers
Military end users. Product needs to survive harsh environments, humid/outdoor conditions, and operator abuse. Cosmetics matter — bead-blasted black finish, quality look and feel. Some customers fly at 15 m/s sustained cruise.

## Key Design Priorities
- **Weight** — every gram counts at 2kg AUW (battery alone is 1000g / 45%)
- **Durability** — mil-grade abuse resistance, branch strike survival
- **Foldability** — arms fold/deploy quickly with positive detent feel
- **Manufacturability** — parts machined overseas, coatings need to be sourceable

## Engineer (Ben)
- Mechanical design lead, working in CAD (CATIA)
- Strong intuition for load paths, manufacturing, and practical design tradeoffs
- Thinks critically about failure modes and assembly sequence
- Comfortable with material selection decisions (magnesium, aluminum, carbon, coatings)
- Balances weight optimization against complexity and manufacturing reality

## Manufacturing Resources
- **Machining:** Vietnam / Thailand shops (aluminum and magnesium capable)
- **Carbon tubes:** Off-the-shelf roll-wrapped 3K with uni core, pultruded available, custom layup possible
- **Coatings available:**
  - Type III hard anodize (aluminum) — readily available in SE Asia
  - E-coat / ED coat (magnesium) — available
  - Cerakote H-series — available globally
  - PEO / Keronite (magnesium) — limited SE Asia availability, possible via China sub-tier
  - Chromate conversion — widely available
- **Hardware:** McMaster-Carr sourced (US-based, Belleville washers etc.)

## Drone Layout
- Hinge axes: vertical, one per side (coaxial front+rear per side)
- Front arms: 200mm, motor Y = 209mm from hinge (wider spread for gimbal clearance)
- Rear arms: 275mm, motor Y = 180mm from hinge
- Gimbal/payload: under front of body, between front arms
- Motor mounts: magnesium (AZ31), 10g each per BOM
- Inner lugs: 7075-T6, 15g each per BOM (optimized wall thickness)

## Propulsion
- Motors: 75g each, $30
- Props: 12.5" diameter, 3-blade, 24g per blade assembly (blades + hub), $39.80
- Motor mount: 10g per BOM (15g per earlier discussion — verify)
- Hover RPM: 3500
- Cruise RPM (15 m/s): 4500
- Max RPM (sea level): 6000

## Performance (estimated)
- Hover power: 260W (65W/motor)
- Max power: 1268W
- T:W ratio: 3:1 (sea level)
- Disc loading: 0.71 g/cm²
- Hover flight time: ~64 min
- With bonuses (reduced compute + fwd flight): ~67.5 min
- Hover sensitivity: 2.4 sec/g saved
- Motor KV: ~323, 8S pack

## Battery
- 8S pack, 3.6V nominal per cell, 9650 mAh per cell
- Cell mass: 896g (8 × 112g)
- Total pack mass: 1000g (cells + enclosure + BMS PCB + wiring)
- Pack energy: 278 Wh
- Gravimetric density: 1116 J/g (cells)

## BOM Summary
- **Total AUW:** 2220g
- **ISR cost:** $5,950
- **Defeatured cost:** $2,414
- **Battery:** Apex, 1000g, $300 (45% of AUW)
- **Hinge system total:** ~130g (Bellevilles + screws + caps + shims + inner lugs)
- **Structure (chassis+frame+covers):** ~161g
- **Propulsion (motors+props):** ~395g

## Key Decisions Made
| Decision | Choice | Rationale |
|---|---|---|
| Hinge material | 7075-T6 aluminum | Best tradeoff of weight, wear, corrosion, cost, simplicity |
| Finish (hinge/frame) | Type III hard anodize, black | Wear + color + corrosion in one process, shows bead blast |
| Motor mounts | AZ31 magnesium | Weight savings, acceptable at non-wear interface |
| Detent mechanism | Belleville preloaded V-ridges/grooves | High holding force for branch strikes + thrust moment resistance, M4 feel |
| Detent wall angle | 45° | 4.2× SF at max thrust (front arm), good tactile feel |
| Hinge support | Double-supported (bolted purple bracket) | Eliminates cantilever, 2mm bearing overlap each end, detents carry tilt |
| Hard stop | None (intentional) | Breakaway = safety fuse on impact |
| Front arm tube | 20mm OD × 1mm wall, standard wound | Adequate vibration margins, weight savings |
| Rear arm tube | 20mm OD × 1mm wall, standard wound (OTS) | Pultruded previously spec'd for vibration margin — reverted to OTS wound, resonance managed by FC notch filters (TBC) |
| Belleville stack | 6 in series, 20mm OD, 330 lbf working | Travel budget for 1.5mm detent depth |

## File Index
- [overview.md](overview.md) — this file
- [arm-hinge.md](arm-hinge.md) — folding hinge design spec and decisions
- [propulsion-vibration.md](propulsion-vibration.md) — vibration analysis and arm resonance
- [vehicle_model.py](vehicle_model.py) — performance model (CLI, matches spreadsheet)
- [vehicle_model_app.py](vehicle_model_app.py) — interactive Streamlit app (`streamlit run vehicle_model_app.py`)

## Open Items
- Yellow part (frame boss) detailed design — not started (integral to frame)
- Fold angle — not specified
- ~~Shoulder screw spec~~ — **M3 titanium, two per coaxial side** (sized by Belleville preload tension)
- ~~Bearing overlap length~~ — **2mm per end** (detents are primary tilt constraint)
- Carbon tube clamp detail design
- Flight controller platform — not discussed
- ESC location (arm tip vs body) — not confirmed
- Motor mount weight discrepancy — BOM says 10g, earlier discussion said 15g
- ~~Pultruded tube sourcing for rear arms~~ — reverted to OTS wound, FC notch filters (TBC)
- Rear arm vibration management — f₁≈73 Hz on cruise 1P with wound tubes, needs FC notch filter confirmation
- ~~Debris skirt~~ — rejected (machining access + seal incompatible with axial travel). Grease + maintenance approach instead.
