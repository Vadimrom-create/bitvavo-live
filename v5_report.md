# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T18:47:01.306141+00:00
État : OK | marchés EUR : 428 | V4 : 404 | données valides : 427
Récupération : 2026-09-28T18:46:29.594746+00:00 | âge ticker : 159.4 s | durée : 160.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- VIRTUAL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.20234 € | IGNITION | score 87.19/100 | entrée 8.20/10
  Entrée 0.20228 € ; stop 0.19476 € ; TP1 0.21731 € ; TP2 0.22483 € ; montant 250.00 € ; risque théorique 11.01 € ; R/R net 1.52.
  Chase risk : 5.057/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AERO-EUR : 0.72067 € ; score 84.05/100 ; SURVEILLE ; WICK_SETUP
- PHA-EUR : 0.052523 € ; score 83.84/100 ; SURVEILLE ; WICK_SETUP
- MIOTA-EUR : 0.04833 € ; score 83.46/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- XPL-EUR : 0.088437 € ; score 82.66/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 13.3049 € ; score 81.02/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.111198 | +33.72 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 210.603 | +27.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.118769 | +13.33 % | DETECTED_EARLY | NONE | NONE |
| XDC-EUR | 0.03143 | +11.58 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0018317 | +10.07 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| MIOTA-EUR | 0.04833 | +8.20 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NMR-EUR | 9.7711 | +8.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MON-EUR | 0.025519 | +7.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LINK-EUR | 13.3049 | +7.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XLM-EUR | 0.20234 | +5.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1713 scans ; 732837 observations ; 1264 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
