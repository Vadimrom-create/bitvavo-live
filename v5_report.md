# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T14:45:49.288751+00:00
État : OK | marchés EUR : 427 | V4 : 384 | données valides : 427
Récupération : 2026-09-26T14:45:20.955890+00:00 | âge ticker : 143.9 s | durée : 144.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- OP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : 0.20159 € | IGNITION | score 87.71/100 | entrée 6.00/10
  Entrée 0.20187 € ; stop 0.19306 € ; TP1 0.21948 € ; TP2 0.22829 € ; montant 237.67 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 5.16/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LINK-EUR : 12.6523 € ; score 94.22/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.6887 € ; score 92.25/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- CFG-EUR : 0.14444 € ; score 91.43/100 ; SURVEILLE ; WICK_SETUP
- TIA-EUR : 0.44355 € ; score 91.13/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ENJ-EUR : 0.027363 € ; score 89.36/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0019054 | +129.40 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019812 | +63.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.12138 | +40.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0005857 | +32.51 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.065218 | +31.24 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.23792 | +23.03 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| KMNO-EUR | 0.043777 | +19.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PROM-EUR | 5.5339 | +15.74 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| RUNE-EUR | 0.64478 | +15.09 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ACE-EUR | 0.194 | +15.03 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1539 scans ; 658521 observations ; 995 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
