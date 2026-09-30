# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T07:56:38.118559+00:00
État : OK | marchés EUR : 429 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T07:55:40.552046+00:00 | âge ticker : 186.5 s | durée : 188.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.20782 € | IGNITION | score 86.01/100 | entrée 6.80/10
  Entrée 0.20783 € ; stop 0.19956 € ; TP1 0.22436 € ; TP2 0.23263 € ; montant 250.00 € ; risque théorique 11.66 € ; R/R net 1.55.
  Chase risk : 2.105/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- BABY-EUR : 0.012657 € | IGNITION | score 80.25/100 | entrée 6.90/10
  Entrée 0.012666 € ; stop 0.012167 € ; TP1 0.013663 € ; TP2 0.014162 € ; montant 250.00 € ; risque théorique 11.56 € ; R/R net 1.54.
  Chase risk : 1.122/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- HBAR-EUR : 0.094002 € ; score 93.42/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.19858 € ; score 91.90/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PLUME-EUR : 0.0160616 € ; score 91.51/100 ; SURVEILLE ; seuil achat non atteint
- POL-EUR : 0.101648 € ; score 91.31/100 ; SURVEILLE ; WICK_SETUP
- BIGTIME-EUR : 0.008132 € ; score 90.62/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.4942 | +73.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.38747 | +37.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.104449 | +36.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GNS-EUR | 0.51946 | +22.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.007891 | +18.84 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| 0G-EUR | 0.29889 | +17.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0022553 | +16.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.5873 | +15.93 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.005084 | +15.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.068619 | +14.64 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1826 scans ; 781264 observations ; 1363 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
