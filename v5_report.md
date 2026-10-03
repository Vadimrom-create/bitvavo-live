# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-03T00:53:05.140831+00:00
État : OK | marchés EUR : 426 | V4 : 398 | données valides : 426
Récupération : 2026-10-03T00:52:35.927757+00:00 | âge ticker : 151.5 s | durée : 152.3 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GMT-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SYRUP-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : 1.057 € | IGNITION | score 82.64/100 | entrée 6.70/10
  Entrée 1.057 € ; stop 0.99568 € ; TP1 1.17963 € ; TP2 1.24095 € ; montant 185.16 € ; risque théorique 12.00 € ; R/R net 1.68.
  Chase risk : 6.822/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ALGO-EUR : 0.114557 € ; score 92.11/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.6945 € ; score 88.01/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 63.274 € ; score 87.96/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : 0.33219 € ; score 87.45/100 ; SURVEILLE ; WICK_SETUP
- SYRUP-EUR : 0.21705 € ; score 86.73/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.060522 | +51.45 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023663 | +17.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0058945 | +13.17 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.030313 | +13.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| APE-EUR | 0.14931 | +12.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.06668 | +11.74 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MANA-EUR | 0.088072 | +10.87 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| WLD-EUR | 0.49908 | +10.65 % | DETECTED_EARLY | NONE | NONE |
| PYTH-EUR | 0.072498 | +9.43 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SPK-EUR | 0.023049 | +9.42 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2017 scans ; 863228 observations ; 1584 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
