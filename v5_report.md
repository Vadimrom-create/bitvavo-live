# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T23:33:50.515089+00:00
État : OK | marchés EUR : 428 | V4 : 399 | données valides : 428
Récupération : 2026-09-28T23:32:50.964034+00:00 | âge ticker : 183.2 s | durée : 184.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.72987 € | IGNITION | score 87.75/100 | entrée 7.20/10
  Entrée 0.73194 € ; stop 0.7012 € ; TP1 0.79342 € ; TP2 0.82416 € ; montant 245.64 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 2.891/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CHR-EUR : 0.018902 € ; score 90.85/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ARX-EUR : 0.22633 € ; score 90.45/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PHA-EUR : 0.053307 € ; score 86.50/100 ; SURVEILLE ; WICK_SETUP
- ETC-EUR : 8.1769 € ; score 85.91/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- W-EUR : 0.012061 € ; score 83.88/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 13.0881 | +44.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.106856 | +27.41 % | DETECTED_EARLY | NONE | NONE |
| ALGO-EUR | 0.118373 | +13.08 % | DETECTED_EARLY | NONE | NONE |
| LINK-EUR | 13.5393 | +10.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 0G-EUR | 0.25418 | +9.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0018274 | +9.73 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| CRV-EUR | 0.33729 | +9.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.048619 | +8.80 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| AZTEC-EUR | 0.016793 | +6.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XLM-EUR | 0.20098 | +6.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1729 scans ; 739685 observations ; 1270 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
