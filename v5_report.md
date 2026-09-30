# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T06:28:41.593494+00:00
État : OK | marchés EUR : 429 | V4 : 389 | données valides : 429
Récupération : 2026-09-30T06:28:05.437128+00:00 | âge ticker : 154.0 s | durée : 154.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XDC-EUR : 0.029641 € ; score 84.20/100 ; SURVEILLE ; seuil achat non atteint
- NMR-EUR : 10.343 € ; score 82.71/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- COMP-EUR : 22.428 € ; score 82.20/100 ; SURVEILLE ; STABILITY_HOLD
- CRV-EUR : 0.34434 € ; score 81.72/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- C-EUR : 0.081692 € ; score 81.67/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.3018 | +52.54 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.37552 | +40.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0023165 | +21.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00050259 | +20.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.6121 | +19.35 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 257.31 | +18.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.0049941 | +16.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.30831 | +15.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.24346 | +15.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.0924 | +15.33 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1822 scans ; 779548 observations ; 1361 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
