# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T22:55:35.260298+00:00
État : OK | marchés EUR : 426 | V4 : 399 | données valides : 426
Récupération : 2026-10-02T22:54:36.769351+00:00 | âge ticker : 179.5 s | durée : 181.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ORCA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZIG-EUR : 0.0507 € ; score 92.40/100 ; SURVEILLE ; WIDE_SPREAD_RISK, WICK_SETUP
- SYRUP-EUR : 0.21311 € ; score 89.16/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ALT-EUR : 0.006938 € ; score 86.94/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- STX-EUR : 0.32412 € ; score 86.74/100 ; SURVEILLE ; seuil achat non atteint
- XDC-EUR : 0.029912 € ; score 85.94/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.058507 | +46.21 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023282 | +15.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0058874 | +13.22 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.088143 | +11.66 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| APE-EUR | 0.14554 | +10.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.029022 | +9.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.53631 | +9.24 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.025668 | +8.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.47129 | +8.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SPK-EUR | 0.022728 | +8.26 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2011 scans ; 860672 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
