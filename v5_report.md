# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T20:23:52.108163+00:00
État : OK | marchés EUR : 430 | V4 : 395 | données valides : 430
Récupération : 2026-09-30T20:23:19.129712+00:00 | âge ticker : 155.5 s | durée : 156.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CRV-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- XLM-EUR : 0.20152 € ; score 94.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ROSE-EUR : 0.00792 € ; score 90.66/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- TRB-EUR : 18.65 € ; score 90.58/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ZIG-EUR : 0.048764 € ; score 87.05/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.09644 € ; score 86.62/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.549 | +51.61 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.35785 | +49.73 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.42476 | +18.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AUDIO-EUR | 0.016014 | +17.04 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CAP-EUR | 0.0606113 | +14.90 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GLMR-EUR | 0.007731 | +14.77 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NOS-EUR | 0.43693 | +13.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.3176 | +11.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BLUR-EUR | 0.019436 | +11.53 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.068176 | +11.12 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1861 scans ; 796308 observations ; 1417 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
