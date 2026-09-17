# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T15:58:17.207838+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : COTI-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.672 | entrée 6.050 | trend 8.300 | rang 6.721
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.788 | entrée 7.050 | trend 8.100 | rang 6.734
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.734
2. COTI-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.721

## Accélération indépendante

- SYN-EUR — CONFIRMED_ACCELERATION — score 6.912/10 — REQUIRES_V4_ENTRY_AND_EXECUTION_VALIDATION
- TREAD-EUR — BUILDING_ACCELERATION — score 5.635/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.549/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 8.330/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 8.285/10 — sources V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 8.251/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.184/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 8.083/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 8.046/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- FET-EUR — ACTIVE_NOW — score mémoire 8.023/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.966/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- PHA-EUR — ACTIVE_NOW — score mémoire 7.946/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- AVA-EUR +88.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- AGI-EUR +31.25% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- TREAD-EUR +27.70% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- PEAQ-EUR +22.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CROSS-EUR +21.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- KSM-EUR +19.56% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- DRIFT-EUR +18.95% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- NEAR-EUR +17.57% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- COTI-EUR +16.09% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PEOPLE-EUR +15.79% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
