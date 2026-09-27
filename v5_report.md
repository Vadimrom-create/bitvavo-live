# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T01:53:46.995925+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T01:53:19.040467+00:00 | âge ticker : 146.8 s | durée : 148.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- EIGEN-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- FIL-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SUI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- TAO-EUR : INSUFFICIENT_NET_RISK_REWARD
- W-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : 0.2067 € | IGNITION | score 87.44/100 | entrée 6.05/10
  Entrée 0.2066 € ; stop 0.1973 € ; TP1 0.2252 € ; TP2 0.2345 € ; montant 231.41 € ; risque théorique 12.00 € ; R/R net 1.60.
  Chase risk : 3.93/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CC-EUR : 0.12164 € ; score 93.72/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TURBO-EUR : 0.0009237 € ; score 88.03/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- FIL-EUR : 0.99883 € ; score 87.58/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FLUX-EUR : 0.064602 € ; score 85.17/100 ; SURVEILLE ; seuil achat non atteint
- ALGO-EUR : 0.102952 € ; score 85.04/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 161.862 | +83.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006685 | +50.06 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.017705 | +35.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.061523 | +21.87 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| RUNE-EUR | 0.68959 | +18.89 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| ZRC-EUR | 0.0012847 | +17.46 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AGI-EUR | 0.006067 | +17.08 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SOON-EUR | 0.20695 | +16.62 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| EDGE-EUR | 0.120111 | +16.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.042133 | +15.42 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1579 scans ; 675601 observations ; 1063 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
