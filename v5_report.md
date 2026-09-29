# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-29T13:58:30.130358+00:00
État : OK | marchés EUR : 429 | V4 : 397 | données valides : 428
Récupération : 2026-09-29T13:57:57.844755+00:00 | âge ticker : 151.3 s | durée : 152.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 428/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- CFG-EUR : INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : INSUFFICIENT_NET_RISK_REWARD
- SHIB-EUR : INSUFFICIENT_NET_RISK_REWARD
- NEAR-EUR : 4.4215 € | IGNITION | score 89.69/100 | entrée 7.90/10
  Entrée 4.4193 € ; stop 4.2093 € ; TP1 4.8393 € ; TP2 5.0493 € ; montant 220.78 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 2.293/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- ENA-EUR : 0.23001 € | IGNITION | score 81.27/100 | entrée 6.90/10
  Entrée 0.22995 € ; stop 0.22156 € ; TP1 0.24672 € ; TP2 0.25511 € ; montant 250.00 € ; risque théorique 10.84 € ; R/R net 1.51.
  Chase risk : 2.898/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GALA-EUR : 0.0020651 € ; score 91.19/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- NOM-EUR : 0.001815 € ; score 90.85/100 ; SURVEILLE ; seuil achat non atteint
- ZRO-EUR : 1.4815 € ; score 88.02/100 ; SURVEILLE ; SELLER_HEAVY_BOOK, WICK_SETUP
- CFG-EUR : 0.142719 € ; score 87.51/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- JASMY-EUR : 0.0047481 € ; score 86.86/100 ; SURVEILLE ; SELLER_HEAVY_BOOK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| 0G-EUR | 0.30628 | +39.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CELO-EUR | 0.09924 | +23.32 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CRV-EUR | 0.35313 | +21.70 % | DETECTED_EARLY | NONE | INTERPRETATION |
| POND-EUR | 0.0015766 | +21.28 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ZBCN-EUR | 0.0021517 | +20.88 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CVX-EUR | 2.0916 | +18.12 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| SYRUP-EUR | 0.22225 | +17.84 % | DETECTED_EARLY | NONE | INTERPRETATION |
| AAVE-EUR | 153.17 | +16.23 % | DETECTED_EARLY | NONE | NONE |
| GRASS-EUR | 0.62018 | +16.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ICP-EUR | 3.0537 | +15.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique : 1772 scans ; 758098 observations ; 1314 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
