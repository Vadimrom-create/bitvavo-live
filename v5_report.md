# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T10:21:12.637536+00:00
État : OK | marchés EUR : 430 | V4 : 389 | données valides : 430
Récupération : 2026-10-02T10:20:36.313240+00:00 | âge ticker : 158.9 s | durée : 159.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HBAR-EUR : 0.094024 € ; score 92.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : 0.08774 € ; score 85.19/100 ; SURVEILLE ; seuil achat non atteint
- CC-EUR : 0.10889 € ; score 84.00/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.47749 € ; score 82.87/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- NOM-EUR : 0.0022528 € ; score 82.35/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.000723 | +177.06 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAND-EUR | 0.055 | +45.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.121867 | +32.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.027038 | +20.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.5236 | +16.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SKY-EUR | 0.080862 | +16.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20491 | +16.28 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.090604 | +15.73 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MAGIC-EUR | 0.053584 | +14.47 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.6553 | +14.36 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1972 scans ; 844038 observations ; 1557 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
