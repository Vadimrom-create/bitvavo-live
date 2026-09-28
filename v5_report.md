# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-09-28T11:21:08.193973+00:00
État : OK | marchés EUR : 427 | V4 : 396 | données valides : 427
Récupération : 2026-09-28T11:20:36.339055+00:00 | âge ticker : 147.5 s | durée : 148.4 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 427/427 ; 15 min 427/427.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- GRAM-EUR : STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- KAS-EUR : INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- XLM-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- LINK-EUR : 12.2791 € | IGNITION | score 80.48/100 | entrée 6.90/10
  Entrée 12.2782 € ; stop 11.8283 € ; TP1 13.1779 € ; TP2 13.6278 € ; montant 250.00 € ; risque théorique 10.88 € ; R/R net 1.52.
  Chase risk : 2.686/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- LTC-EUR : 63.224 € ; score 92.84/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- AVNT-EUR : 0.10904 € ; score 90.05/100 ; SURVEILLE ; seuil achat non atteint
- GALA-EUR : 0.001905 € ; score 88.30/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- MOVR-EUR : 0.8837 € ; score 84.34/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- BEAM-EUR : 0.0017742 € ; score 83.25/100 ; SURVEILLE ; seuil achat non atteint

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| QNT-EUR | 215.047 | +48.60 % | DETECTED_EARLY | NONE | INTERPRETATION |
| HBAR-EUR | 0.101316 | +21.82 % | DETECTED_EARLY | NONE | NONE |
| AUDIO-EUR | 0.014949 | +13.79 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| GRT-EUR | 0.02768 | +13.19 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SOON-EUR | 0.2757 | +11.06 % | DETECTED_EARLY | NONE | INTERPRETATION |
| IKA-EUR | 0.0018225 | +10.60 % | DETECTED_TOO_LATE | NONE | INTERPRETATION |
| PUMP-EUR | 0.0042972 | +10.00 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| NMR-EUR | 9.3017 | +9.35 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| XDC-EUR | 0.029963 | +9.29 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ALGO-EUR | 0.111976 | +8.52 % | DETECTED_EARLY | NONE | NONE |

Historique : 1691 scans ; 723425 observations ; 1243 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
