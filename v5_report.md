# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T02:48:09.662740+00:00
État : OK | marchés EUR : 426 | V4 : 404 | données valides : 426
Récupération : 2026-09-24T02:47:44.668337+00:00 | âge ticker : 140.1 s | durée : 140.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- INJ-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LTC-EUR : 57.184 € | IGNITION | score 85.16/100 | entrée 7.30/10
  Entrée 57.264 € ; stop 53.988 € ; TP1 63.816 € ; TP2 67.092 € ; montant 187.48 € ; risque théorique 12.00 € ; R/R net 1.67.
  Chase risk : 6.787/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- EIGEN-EUR : 0.21259 € | IGNITION | score 80.94/100 | entrée 6.90/10
  Entrée 0.21314 € ; stop 0.20348 € ; TP1 0.23246 € ; TP2 0.24212 € ; montant 230.05 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 6.76/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- PLUME-EUR : 0.0139265 € ; score 93.14/100 ; SURVEILLE ; seuil achat non atteint
- BONK-EUR : 3.1334e-06 € ; score 89.73/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MANTA-EUR : 0.061095 € ; score 88.93/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- VIRTUAL-EUR : 0.62612 € ; score 88.24/100 ; SURVEILLE ; seuil achat non atteint
- ROSE-EUR : 0.006702 € ; score 87.31/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.120851 | +50.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0020637 | +34.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SAGA-EUR | 0.041094 | +18.33 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.0296 | +15.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.3844 | +11.39 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.018099 | +11.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IMU-EUR | 0.0018709 | +10.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| LSK-EUR | 0.30635 | +10.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.033273 | +10.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0455862 | +9.88 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1322 scans ; 565909 observations ; 678 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
