# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T08:01:08.310441+00:00
État : OK | marchés EUR : 430 | V4 : 391 | données valides : 430
Récupération : 2026-10-01T08:00:07.226558+00:00 | âge ticker : 186.4 s | durée : 187.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- QNT-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- ICP-EUR : 2.9142 € ; score 93.49/100 ; SURVEILLE ; seuil achat non atteint
- DIA-EUR : 0.15355 € ; score 89.89/100 ; SURVEILLE ; VERY_SELLER_HEAVY_BOOK, WICK_SETUP
- SUSHI-EUR : 0.23222 € ; score 89.76/100 ; SURVEILLE ; seuil achat non atteint
- NPC-EUR : 0.019164 € ; score 85.65/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- ALICE-EUR : 0.1499 € ; score 84.21/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 2.5552 | +69.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.3675 | +53.77 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NOM-EUR | 0.0025649 | +37.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.35291 | +27.67 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.0647027 | +20.42 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.02835 | +18.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.47256 | +17.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TRAC-EUR | 0.41951 | +14.50 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ESP-EUR | 0.097428 | +12.12 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| RED-EUR | 0.16038 | +11.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1895 scans ; 810928 observations ; 1453 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
