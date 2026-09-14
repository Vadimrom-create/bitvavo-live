# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T19:02:43.734799+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.309 | entrée 6.950 | trend 7.650 | rang 7.555
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.555
2. DOT-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.211
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.777

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 6.633/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- CNPY-EUR — BUILDING_ACCELERATION — score 4.808/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.377/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.268/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.050/10 — sources V4 — WATCH_ONLY
- TIA-EUR — ACTIVE_NOW — score mémoire 7.936/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.934/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.885/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.860/10 — sources V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.845/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.798/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +33.46% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +28.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +26.29% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SENT-EUR +18.68% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +15.45% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +14.03% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PENDLE-EUR +11.11% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ACX-EUR +9.10% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +8.83% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RON-EUR +8.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
