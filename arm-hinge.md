# Folding Arm Hinge Design

## Overview
Belleville washer preloaded detent hinge. Two positions: deployed + folded. Breakaway design — arm folds on impact as a safety fuse (no hard stop). Tactile feel target: M4 charging handle.

## Architecture
- **Hinge axis:** Vertical, one per side, coaxial (front + rear arms share same vertical hinge axis per side)
- **Fold direction:** Horizontal — arms swing inward to fold
- **Green part (rotating):** Holds carbon tube, contains Belleville stack, has detent ridges. Swings with arm.
- **Yellow part (fixed):** Integral boss on frame. Has detent grooves (4 total), shoulder screw threaded hole.
- **Purple cap:** Separate part, retains Bellevilles on shaft from below. Cannot be integrated into green part (Bellevilles need to be installed through bore).
- **Shoulder screw:** Fixed into yellow/frame. Green part rotates around the shoulder.

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
- Then green bore contacts yellow boss — **cylindrical fit is primary bending load path.**
- Bore-to-boss fit: H7/g6 slip fit. Bearing length sets wobble and contact stress.
- Shoulder screw is retention/shear only, not the primary bending member.

## Materials
- Green part (inner lug): **7075-T6 aluminum**, 15g each per BOM
- Yellow part: **7075-T6 aluminum** (integral to frame)
- Finish: **Type III hard anodize (black, 50+ micron)**
  - Provides: color, wear resistance on detent faces, corrosion protection, bead blast texture visible
  - Detent faces: anodized 7075 on anodized 7075 (proven wear pair)
- Bellevilles: 17-7 PH stainless steel
- Shoulder screw: titanium (weight savings)
- Bushings: PEEK (galvanic isolation + bearing surface)
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
- PEEK washer between bottom Belleville and green part internal ledge (galvanic isolation)

## Detent Geometry
- **2 positions** (deployed + folded), **2 detents per position** (180° apart, balanced — prevents tilting moment on shaft)
- 4 grooves total in yellow part, 2 ridges on green part
- Detent radius: ~9mm from shaft center
- Detent depth: 1.5mm
- Ridge: 2.5mm wide at base, R0.75mm rounded tip (rounded to prevent Type III anodize cracking)
- Groove: 3.5mm wide at top, 1.0mm flat bottom, R0.5mm bottom fillet, R0.3mm top edge break
- Wall angle: **45° from horizontal** (selected for mil use — provides 4.2× safety factor at max thrust on front arm)
- Flat plateau between grooves: 3-4mm (provides steady resistance during fold action)
- Radial feature width: 3-4mm (R=7.5 to R=10.5mm)
- Breakout torque at 45°: **13.2 N-m**

## Breakout Force at Arm Tip (200mm arm)
| Wall angle | Tip force | Breakout torque | SF at max thrust (front) |
|---|---|---|---|
| 30° | 38N / 8.6 lbs | 7.6 N-m | 2.4× |
| 45° | 66N / 14.9 lbs | 13.2 N-m | 4.2× |
| 60° | 114N / 25.7 lbs | 22.9 N-m | 7.3× |

45° selected: M4 charging handle feel + adequate margin for branch strikes.

## Green Part Wall Thickness
- **Overlap/bearing zone** (where green mates with yellow): 2.0-2.5mm walls. Concentricity-critical.
- **Belleville guide zone** (lower barrel): 1.0-1.2mm walls. Just prevents washer lateral walk. Thinned from original design — saved 4g per hinge (16g total).
- **Transition ledge** between zones: 2mm height, R0.5mm internal fillet. Bears Belleville preload (~6.5 MPa, trivial vs 500 MPa yield).
- Lightening pockets: aggressive in guide zone, conservative in overlap zone.

## Rib and General Wall Minimums (7075-T6)
- Perimeter walls: 1.5mm min, 2.0mm comfortable
- Ribs: 1.0mm min, 1.2mm comfortable
- Overlap zone (double wall): 1.2-1.5mm per wall
- Bore wall around shoulder screw: 2.5mm min (highest stress)
- Practical limit is machinability, not strength — below 1.5mm walls chatter during milling

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
- Magnesium (AZ31) considered for green/yellow parts — rejected due to galvanic corrosion complexity (carbon tube, steel Bellevilles, steel screw all bad couples with Mg), detent wear (Mg too soft), and need for steel ring inserts that added back complexity/weight. Weight savings was ~10-12g/hinge but not worth the corrosion management.
- Steel detent ring inserts (17-4 PH) explored for Mg parts — hex OD press-fit into hex counterbore with Loctite 620. Ring insert preferred over individual pins (pins drag across Mg between positions). Rejected when decision moved to all-7075.
- Magnesium coatings evaluated: e-coat (buries bead blast), PEO/Keronite (grey/white, hard to get black), Cerakote H-series (thin, black, tough, shows texture — best option for Mg). Moot after moving to 7075.
- Ball detent approach considered — much simpler but produces 5-10× less holding force than Belleville approach. Insufficient for branch-strike resistance and thrust moment resistance.
- Belleville count: 4 vs 6 analyzed. 4 washers give same force but only 1.17mm usable travel — too tight for 1.5mm detent depth. 6 washers chosen.
- Green part wall thinning in Belleville guide zone: reduced from ~2mm to 1.0-1.2mm. Saved 4g/hinge. Overlap zone kept at 2.0-2.5mm for concentricity.
