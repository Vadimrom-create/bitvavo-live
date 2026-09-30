# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T07:36:52.216221+00:00
État : OK | marchés EUR : 429 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T07:36:21.649947+00:00 | âge ticker : 153.1 s | durée : 154.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ICP-EUR : 3.0249 € ; score 90.21/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BIGTIME-EUR : 0.008132 € ; score 85.46/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP
- HBAR-EUR : 0.093152 € ; score 82.97/100 ; SURVEILLE ; seuil achat non atteint
- COMP-EUR : 22.434 € ; score 80.43/100 ; SURVEILLE ; seuil achat non atteint
- XLM-EUR : 0.19687 € ; score 80.37/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.4221 | +65.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.38791 | +42.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.098266 | +28.90 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ARK-EUR | 0.25406 | +19.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.00782 | +17.93 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZBCN-EUR | 0.0022797 | +17.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.0004905 | +16.61 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 251.592 | +16.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.0674 | +15.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.30083 | +14.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1825 scans ; 780835 observations ; 1362 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
