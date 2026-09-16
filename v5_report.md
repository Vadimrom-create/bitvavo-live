# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-16T20:01:37.061216+00:00
État : OK | marchés EUR : 430 | V4 : 379 | données valides : 10
Récupération : 2026-09-16T20:01:02.278300+00:00 | âge ticker : 144.7 s | durée : 145.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 37/430 ; 15 min 56/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : STABILITY_HOLD, STALE_DAILY_PROFILE
- ONDO-EUR : STALE_DAILY_PROFILE

## SURVEILLE

- VET-EUR : 0.0061229 € ; score 82.48/100 ; SURVEILLE ; WICK_SETUP
- SUI-EUR : 0.61681 € ; score 81.39/100 ; SURVEILLE ; WICK_SETUP
- UNI-EUR : 5.5474 € ; score 79.44/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 101.5 € ; score 77.45/100 ; SURVEILLE ; WICK_SETUP
- WLD-EUR : 0.32002 € ; score 77.27/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.168092 | +141.62 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| LSK-EUR | 0.6185 | +83.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HEI-EUR | 0.121666 | +25.75 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FOLD-EUR | 0.045708 | +19.38 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| IOST-EUR | 0.0007454 | +14.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.004055 | +13.30 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| RAY-EUR | 1.19984 | +11.59 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NEAR-EUR | 2.2183 | +9.73 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOSO-EUR | 0.27508 | +9.42 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ARB-EUR | 0.14029 | +9.29 % | NOT_DETECTED | DATA | NOT_APPLICABLE |

Historique : 656 scans ; 281474 observations ; 103 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
