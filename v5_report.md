# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T19:13:20.784735+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-21T19:12:46.209579+00:00 | âge ticker : 155.4 s | durée : 156.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- STX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 251.3 € | IGNITION | score 83.64/100 | entrée 6.60/10
  Entrée 251.65 € ; stop 240.67 € ; TP1 273.61 € ; TP2 284.59 € ; montant 237.72 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 2.369/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ATH-EUR : 0.0048025 € ; score 91.85/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XTZ-EUR : 0.30455 € ; score 91.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GRASS-EUR : 0.32522 € ; score 89.45/100 ; SURVEILLE ; WICK_SETUP
- NMR-EUR : 8.1505 € ; score 82.83/100 ; SURVEILLE ; seuil achat non atteint
- VET-EUR : 0.0078217 € ; score 81.14/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.00176 | +128.69 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.013948 | +65.46 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.053069 | +58.09 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| SWELL-EUR | 0.00094 | +44.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.044781 | +40.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.31106 | +38.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010232 | +34.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.103648 | +30.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.335e-06 | +24.29 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.230171 | +23.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1104 scans ; 473041 observations ; 402 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
