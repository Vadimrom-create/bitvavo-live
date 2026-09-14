# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T14:16:35.260618+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.734 | entrée 5.600 | trend 9.200 | rang 7.782
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.782
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.550
3. FET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.164

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.158/10 — sources V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- GRT-EUR — ACTIVE_NOW — score mémoire 7.908/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.801/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.782/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.762/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.751/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.677/10 — sources V4 — WATCH_ONLY
- ALGO-EUR — ACTIVE_NOW — score mémoire 7.654/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +56.32% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +34.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +25.53% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +17.12% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +16.52% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +14.69% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +13.26% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZRC-EUR +12.79% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- QKC-EUR +9.99% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- LIGHTER-EUR +9.79% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
