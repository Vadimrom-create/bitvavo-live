# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T12:23:29.309291+00:00
État : OK | marchés EUR : 426 | V4 : 386 | données valides : 426
Récupération : 2026-10-02T12:22:53.580439+00:00 | âge ticker : 156.0 s | durée : 156.8 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : INSUFFICIENT_NET_RISK_REWARD
- ZRO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- WLD-EUR : 0.49346 € | IGNITION | score 93.29/100 | entrée 7.85/10
  Entrée 0.49366 € ; stop 0.47431 € ; TP1 0.53235 € ; TP2 0.5517 € ; montant 250.00 € ; risque théorique 11.51 € ; R/R net 1.54.
  Chase risk : 2.865/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- IMX-EUR : 0.16351 € ; score 89.16/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- PYTH-EUR : 0.069624 € ; score 87.23/100 ; SURVEILLE ; seuil achat non atteint
- HBAR-EUR : 0.09472 € ; score 84.95/100 ; SURVEILLE ; seuil achat non atteint
- ESP-EUR : 0.0937 € ; score 83.84/100 ; SURVEILLE ; LOW_LIQUIDITY, WICK_SETUP
- CELO-EUR : 0.091575 € ; score 83.34/100 ; SURVEILLE ; LOW_LIQUIDITY

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.063394 | +66.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ENJ-EUR | 0.034964 | +36.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.108233 | +21.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MANA-EUR | 0.094479 | +20.82 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SKY-EUR | 0.083268 | +18.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GALA-EUR | 0.0023252 | +16.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NOS-EUR | 0.52769 | +15.98 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MAGIC-EUR | 0.05387 | +15.70 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.19992 | +14.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.49665 | +14.22 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1978 scans ; 846614 observations ; 1561 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
