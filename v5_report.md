# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-19T01:26:58.581501+00:00
État : OK | marchés EUR : 427 | V4 : 395 | données valides : 23
Récupération : 2026-09-19T01:26:26.616406+00:00 | âge ticker : 145.4 s | durée : 146.2 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 24/427 ; 15 min 66/427.
Les trous de cotation restent visibles ; aucune bougie sans transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, STABILITY_HOLD, INVALID_5M
- AVAX-EUR : INVALID_5M
- ENA-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- HYPE-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : WICK_SETUP, INVALID_15M, INVALID_5M

## SURVEILLE

- HYPE-EUR : 80.832 € ; score 81.51/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.15901 € ; score 79.57/100 ; SURVEILLE ; seuil achat non atteint
- ENA-EUR : 0.1488 € ; score 71.39/100 ; SURVEILLE ; STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- ONDO-EUR : 0.34624 € ; score 70.32/100 ; SURVEILLE ; STABILITY_HOLD
- SUI-EUR : 0.70774 € ; score 64.34/100 ; SURVEILLE ; STABILITY_HOLD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| G-EUR | 0.0063732 | +47.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| STRK-EUR | 0.036557 | +44.37 % | DETECTED_EARLY | NONE | INTERPRETATION |
| F-EUR | 0.0039478 | +38.93 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZAMA-EUR | 0.054226 | +24.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SYN-EUR | 0.193519 | +22.96 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| APT-EUR | 0.6535 | +22.24 % | DETECTED_EARLY | NONE | INTERPRETATION |
| QKC-EUR | 0.0024742 | +21.48 % | NOT_DETECTED | DATA | NOT_APPLICABLE |
| ZIG-EUR | 0.044489 | +21.42 % | DETECTED_EARLY | NONE | INTERPRETATION |
| S-EUR | 0.028698 | +20.63 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ARB-EUR | 0.1901 | +18.93 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 848 scans ; 363875 observations ; 185 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
