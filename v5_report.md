# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T01:23:16.583958+00:00
État : OK | marchés EUR : 427 | V4 : 387 | données valides : 427
Récupération : 2026-09-26T01:22:42.816321+00:00 | âge ticker : 156.4 s | durée : 157.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CAKE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PENGU-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : 1.098 € | IGNITION | score 91.97/100 | entrée 7.50/10
  Entrée 1.0986 € ; stop 1.0516 € ; TP1 1.1925 € ; TP2 1.2395 € ; montant 241.78 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 3.921/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AAVE-EUR : 136.64 € ; score 93.53/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : 0.22891 € ; score 91.46/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : 0.026769 € ; score 88.89/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.033072 € ; score 86.80/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 64.107 € ; score 86.62/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0013562 | +73.21 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.073876 | +65.14 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.22259 | +38.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.103999 | +36.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.06773 | +22.64 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.7266 | +18.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 0.712 | +16.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WMTX-EUR | 0.022056 | +16.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CC-EUR | 0.11659 | +15.20 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ENA-EUR | 0.2336 | +14.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1491 scans ; 638025 observations ; 917 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
