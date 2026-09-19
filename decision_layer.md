# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T05:45:26.336018+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : XRP-EUR | action ACHETE_MAINTENANT | opportunité 8.443 | entrée 7.700 | trend 4.750 | rang 6.580
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.426 | entrée 6.100 | trend 8.250 | rang 7.358
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.358
2. XRP-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 6.580

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.234/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.187/10 — sources ACCELERATION, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.011/10 — sources V4 — WATCH_ONLY
- SENT-EUR — MEMORY_24H — score mémoire 7.950/10 — sources V4 — MEMORY_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 7.852/10 — sources ACCELERATION, V4 — WATCH_ONLY
- SSV-EUR — ACTIVE_NOW — score mémoire 7.845/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.823/10 — sources V4 — WATCH_ONLY
- PYTH-EUR — ACTIVE_NOW — score mémoire 7.747/10 — sources V4 — WATCH_ONLY
- T-EUR — ACTIVE_NOW — score mémoire 7.733/10 — sources ACCELERATION, V4 — WATCH_ONLY
- BEAM-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +57.94% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- F-EUR +34.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +31.13% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +27.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +27.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +26.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +22.76% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ZIG-EUR +21.37% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +21.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +18.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
