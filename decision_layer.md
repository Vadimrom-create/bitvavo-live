# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T12:06:42.865257+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.002 | entrée 5.750 | trend 9.200 | rang 7.923
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.923
2. VET-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.649
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.451

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- INJ-EUR — ACTIVE_NOW — score mémoire 8.173/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.923/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.881/10 — sources V4 — WATCH_ONLY
- NPC-EUR — ACTIVE_NOW — score mémoire 7.807/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.699/10 — sources V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.668/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.656/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.649/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ZIL-EUR — ACTIVE_NOW — score mémoire 7.579/10 — sources DECISION_LAYER, V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CPOOL-EUR +52.75% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CAP-EUR +37.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +23.35% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +22.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +18.76% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +15.42% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MIOTA-EUR +12.51% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- NPC-EUR +11.40% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- IQ-EUR +10.90% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- CNPY-EUR +10.34% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
