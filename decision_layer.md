# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T19:41:12.862906+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : WLD-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.370 | entrée 7.350 | trend 8.150 | rang 7.352
  - Trend remains strong; candidate retained for re-entry instead of discarded.

## Top cross-sectionnel

1. WLD-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.352
2. LSK-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.348
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.875

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- CAKE-EUR — ACTIVE_NOW — score mémoire 8.315/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.300/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 8.124/10 — sources V4 — WATCH_ONLY
- PHA-EUR — MEMORY_24H — score mémoire 8.050/10 — sources V4 — MEMORY_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.891/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.879/10 — sources V4 — WATCH_ONLY
- FORM-EUR — ACTIVE_NOW — score mémoire 7.763/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.677/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.665/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.652/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +37.31% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +36.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +21.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +16.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SENT-EUR +15.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- MTL-EUR +15.66% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- PENDLE-EUR +10.08% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- ACX-EUR +9.11% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +8.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NEAR-EUR +8.58% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
