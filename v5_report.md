# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T02:01:11.626587+00:00
État : OK | marchés EUR : 427 | V4 : 390 | données valides : 427
Récupération : 2026-09-25T02:00:37.569631+00:00 | âge ticker : 155.5 s | durée : 156.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- TIA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LINK-EUR : 11.7923 € ; score 91.01/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HOME-EUR : 0.005725 € ; score 83.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- HUMA-EUR : 0.022716 € ; score 83.05/100 ; SURVEILLE ; WICK_SETUP
- SAND-EUR : 0.038319 € ; score 82.49/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- APE-EUR : 0.13462 € ; score 81.90/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.063891 | +56.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ONDO-EUR | 0.46207 | +28.67 % | DETECTED_EARLY | NONE | NONE |
| QNT-EUR | 78.933 | +28.59 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.62389 | +27.16 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XPL-EUR | 0.099044 | +26.25 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| DYM-EUR | 0.019067 | +21.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEAQ-EUR | 0.037249 | +20.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DBR-EUR | 0.021315 | +18.14 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.16064 | +15.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FET-EUR | 0.19615 | +15.57 % | DETECTED_EARLY | NONE | NONE |

Historique : 1408 scans ; 602584 observations ; 793 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
