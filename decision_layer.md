# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-20T07:58:28.130108+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.914 | entrée 6.300 | trend 8.300 | rang 7.550
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.550
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.244
3. SAGA-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.074

## Accélération indépendante

- CELR-EUR — CONFIRMED_ACCELERATION — score 7.471/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- COW-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources V4 — WATCH_ONLY
- NPC-EUR — MEMORY_24H — score mémoire 7.903/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- MERL-EUR — ACTIVE_NOW — score mémoire 7.844/10 — sources V4 — WATCH_ONLY
- PROVE-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.766/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.731/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZK-EUR — ACTIVE_NOW — score mémoire 7.703/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — ACTIVE_NOW — score mémoire 7.700/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.641/10 — sources V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.606/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CELR-EUR +79.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZIL-EUR +32.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +26.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +19.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SKL-EUR +16.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- C-EUR +16.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTSI-EUR +15.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ONG-EUR +14.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +13.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- JTO-EUR +12.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
