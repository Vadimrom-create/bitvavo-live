# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T04:00:49.960489+00:00
État : OK | marchés EUR : 429 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T04:00:19.853504+00:00 | âge ticker : 159.5 s | durée : 160.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- COW-EUR : 0.14574 € ; score 91.94/100 ; SURVEILLE ; LOW_LIQUIDITY
- SPK-EUR : 0.020609 € ; score 90.39/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- NOM-EUR : 0.0018689 € ; score 90.18/100 ; SURVEILLE ; seuil achat non atteint
- AZTEC-EUR : 0.015006 € ; score 87.06/100 ; SURVEILLE ; seuil achat non atteint
- ATOM-EUR : 1.5091 € ; score 85.62/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00181 | +42.52 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.35628 | +35.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.122 | +33.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 261.881 | +24.86 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ZBCN-EUR | 0.0023444 | +23.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0050332 | +19.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00048779 | +18.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| INIT-EUR | 0.091034 | +17.89 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.5793 | +16.58 % | DETECTED_EARLY | NONE | NONE |
| PHA-EUR | 0.062494 | +14.99 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1815 scans ; 776545 observations ; 1354 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
