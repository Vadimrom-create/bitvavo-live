# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T11:58:39.282230+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 427
Récupération : 2026-09-28T11:58:09.782068+00:00 | âge ticker : 151.1 s | durée : 152.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- LINK-EUR : 12.3917 € | IGNITION | score 77.62/100 | entrée 7.65/10
  Entrée 12.3924 € ; stop 11.8267 € ; TP1 13.5238 € ; TP2 14.0895 € ; montant 228.62 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.802/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- PUMP-EUR : 0.0043896 € | IGNITION | score 72.88/100 | entrée 6.35/10
  Entrée 0.0043999 € ; stop 0.0041346 € ; TP1 0.0049304 € ; TP2 0.0051957 € ; montant 178.88 € ; risque théorique 12.00 € ; R/R net 1.69.
  Chase risk : 5.015/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AVNT-EUR : 0.10971 € ; score 90.85/100 ; SURVEILLE ; seuil achat non atteint
- EIGEN-EUR : 0.22552 € ; score 90.83/100 ; SURVEILLE ; WICK_SETUP
- ZETA-EUR : 0.045845 € ; score 85.79/100 ; SURVEILLE ; seuil achat non atteint
- XVG-EUR : 0.0028098 € ; score 85.74/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- BIGTIME-EUR : 0.008193 € ; score 84.02/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 204.95 | +42.14 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.103118 | +23.90 % | DETECTED_EARLY | NONE | NONE |
| NMR-EUR | 9.8777 | +15.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.027979 | +14.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0018837 | +13.42 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| AUDIO-EUR | 0.014737 | +12.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.27223 | +12.12 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALGO-EUR | 0.115446 | +12.04 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.0043896 | +11.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SEI-EUR | 0.07113 | +7.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1693 scans ; 724279 observations ; 1244 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
