# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-21T18:59:24.828881+00:00
État : OK | marchés EUR : 426 | V4 : 403 | données valides : 426
Récupération : 2026-09-21T18:58:54.220713+00:00 | âge ticker : 148.2 s | durée : 149.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- SHIB-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VET-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- TAO-EUR : 249.51 € | IGNITION | score 84.29/100 | entrée 7.05/10
  Entrée 249.57 € ; stop 240.61 € ; TP1 267.48 € ; TP2 276.44 € ; montant 250.00 € ; risque théorique 10.69 € ; R/R net 1.51.
  Chase risk : 2.22/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XTZ-EUR : 0.30256 € ; score 91.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- ATH-EUR : 0.0048022 € ; score 88.63/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, STABILITY_HOLD
- COTI-EUR : 0.015024 € ; score 87.42/100 ; SURVEILLE ; WICK_SETUP
- WCT-EUR : 0.036282 € ; score 83.29/100 ; SURVEILLE ; seuil achat non atteint
- STX-EUR : 0.29013 € ; score 83.24/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZRC-EUR | 0.0015652 | +103.38 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ICX-EUR | 0.013388 | +58.81 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZETA-EUR | 0.053193 | +58.04 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| PHA-EUR | 0.04456 | +39.45 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.30991 | +38.97 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PTB-EUR | 0.0010192 | +29.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AIOZ-EUR | 0.099318 | +25.37 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PEPE-EUR | 4.3505e-06 | +24.97 % | DETECTED_EARLY | NONE | NONE |
| NOS-EUR | 0.31822 | +23.01 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SWELL-EUR | 0.0007934 | +22.08 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1102 scans ; 472189 observations ; 401 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
