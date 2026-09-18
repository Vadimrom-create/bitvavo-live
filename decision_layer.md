# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-18T21:03:54.404386+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : USELESS-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.662 | entrée 6.700 | trend 8.100 | rang 6.741
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : LSK-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.772 | entrée 6.050 | trend 8.400 | rang 7.548
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.548
2. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.433
3. USELESS-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.741

## Accélération indépendante

- G-EUR — BUILDING_ACCELERATION — score 5.019/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- LDO-EUR — ACTIVE_NOW — score mémoire 8.115/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.998/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- METIS-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.946/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.930/10 — sources V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 7.929/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- ORCA-EUR — MEMORY_24H — score mémoire 7.810/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.772/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.765/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- TRB-EUR — ACTIVE_NOW — score mémoire 7.719/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- G-EUR +53.93% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- STRK-EUR +51.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- F-EUR +40.50% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARB-EUR +25.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- APT-EUR +24.78% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZAMA-EUR +24.70% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- S-EUR +21.10% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +20.92% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CHIP-EUR +20.42% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZK-EUR +20.37% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
