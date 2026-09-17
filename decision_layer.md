# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T00:21:02.207309+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.039 | entrée 6.000 | trend 9.200 | rang 7.970
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.970
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.553

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- NEAR-EUR — BUILDING_ACCELERATION — score 5.545/10 — DETECTED_BUT_TOO_LATE
- ONDO-EUR — BUILDING_ACCELERATION — score 4.833/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.253/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 8.199/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.143/10 — sources V4 — DETECTED_BUT_TOO_LATE
- SOMI-EUR — ACTIVE_NOW — score mémoire 8.122/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.105/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.984/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.982/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.970/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +86.74% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LSK-EUR +44.31% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FOLD-EUR +20.85% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +17.21% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- HNT-EUR +16.87% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- DGB-EUR +15.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AGI-EUR +15.17% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NEAR-EUR +14.63% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- RAY-EUR +14.39% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CC-EUR +12.74% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
