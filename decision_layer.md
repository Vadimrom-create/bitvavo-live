# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T16:41:44.616359+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : DOT-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.844 | entrée 6.500 | trend 8.300 | rang 7.418
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.418
2. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.099
3. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.824

## Accélération indépendante

- CNPY-EUR — CONFIRMED_ACCELERATION — score 9.990/10 — DETECTED_BUT_TOO_LATE
- G-EUR — BUILDING_ACCELERATION — score 5.546/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CNPY-EUR — ACTIVE_NOW — score mémoire 9.990/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.221/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.173/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.121/10 — sources V4 — WATCH_ONLY
- ZIG-EUR — MEMORY_24H — score mémoire 8.066/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- PEAQ-EUR — MEMORY_24H — score mémoire 7.955/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.954/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- LPT-EUR — MEMORY_24H — score mémoire 7.863/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.834/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.826/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +91.14% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +64.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +53.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- C-EUR +36.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +31.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARB-EUR +27.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +26.00% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- A-EUR +21.70% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- UNI-EUR +20.99% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- S-EUR +20.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
