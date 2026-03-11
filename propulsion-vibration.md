# Propulsion Vibration Analysis

## System Parameters
- AUW: 2 kg (quad)
- Props: 12.5" diameter, 3-blade
- Motors: 75g each
- Blade assembly (3 blades + hub): 24g
- Motor mount: 15g (BOM shows 10g — verify)
- Total tip mass: ~125g (incl. wiring/ESC)

## Arm Geometry
| | Front | Rear |
|---|---|---|
| Arm length | 200mm | 275mm |
| Motor Y (from hinge axis) | 209mm | 180mm |
| Tube spec | 20mm OD × 1mm wall | 20mm OD × 1mm wall |
| Tube type | Standard wound | **Pultruded** (higher modulus required) |

Hinge axes are **vertical**, one per side, coaxial (front + rear arm share same hinge axis per side). Arms fold horizontally.
Front arms spread wider than rear to clear gimbal payload.

## RPM Operating Points
| Condition | RPM |
|---|---|
| Idle/descent | ~2000 |
| Hover | 3500 |
| 15 m/s cruise | 4500 |
| Max throttle (sea level) | 6000 |

## Arm First Bending Mode
Calculation: f₁ = 1/(2π) × √(3EI / (L³ × (M_tip + 0.24 × m_beam)))

### Front Arms (200mm)
| Tube | E (GPa) | f₁ (Hz) |
|---|---|---|
| 20mm OD × 1mm wall | 70 (wound) | ~118 |
| 20mm OD × 1mm wall | 100 (uni-core) | ~141 |
| 22mm OD × 1mm wall | 70 (wound) | ~136 |

### Rear Arms (275mm)
| Tube | E (GPa) | f₁ (Hz) |
|---|---|---|
| 20mm OD × 1mm wall | 70 (wound) | ~73 — **bad, on cruise 1P** |
| 20mm OD × 1mm wall | 100 (uni-core) | ~87 |
| 20mm OD × 1mm wall | 130 (pultruded) | ~99 |
| 22mm OD × 1mm wall | 70 (wound) | ~80 — **bad, near cruise 1P** |

## Excitation Frequencies — Front Arms (f₁ ≈ 118 Hz, 20mm wound)
| Condition | RPM | 1P (Hz) | 3P (Hz) | Notes |
|---|---|---|---|---|
| 3P crosses f₁ | 2360 | 39 | **118** | Transient, low thrust |
| Hover | 3500 | 58 | 175 | 1P: 2.0× below, 3P: 1.48× above. **Safe.** |
| 15 m/s cruise | 4500 | 75 | 225 | 1P: 1.57× below, 3P: 1.9× above. **Safe.** |
| Max throttle | 6000 | 100 | 300 | 1P: 1.18× below — marginal but transient |

## Excitation Frequencies — Rear Arms (f₁ ≈ 99 Hz, 20mm pultruded)
| Condition | RPM | 1P (Hz) | 3P (Hz) | Notes |
|---|---|---|---|---|
| 3P crosses f₁ | 1980 | 33 | **99** | Transient, low thrust |
| Hover | 3500 | 58 | 175 | 1P: 1.71× below, 3P: 1.77× above. **Safe.** |
| 15 m/s cruise | 4500 | 75 | 225 | 1P: 1.32× below. **Adequate.** |
| Max throttle | 6000 | 100 | 300 | 1P: 1.01× — **on resonance, transient only** |

## Tube Selection Decision
- **Front arms:** 20mm OD × 1mm wall, standard wound carbon. Adequate margins at all sustained conditions.
- **Rear arms:** 20mm OD × 1mm wall, **pultruded carbon** (E ≈ 130 GPa). Required to avoid 1P resonance at cruise. Standard wound (E=70) puts f₁ at 73 Hz — directly on 1P at cruise (75 Hz). Pultruded not ideal at max throttle (1P ≈ f₁) but max throttle is transient.
- Same 20mm OD for all arms keeps motor mounts and inner lugs identical.
- Pultruded tradeoff: weaker in torsion/crush (all uni fiber), but bending-dominated application — acceptable. Split clamp distributes tube clamping loads.

## Key Conclusions
- 1P = shaft frequency (prop imbalance). 3P = blade pass frequency (primary excitation for 3-blade).
- Front arm resonance sits safely between 1P and 3P at all sustained operating points.
- Rear arms are the critical case due to 275mm length — **pultruded tubes mandatory.**
- Custom higher-modulus wound layup not justified — pultruded is off-the-shelf and sufficient.
- Most drones in this class manage residual arm vibration via FC notch filters + soft mounting.

## Vibration Amplification Reference
Amplification factor = 1 / |1 - (f/f_n)²|
- At 1.5× separation: ~1.8× amplification
- At 2.0× separation: ~1.3× amplification
- At 1.18× separation: ~3.5× amplification (avoid sustained operation here)
