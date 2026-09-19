# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T15:34:16.525291+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 9.143 | entrée 8.900 | trend 8.750 | rang 8.608
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : INJ-EUR | action LATENT_ACCELERATOR | opportunité 7.566 | entrée 5.400 | trend 8.550 | rang 6.828
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.070 | entrée 7.450 | trend 8.300 | rang 7.721
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.608
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.721
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.607

## Accélération indépendante

- ZAMA-EUR — BUILDING_ACCELERATION — score 5.963/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- HYPE-EUR — ACTIVE_NOW — score mémoire 8.608/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.182/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.082/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.035/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- SENT-EUR — ACTIVE_NOW — score mémoire 8.014/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 7.958/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TIA-EUR — MEMORY_24H — score mémoire 7.871/10 — sources V4 — MEMORY_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.867/10 — sources V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 7.862/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +46.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +35.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- XTZ-EUR +33.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +27.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +25.08% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +20.48% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +19.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NOS-EUR +19.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ENA-EUR +18.80% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- EDGE-EUR +16.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
