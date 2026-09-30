# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-30T05:44:39.336888+00:00
État : OK | marchés EUR : 429 | V4 : 392 | données valides : 429
Récupération : 2026-09-30T05:43:42.281088+00:00 | âge ticker : 175.3 s | durée : 175.9 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 429/429 ; 15 min 429/429.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- ADA-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : INSUFFICIENT_NET_RISK_REWARD
- ICP-EUR : 3.0656 € | IGNITION | score 87.88/100 | entrée 6.65/10
  Entrée 3.0654 € ; stop 2.9368 € ; TP1 3.3226 € ; TP2 3.4512 € ; montant 245.88 € ; risque théorique 12.00 € ; R/R net 1.57.
  Chase risk : 1.983/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- AVNT-EUR : 0.11105 € ; score 92.35/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : 59.296 € ; score 91.21/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.0020129 € ; score 90.19/100 ; SURVEILLE ; WICK_SETUP
- ADA-EUR : 0.21668 € ; score 89.83/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- SEI-EUR : 0.065946 € ; score 89.11/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SOON-EUR | 0.38048 | +47.06 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MOVR-EUR | 1.2417 | +47.05 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZBCN-EUR | 0.0024415 | +28.75 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEW-EUR | 0.00050211 | +22.14 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ZRO-EUR | 1.6333 | +21.33 % | DETECTED_EARLY | NONE | NONE |
| PUMP-EUR | 0.0050667 | +18.18 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PHA-EUR | 0.065349 | +17.53 % | DETECTED_EARLY | NONE | INTERPRETATION |
| INIT-EUR | 0.092521 | +17.03 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| QNT-EUR | 250.859 | +15.65 % | DETECTED_EARLY | NONE | INTERPRETATION |
| FUEL-EUR | 0.0006726 | +14.58 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |

Historique : 1820 scans ; 778690 observations ; 1358 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
