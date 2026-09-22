# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T21:06:41.285050+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-09-22T21:06:10.470781+00:00 | âge ticker : 146.7 s | durée : 147.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ETC-EUR : 8.1796 € ; score 92.02/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AXL-EUR : 0.047064 € ; score 91.08/100 ; SURVEILLE ; LOW_LIQUIDITY, VERY_SELLER_HEAVY_BOOK
- WLD-EUR : 0.40545 € ; score 87.34/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TNSR-EUR : 0.03357 € ; score 86.25/100 ; SURVEILLE ; seuil achat non atteint
- TRX-EUR : 0.29857 € ; score 86.11/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| DRIFT-EUR | 0.019644 | +33.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CHR-EUR | 0.020174 | +30.05 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| BCH-EUR | 297.83 | +28.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.051906 | +22.54 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.29661 | +17.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.50493 | +17.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PENGU-EUR | 0.00882 | +16.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.193 | +16.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KITE-EUR | 0.12031 | +16.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.06843 | +15.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1216 scans ; 520753 observations ; 535 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
