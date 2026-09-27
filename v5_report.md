# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-27T01:21:59.828422+00:00
État : OK | marchés EUR : 427 | V4 : 383 | données valides : 427
Récupération : 2026-09-27T01:21:27.551369+00:00 | âge ticker : 161.4 s | durée : 162.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AERO-EUR : CHASE_RISK, BASELINE_BUY_CHASE_CONTRADICTION
- CC-EUR : INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : INSUFFICIENT_NET_RISK_REWARD
- DOT-EUR : INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : INSUFFICIENT_NET_RISK_REWARD
- RAY-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- UNI-EUR : 8.6399 € ; score 92.23/100 ; SURVEILLE ; seuil achat non atteint
- RAY-EUR : 1.82538 € ; score 91.83/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- DATAIP-EUR : 0.2037 € ; score 91.34/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- VIRTUAL-EUR : 0.69022 € ; score 90.82/100 ; SURVEILLE ; seuil achat non atteint
- MOODENG-EUR : 0.042946 € ; score 90.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 148.481 | +70.59 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006848 | +53.71 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| HFT-EUR | 0.007637 | +38.25 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| RARE-EUR | 0.01766 | +34.11 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.060821 | +21.09 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.21156 | +19.22 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006163 | +18.93 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.67148 | +17.05 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| TREAD-EUR | 0.82428 | +15.77 % | DETECTED_EARLY | NONE | INTERPRETATION |
| KMNO-EUR | 0.042311 | +15.60 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1577 scans ; 674747 observations ; 1058 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
