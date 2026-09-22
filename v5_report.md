# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-22T13:57:54.059030+00:00
État : OK | marchés EUR : 426 | V4 : 402 | données valides : 426
Récupération : 2026-09-22T13:57:23.178929+00:00 | âge ticker : 151.4 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : WICK_SETUP, PORTFOLIO_LIMIT
- LINK-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : 0.08444 € | IGNITION | score 92.13/100 | entrée 7.95/10
  Entrée 0.084433 € ; stop 0.081303 € ; TP1 0.090692 € ; TP2 0.093822 € ; montant 250.00 € ; risque théorique 10.99 € ; R/R net 1.52.
  Chase risk : 2.418/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ADA-EUR : 0.22037 € | IGNITION | score 90.89/100 | entrée 8.15/10
  Entrée 0.22041 € ; stop 0.21235 € ; TP1 0.23652 € ; TP2 0.24458 € ; montant 250.00 € ; risque théorique 10.86 € ; R/R net 1.52.
  Chase risk : 2.288/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- XRP-EUR : 1.38178 € | IGNITION | score 89.48/100 | entrée 7.75/10
  Entrée 1.38179 € ; stop 1.32962 € ; TP1 1.48613 € ; TP2 1.5383 € ; montant 48.29 € ; risque théorique 2.15 € ; R/R net 1.53.
  Chase risk : 2.093/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AVNT-EUR : 0.10263 € ; score 89.86/100 ; SURVEILLE ; SPREAD_RISK
- COW-EUR : 0.13765 € ; score 88.35/100 ; SURVEILLE ; seuil achat non atteint
- WLD-EUR : 0.40101 € ; score 86.12/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : 0.18757 € ; score 85.88/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XDC-EUR : 0.0269 € ; score 85.14/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ICX-EUR | 0.0162 | +86.19 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRC-EUR | 0.0014026 | +78.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NIL-EUR | 0.074359 | +33.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| KERNEL-EUR | 0.052846 | +26.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| BCH-EUR | 285.15 | +21.56 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| FORM-EUR | 0.2801 | +19.91 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FLOCK-EUR | 0.075302 | +18.80 % | DETECTED_EARLY | NONE | INTERPRETATION |
| THQ-EUR | 0.011725 | +18.31 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| XMN-EUR | 0.000489 | +17.27 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GRASS-EUR | 0.37768 | +15.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1190 scans ; 509677 observations ; 508 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
