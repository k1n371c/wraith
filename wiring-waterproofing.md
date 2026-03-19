# Wiring, Connectors & Waterproofing

## Motor Wiring Through Hinge

- 3-phase motor wires run inside hollow carbon arm tubes (18mm ID)
- Wires exit tube at the split clamp end of the green inner lug
- Service loop near hinge axis crosses the fold joint — close to axis minimizes bending during fold/deploy
- Secure loop to green lug with cable tie mount so it rotates with the arm

## Motor Wire Connectors

- Vehicle-side connectors are bulkhead-mounted on the blue frame bracket (fixed position, strain-relieved)
- Arm-side plugs in from outside — unplug to swap an arm
- Inline bullet connectors (3× 2mm) are simplest: TE or Molex crimp terminals, ~1g total
- Phase order not enforced with individual bullets — color-code wires or use asymmetric spacing
- Amass MR30 (3-pin, 30A, keyed) is ideal but Chinese-sourced — no US/EU alternative exists at that size/current
- Molex Mini-Fit Jr (13A/pin) works if peak phase current stays under 13A — actual peak is ~29A at max throttle/low voltage, so too small
- Anderson Powerpole 30A or Deutsch DT size 12 (25A) are non-Chinese options but physically large

## RF Connectors

- SMPM: 3.2mm OD, DC-65 GHz, push-on, Amphenol/SV Microwave (US)
- MMCX: 2.4mm OD, DC-6 GHz, snap-on, Amphenol/TE (US) — smaller than SMPM
- **Selected: Amphenol RF 262148** — MMCX straight crimp jack, 1.37mm micro-cable, bulkhead rear mount, 50Ω
- Seal with custom o-ring around the bulkhead flange in a counterbore
- U.FL: no bulkhead variant exists, PCB-mount only

## Waterproofing Small Enclosures (50×50×10mm)

### Sealing Approach — All Mechanical (No Sealant/Potting)

**RF penetrations:** MMCX bulkhead (262148) with o-ring in machined counterbore
**USB-C penetrations:** Panel-mount USB-C with integrated gasket/o-ring
**Cable pass-throughs:** Compression cable glands (Heyco/Sealcon, smallest size ~2-3mm cable OD)
**Housing seam:** Perimeter gasket in machined groove, bolted closed
**O-ring sizing:** Per Parker O-Ring Handbook for counterbore/groove dimensions

All seals are inspectable, re-openable, no cure times, no voids.

### PCB Assembly Into Sealed Housing
- Right-angle connectors on 3 sides prevents drop-in assembly
- **Solution: slide-in from the 4th side (no connectors)**
  - Housing is U-shape + bottom with one open side
  - PCB slides in, all 3 connector sets enter wall holes in one motion
  - 4th wall panel bolts on last, sealed with gasket
  - Lead-in chamfers on wall holes for alignment tolerance

## Sourcing Constraints
- No Chinese sourcing
- Amass MR30/XT30 are ideal but restricted — no Western equivalent exists at 30A in that form factor
- Amphenol, TE, Molex, Deutsch, Anderson are approved sources
- Niche opportunity: US-made 30A micro motor connector for defense drone market
