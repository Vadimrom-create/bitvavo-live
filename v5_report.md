# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T13:53:50.027907+00:00
État : OK | marchés EUR : 428 | V4 : 401 | données valides : 427
Récupération : 2026-09-28T13:53:14.610790+00:00 | âge ticker : 157.9 s | durée : 159.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/428 ; 15 min 427/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- RPL-EUR : 1.7309 € ; score 88.12/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- AXL-EUR : 0.046226 € ; score 87.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- HUMA-EUR : 0.024622 € ; score 87.28/100 ; SURVEILLE ; seuil achat non atteint
- CHIP-EUR : 0.039656 € ; score 84.29/100 ; SURVEILLE ; seuil achat non atteint
- BAT-EUR : 0.08053 € ; score 83.11/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 213.868 | +51.60 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.105284 | +27.60 % | DETECTED_EARLY | NONE | NONE |
| XDP-EUR | 0.031439 | +24.27 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRT-EUR | 0.028114 | +14.93 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 9.8148 | +14.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.117496 | +14.23 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.0045645 | +13.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DGB-EUR | 0.0042711 | +10.22 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.27916 | +9.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.025453 | +9.45 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1698 scans ; 726417 observations ; 1245 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
