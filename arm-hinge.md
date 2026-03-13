# Folding Arm Hinge Design

## Overview
Belleville washer preloaded detent hinge. Two positions: deployed + folded. Breakaway design — arm folds on impact as a safety fuse (no hard stop). Tactile feel target: M4 charging handle.

## Architecture
- **Hinge axis:** Vertical, one per side, coaxial (front + rear arms share same vertical hinge axis per side)
- **Fold direction:** Horizontal — arms swing inward to fold
- **Green part (rotating):** Holds carbon tube, contains Belleville stack, has detent ridges. Swings with arm.
- **Yellow part (fixed):** Integral boss on frame (upper). Has detent grooves (4 total), shoulder screw threaded hole.
- **Purple bracket (fixed):** Bolted to fuselage underside (2-3 × M2.5/M3 screws into threaded inserts). Provides lower bearing surface for green part. Replaces old free-spinning cap.
- **Shoulder screw:** Fixed into yellow/frame. Head captured in purple bracket pocket. Green part rotates around the shoulder.
- **Support:** Double-supported — green part bears on yellow boss (top) and purple bracket (bottom). Not cantilevered.

### Assembly Sequence
1. Load Bellevilles + stainless shims into green part bore (open bottom)
2. Slide green+Bellevilles onto yellow boss from below
3. Insert shoulder screw from below, thread into yellow/frame
4. Bolt purple bracket to fuselage underside — captures shoulder screw head, provides lower bearing

### Sliding Interface
Stainless shim washers at each end of the Belleville stack embed into the Belleville edges and rotate as a unit with the stack. The rotation interface is stainless-on-hard-anodized-7075 at whichever end (top green ledge or bottom purple bracket face) has less friction — both are flat-on-flat and acceptable wear pairs.

## Load Path — Detent (Abuse / Impact)
**The detent resists lateral forces that try to rotate the arm about the vertical hinge axis.** Thrust is vertical and parallel to the hinge axis — it does not load the detent. Steady-state flight loads on the detent are negligible (motor reaction torque ≈ 0.12 N-m at hover).

The detent is sized for **abuse loads**: branch strikes, broken prop imbalance, crash impacts, rough handling. It acts as a safety fuse — strong enough to hold through incidental contact, weak enough to break away on a real hit.

| | Front | Rear |
|---|---|---|
| Arm length (hinge to motor) | 200mm | 275mm |
| Belleville working load | 1,134 N (0.9mm) | 1,468 N (1.0mm) |
| Breakout torque (45° wall) | 10.2 N-m | 13.2 N-m |
| **Tip breakaway force** | **51N / 11.5 lbs** | **48N / 10.8 lbs** |

Tip feel matched within ~6% across front and rear arms. ~50N / ~11 lbs at the tip — solid tactile detent without preventing breakaway on impact.

## Load Path — Bending
- Thrust and arm weight create bending loads perpendicular to the hinge axis.
- Small deflections absorbed by Belleville stack (off-axis compression).
- **Detent ridges/grooves are the primary tilt constraint** — Belleville preload (1,134-1,468N) on 45° walls at ~9mm radius creates a strong restoring moment against any tilt.
- **Centering: green part rides on yellow boss (top) and purple bracket (bottom).** Short cylindrical overlaps at each end, hard-anodized 7075 on hard-anodized 7075 — same proven wear pair as detent faces. Sliding fit (~0.05-0.10mm radial clearance post-anodize) accommodates both rotation and 1.5mm axial travel during fold action.
- Shoulder screw provides axial retention only (not centering) — green part bore has clearance around screw shaft in the middle. Detents provide tilt stiffness + fold resistance.

## Materials
- Green part (inner lug): **7075-T6 aluminum**, 15g each per BOM
- Yellow part: **7075-T6 aluminum** (integral to frame)
- Finish: **Type III hard anodize (black, 50+ micron)**
  - Provides: color, wear resistance on detent faces, corrosion protection, bead blast texture visible
  - Detent faces: anodized 7075 on anodized 7075 (proven wear pair)
- Bellevilles: 17-7 PH stainless steel
- Shoulder screw: **M3 titanium** (Ti-6Al-4V). Sized by Belleville preload in tension: 1,468N vs ~4,175N yield capacity (35% utilization). M2 rejected — 85% of yield, no margin. Two separate screws per coaxial side (not one long shared screw — avoids dead weight spanning gap between upper and lower hinge).
- Bushings: none — centering overlaps are anodized 7075 on anodized 7075 (Type III anodize is alumina ceramic, provides galvanic isolation and wear resistance)
- Carbon tube interface: direct to e-coated magnesium motor mount (e-coat provides galvanic isolation)

## Belleville Washers
Front and rear arms use different Belleville thicknesses to equalize tip feel despite different arm lengths (200mm front vs 275mm rear). Force ratio 1,134/1,468 = 0.772 ≈ arm length ratio 200/275 = 0.727 — matched within 6%.

### Rear Arms (1.0mm thick)
- Part: McMaster 96475K247
- Spec: 20mm OD, 10.2mm ID, 1.0mm thick, 1.55mm free height (h=0.55mm)
- Working load: 330 lbf / 1,468 N at 0.39mm deflection
- Flat load: 441 lbf / 1,962 N at 0.55mm deflection

### Front Arms (0.9mm thick)
- Part: McMaster 96475K246 (TBC)
- Spec: 20mm OD, 10.2mm ID, 0.9mm thick, 1.45mm free height (h=0.55mm)
- Working load: 255 lbf / 1,134 N at 0.42mm deflection
- Flat load: 318 lbf / 1,415 N at 0.55mm deflection

### Common
- Material: 17-7 PH stainless, DIN 2093
- Stack: **6 in series** (alternating orientation), force = single washer force
- QPV: 24 (6 per hinge × 4 hinges)
- Stainless shim washers at each end of stack (protect surfaces from Belleville edge loading, rotate with stack). Galvanic isolation between stainless and anodized 7075 provided by Type III anodize layer (alumina ceramic insulator).

### Cavity Sizing
Green inner lug is **common** across front and rear — cavity sized for the taller rear stack. Shim thickness differs to set correct preload.

| | Front | Rear |
|---|---|---|
| Stack free height (6 washers) | 8.70mm | 9.30mm |
| Shim washers (2×) | 2 × 0.80mm = 1.60mm | 2 × 0.50mm = 1.00mm |
| Nominal stack height | 10.30mm | 10.30mm |
| Initial compression | 0.60mm | 0.60mm |
| Compressed cavity | **9.70mm** | **9.70mm** |

Same cavity, same green part, same purple bracket. Shims are the only difference between front and rear.

## Detent Geometry
- **2 positions** (deployed + folded), **2 detents per position** (180° apart, balanced — prevents tilting moment on shaft)
- 4 grooves total in yellow part, 2 ridges on green part
- Detent radial span: R=7.5 to R=10.5mm from shaft center
- Detent depth: 1.5mm
- **Ridge profile (trapezoidal):** At R=7.5mm: 2.0mm top flat, 4.8mm base. Widens with radius (radial taper). R0.75mm fillets at top edges (flat-to-wall transitions, prevents anodize cracking). Trapezoidal chosen over pointed V — flat top distributes contact stress during sliding across plateaus.
- **Groove profile:** 1.0mm flat bottom, 45° walls, R0.5mm bottom fillets (endmill corner radius), R0.3mm top edge break. Ridge does not bottom out in groove — 1.0mm clearance between ridge and groove bottom when seated.
- Wall angle: **45° from horizontal** (selected for mil use — ~50N tip breakaway, M4 charging handle feel)
- Flat plateau between grooves: 3-4mm (provides steady resistance during fold action)
- Radial feature extent: R=7.5 to R=10.5mm (3mm span).
- **Groove/ridge slope faces are radial planes** (point at shaft center) — ensures ridge engages full wall simultaneously during rotation. Groove is slightly wider at OD than ID (natural taper from radial geometry).

## Breakout Force at Arm Tip
| | Front (200mm, 1,134N) | Rear (275mm, 1,468N) |
|---|---|---|
| Tip force (45° wall) | 51N / 11.5 lbs | 48N / 10.8 lbs |
| Breakout torque | 10.2 N-m | 13.2 N-m |

Tip feel matched within ~6%. 45° wall angle selected: M4 charging handle feel + breakaway on impact.

## Green Part Wall Thickness
- **Centering overlap zones** (top and bottom, where green rides on yellow boss / purple bracket): top 2.0-2.5mm, bottom 1.1mm (purple bracket is thick/structural). Anodized 7075 on anodized 7075 sliding fit, ~0.05-0.10mm radial clearance post-anodize. Centering only — detents carry tilt loads.
- **Belleville guide zone** (middle barrel): 1.0-1.2mm walls. Just prevents washer lateral walk. Thinned from original design — saved 4g per hinge (16g total).
- **Transition ledge** between zones: 2mm height, R0.5mm internal fillet. Bears Belleville preload (~6.5 MPa, trivial vs 500 MPa yield).
- Lightening pockets: aggressive in guide zone, conservative in bearing zones.

## Rib and General Wall Minimums (7075-T6)
- Perimeter walls: 1.5mm min, 2.0mm comfortable
- Ribs: 1.0mm min, 1.2mm comfortable
- Overlap zone (double wall): 1.2-1.5mm per wall
- Bore wall around shoulder screw: 2.5mm min (highest stress)
- Practical limit is machinability, not strength — below 1.5mm walls chatter during milling

## Debris Management
- Detent faces (grooves/ridges) are exposed at the hinge OD — outboard of the bearing overlaps, no inherent shielding.
- **Integral debris skirt rejected:** Skirt on yellow blocks CNC access to V-grooves; skirt on green creates fillet interference with ridges. Separate skirt ring adds a part. All options add complexity for incomplete protection.
- **Radial wiper seal rejected:** Combined rotation + 1.5mm axial travel during fold action destroys any seal in the radial gap.
- **Approach:** Light grease (e.g. Nye Rheolube or similar mil-spec) on detent faces during assembly and field maintenance. Grease fills V-grooves, displaces particulates, improves tactile feel. Hard anodize (alumina, ~9 Mohs) resists sand abrasion (quartz, ~7 Mohs). 4.2× safety factor provides margin for degraded conditions. Field maintenance: wipe and re-grease periodically.

## Carbon Tube Attachment
- Split clamp with bolts (not set screws — carbon can't take point loads)
- Clamp gap on neutral/tension side of bending load, not compression side
- Consider bonded + pinned (roll pin through lug and tube) for mil abuse resistance
- **Speed holes:** CNC hex pattern cut after layup by carbon cutting vendor. Keep ligament width ≥ 1.5mm. No holes in clamp zones (within ~1.5× tube OD of clamp). Front arms: holes all around (ample EI margin). Rear arms: may need to limit hole pattern depending on final tube modulus vs EI margin.

## Weight — BOM Actuals (per hinge set, all 4 hinges)
| Part | QPV | Unit weight | Total |
|---|---|---|---|
| Belleville springs (0.9mm, front) | 12 | ~1.65g | 19.8g |
| Belleville springs (1.0mm, rear) | 12 | 1.83g | 22.0g |
| Hinge screws | 4 | 2.73g | 10.9g |
| Caps | 4 | 2.77g | 11.1g |
| Shim washers (0.80mm, front) | 4 | ~0.80g | 3.2g |
| Shim washers (0.50mm, rear) | 4 | 0.50g | 2.0g |
| Inner lugs (green parts) | 4 | 15.0g | 60.0g |
| **Total hinge system** | | | **~130g** |

## Design History / Decisions
- **Double-supported hinge** replaces cantilevered design. Purple cap replaced with structural bracket bolted to fuselage. Green part now supported at both ends (yellow top, purple bottom). Bearing overlap reduced from 10mm (single end, cantilever) to 2mm per end — detent faces are the primary tilt constraint, cylindrical fit is just a centering guide. Saves ~3-5g per hinge from shorter boss/overlap zones. Sliding interface is stainless shim on hard-anodized 7075 at one end of the Belleville stack.
- **Hexagonal arm tubes** considered for anti-rotation in clamp and aesthetics. Rejected — lower bending stiffness than circular for same OD/wall (flat faces closer to neutral axis), stress concentrations at corners, and heavier for equivalent performance. Anti-rotation solved by roll pin or bond on round tube.
- **Speed holes in carbon tubes** considered (AR-15 handguard style). Rejected — 20mm OD × 1mm wall tubes are the primary bending structure (unlike handguards which are non-structural shrouds over a barrel). Analysis: neutral-axis holes (3+9 o'clock) save ~0.5-0.7g/tube with negligible I loss (<0.1%); ±45° holes save ~1.2g/tube but cost ~6% bending stiffness. Total potential 3-5g/tube but rear arms already marginal on vibration (f₁=73 Hz vs cruise 1P=75 Hz). Not worth the risk.
- **Shoulder screw sizing:** M3 titanium selected. M2 rejected — Belleville preload (1,468N) is 85% of M2 Ti yield (1,718N), no margin for assembly torque or fatigue. M3 at 35% utilization (4,175N capacity) is comfortable.
- Magnesium (AZ31) considered for green/yellow parts — rejected due to galvanic corrosion complexity (carbon tube, steel Bellevilles, steel screw all bad couples with Mg), detent wear (Mg too soft), and need for steel ring inserts that added back complexity/weight. Weight savings was ~10-12g/hinge but not worth the corrosion management.
- Steel detent ring inserts (17-4 PH) explored for Mg parts — hex OD press-fit into hex counterbore with Loctite 620. Ring insert preferred over individual pins (pins drag across Mg between positions). Rejected when decision moved to all-7075.
- Magnesium coatings evaluated: e-coat (buries bead blast), PEO/Keronite (grey/white, hard to get black), Cerakote H-series (thin, black, tough, shows texture — best option for Mg). Moot after moving to 7075.
- Ball detent approach considered — much simpler but produces 5-10× less holding force than Belleville approach. Insufficient for branch-strike and abuse resistance.
- Belleville count: 4 vs 6 analyzed. 4 washers give same force but only 1.17mm usable travel — too tight for 1.5mm detent depth. 6 washers chosen.
- Green part wall thinning in Belleville guide zone: reduced from ~2mm to 1.0-1.2mm. Saved 4g/hinge. Overlap zone kept at 2.0-2.5mm for concentricity.
- **PEEK bushings eliminated.** Centering moved from shoulder screw to green-on-yellow (top) and green-on-purple (bottom) cylindrical overlaps. All interfaces are anodized 7075 on anodized 7075 — Type III hard anodize (alumina ceramic) provides both galvanic isolation and wear resistance. Shoulder screw is axial retention only, green part bore has clearance around shaft.
- **Trapezoidal ridge replaces pointed V-ridge.** Flat top added. Pointed V concentrates full Belleville preload on a tiny contact patch while sliding across plateaus — gouges anodize. Trapezoidal flat top distributes load face-to-face during transition. No effect on breakout torque (same wall angle, same preload).
- **Radial-plane detent walls** (slope faces point at shaft center) — ensures ridge engages full wall simultaneously during rotation. Corrected from earlier straight/planar approach which caused uneven engagement.
- Split Belleville spec (0.9mm front, 1.0mm rear) to equalize arm tip feel across different arm lengths. Common green lug achieved by using different shim thicknesses (0.80mm front, 0.50mm rear) — same cavity depth, same purple bracket.
