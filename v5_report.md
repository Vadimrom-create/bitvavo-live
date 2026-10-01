# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T23:29:07.723863+00:00
État : OK | marchés EUR : 430 | V4 : 381 | données valides : 430
Récupération : 2026-10-01T23:28:32.618154+00:00 | âge ticker : 156.9 s | durée : 157.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- REZ-EUR : 0.0039597 € ; score 90.50/100 ; SURVEILLE ; seuil achat non atteint
- KMNO-EUR : 0.036246 € ; score 90.42/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AAVE-EUR : 153.67 € ; score 90.01/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KITE-EUR : 0.13468 € ; score 86.68/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WLD-EUR : 0.44678 € ; score 83.19/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00057 | +121.03 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.12892 | +56.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.5532 | +34.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.1857 | +25.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.43928 | +24.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04527 | +23.18 % | DETECTED_EARLY | NONE | NONE |
| NOM-EUR | 0.0024455 | +19.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.163441 | +16.51 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VELO-EUR | 0.0055168 | +14.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.49552 | +14.43 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1940 scans ; 830278 observations ; 1508 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
