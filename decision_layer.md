# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T17:11:00.188141+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.700 | entrée 7.250 | trend 7.650 | rang 7.046
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.046
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.491

## Accélération indépendante

- UNI-EUR — BUILDING_ACCELERATION — score 5.829/10 — DETECTED_BUT_TOO_LATE
- AVA-EUR — BUILDING_ACCELERATION — score 5.817/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 4.946/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 4.901/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.193/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 8.088/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ZRO-EUR — ACTIVE_NOW — score mémoire 8.025/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.986/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.980/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.979/10 — sources V4 — WATCH_ONLY
- JUP-EUR — ACTIVE_NOW — score mémoire 7.959/10 — sources V4 — DETECTED_BUT_TOO_LATE
- TAO-EUR — ACTIVE_NOW — score mémoire 7.907/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.853/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- AVA-EUR +100.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +33.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KSM-EUR +26.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +25.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- UNI-EUR +25.24% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +22.90% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- PEAQ-EUR +21.81% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- GALA-EUR +20.23% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ROSE-EUR +16.54% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QUID-EUR +16.19% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
