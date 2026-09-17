# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-17T10:28:58.030434+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NEAR-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.740 | entrée 6.600 | trend 8.100 | rang 6.723
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : FET-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.457 | entrée 7.050 | trend 7.650 | rang 7.241
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.241
2. NEAR-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.723
3. USELESS-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 6.508

## Accélération indépendante

- AVA-EUR — CONFIRMED_ACCELERATION — score 9.789/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- AVA-EUR — ACTIVE_NOW — score mémoire 9.789/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ICP-EUR — ACTIVE_NOW — score mémoire 8.171/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.150/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 8.067/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.944/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.845/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.832/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — MEMORY_24H — score mémoire 7.750/10 — sources V4 — MEMORY_ONLY
- LTC-EUR — MEMORY_24H — score mémoire 7.691/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- AVA-EUR +66.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FOLD-EUR +38.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QUID-EUR +22.39% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- HNT-EUR +19.05% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PEAQ-EUR +18.06% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- USELESS-EUR +17.38% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NEAR-EUR +16.53% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SYN-EUR +15.65% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- EDEN-EUR +14.74% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- VVV-EUR +14.29% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
