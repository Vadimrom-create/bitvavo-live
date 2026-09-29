# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T08:25:15.147775+00:00
État : OK | marchés EUR : 428 | V4 : 390 | données valides : 428
Récupération : 2026-09-29T08:24:15.477542+00:00 | âge ticker : 184.0 s | durée : 184.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : STABILITY_HOLD, BELOW_EXCHANGE_MINIMUM
- VIRTUAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : 0.00206 € | IGNITION | score 85.49/100 | entrée 6.60/10
  Entrée 0.0020619 € ; stop 0.001913 € ; TP1 0.0023597 € ; TP2 0.0025086 € ; montant 151.97 € ; risque théorique 12.00 € ; R/R net 1.73.
  Chase risk : 5.93/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- UNI-EUR : 8.167 € | IGNITION | score 80.71/100 | entrée 6.75/10
  Entrée 8.1411 € ; stop 7.625 € ; TP1 9.1733 € ; TP2 9.6894 € ; montant 171.01 € ; risque théorique 12.00 € ; R/R net 1.70.
  Chase risk : 4.594/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- SKY-EUR : 0.072617 € ; score 92.94/100 ; SURVEILLE ; seuil achat non atteint
- RARE-EUR : 0.015339 € ; score 90.82/100 ; SURVEILLE ; WICK_SETUP
- JUP-EUR : 0.29071 € ; score 88.86/100 ; SURVEILLE ; seuil achat non atteint
- ADA-EUR : 0.22346 € ; score 87.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : 0.06681 € ; score 86.60/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.0017002 | +38.68 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NMR-EUR | 11.3312 | +32.13 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.35139 | +21.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.104203 | +19.74 % | DETECTED_EARLY | NONE | NONE |
| CELO-EUR | 0.09434 | +17.66 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.061753 | +16.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYRUP-EUR | 0.21042 | +14.92 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.08579 | +14.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MIOTA-EUR | 0.049471 | +14.14 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ICP-EUR | 2.99 | +14.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1756 scans ; 751241 observations ; 1286 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
