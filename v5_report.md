# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T14:05:02.236547+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T14:04:25.523973+00:00 | âge ticker : 153.0 s | durée : 154.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- NEAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- NOM-EUR : 0.0018171 € ; score 90.31/100 ; SURVEILLE ; LOW_LIQUIDITY, SPREAD_RISK, WICK_SETUP
- ACE-EUR : 0.17558 € ; score 87.29/100 ; SURVEILLE ; seuil achat non atteint
- WAL-EUR : 0.032725 € ; score 86.42/100 ; SURVEILLE ; seuil achat non atteint
- CFG-EUR : 0.145662 € ; score 85.49/100 ; SURVEILLE ; WICK_SETUP
- BEAM-EUR : 0.0018777 € ; score 84.99/100 ; SURVEILLE ; SPREAD_RISK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 144.511 | +54.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.11184 | +51.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008584 | +45.57 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AUDIO-EUR | 0.017805 | +39.59 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.25351 | +33.04 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.25506 | +26.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.55088 | +20.91 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.00649 | +18.82 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| INX-EUR | 0.006064 | +16.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WLD-EUR | 0.50111 | +15.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1621 scans ; 693535 observations ; 1145 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
