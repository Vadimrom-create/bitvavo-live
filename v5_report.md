# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-06T20:58:39.204827+00:00
État : OK | marchés EUR : 427 | V4 : 380 | données valides : 427
Récupération : 2026-10-06T20:58:06.381746+00:00 | âge ticker : 150.4 s | durée : 151.4 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AKT-EUR : INSUFFICIENT_NET_RISK_REWARD
- APT-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## SURVEILLE

- AKT-EUR : 0.68426 € ; score 92.77/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- HNT-EUR : 0.46157 € ; score 85.81/100 ; SURVEILLE ; WICK_SETUP
- API3-EUR : 0.2951 € ; score 85.02/100 ; SURVEILLE ; seuil achat non atteint
- APT-EUR : 0.7531 € ; score 81.73/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : 1.9028 € ; score 81.53/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| ZEUS-EUR | 0.005639 | +59.02 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ORCA-EUR | 2.74517 | +40.34 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 13.7896 | +29.36 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CAP-EUR | 0.0791129 | +20.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| RLC-EUR | 0.6838 | +20.24 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| EDU-EUR | 0.06091 | +13.64 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MET-EUR | 0.29694 | +12.69 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NPC-EUR | 0.0205112 | +12.09 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| TRB-EUR | 20.158 | +11.48 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PARTI-EUR | 0.029957 | +8.83 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2088 scans ; 893492 observations ; 1652 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
