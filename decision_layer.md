# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T08:59:21.708216+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : KAS-EUR | action ACHETE_MAINTENANT | opportunité 9.338 | entrée 8.200 | trend 8.450 | rang 8.403
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : ZEN-EUR | action PLACE_LIMITE_PASSIVE | opportunité 8.622 | entrée 6.000 | trend 7.550 | rang 7.579
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : WAL-EUR | action LATENT_ACCELERATOR | opportunité 8.269 | entrée 4.500 | trend 8.950 | rang 7.720
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : GRASS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.176 | entrée 7.150 | trend 8.250 | rang 8.191
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.403
2. INJ-EUR — MEILLEUR_ACHAT_IMMEDIAT — ACHETE_MAINTENANT — rank 8.246
3. GRASS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.191

## Accélération indépendante

- USELESS-EUR — CONFIRMED_ACCELERATION — score 9.492/10 — DETECTED_BUT_TOO_LATE
- ZETA-EUR — CONFIRMED_ACCELERATION — score 9.088/10 — DETECTED_BUT_TOO_LATE
- NOS-EUR — CONFIRMED_ACCELERATION — score 9.000/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- FET-EUR — CONFIRMED_ACCELERATION — score 8.482/10 — DETECTED_BUT_TOO_LATE
- METIS-EUR — CONFIRMED_ACCELERATION — score 8.477/10 — DETECTED_BUT_TOO_LATE
- BOME-EUR — CONFIRMED_ACCELERATION — score 8.119/10 — DETECTED_BUT_TOO_LATE
- ENS-EUR — CONFIRMED_ACCELERATION — score 7.398/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- TAI-EUR — CONFIRMED_ACCELERATION — score 7.337/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- 0G-EUR — CONFIRMED_ACCELERATION — score 6.960/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- KNC-EUR — CONFIRMED_ACCELERATION — score 6.701/10 — REQUIRES_FINAL_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- XLM-EUR — ACTIVE_NOW — score mémoire 7.368/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- PENGU-EUR — ACTIVE_NOW — score mémoire 6.991/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- USELESS-EUR — ACTIVE_NOW — score mémoire 9.492/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- CTC-EUR — MEMORY_24H — score mémoire 9.245/10 — sources ACCELERATION — MEMORY_ONLY
- ZETA-EUR — ACTIVE_NOW — score mémoire 9.088/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- SWEAT-EUR — MEMORY_24H — score mémoire 9.049/10 — sources ACCELERATION — MEMORY_ONLY
- NOS-EUR — ACTIVE_NOW — score mémoire 9.000/10 — sources ACCELERATION, V4 — WATCH_ONLY
- MOCA-EUR — MEMORY_24H — score mémoire 8.589/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- LSK-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.482/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- ZETA-EUR +81.99% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PTB-EUR +51.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +39.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +35.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +34.04% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KMNO-EUR +30.05% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EPIC-EUR +26.61% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +25.66% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PHA-EUR +23.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +23.08% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
