# Bitvavo — V4 mesurée / infrastructure V5

Scan UTC : 2026-10-02T06:28:03.496841+00:00
État : OK | marchés EUR : 430 | V4 : 384 | données valides : 430
Récupération : 2026-10-02T06:27:30.431825+00:00 | âge ticker : 155.8 s | durée : 157.1 s

## ACHÈTE — signal V4 et plan théorique

Bougies utilisables : 5 min 430/430 ; 15 min 430/430.
Les intervalles sans transaction sont représentés explicitement à volume 0 ; aucune transaction n’est inventée.

Achats bruts V4 bloqués avant alerte :
- HYPE-EUR : WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD
- LTC-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- PUMP-EUR : WICK_SETUP, STABILITY_HOLD, INSUFFICIENT_NET_RISK_REWARD
- AAVE-EUR : 162.93 € | IGNITION | score 84.41/100 | entrée 7.05/10
  Entrée 163.24 € ; stop 156.01 € ; TP1 177.7 € ; TP2 184.93 € ; montant 234.67 € ; risque théorique 12.00 € ; R/R net 1.59.
  Chase risk : 2.681/10 (diagnostic non calibré). Probabilités +10/+20/+30/+40 % : indisponibles.

## SURVEILLE

- WLD-EUR : 0.47874 € ; score 89.13/100 ; SURVEILLE ; WICK_SETUP
- TIA-EUR : 0.40555 € ; score 86.45/100 ; SURVEILLE ; WICK_SETUP
- BRETT-EUR : 0.0053253 € ; score 85.07/100 ; SURVEILLE ; SELLER_HEAVY_BOOK
- VVV-EUR : 25.3597 € ; score 82.78/100 ; SURVEILLE ; WICK_SETUP
- HYPE-EUR : 80.221 € ; score 82.23/100 ; SURVEILLE ; WICK_SETUP, INSUFFICIENT_NET_RISK_REWARD

## Contrôle des hausses

| Marché | Prix € | 24 h | Détection | Couche d’échec | Actionnabilité |
|---|---:|---:|---|---|---|
| SWEAT-EUR | 0.00075463 | +190.35 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| GTC-EUR | 0.130417 | +53.98 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| CT-EUR | 0.48405 | +32.26 % | DETECTED_EARLY | NONE | INTERPRETATION |
| SCR-EUR | 0.029013 | +29.72 % | DETECTED_EARLY | NONE | INTERPRETATION |
| MEGA-EUR | 0.04665 | +16.02 % | DETECTED_EARLY | NONE | NONE |
| TREAD-EUR | 0.83822 | +11.61 % | DETECTED_EARLY | NONE | INTERPRETATION |
| PONKE-EUR | 0.023239 | +11.15 % | NOT_DETECTED | SCANNER_SCORING | NOT_APPLICABLE |
| SUPER-EUR | 0.20219 | +11.03 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| ZRO-EUR | 1.662 | +10.80 % | DETECTED_EARLY | NONE | ENTRY_TIMING_OR_EXECUTION |
| SYN-EUR | 0.16074 | +10.73 % | DETECTED_EARLY | NONE | INTERPRETATION |

Historique : 1961 scans ; 839308 observations ; 1530 épisodes d’achat évaluables.
V5 optimisée : aucune. Supériorité sur V4 : non démontrée. Probabilités : non calibrées.
Le cash et le portefeuille du plan sont hypothétiques. Aucun ordre réel n’est envoyé.
