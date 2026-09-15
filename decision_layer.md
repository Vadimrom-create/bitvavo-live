# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T04:59:27.800571+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NPC-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.000 | entrée 6.750 | trend 7.750 | rang 7.860
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NPC-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.860
2. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.658
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.206

## Accélération indépendante

- NPC-EUR — BUILDING_ACCELERATION — score 4.751/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION — MEMORY_ONLY
- CNPY-EUR — MEMORY_24H — score mémoire 8.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.417/10 — sources V4 — WATCH_ONLY
- USELESS-EUR — ACTIVE_NOW — score mémoire 8.086/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- AERO-EUR — ACTIVE_NOW — score mémoire 8.079/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.022/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 8.010/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.904/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.758/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +33.70% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +28.63% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +16.75% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- ASTR-EUR +14.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CTR-EUR +11.12% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACX-EUR +9.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +6.98% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- OP-EUR +6.97% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RED-EUR +6.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- INIT-EUR +6.89% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
