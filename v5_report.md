# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T09:43:56.907951+00:00
État : OK | marchés EUR : 429 | V4 : 393 | données valides : 429
Récupération : 2026-09-30T09:43:28.341558+00:00 | âge ticker : 144.9 s | durée : 146.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : INSUFFICIENT_NET_RISK_REWARD
- LDO-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SOL-EUR : INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : INSUFFICIENT_NET_RISK_REWARD
- CRV-EUR : 0.35854 € | IGNITION | score 93.29/100 | entrée 7.25/10
  Entrée 0.35877 € ; stop 0.34207 € ; TP1 0.39216 € ; TP2 0.40886 € ; montant 224.78 € ; risque théorique 12.00 € ; R/R net 1.61.
  Chase risk : 4.446/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- DOT-EUR : 1.0923 € | IGNITION | score 89.25/100 | entrée 7.00/10
  Entrée 1.0938 € ; stop 1.0505 € ; TP1 1.1804 € ; TP2 1.2237 € ; montant 250.00 € ; risque théorique 11.61 € ; R/R net 1.55.
  Chase risk : 2.999/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- XLM-EUR : 0.20089 € ; score 93.65/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- W-EUR : 0.01205 € ; score 92.10/100 ; SURVEILLE ; WICK_SETUP
- GRT-EUR : 0.025311 € ; score 91.75/100 ; SURVEILLE ; seuil achat non atteint
- SUSHI-EUR : 0.242 € ; score 90.68/100 ; SURVEILLE ; seuil achat non atteint
- LDO-EUR : 0.42355 € ; score 90.12/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| MOVR-EUR | 1.7732 | +100.09 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GTC-EUR | 0.103361 | +33.74 % | DETECTED_EARLY | NONE | INTERPRETATION |
| GLMR-EUR | 0.008979 | +32.49 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SOON-EUR | 0.40007 | +31.17 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| PHA-EUR | 0.071258 | +25.13 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ARK-EUR | 0.2627 | +21.41 % | DETECTED_EARLY | NONE | INTERPRETATION |
| 0G-EUR | 0.29829 | +13.71 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GWEI-EUR | 0.0208 | +13.15 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZRO-EUR | 1.551 | +12.60 % | DETECTED_EARLY | NONE | NONE |
| MEW-EUR | 0.00047617 | +12.42 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1831 scans ; 783409 observations ; 1365 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
