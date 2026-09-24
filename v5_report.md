# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T15:42:00.530527+00:00
État : OK | marchés EUR : 426 | V4 : 389 | données valides : 426
Récupération : 2026-09-24T15:41:29.490971+00:00 | âge ticker : 146.6 s | durée : 147.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.26766 € | IGNITION | score 92.10/100 | entrée 7.40/10
  Entrée 0.269 € ; stop 0.25665 € ; TP1 0.2937 € ; TP2 0.30605 € ; montant 227.49 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 4.179/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- TAIKO-EUR : 0.07857 € | IGNITION | score 81.74/100 | entrée 7.00/10
  Entrée 0.07863 € ; stop 0.07519 € ; TP1 0.08551 € ; TP2 0.08895 € ; montant 237.17 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 2.202/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CAKE-EUR : 2.4235 € ; score 90.32/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SOL-EUR : 102.188 € ; score 89.26/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DBR-EUR : 0.017677 € ; score 87.19/100 ; SURVEILLE ; WICK_SETUP
- CHIP-EUR : 0.038292 € ; score 84.57/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD
- AVA-EUR : 0.23291 € ; score 84.20/100 ; SURVEILLE ; WIDE_SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0020482 | +39.13 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LSK-EUR | 0.33813 | +27.53 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.45605 | +25.62 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 64.819 | +23.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0009575 | +22.27 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.10119 | +21.87 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.036076 | +19.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.2263 | +17.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0157087 | +15.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ETC-EUR | 8.9414 | +15.46 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1365 scans ; 584227 observations ; 718 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
