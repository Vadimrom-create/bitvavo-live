# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T21:58:05.572295+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : VET-EUR | action ACHETE_MAINTENANT | opportunité 8.264 | entrée 7.400 | trend 8.700 | rang 7.902
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : PYTH-EUR | action PLACE_LIMITE_PASSIVE | opportunité 9.107 | entrée 6.300 | trend 7.500 | rang 7.885
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ACH-EUR | action LATENT_ACCELERATOR | opportunité 8.905 | entrée 5.650 | trend 7.400 | rang 7.652
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : SUPER-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.837 | entrée 6.650 | trend 8.950 | rang 7.832
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VET-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.902
2. DOT-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 7.894
3. PYTH-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.885

## Accélération indépendante

- SWELL-EUR — CONFIRMED_ACCELERATION — score 9.031/10 — DETECTED_BUT_TOO_LATE
- POND-EUR — CONFIRMED_ACCELERATION — score 8.091/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- DGB-EUR — CONFIRMED_ACCELERATION — score 7.997/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KERNEL-EUR — CONFIRMED_ACCELERATION — score 6.890/10 — DETECTED_BUT_TOO_LATE
- ELSA-EUR — BUILDING_ACCELERATION — score 5.592/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- GIGA-EUR — MEMORY_24H — score mémoire 9.738/10 — sources ACCELERATION — MEMORY_ONLY
- SWELL-EUR — ACTIVE_NOW — score mémoire 9.031/10 — sources ACCELERATION, DECISION_LAYER — DETECTED_BUT_TOO_LATE
- BTT-EUR — MEMORY_24H — score mémoire 8.767/10 — sources ACCELERATION — MEMORY_ONLY
- LUMIA-EUR — MEMORY_24H — score mémoire 8.655/10 — sources ACCELERATION — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- SFP-EUR — MEMORY_24H — score mémoire 8.323/10 — sources ACCELERATION — MEMORY_ONLY
- POND-EUR — ACTIVE_NOW — score mémoire 8.091/10 — sources ACCELERATION, V4 — WATCH_ONLY
- DGB-EUR — ACTIVE_NOW — score mémoire 7.997/10 — sources ACCELERATION, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.902/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- ZRC-EUR +91.73% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +88.61% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZETA-EUR +51.25% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- SWELL-EUR +44.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FORM-EUR +40.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AIOZ-EUR +36.05% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PHA-EUR +34.20% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PTB-EUR +32.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GRASS-EUR +23.72% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PUFFER-EUR +23.12% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
