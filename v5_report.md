# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T14:11:17.556889+00:00
État : OK | marchés EUR : 430 | V4 : 385 | données valides : 430
Récupération : 2026-10-01T14:10:18.531901+00:00 | âge ticker : 188.3 s | durée : 189.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ZIG-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AAVE-EUR : 147.96 € ; score 94.09/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TRB-EUR : 18.92 € ; score 91.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP, STABILITY_HOLD
- JTO-EUR : 0.46952 € ; score 89.58/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- CRV-EUR : 0.33835 € ; score 87.85/100 ; SURVEILLE ; WICK_SETUP
- GRT-EUR : 0.025658 € ; score 86.46/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00065677 | +154.76 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.3463 | +66.52 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.44544 | +34.34 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0701584 | +25.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AUDIO-EUR | 0.016293 | +17.78 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MON-EUR | 0.028742 | +16.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.171548 | +16.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| STX-EUR | 0.32866 | +13.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.46435 | +13.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.0024126 | +12.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1912 scans ; 818238 observations ; 1478 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
