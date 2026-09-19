# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T12:42:48.644995+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 8.263 | entrée 7.800 | trend 8.750 | rang 8.080
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : RAY-EUR | action LATENT_ACCELERATOR | opportunité 7.693 | entrée 4.500 | trend 8.550 | rang 7.380
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : VET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.935 | entrée 7.600 | trend 8.700 | rang 7.732
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.080
2. ONDO-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.875
3. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.732

## Accélération indépendante

- COTI-EUR — BUILDING_ACCELERATION — score 5.005/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- ONDO-EUR — ACTIVE_NOW — score mémoire 7.875/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- KMNO-EUR — ACTIVE_NOW — score mémoire 8.535/10 — sources V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ROSE-EUR — ACTIVE_NOW — score mémoire 8.321/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.309/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.155/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 8.115/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- HYPE-EUR — ACTIVE_NOW — score mémoire 8.080/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.067/10 — sources V4 — DETECTED_BUT_TOO_LATE
- COW-EUR — ACTIVE_NOW — score mémoire 8.067/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- EDGE-EUR +40.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +39.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +36.13% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZAMA-EUR +35.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HEI-EUR +31.52% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +29.39% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- CAP-EUR +27.47% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +26.20% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +23.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +21.68% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
