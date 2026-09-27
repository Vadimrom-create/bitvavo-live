# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T16:20:26.524163+00:00
État : OK | marchés EUR : 427 | V4 : 385 | données valides : 427
Récupération : 2026-09-27T16:19:53.244711+00:00 | âge ticker : 152.5 s | durée : 153.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETC-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION

## SURVEILLE

- IMX-EUR : 0.14954 € ; score 90.27/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZIL-EUR : 0.0032682 € ; score 87.40/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- BAT-EUR : 0.08472 € ; score 87.27/100 ; SURVEILLE ; WICK_SETUP
- AEVO-EUR : 0.023857 € ; score 87.03/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- PENDLE-EUR : 2.3581 € ; score 86.40/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 161.879 | +57.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.30104 | +57.66 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| TREAD-EUR | 1.03507 | +39.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008157 | +33.74 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| AUDIO-EUR | 0.016903 | +32.97 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARX-EUR | 0.26559 | +30.77 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INX-EUR | 0.00646 | +22.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| W-EUR | 0.013479 | +19.85 % | DETECTED_EARLY | NONE | NONE |
| AGI-EUR | 0.006713 | +16.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.54331 | +14.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1629 scans ; 696951 observations ; 1154 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
