# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T03:19:23.661499+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T03:18:21.825307+00:00 | âge ticker : 180.1 s | durée : 180.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AXS-EUR : 1.1172 € ; score 86.13/100 ; SURVEILLE ; seuil achat non atteint
- ORCA-EUR : 1.58721 € ; score 84.24/100 ; SURVEILLE ; seuil achat non atteint
- CHZ-EUR : 0.0153 € ; score 83.98/100 ; SURVEILLE ; seuil achat non atteint
- MAGIC-EUR : 0.05277 € ; score 83.75/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- WLD-EUR : 0.50262 € ; score 83.60/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.067556 | +69.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.032646 | +20.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.093429 | +18.32 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GALA-EUR | 0.002387 | +16.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0060053 | +14.20 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BAT-EUR | 0.08904 | +11.65 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| APE-EUR | 0.14786 | +10.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| TREAD-EUR | 0.82922 | +10.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.50262 | +10.62 % | DETECTED_EARLY | NONE | NONE |
| AGI-EUR | 0.006219 | +9.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 2024 scans ; 866210 observations ; 1592 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
