# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-06T21:02:40.276553+00:00
État : OK | marchés EUR : 427 | V4 : 379 | données valides : 427
Récupération : 2026-10-06T21:02:03.751865+00:00 | âge ticker : 146.5 s | durée : 147.6 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AKT-EUR : INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AKT-EUR : 0.685 € ; score 82.51/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- API3-EUR : 0.29804 € ; score 81.83/100 ; SURVEILLE ; SPREAD_RISK
- RENDER-EUR : 1.9044 € ; score 81.74/100 ; SURVEILLE ; seuil achat non atteint
- SCR-EUR : 0.02384 € ; score 80.47/100 ; SURVEILLE ; SPREAD_RISK
- APT-EUR : 0.7531 € ; score 79.91/100 ; SURVEILLE ; WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.0058149 | +61.36 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ORCA-EUR | 2.69962 | +38.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 13.8105 | +29.56 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0790115 | +19.95 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RLC-EUR | 0.68628 | +17.90 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MET-EUR | 0.29793 | +13.07 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NPC-EUR | 0.0205731 | +12.43 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.06027 | +12.40 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRB-EUR | 20.262 | +11.63 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| API3-EUR | 0.29804 | +9.48 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2088 scans ; 893492 observations ; 1652 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
