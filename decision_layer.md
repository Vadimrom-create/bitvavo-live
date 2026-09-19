# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T18:22:06.622604+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : PEPE-EUR | action ACHETE_MAINTENANT | opportunité 8.057 | entrée 6.900 | trend 8.450 | rang 7.278
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.067 | entrée 7.550 | trend 7.550 | rang 7.682
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.682
2. HYPE-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.652
3. SOL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.470

## Accélération indépendante

- ZAMA-EUR — CONFIRMED_ACCELERATION — score 6.831/10 — DETECTED_BUT_TOO_LATE
- EPIC-EUR — BUILDING_ACCELERATION — score 6.188/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PEPE-EUR — ACTIVE_NOW — score mémoire 7.278/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PROVE-EUR — ACTIVE_NOW — score mémoire 8.324/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.005/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.882/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- RED-EUR — ACTIVE_NOW — score mémoire 7.821/10 — sources V4 — WATCH_ONLY
- ATH-EUR — ACTIVE_NOW — score mémoire 7.740/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.717/10 — sources V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.686/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +44.15% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +36.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +36.49% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +28.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +25.72% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +22.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +19.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +19.23% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- G-EUR +18.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +16.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
