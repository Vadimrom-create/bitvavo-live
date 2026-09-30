# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T11:59:46.155094+00:00
État : OK | marchés EUR : 430 | V4 : 390 | données valides : 429
Récupération : 2026-09-30T11:59:16.756831+00:00 | âge ticker : 148.0 s | durée : 148.6 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/430 ; 15 min 429/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- BNB-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.095901 € | IGNITION | score 86.45/100 | entrée 6.90/10
  Entrée 0.096109 € ; stop 0.092296 € ; TP1 0.103735 € ; TP2 0.107547 € ; montant 250.00 € ; risque théorique 11.63 € ; R/R net 1.55.
  Chase risk : 3.219/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CRV-EUR : 0.35686 € ; score 93.07/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TRB-EUR : 18.188 € ; score 92.83/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- AAVE-EUR : 142.4 € ; score 92.81/100 ; SURVEILLE ; WICK_SETUP
- SYRUP-EUR : 0.20458 € ; score 92.31/100 ; SURVEILLE ; seuil achat non atteint
- POL-EUR : 0.102312 € ; score 91.51/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.4379 | +58.95 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.33069 | +53.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CT-EUR | 0.36407 | +52.33 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SOON-EUR | 0.3854 | +33.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 277.197 | +26.35 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008092 | +21.21 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.090524 | +17.13 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.066112 | +16.62 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| NIL-EUR | 0.08525 | +14.86 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOM-EUR | 0.0020491 | +13.02 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1838 scans ; 786418 observations ; 1370 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
