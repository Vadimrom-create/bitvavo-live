# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T07:45:47.900800+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.237 | entrée 7.600 | trend 7.950 | rang 7.761
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.853 | entrée 6.850 | trend 8.300 | rang 7.588
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.761
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.588
3. SAGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.026

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 7.876/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.861/10 — sources V4 — WATCH_ONLY
- COW-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources V4 — WATCH_ONLY
- ETC-EUR — MEMORY_24H — score mémoire 7.770/10 — sources V4 — MEMORY_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 7.761/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.730/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.714/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.711/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +71.97% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +35.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +26.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +17.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +17.27% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +15.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +14.46% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +12.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVAX-EUR +12.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SOLV-EUR +12.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
