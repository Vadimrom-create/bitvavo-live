# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T17:24:30.677728+00:00
État : OK | marchés EUR : 428 | V4 : 404 | données valides : 427
Récupération : 2026-09-28T17:24:01.462462+00:00 | âge ticker : 143.6 s | durée : 145.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- XDC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- OP-EUR : 0.12019 € ; score 90.66/100 ; SURVEILLE ; seuil achat non atteint
- TIA-EUR : 0.39997 € ; score 89.24/100 ; SURVEILLE ; seuil achat non atteint
- LINK-EUR : 13.4787 € ; score 87.87/100 ; SURVEILLE ; seuil achat non atteint
- AERO-EUR : 0.71569 € ; score 87.73/100 ; SURVEILLE ; WICK_SETUP
- JASMY-EUR : 0.0045411 € ; score 87.64/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HBAR-EUR | 0.111729 | +35.93 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 218.321 | +33.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.119239 | +15.64 % | DETECTED_EARLY | NONE | NONE |
| IKA-EUR | 0.0018822 | +13.11 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| NMR-EUR | 9.7261 | +11.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MIOTA-EUR | 0.048754 | +10.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MON-EUR | 0.025609 | +10.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PUMP-EUR | 0.004687 | +9.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LINK-EUR | 13.4787 | +8.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.027443 | +8.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1708 scans ; 730697 observations ; 1264 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
