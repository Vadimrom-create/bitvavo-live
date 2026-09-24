# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-24T17:10:41.088330+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-24T17:10:07.416214+00:00 | âge ticker : 154.7 s | durée : 155.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- DOGE-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ENA-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- JUP-EUR : WICK_SETUP, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- KMNO-EUR : SELLER_HEAVY_BOOK, CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- NEAR-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SEI-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- TAIKO-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DATAIP-EUR : 0.1937 € ; score 91.39/100 ; SURVEILLE ; seuil achat non atteint
- XLM-EUR : 0.18522 € ; score 89.20/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- MIOTA-EUR : 0.042637 € ; score 89.18/100 ; SURVEILLE ; WICK_SETUP
- MOODENG-EUR : 0.041446 € ; score 88.95/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- LUNA2-EUR : 0.047075 € ; score 88.78/100 ; SURVEILLE ; LOW_LIQUIDITY, STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| NOM-EUR | 0.0021232 | +42.01 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| LSK-EUR | 0.35294 | +35.50 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ONDO-EUR | 0.45556 | +25.51 % | DETECTED_EARLY | NONE | NONE |
| LTC-EUR | 65.042 | +23.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.10478 | +23.56 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QNT-EUR | 75.244 | +20.24 % | DETECTED_EARLY | NONE | NONE |
| PEAQ-EUR | 0.035856 | +19.90 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARX-EUR | 0.22952 | +19.84 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PLUME-EUR | 0.0160831 | +18.26 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XAI-EUR | 0.0081072 | +17.35 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1370 scans ; 586358 observations ; 726 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
