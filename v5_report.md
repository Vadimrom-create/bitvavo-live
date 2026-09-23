# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-23T21:58:03.498846+00:00
État : OK | marchés EUR : 426 | V4 : 409 | données valides : 426
Récupération : 2026-09-23T21:57:31.505269+00:00 | âge ticker : 151.2 s | durée : 152.7 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 426/426 ; 15 min 426/426.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- FET-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : INSUFFICIENT_NET_RISK_REWARD
- PYTH-EUR : INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- PYTH-EUR : 0.05576 € ; score 93.26/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- FET-EUR : 0.17301 € ; score 91.11/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.5189 € ; score 90.29/100 ; SURVEILLE ; WICK_SETUP
- WIF-EUR : 0.20405 € ; score 88.12/100 ; SURVEILLE ; WICK_SETUP
- LTC-EUR : 54.022 € ; score 85.31/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SAGA-EUR | 0.0439 | +27.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CPOOL-EUR | 0.032207 | +27.55 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NIL-EUR | 0.087245 | +27.34 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DBR-EUR | 0.01805 | +24.20 % | NOT_DETECTED | SCANNER_COVERAGE | NOT_APPLICABLE |
| NOM-EUR | 0.0017204 | +15.05 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RAY-EUR | 1.76265 | +14.01 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CAP-EUR | 0.0464326 | +13.94 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SUPER-EUR | 0.15545 | +13.38 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.328 | +12.41 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MET-EUR | 0.3039 | +10.57 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1301 scans ; 556963 observations ; 666 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
