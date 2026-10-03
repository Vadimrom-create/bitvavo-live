# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T08:16:29.114215+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T08:15:59.104343+00:00 | âge ticker : 150.3 s | durée : 151.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 160.47 € ; score 94.57/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : 0.2154 € ; score 93.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, INSUFFICIENT_NET_RISK_REWARD
- MAGIC-EUR : 0.050525 € ; score 89.70/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- WOO-EUR : 0.012433 € ; score 89.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- UNI-EUR : 8.2112 € ; score 87.98/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.067072 | +26.85 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 234.983 | +13.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.0643 | +11.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ATH-EUR | 0.0059956 | +10.62 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.098948 | +7.86 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SYN-EUR | 0.166774 | +7.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XDP-EUR | 0.018931 | +7.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.2154 | +7.26 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ENJ-EUR | 0.030118 | +6.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| UP-EUR | 0.064663 | +6.48 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2037 scans ; 871748 observations ; 1607 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
