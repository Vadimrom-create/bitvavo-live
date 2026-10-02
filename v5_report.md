# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T15:58:50.273957+00:00
État : OK | marchés EUR : 426 | V4 : 392 | données valides : 426
Récupération : 2026-10-02T15:58:17.618073+00:00 | âge ticker : 157.7 s | durée : 159.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : INSUFFICIENT_NET_RISK_REWARD
- ALGO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- DYDX-EUR : 0.13639 € ; score 92.95/100 ; SURVEILLE ; SPREAD_RISK
- ALGO-EUR : 0.116969 € ; score 90.16/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RE-EUR : 0.44986 € ; score 89.38/100 ; SURVEILLE ; seuil achat non atteint
- AAVE-EUR : 162.68 € ; score 86.27/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HNT-EUR : 0.46638 € ; score 82.70/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAND-EUR | 0.054883 | +39.64 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GTC-EUR | 0.113891 | +23.15 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| WLD-EUR | 0.50907 | +17.23 % | DETECTED_EARLY | NONE | NONE |
| SKY-EUR | 0.083702 | +16.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| APE-EUR | 0.1516 | +15.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GALA-EUR | 0.0023071 | +14.74 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SPK-EUR | 0.024202 | +14.50 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.7253 | +12.69 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ATH-EUR | 0.0058196 | +12.41 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| NOS-EUR | 0.53908 | +12.17 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1988 scans ; 850874 observations ; 1573 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
