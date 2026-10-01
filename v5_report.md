# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T19:58:50.154637+00:00
État : OK | marchés EUR : 430 | V4 : 381 | données valides : 430
Récupération : 2026-10-01T19:58:17.812307+00:00 | âge ticker : 147.9 s | durée : 148.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- LINK-EUR : 12.8268 € ; score 90.77/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : 0.0052282 € ; score 89.64/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 60.622 € ; score 86.96/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FLR-EUR : 0.0065671 € ; score 86.90/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD
- AAVE-EUR : 150.27 € ; score 85.67/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00062686 | +143.18 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.6055 | +70.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.1946 | +35.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.106995 | +29.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0764673 | +26.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MEGA-EUR | 0.04587 | +24.48 % | DETECTED_EARLY | NONE | NONE |
| MON-EUR | 0.030962 | +21.81 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| VELO-EUR | 0.0056719 | +20.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.170248 | +19.49 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVE-EUR | 0.009572 | +19.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1929 scans ; 825548 observations ; 1491 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
