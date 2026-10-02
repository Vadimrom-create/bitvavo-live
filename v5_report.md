# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T02:49:34.637438+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T02:49:04.397567+00:00 | âge ticker : 152.3 s | durée : 153.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- JASMY-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- ONDO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PROM-EUR : 5.7234 € ; score 92.98/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.092616 € ; score 90.65/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.4041 € ; score 86.97/100 ; SURVEILLE ; seuil achat non atteint
- XVG-EUR : 0.0028691 € ; score 86.82/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.0020479 € ; score 86.41/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00059922 | +132.36 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.1495 | +79.18 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SCR-EUR | 0.027405 | +24.23 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.43511 | +23.31 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MOVR-EUR | 2.5987 | +22.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04706 | +21.82 % | DETECTED_EARLY | NONE | NONE |
| SYN-EUR | 0.165998 | +19.48 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0024739 | +18.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALICE-EUR | 0.1739 | +17.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.207 | +16.94 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1950 scans ; 834578 observations ; 1517 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
