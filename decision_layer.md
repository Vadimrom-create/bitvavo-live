# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T06:18:56.067773+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : HYPE-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.700 | entrée 6.750 | trend 7.950 | rang 7.452
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.452
2. UNI-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.297
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.004

## Accélération indépendante

- ZAMA-EUR — CONFIRMED_ACCELERATION — score 7.960/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- C-EUR — MEMORY_24H — score mémoire 8.647/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.979/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZAMA-EUR — ACTIVE_NOW — score mémoire 7.960/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources V4 — WATCH_ONLY
- DOT-EUR — MEMORY_24H — score mémoire 7.831/10 — sources DECISION_LAYER, V4 — MEMORY_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- WAL-EUR — ACTIVE_NOW — score mémoire 7.696/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — MEMORY_24H — score mémoire 7.654/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- CELR-EUR +104.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- G-EUR +95.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +39.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +28.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SKL-EUR +27.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +21.96% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +19.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STX-EUR +17.16% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +15.04% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARK-EUR +14.72% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
