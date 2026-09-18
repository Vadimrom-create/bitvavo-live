# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T05:42:56.243231+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : SYRUP-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.621 | entrée 6.700 | trend 7.950 | rang 7.326
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.576 | entrée 7.200 | trend 7.650 | rang 7.250
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. SYRUP-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.326
2. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.250
3. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.237

## Accélération indépendante

- AVA-EUR — CONFIRMED_ACCELERATION — score 7.549/10 — DETECTED_BUT_TOO_LATE
- SYN-EUR — BUILDING_ACCELERATION — score 5.962/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- DRIFT-EUR — BUILDING_ACCELERATION — score 5.233/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.268/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.160/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZORA-EUR — ACTIVE_NOW — score mémoire 8.087/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.076/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.044/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.979/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.895/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- INJ-EUR — ACTIVE_NOW — score mémoire 7.839/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- XVG-EUR — ACTIVE_NOW — score mémoire 7.836/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- DRIFT-EUR +32.03% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +30.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- COTI-EUR +28.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +28.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +26.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +25.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +23.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +22.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TREAD-EUR +20.57% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MET-EUR +20.33% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
