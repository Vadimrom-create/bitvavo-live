# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T02:53:16.641955+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-03T02:52:46.806889+00:00 | âge ticker : 152.2 s | durée : 153.0 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- UNI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- IMX-EUR : 0.16386 € ; score 87.79/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- FLUID-EUR : 1.4201 € ; score 87.12/100 ; SURVEILLE ; seuil achat non atteint
- XDP-EUR : 0.017394 € ; score 82.68/100 ; SURVEILLE ; seuil achat non atteint
- ZAMA-EUR : 0.068793 € ; score 81.25/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SKY-EUR : 0.078768 € ; score 81.11/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.063908 | +60.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.032749 | +22.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023936 | +16.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.091 | +14.92 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ATH-EUR | 0.0060053 | +13.76 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BAT-EUR | 0.0892 | +11.85 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| APE-EUR | 0.14915 | +11.81 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.50568 | +10.92 % | DETECTED_EARLY | NONE | NONE |
| CT-EUR | 0.47526 | +10.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.006219 | +9.68 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 2023 scans ; 865784 observations ; 1586 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
