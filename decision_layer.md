# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T05:58:39.688793+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : AAVE-EUR | action ACHETE_MAINTENANT | opportunité 8.405 | entrée 7.400 | trend 8.950 | rang 8.156
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : APT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.494 | entrée 6.550 | trend 8.450 | rang 7.172
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : SOL-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.937 | entrée 7.350 | trend 8.250 | rang 7.701
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. AAVE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.156
2. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.701
3. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.643

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- PENDLE-EUR — ACTIVE_NOW — score mémoire 8.294/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.156/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RAY-EUR — ACTIVE_NOW — score mémoire 8.140/10 — sources ACCELERATION, V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.972/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.863/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources V4 — WATCH_ONLY
- SSV-EUR — MEMORY_24H — score mémoire 7.845/10 — sources V4 — MEMORY_ONLY
- T-EUR — MEMORY_24H — score mémoire 7.733/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ARX-EUR — ACTIVE_NOW — score mémoire 7.726/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +55.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EDGE-EUR +46.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +30.91% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +29.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +26.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CPOOL-EUR +21.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +21.10% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- ZAMA-EUR +21.02% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +20.38% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIG-EUR +19.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
