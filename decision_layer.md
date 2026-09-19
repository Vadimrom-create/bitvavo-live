# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-19T15:19:15.097339+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 9.250 | entrée 8.250 | trend 8.750 | rang 8.582
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : VET-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.895 | entrée 5.950 | trend 8.700 | rang 7.611
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : UNI-EUR | action LATENT_ACCELERATOR | opportunité 7.402 | entrée 4.500 | trend 8.150 | rang 6.848
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.448 | entrée 7.200 | trend 8.300 | rang 7.847
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. HYPE-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.582
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.847
3. VET-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.611

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- HYPE-EUR — ACTIVE_NOW — score mémoire 8.582/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZAMA-EUR — MEMORY_24H — score mémoire 8.324/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ENS-EUR — ACTIVE_NOW — score mémoire 8.129/10 — sources V4 — WATCH_ONLY
- AAVE-EUR — ACTIVE_NOW — score mémoire 8.073/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- MIOTA-EUR — ACTIVE_NOW — score mémoire 8.036/10 — sources V4 — WATCH_ONLY
- VVV-EUR — ACTIVE_NOW — score mémoire 8.007/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources V4 — WATCH_ONLY
- SUPER-EUR — ACTIVE_NOW — score mémoire 7.913/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.872/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 7.871/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZAMA-EUR +41.77% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +39.25% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SYN-EUR +31.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- EPIC-EUR +27.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- SAGA-EUR +27.83% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRK-EUR +24.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDGE-EUR +20.89% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AIOZ-EUR +20.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ENA-EUR +19.98% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AVAX-EUR +16.04% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
