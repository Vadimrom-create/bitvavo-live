# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T14:59:55.397465+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.779 | entrée 7.250 | trend 8.100 | rang 7.318
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.318
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.805

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.284/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.189/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.117/10 — sources V4 — DETECTED_BUT_TOO_LATE
- UNI-EUR — ACTIVE_NOW — score mémoire 8.006/10 — sources V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 8.002/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources ACCELERATION, V4 — WATCH_ONLY
- APT-EUR — ACTIVE_NOW — score mémoire 7.909/10 — sources V4 — WATCH_ONLY
- BAT-EUR — ACTIVE_NOW — score mémoire 7.891/10 — sources V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — ACTIVE_NOW — score mémoire 7.847/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +224.37% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +74.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +23.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +21.07% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- STRAX-EUR +20.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUNDIX-EUR +18.06% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- POWR-EUR +14.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTC-EUR +14.46% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- FLOCK-EUR +13.58% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +13.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
