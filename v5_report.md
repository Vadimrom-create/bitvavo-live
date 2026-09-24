# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T21:34:18.150997+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-24T21:33:45.948019+00:00 | âge ticker : 156.8 s | durée : 157.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 127.95 € ; score 90.83/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- APE-EUR : 0.13303 € ; score 90.53/100 ; SURVEILLE ; seuil achat non atteint
- BEAM-EUR : 0.0017853 € ; score 90.39/100 ; SURVEILLE ; WICK_SETUP
- ACE-EUR : 0.16209 € ; score 88.43/100 ; SURVEILLE ; WICK_SETUP
- DATAIP-EUR : 0.1968 € ; score 88.21/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| XAI-EUR | 0.009283 | +33.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LSK-EUR | 0.39573 | +29.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PEAQ-EUR | 0.039401 | +28.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ONDO-EUR | 0.45789 | +26.23 % | DETECTED_EARLY | NONE | NONE |
| XPL-EUR | 0.099127 | +25.00 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 77.339 | +23.89 % | DETECTED_EARLY | NONE | NONE |
| ARK-EUR | 0.1695 | +22.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.5647 | +22.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.100567 | +19.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| FET-EUR | 0.20342 | +17.31 % | DETECTED_EARLY | NONE | NONE |

Historique : 1392 scans ; 595752 observations ; 764 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
