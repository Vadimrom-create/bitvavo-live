# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T16:01:38.871451+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : INJ-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.640 | entrée 7.250 | trend 8.300 | rang 7.313
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.313
2. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.011

## Accélération indépendante

- REZ-EUR — CONFIRMED_ACCELERATION — score 9.305/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- REZ-EUR — ACTIVE_NOW — score mémoire 9.305/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 8.248/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.051/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.778/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.771/10 — sources V4 — WATCH_ONLY
- AVAX-EUR — MEMORY_24H — score mémoire 7.656/10 — sources V4 — MEMORY_ONLY
- PROM-EUR — ACTIVE_NOW — score mémoire 7.655/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.647/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.622/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.595/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +264.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +68.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +35.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +19.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +18.89% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +17.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- STRAX-EUR +10.40% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- BAT-EUR +10.20% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +9.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FLUX-EUR +9.75% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
