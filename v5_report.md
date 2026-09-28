# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T19:03:47.817472+00:00
État : OK | marchés EUR : 428 | V4 : 404 | données valides : 427
Récupération : 2026-09-28T19:02:45.640648+00:00 | âge ticker : 178.8 s | durée : 179.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.20481 € | IGNITION | score 93.64/100 | entrée 7.70/10
  Entrée 0.20485 € ; stop 0.19512 € ; TP1 0.22431 € ; TP2 0.23404 € ; montant 220.86 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 5.115/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- JUP-EUR : 0.2932 € ; score 91.55/100 ; SURVEILLE ; seuil achat non atteint
- SENT-EUR : 0.018238 € ; score 90.82/100 ; SURVEILLE ; seuil achat non atteint
- VIRTUAL-EUR : 0.72097 € ; score 89.34/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : 0.1942 € ; score 86.05/100 ; SURVEILLE ; seuil achat non atteint
- PHA-EUR : 0.052976 € ; score 85.98/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.112297 | +34.41 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 214.258 | +27.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.117411 | +12.30 % | DETECTED_EARLY | NONE | NONE |
| XDC-EUR | 0.031873 | +12.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 9.9535 | +11.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0018397 | +10.55 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MIOTA-EUR | 0.048931 | +9.35 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| LINK-EUR | 13.3644 | +7.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XLM-EUR | 0.20481 | +7.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| LINEA-EUR | 0.0027264 | +5.84 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1714 scans ; 733265 observations ; 1264 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
