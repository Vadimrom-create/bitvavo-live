# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T00:54:31.731933+00:00
État : OK | marchés EUR : 428 | V4 : 398 | données valides : 428
Récupération : 2026-09-29T00:53:59.771837+00:00 | âge ticker : 146.4 s | durée : 147.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 428/428 ; 15 min 428/428.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ALGO-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- XDC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- C-EUR : 0.080476 € ; score 91.70/100 ; SURVEILLE ; seuil achat non atteint
- XDC-EUR : 0.030624 € ; score 89.23/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SKY-EUR : 0.069602 € ; score 84.97/100 ; SURVEILLE ; WICK_SETUP
- AVAX-EUR : 9.4281 € ; score 84.83/100 ; SURVEILLE ; seuil achat non atteint
- POWR-EUR : 0.060675 € ; score 84.59/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NMR-EUR | 12.4468 | +34.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| HBAR-EUR | 0.106087 | +25.07 % | DETECTED_EARLY | NONE | NONE |
| 0G-EUR | 0.26666 | +16.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.119063 | +13.63 % | DETECTED_EARLY | NONE | NONE |
| LINK-EUR | 13.6262 | +10.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| IKA-EUR | 0.0018305 | +9.91 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| SYRUP-EUR | 0.21076 | +9.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NPC-EUR | 0.0208528 | +7.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AZTEC-EUR | 0.016872 | +7.31 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CRV-EUR | 0.32702 | +7.26 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1733 scans ; 741397 observations ; 1272 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
