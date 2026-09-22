# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-22T06:53:14.178439+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : HYPE-EUR | action ACHETE_MAINTENANT | opportunité 7.956 | entrée 7.850 | trend 7.400 | rang 7.404
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : INIT-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.236 | entrée 6.000 | trend 9.200 | rang 8.015
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : ARX-EUR | action LATENT_ACCELERATOR | opportunité 8.245 | entrée 5.650 | trend 8.550 | rang 7.491
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : 0G-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.256 | entrée 6.300 | trend 8.600 | rang 8.272
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. 0G-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.272
2. COW-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.091
3. INIT-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 8.015

## Accélération indépendante

- FLOCK-EUR — CONFIRMED_ACCELERATION — score 8.979/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — CONFIRMED_ACCELERATION — score 8.235/10 — DETECTED_BUT_TOO_LATE
- SEI-EUR — CONFIRMED_ACCELERATION — score 8.037/10 — DETECTED_BUT_TOO_LATE
- CARV-EUR — CONFIRMED_ACCELERATION — score 7.482/10 — DETECTED_BUT_TOO_LATE
- EGLD-EUR — BUILDING_ACCELERATION — score 6.399/10 — DETECTED_BUT_TOO_LATE
- FARTCOIN-EUR — BUILDING_ACCELERATION — score 6.286/10 — DETECTED_BUT_TOO_LATE
- ZRC-EUR — BUILDING_ACCELERATION — score 5.843/10 — DETECTED_BUT_TOO_LATE
- COW-EUR — BUILDING_ACCELERATION — score 5.615/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- USELESS-EUR — BUILDING_ACCELERATION — score 5.606/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.366/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- PHA-EUR — MEMORY_24H — score mémoire 9.177/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- GIGA-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- SWEAT-EUR — MEMORY_24H — score mémoire 9.062/10 — sources ACCELERATION — MEMORY_ONLY
- VELO-EUR — MEMORY_24H — score mémoire 9.000/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FLOCK-EUR — ACTIVE_NOW — score mémoire 8.979/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ZEUS-EUR — MEMORY_24H — score mémoire 8.781/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- MEW-EUR — MEMORY_24H — score mémoire 8.523/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XMN-EUR — MEMORY_24H — score mémoire 8.438/10 — sources ACCELERATION — MEMORY_ONLY
- 0G-EUR — ACTIVE_NOW — score mémoire 8.272/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- BOME-EUR — ACTIVE_NOW — score mémoire 8.235/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ZRC-EUR +109.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ICX-EUR +107.09% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- AIOZ-EUR +49.12% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEPE-EUR +27.88% — DETECTED_EARLY — couche NONE — action NONE
- WIF-EUR +23.18% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- KERNEL-EUR +23.11% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GRASS-EUR +21.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FORM-EUR +20.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FARTCOIN-EUR +19.11% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CARV-EUR +18.53% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
