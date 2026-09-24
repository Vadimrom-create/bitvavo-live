# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T15:23:49.784881+00:00
État : OK | marchés EUR : 426 | V4 : 389 | données valides : 426
Récupération : 2026-09-24T15:23:15.079368+00:00 | âge ticker : 150.6 s | durée : 151.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- INJ-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.21744 € | IGNITION | score 77.13/100 | entrée 7.20/10
  Entrée 0.2174 € ; stop 0.20812 € ; TP1 0.23596 € ; TP2 0.24524 € ; montant 242.24 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 4.368/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- STX-EUR : 0.27637 € ; score 88.48/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.059696 € ; score 87.61/100 ; SURVEILLE ; seuil achat non atteint
- CAKE-EUR : 2.3912 € ; score 85.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SUSHI-EUR : 0.22499 € ; score 85.47/100 ; SURVEILLE ; WICK_SETUP
- BIGTIME-EUR : 0.007248 € ; score 83.55/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.002011 | +35.27 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LSK-EUR | 0.33345 | +23.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.45279 | +22.98 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 64.388 | +20.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.10007 | +18.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEAQ-EUR | 0.034959 | +15.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.22118 | +14.37 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ETC-EUR | 8.8283 | +12.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.015415 | +12.23 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAT-EUR | 2.0688e-06 | +11.58 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1364 scans ; 583801 observations ; 718 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
