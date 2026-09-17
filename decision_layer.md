# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T03:57:34.501525+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.928 | entrée 4.800 | trend 8.400 | rang 7.232
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.232
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.964
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.206

## Accélération indépendante

- SYN-EUR — BUILDING_ACCELERATION — score 4.880/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.190/10 — sources V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 8.183/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.127/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.017/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.989/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.765/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KMNO-EUR — ACTIVE_NOW — score mémoire 7.764/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.746/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.675/10 — sources V4 — WATCH_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.664/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- SYN-EUR +86.85% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +25.33% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +23.92% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HNT-EUR +21.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +20.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IOST-EUR +18.75% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +16.34% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +15.67% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- VVV-EUR +15.19% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AVA-EUR +14.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
