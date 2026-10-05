# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-05T12:28:27.145345+00:00
État : OK | marchés EUR : 427 | V4 : 357 | données valides : 426
Récupération : 2026-10-05T12:27:52.863190+00:00 | âge ticker : 151.2 s | durée : 151.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 426/427 ; 15 min 426/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ICP-EUR : INSUFFICIENT_NET_RISK_REWARD
- PENDLE-EUR : 2.2922 € | IGNITION | score 80.79/100 | entrée 6.85/10
  Entrée 2.2976 € ; stop 2.1995 € ; TP1 2.4938 € ; TP2 2.5919 € ; montant 242.19 € ; risque théorique 12.00 € ; R/R net 1.58.
  Chase risk : 5.4/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- ICP-EUR : 3.0195 € ; score 89.90/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SKY-EUR : 0.088186 € ; score 87.31/100 ; SURVEILLE ; seuil achat non atteint
- KAIA-EUR : 0.03616 € ; score 86.94/100 ; SURVEILLE ; seuil achat non atteint
- APE-EUR : 0.15238 € ; score 85.51/100 ; SURVEILLE ; WICK_SETUP
- ALICE-EUR : 0.16256 € ; score 85.25/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.193983 | +76.16 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RLC-EUR | 0.51135 | +58.34 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| FLUID-EUR | 1.96 | +27.33 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.027366 | +23.03 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CARV-EUR | 0.046109 | +15.10 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| MOVR-EUR | 1.867 | +14.77 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PARTI-EUR | 0.028231 | +14.57 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PNT-EUR | 0.05565 | +12.89 % | NO_CONFIRMED_SHORT_TERM_EVENT | NOT_APPLICABLE | NOT_APPLICABLE |
| EDU-EUR | 0.05202 | +12.40 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| ADA-EUR | 0.24211 | +11.12 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 2071 scans ; 886233 observations ; 1639 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
