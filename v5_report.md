# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T03:04:20.054103+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T03:03:24.406040+00:00 | âge ticker : 178.9 s | durée : 179.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- WIF-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XPL-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- SUI-EUR : 1.06054 € ; score 89.14/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- BABY-EUR : 0.012182 € ; score 87.84/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- GALA-EUR : 0.0020479 € ; score 86.41/100 ; SURVEILLE ; seuil achat non atteint
- XPL-EUR : 0.086612 € ; score 86.36/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 274.08 € ; score 86.23/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00062874 | +143.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.149956 | +79.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.43186 | +26.96 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.027959 | +26.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04765 | +21.77 % | DETECTED_EARLY | NONE | NONE |
| MOVR-EUR | 2.5603 | +21.03 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.165998 | +19.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.20898 | +18.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALICE-EUR | 0.1738 | +17.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOM-EUR | 0.002448 | +16.68 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1951 scans ; 835008 observations ; 1517 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
