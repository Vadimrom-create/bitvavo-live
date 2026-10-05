# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T15:56:34.657091+00:00
État : OK | marchés EUR : 427 | V4 : 366 | données valides : 426
Récupération : 2026-10-05T15:56:01.918929+00:00 | âge ticker : 147.8 s | durée : 148.5 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 426/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.
- ICP-EUR : 3.1005 € | IGNITION | score 88.66/100 | entrée 6.75/10
  Entrée 3.1028 € ; stop 2.9721 € ; TP1 3.3641 € ; TP2 3.4948 € ; montant 245.02 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 3.353/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- CAP-EUR : 0.0619201 € ; score 83.00/100 ; SURVEILLE ; SPREAD_RISK, SELLER_HEAVY_BOOK
- BAT-EUR : 0.09333 € ; score 82.80/100 ; SURVEILLE ; WICK_SETUP
- MAGIC-EUR : 0.05528 € ; score 80.52/100 ; SURVEILLE ; seuil achat non atteint
- HOT-EUR : 0.00040537 € ; score 80.28/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- WLD-EUR : 0.50567 € ; score 78.96/100 ; SURVEILLE ; WICK_SETUP

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.191282 | +76.51 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RLC-EUR | 0.515 | +59.78 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.069821 | +41.64 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.9075 | +22.99 % | DETECTED_EARLY | NONE | INTERPRETATION |
| ZEUS-EUR | 0.0024855 | +22.73 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SCR-EUR | 0.025947 | +16.38 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.046134 | +15.83 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RAD-EUR | 0.27294 | +15.56 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.8063 | +14.66 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| NIL-EUR | 0.090587 | +13.91 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |

Historique (snapshot asynchrone) : 2076 scans ; 888368 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
