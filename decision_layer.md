# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-15T07:46:27.243842+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : NPC-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.512 | entrée 6.550 | trend 7.750 | rang 7.124
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.870 | entrée 6.100 | trend 9.200 | rang 7.546
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.546
2. NPC-EUR — MEILLEURE_LIMITE_PASSIVE — PLACE_LIMITE_PASSIVE — rank 7.124
3. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.115

## Accélération indépendante

- LAPTOP-EUR — CONFIRMED_ACCELERATION — score 6.500/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — BUILDING_ACCELERATION — score 5.932/10 — DETECTED_BUT_TOO_LATE
- CNPY-EUR — BUILDING_ACCELERATION — score 5.161/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- CAP-EUR — MEMORY_24H — score mémoire 9.037/10 — sources ACCELERATION — MEMORY_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.021/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.969/10 — sources V4 — WATCH_ONLY
- BNB-EUR — ACTIVE_NOW — score mémoire 7.888/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.846/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YB-EUR — ACTIVE_NOW — score mémoire 7.755/10 — sources V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.745/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VET-EUR — MEMORY_24H — score mémoire 7.651/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- PEAQ-EUR — ACTIVE_NOW — score mémoire 7.633/10 — sources V4 — DETECTED_BUT_TOO_LATE
- CHIP-EUR — ACTIVE_NOW — score mémoire 7.626/10 — sources V4 — DETECTED_BUT_TOO_LATE

## Audit des plus fortes hausses

- CAP-EUR +28.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +25.03% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PUFFER-EUR +24.24% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ASTR-EUR +18.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LAPTOP-EUR +13.22% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ACX-EUR +11.82% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SAGA-EUR +10.89% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE
- CROSS-EUR +8.47% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- AXL-EUR +7.59% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZRC-EUR +6.88% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
