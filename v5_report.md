# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-26T16:57:15.117710+00:00
État : OK | marchés EUR : 427 | V4 : 389 | données valides : 427
Récupération : 2026-09-26T16:56:32.648255+00:00 | âge ticker : 165.5 s | durée : 166.5 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- AXS-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- HBAR-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- MAGIC-EUR : 0.04584 € ; score 90.66/100 ; SURVEILLE ; LOW_LIQUIDITY, SELLER_HEAVY_BOOK
- ONG-EUR : 0.08558 € ; score 88.89/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- AAVE-EUR : 136.4 € ; score 88.10/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- TURBO-EUR : 0.0009577 € ; score 87.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- HBAR-EUR : 0.083615 € ; score 87.12/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| POND-EUR | 0.00173 | +115.87 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AMP-EUR | 0.0006634 | +48.78 % | DETECTED_TOO_LATE | NONE | ENTRY_TIMING_OR_EXECUTION |
| RARE-EUR | 0.019387 | +34.58 % | DETECTED_EARLY | NONE | INTERPRETATION |
| EDGE-EUR | 0.115163 | +32.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| QNT-EUR | 106.071 | +23.08 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| AGI-EUR | 0.006179 | +21.30 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FIL-EUR | 1.0705 | +19.25 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| 2Z-EUR | 0.0605 | +18.39 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ACE-EUR | 0.19541 | +16.90 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RUNE-EUR | 0.65922 | +16.65 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |

Historique : 1547 scans ; 661937 observations ; 1013 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
