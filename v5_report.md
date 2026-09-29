# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T21:41:22.532556+00:00
État : OK | marchés EUR : 429 | V4 : 395 | données valides : 429
Récupération : 2026-09-29T21:40:48.633889+00:00 | âge ticker : 148.6 s | durée : 150.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- NOM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : 1.4241 € | IGNITION | score 92.57/100 | entrée 7.45/10
  Entrée 1.4245 € ; stop 1.3684 € ; TP1 1.5367 € ; TP2 1.5928 € ; montant 250.00 € ; risque théorique 11.56 € ; R/R net 1.55.
  Chase risk : 2.89/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ENA-EUR : 0.22078 € ; score 91.55/100 ; SURVEILLE ; WICK_SETUP
- LINEA-EUR : 0.0025506 € ; score 88.17/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK
- ROSE-EUR : 0.007936 € ; score 84.54/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- W-EUR : 0.012184 € ; score 82.02/100 ; SURVEILLE ; seuil achat non atteint
- FLR-EUR : 0.0066187 € ; score 81.99/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GRASS-EUR | 0.66258 | +31.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| POND-EUR | 0.0016677 | +29.28 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.0599 | +25.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0021501 | +20.41 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.35801 | +19.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.28619 | +19.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PUMP-EUR | 0.0051468 | +17.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.060395 | +15.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICP-EUR | 3.0391 | +14.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRB-EUR | 18.687 | +14.61 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1795 scans ; 767965 observations ; 1339 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
