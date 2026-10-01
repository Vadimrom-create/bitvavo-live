# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-01T17:38:44.564203+00:00
État : OK | marchés EUR : 430 | V4 : 387 | données valides : 430
Récupération : 2026-10-01T17:38:17.947455+00:00 | âge ticker : 145.9 s | durée : 147.2 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- AAVE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : INSUFFICIENT_NET_RISK_REWARD
- BNB-EUR : INSUFFICIENT_NET_RISK_REWARD
- ETH-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- GALA-EUR : INSUFFICIENT_NET_RISK_REWARD
- RENDER-EUR : INSUFFICIENT_NET_RISK_REWARD
- STX-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- SUI-EUR : 1.04728 € | IGNITION | score 90.05/100 | entrée 7.85/10
  Entrée 1.04763 € ; stop 1.00048 € ; TP1 1.14193 € ; TP2 1.18908 € ; montant 231.44 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 3.889/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.
- WIF-EUR : 0.22798 € | IGNITION | score 86.87/100 | entrée 7.00/10
  Entrée 0.22839 € ; stop 0.2166 € ; TP1 0.25197 € ; TP2 0.26376 € ; montant 205.33 € ; risque théorique 12.00 € ; R/R net 1.64.
  Chase risk : 5.573/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- GALA-EUR : 0.0020507 € ; score 92.88/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- AVAX-EUR : 9.7542 € ; score 90.86/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- WAL-EUR : 0.030329 € ; score 88.09/100 ; SURVEILLE ; seuil achat non atteint
- RENDER-EUR : 1.7053 € ; score 87.95/100 ; SURVEILLE ; INSUFFICIENT_NET_RISK_REWARD
- SUPER-EUR : 0.18348 € ; score 86.91/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00056696 | +117.72 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| MOVR-EUR | 2.595 | +81.79 % | DETECTED_EARLY | NONE | INTERPRETATION |
| CAP-EUR | 0.077903 | +33.47 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| CT-EUR | 0.43249 | +28.17 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| ALICE-EUR | 0.18174 | +27.16 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| MEGA-EUR | 0.04657 | +24.52 % | DETECTED_EARLY | NONE | NONE |
| MON-EUR | 0.030702 | +22.12 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.17655 | +20.89 % | DETECTED_EARLY | NONE | INTERPRETATION |
| NOS-EUR | 0.48805 | +19.82 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ARK-EUR | 0.22101 | +16.18 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1922 scans ; 822538 observations ; 1485 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
