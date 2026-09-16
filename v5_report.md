# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-16T19:20:18.333956+00:00
État : OK | marchés EUR : 430 | V4 : 380 | données valides : 13
Récupération : 2026-09-16T19:19:42.516698+00:00 | âge ticker : 151.0 s | durée : 152.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 32/430 ; 15 min 58/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : CHASE_RISK, STALE_DAILY_PROFILE
- UNI-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE

## SURVEILLE

- VTHO-EUR : 0.00058761 € ; score 80.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- VET-EUR : 0.0060687 € ; score 76.79/100 ; SURVEILLE ; SPREAD_RISK, WICK_SETUP, STABILITY_HOLD
- LINK-EUR : 9.4846 € ; score 76.11/100 ; SURVEILLE ; STABILITY_HOLD
- TAO-EUR : 190.17 € ; score 75.83/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- SUI-EUR : 0.60952 € ; score 75.66/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.16422 | +136.23 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LSK-EUR | 0.66795 | +95.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.122138 | +26.59 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FOLD-EUR | 0.045888 | +20.87 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AGI-EUR | 0.004064 | +13.55 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| RAY-EUR | 1.21002 | +12.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZEN-EUR | 5.9936 | +11.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IOST-EUR | 0.0007221 | +10.40 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LIGHTER-EUR | 3.9789 | +9.47 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CNPY-EUR | 0.3579 | +9.18 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 653 scans ; 280184 observations ; 103 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
