# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T06:30:37.521816+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-09-23T06:30:03.847939+00:00 | âge ticker : 149.8 s | durée : 150.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 2.6694 € ; score 91.15/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : 8.3492 € ; score 86.31/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 132.7 € ; score 86.29/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 56.047 € ; score 86.19/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- MAVIA-EUR : 0.030007 € ; score 84.79/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NIL-EUR | 0.098111 | +51.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| BCH-EUR | 311.96 | +35.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.31427 | +32.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.031832 | +29.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.0195 | +26.30 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| TREAD-EUR | 0.48275 | +25.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.1629 | +24.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.2611 | +23.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.0094917 | +20.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.292905 | +20.61 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1249 scans ; 534811 observations ; 603 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
