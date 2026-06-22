# SA-beta-Galactosidase Senescence Calculator

A lightweight Python utility designed for biologists to rapidly quantify cellular senescence from manual microscopy data.

## Features
- **Multi-FOV Tracking:** Aggregates raw cell counts across multiple fields of view (FOV) to ensure statistical robustness.
- **Automated Indexing:** Calculates the overall percentage of SA-beta-gal positive cells.
- **Biological Interpretation:** Categorizes the culture's physiological state based on established senescence thresholds.

## Background
Senescence-associated beta-galactosidase (SA-beta-gal) staining remains a golden standard for identifying senescent cells *in vitro*. Cells exhibiting increased lysosomal beta-gal activity turn blue under brightfield microscopy. 
- **< 20%**: Proliferating, healthy culture.
- **20% - 60%**: Early or transitionary moderate senescence.
- **> 60%**: Pronounced senescence, typically associated with the Senescence-Associated Secretory Phenotype (SASP).

## How to Run
Ensure you have Python 3.x installed. Run the script via your terminal:
```bash
python senescence_calculator.py
