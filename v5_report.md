# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T09:58:29.114160+00:00
État : OK | marchés EUR : 430 | V4 : 386 | données valides : 430
Récupération : 2026-10-02T09:57:57.081831+00:00 | âge ticker : 154.6 s | durée : 156.3 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HBAR-EUR : INSUFFICIENT_NET_RISK_REWARD
- WLD-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- HBAR-EUR : 0.094408 € ; score 92.36/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RECALL-EUR : 0.043202 € ; score 88.26/100 ; SURVEILLE ; seuil achat non atteint
- LISTA-EUR : 0.077317 € ; score 86.06/100 ; SURVEILLE ; LOW_LIQUIDITY
- WLD-EUR : 0.48393 € ; score 86.05/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- CC-EUR : 0.10855 € ; score 83.98/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00073063 | +179.99 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SAND-EUR | 0.056499 | +48.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.1177 | +30.99 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.52864 | +29.82 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.027 | +19.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MANA-EUR | 0.091224 | +17.12 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MAGIC-EUR | 0.054073 | +15.51 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SKY-EUR | 0.078911 | +14.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SUPER-EUR | 0.20146 | +14.32 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.6574 | +14.30 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1971 scans ; 843608 observations ; 1555 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
