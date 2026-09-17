# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-17T05:30:38.087873+00:00
État : OK | marchés EUR : 430 | V4 : 375 | données valides : 6
Récupération : 2026-09-17T05:30:09.228747+00:00 | âge ticker : 136.4 s | durée : 137.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 20/430 ; 15 min 41/430.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : STABILITY_HOLD, INVALID_15M, INVALID_5M, STALE_DAILY_PROFILE
- XPL-EUR : STABILITY_HOLD, INVALID_5M, STALE_DAILY_PROFILE

## SURVEILLE

- ONDO-EUR : 0.30537 € ; score 78.71/100 ; SURVEILLE ; seuil achat non atteint
- TAO-EUR : 195.7 € ; score 77.56/100 ; SURVEILLE ; seuil achat non atteint
- SUI-EUR : 0.62891 € ; score 75.58/100 ; SURVEILLE ; STABILITY_HOLD
- UNI-EUR : 5.8959 € ; score 72.05/100 ; SURVEILLE ; STABILITY_HOLD
- ETH-EUR : 2129.68 € ; score 66.53/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SYN-EUR | 0.154632 | +58.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FOLD-EUR | 0.058597 | +29.41 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVA-EUR | 0.17028 | +26.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| USELESS-EUR | 0.24392 | +23.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HNT-EUR | 0.42209 | +22.54 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| QUID-EUR | 0.060029 | +21.25 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| VVV-EUR | 21.869 | +16.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LIGHTER-EUR | 4.1938 | +15.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HEI-EUR | 0.112739 | +15.32 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOODENG-EUR | 0.037507 | +14.63 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 688 scans ; 295234 observations ; 115 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
