# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-13T02:47:54.494365+00:00
État : OK | marchés EUR : 427 | V4 : 396 | données valides : 427
Récupération : 2026-10-13T02:46:45.670344+00:00 | âge ticker : 184.1 s | durée : 184.9 s

## ACHÈTE — signal V4 et plan théorique

AUCUN ACHAT VALIDÉ — cette absence ne valide pas les marchés aux données insuffisantes.
Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

## SURVEILLE

- FLUID-EUR : 1.9855 € ; score 76.94/100 ; SURVEILLE ; WICK_SETUP
- TIA-EUR : 0.51192 € ; score 74.94/100 ; SURVEILLE ; seuil achat non atteint
- PYTH-EUR : 0.074969 € ; score 74.40/100 ; SURVEILLE ; seuil achat non atteint
- HUMA-EUR : 0.030583 € ; score 73.45/100 ; SURVEILLE ; seuil achat non atteint
- LUMIA-EUR : 0.099622 € ; score 73.11/100 ; SURVEILLE ; SPREAD_RISK

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| GTC-EUR | 0.21411 | +35.20 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| OSMO-EUR | 0.042814 | +31.30 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| CT-EUR | 0.36377 | +28.85 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RSR-EUR | 0.0018286 | +24.33 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SKL-EUR | 0.0052389 | +17.94 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| RENDER-EUR | 1.8857 | +6.10 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| PUFFER-EUR | 0.021409 | +6.00 % | DETECTED_EARLY | NONE | INTERPRETATION |
| DODO-EUR | 0.017702 | +5.70 % | INSUFFICIENT_HISTORY | HISTORY | NOT_APPLICABLE |
| SAFE-EUR | 0.110273 | +4.96 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| STX-EUR | 0.36542 | +4.72 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |

Historique (snapshot asynchrone) : 2151 scans ; 920369 observations ; 1658 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
