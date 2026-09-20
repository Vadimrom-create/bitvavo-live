# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-20T22:58:30.288951+00:00
État : OK | marchés EUR : 426 | V4 : 382 | données valides : 426
Récupération : 2026-09-20T22:57:58.472115+00:00 | âge ticker : 150.1 s | durée : 150.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : INSUFFICIENT_NET_RISK_REWARD
- POL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- PORTAL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.25178 € | IGNITION | score 89.75/100 | entrée 7.55/10
  Entrée 0.25185 € ; stop 0.2409 € ; TP1 0.27375 € ; TP2 0.2847 € ; montant 238.44 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 4.136/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ONDO-EUR : 0.37735 € | IGNITION | score 83.07/100 | entrée 7.20/10
  Entrée 0.37767 € ; stop 0.36346 € ; TP1 0.40609 € ; TP2 0.4203 € ; montant 250.00 € ; risque théorique 11.12 € ; R/R net 1.53.
  Chase risk : 3.517/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- SUI-EUR : 0.78088 € | IGNITION | score 71.99/100 | entrée 7.25/10
  Entrée 0.78134 € ; stop 0.75369 € ; TP1 0.83664 € ; TP2 0.86429 € ; montant 20.74 € ; risque théorique 0.88 € ; R/R net 1.50.
  Chase risk : 2.501/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- MERL-EUR : 0.022894 € ; score 89.44/100 ; SURVEILLE ; seuil achat non atteint
- POL-EUR : 0.093967 € ; score 89.17/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- ROSE-EUR : 0.006659 € ; score 88.99/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MIRA-EUR : 0.045322 € ; score 88.36/100 ; SURVEILLE ; seuil achat non atteint
- SKY-EUR : 0.062053 € ; score 88.17/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.032001 | +46.39 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0008096 | +32.31 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| FTT-EUR | 0.23958 | +29.84 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| NIL-EUR | 0.056091 | +25.87 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EPIC-EUR | 0.49882 | +22.86 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KMNO-EUR | 0.028851 | +20.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.034584 | +19.88 % | DETECTED_EARLY | NONE | INTERPRETATION |
| LUNA2-EUR | 0.048408 | +15.70 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| AVAX-EUR | 9.8249 | +15.49 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CFG-EUR | 0.123537 | +13.54 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1026 scans ; 439813 observations ; 277 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
