# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T06:24:16.506343+00:00
État : OK | marchés EUR : 426 | V4 : 401 | données valides : 426
Récupération : 2026-09-22T06:23:18.611629+00:00 | âge ticker : 174.5 s | durée : 175.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- ZORA-EUR : 0.007437 € ; score 85.58/100 ; SURVEILLE ; WICK_SETUP
- THE-EUR : 0.07195 € ; score 83.82/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- MERL-EUR : 0.024706 € ; score 81.88/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- SOL-EUR : 101.64 € ; score 81.74/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KITE-EUR : 0.10907 € ; score 80.95/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0016318 | +110.07 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.017 | +101.80 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AIOZ-EUR | 0.1235 | +54.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.056544 | +31.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SAGA-EUR | 0.038931 | +26.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| PEPE-EUR | 4.4703e-06 | +26.86 % | DETECTED_EARLY | NONE | NONE |
| BONK-EUR | 3.2242e-06 | +20.91 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| WIF-EUR | 0.21366 | +20.20 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.273 | +20.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.37986 | +19.76 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1155 scans ; 494767 observations ; 463 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
