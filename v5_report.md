# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T13:01:37.456984+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T13:01:09.890504+00:00 | âge ticker : 143.1 s | durée : 143.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- UNI-EUR : STABILITY_HOLD, PORTFOLIO_LIMIT
- ZORA-EUR : 0.007568 € | IGNITION | score 82.26/100 | entrée 6.95/10
  Entrée 0.007573 € ; stop 0.007296 € ; TP1 0.008126 € ; TP2 0.008403 € ; montant 250.00 € ; risque théorique 10.86 € ; R/R net 1.51.
  Chase risk : 3.488/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- AAVE-EUR : 126.06 € | IGNITION | score 80.43/100 | entrée 6.60/10
  Entrée 126.14 € ; stop 121.53 € ; TP1 135.36 € ; TP2 139.97 € ; montant 250.00 € ; risque théorique 10.85 € ; R/R net 1.52.
  Chase risk : 2.556/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- NEAR-EUR : 4.0071 € | IGNITION | score 77.97/100 | entrée 7.20/10
  Entrée 4.0095 € ; stop 3.868 € ; TP1 4.2925 € ; TP2 4.434 € ; montant 54.14 € ; risque théorique 2.28 € ; R/R net 1.50.
  Chase risk : 2.674/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WAL-EUR : 0.030106 € ; score 93.83/100 ; SURVEILLE ; WICK_SETUP
- CAKE-EUR : 2.225 € ; score 89.76/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- RPL-EUR : 1.7115 € ; score 89.68/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK, WICK_SETUP
- NEWT-EUR : 0.043142 € ; score 88.32/100 ; SURVEILLE ; seuil achat non atteint
- MMT-EUR : 0.14459 € ; score 88.20/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.017051 | +95.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014156 | +80.10 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KERNEL-EUR | 0.05368 | +28.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| XMN-EUR | 0.000537 | +27.55 % | DETECTED_EARLY | NONE | INTERPRETATION |
| WIF-EUR | 0.23807 | +21.88 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.28539 | +21.73 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.069765 | +21.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRASS-EUR | 0.38209 | +17.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3035e-06 | +15.65 % | DETECTED_EARLY | NONE | NONE |
| BCH-EUR | 270.51 | +14.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1186 scans ; 507973 observations ; 506 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
