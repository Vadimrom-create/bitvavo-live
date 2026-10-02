# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T00:30:58.759516+00:00
État : OK | marchés EUR : 430 | V4 : 382 | données valides : 430
Récupération : 2026-10-02T00:30:25.494280+00:00 | âge ticker : 148.9 s | durée : 149.8 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- WLD-EUR : 0.45093 € ; score 91.08/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SENT-EUR : 0.019378 € ; score 87.60/100 ; SURVEILLE ; seuil achat non atteint
- CFG-EUR : 0.133419 € ; score 87.04/100 ; SURVEILLE ; seuil achat non atteint
- NMR-EUR : 10.1003 € ; score 86.01/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ENSO-EUR : 0.905 € ; score 85.56/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.000524 | +103.20 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.1281 | +54.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 2.6777 | +34.83 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ALICE-EUR | 0.19453 | +30.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04755 | +28.27 % | DETECTED_EARLY | NONE | NONE |
| CT-EUR | 0.4506 | +26.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0024797 | +18.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20704 | +17.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.16308 | +16.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| VELO-EUR | 0.0054179 | +14.52 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1943 scans ; 831568 observations ; 1512 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
