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

## Load Path — Detent (Critical)
**The detent resists thrust-induced folding moment.** Because the hinge axis is vertical and thrust is vertical, thrust creates a moment about the hinge axis that tries to fold/unfold the arm. The detent is the primary structural element resisting this.

| | Front | Rear |
|---|---|---|
| Motor Y distance from hinge axis | 209mm | 180mm |
| Hover thrust moment (5N/motor) | 1.05 N-m | 0.90 N-m |
| Max thrust moment (15N/motor) | 3.14 N-m | 2.70 N-m |
| **Detent breakout torque (45° wall)** | **13.2 N-m** | **13.2 N-m** |
| **Safety factor at max thrust** | **4.2×** | **4.9×** |

Front arm is the critical case (wider spread for gimbal clearance → longer moment arm).

## Load Path — Bending
- Thrust and arm weight create bending loads perpendicular to the hinge axis.
- Small deflections absorbed by Belleville stack (off-axis compression).
- **Detent ridges/grooves are the primary tilt constraint** — Belleville preload (1,468N) on 45° walls at ~9mm radius creates a strong restoring moment against any tilt.
- **Centering: green part rides on yellow boss (top) and purple bracket (bottom).** Short cylindrical overlaps at each end, hard-anodized 7075 on hard-anodized 7075 — same proven wear pair as detent faces. Sliding fit accommodates both rotation and 1.5mm axial travel during fold action.
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
- Carbon tube interface: fiberglass liner or G10 sleeve (galvanic isolation)

## Belleville Washers
- Part: McMaster 96475K247
- Spec: 20mm OD, 10.2mm ID, 1mm thick, 1.55mm free height (h=0.55mm)
- Working load: 330 lbf / 1,468 N at 0.39mm deflection
- Flat load: 441 lbf / 1,962 N at 0.55mm deflection
- Material: 17-7 PH stainless, DIN 2093
- Stack: **6 in series** (alternating orientation)
  - Force: 1,468 N (same as single washer)
  - Total travel: 2.34mm
  - Usable travel at 75% life: 1.75mm
- QPV: 24 (6 per hinge × 4 hinges), BOM total 43.9g
- Stainless shim washers at each end of stack (protect surfaces from Belleville edge loading, rotate with stack). Galvanic isolation between stainless and anodized 7075 provided by Type III anodize layer (alumina ceramic insulator).

## Detent Geometry
- **2 positions** (deployed + folded), **2 detents per position** (180° apart, balanced — prevents tilting moment on shaft)
- 4 grooves total in yellow part, 2 ridges on green part
- Detent radius: ~9mm from shaft center
- Detent depth: 1.5mm
- **Ridge profile (trapezoidal):** 1.5mm flat top, 45° walls each side, R0.75mm fillets at top edges (flat-to-wall transitions). Base width: 4.5mm (1.5 + 2×1.5). Trapezoidal chosen over pointed V — flat top distributes contact stress during sliding across plateaus between positions, prevents anodize gouging under full Belleville preload.
- **Groove profile:** 2.0mm flat bottom, 45° walls, R0.5mm bottom fillets (endmill corner radius), R0.3mm top edge break. Top width: 5.0mm (2.0 + 2×1.5). Ridge does not bottom out in groove — clearance between ridge flat top and groove flat bottom when seated.
- Wall angle: **45° from horizontal** (selected for mil use — provides 4.2× safety factor at max thrust on front arm)
- Flat plateau between grooves: 3-4mm (provides steady resistance during fold action)
- Radial feature extent: 4mm. Wider is better for contact stress distribution, but diminishing returns past ~4mm.
- **Feature geometry: straight/planar walls** (not radial/pie-slice). All wall surfaces are flat planes at 45° — machinable in a single tool pass. Plan-view edges are parallel straight lines, not converging to center. Slight geometric deviation from true radial at 4mm extent on ~9mm radius is negligible.
- Breakout torque at 45°: **13.2 N-m**

## Breakout Force at Arm Tip (200mm arm)
| Wall angle | Tip force | Breakout torque | SF at max thrust (front) |
|---|---|---|---|
| 30° | 38N / 8.6 lbs | 7.6 N-m | 2.4× |
| 45° | 66N / 14.9 lbs | 13.2 N-m | 4.2× |
| 60° | 114N / 25.7 lbs | 22.9 N-m | 7.3× |

45° selected: M4 charging handle feel + adequate margin for branch strikes.

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

## Weight — BOM Actuals (per hinge set, all 4 hinges)
| Part | QPV | Unit weight | Total |
|---|---|---|---|
| Belleville springs | 24 | 1.83g | 43.9g |
| Hinge screws | 4 | 2.73g | 10.9g |
| Caps | 4 | 2.77g | 11.1g |
| Shim washers | 8 | 0.50g | 4.0g |
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
- Ball detent approach considered — much simpler but produces 5-10× less holding force than Belleville approach. Insufficient for branch-strike resistance and thrust moment resistance.
- Belleville count: 4 vs 6 analyzed. 4 washers give same force but only 1.17mm usable travel — too tight for 1.5mm detent depth. 6 washers chosen.
- Green part wall thinning in Belleville guide zone: reduced from ~2mm to 1.0-1.2mm. Saved 4g/hinge. Overlap zone kept at 2.0-2.5mm for concentricity.
- **PEEK bushings eliminated.** Centering moved from shoulder screw to green-on-yellow (top) and green-on-purple (bottom) cylindrical overlaps. All interfaces are anodized 7075 on anodized 7075 — Type III hard anodize (alumina ceramic) provides both galvanic isolation and wear resistance. Shoulder screw is axial retention only, green part bore has clearance around shaft.
- **Trapezoidal ridge replaces pointed V-ridge.** 1.5mm flat top added. Pointed V (R0.75mm tip) concentrates full Belleville preload on a tiny contact patch while sliding across plateaus between detent positions — gouges anodize. Trapezoidal flat top distributes load face-to-face during transition. No effect on breakout torque (same wall angle, same preload).
- **Straight/planar detent walls chosen over radial/pie-slice.** Radial (converging-to-center) walls create twisted ruled surfaces that can't be cut in a single tool pass. Straight walls are flat planes at 45° — one-pass machinable. At 4mm radial extent on ~9mm radius, the geometric deviation from true radial is negligible.
