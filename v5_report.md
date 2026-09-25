# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-25T22:01:50.697549+00:00
État : OK | marchés EUR : 427 | V4 : 386 | données valides : 427
Récupération : 2026-09-25T22:00:50.443041+00:00 | âge ticker : 180.1 s | durée : 181.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SENT-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- TAIKO-EUR : 0.08036 € ; score 92.63/100 ; SURVEILLE ; seuil achat non atteint
- TIA-EUR : 0.42657 € ; score 90.85/100 ; SURVEILLE ; seuil achat non atteint
- WIF-EUR : 0.21364 € ; score 90.16/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.064662 € ; score 88.11/100 ; SURVEILLE ; WICK_SETUP
- MOVR-EUR : 0.8557 € ; score 86.92/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| PHA-EUR | 0.085785 | +93.41 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| ARK-EUR | 0.21156 | +26.67 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AERO-EUR | 0.74685 | +22.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.013849 | +21.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SEI-EUR | 0.064306 | +17.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ENA-EUR | 0.22929 | +16.78 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| DEEP-EUR | 0.019966 | +15.33 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| TREAD-EUR | 0.658 | +15.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| JTO-EUR | 0.4937 | +15.29 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.45519 | +14.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1476 scans ; 631620 observations ; 893 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
