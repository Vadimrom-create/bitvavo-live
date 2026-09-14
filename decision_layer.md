# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T12:55:44.815826+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : VET-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.498 | entrée 6.050 | trend 8.650 | rang 7.529
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.087 | entrée 5.750 | trend 9.200 | rang 7.962
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.962
2. VET-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.529
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.399

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 7.962/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- RED-EUR — ACTIVE_NOW — score mémoire 7.932/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.924/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.725/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.692/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.674/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources V4 — WATCH_ONLY
- WLD-EUR — ACTIVE_NOW — score mémoire 7.624/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- PENDLE-EUR — ACTIVE_NOW — score mémoire 7.617/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +43.66% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +41.07% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +30.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZRC-EUR +19.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +19.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +18.93% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +17.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- T-EUR +14.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MIOTA-EUR +14.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LIGHTER-EUR +10.71% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
