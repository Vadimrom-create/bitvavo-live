# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T10:38:28.404557+00:00
État : OK | marchés EUR : 426 | V4 : 396 | données valides : 426
Récupération : 2026-10-03T10:37:57.657322+00:00 | âge ticker : 150.3 s | durée : 153.0 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : SELLER_HEAVY_BOOK, WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.20109 € | IGNITION | score 87.43/100 | entrée 7.40/10
  Entrée 0.20114 € ; stop 0.1929 € ; TP1 0.21762 € ; TP2 0.22586 € ; montant 250.00 € ; risque théorique 11.96 € ; R/R net 1.56.
  Chase risk : 4.09/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ATH-EUR : 0.0063192 € | IGNITION | score 87.39/100 | entrée 7.55/10
  Entrée 0.0063165 € ; stop 0.0059448 € ; TP1 0.0070599 € ; TP2 0.0074316 € ; montant 182.82 € ; risque théorique 12.00 € ; R/R net 1.68.
  Chase risk : 6.393/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- RENDER-EUR : 1.7413 € ; score 88.89/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.43418 € ; score 87.67/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : 0.28342 € ; score 86.80/100 ; SURVEILLE ; WICK_SETUP
- VVV-EUR : 24.6708 € ; score 86.33/100 ; SURVEILLE ; WICK_SETUP
- VIRTUAL-EUR : 0.69801 € ; score 84.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| HFT-EUR | 0.007063 | +26.94 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SAND-EUR | 0.065103 | +14.43 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ATH-EUR | 0.0063192 | +13.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.006484 | +12.14 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WLD-EUR | 0.5372 | +11.78 % | DETECTED_EARLY | NONE | NONE |
| FOLD-EUR | 0.06414 | +11.70 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 229.278 | +11.11 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.22181 | +7.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| INIT-EUR | 0.097175 | +7.43 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| GRASS-EUR | 0.65753 | +6.69 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 2044 scans ; 874730 observations ; 1608 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
