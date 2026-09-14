# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T13:55:09.382301+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.084 | entrée 5.800 | trend 9.200 | rang 7.878
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.878
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.584

## Accélération indépendante

- CAP-EUR — CONFIRMED_ACCELERATION — score 7.344/10 — DETECTED_BUT_TOO_LATE
- NPC-EUR — BUILDING_ACCELERATION — score 5.086/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ZIL-EUR — ACTIVE_NOW — score mémoire 8.088/10 — sources DECISION_LAYER, V4 — WATCH_ONLY
- AERO-EUR — ACTIVE_NOW — score mémoire 7.896/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- INJ-EUR — ACTIVE_NOW — score mémoire 7.872/10 — sources DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- LDO-EUR — ACTIVE_NOW — score mémoire 7.856/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEO-EUR — MEMORY_24H — score mémoire 7.738/10 — sources V4 — MEMORY_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.716/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.712/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.646/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- CAP-EUR +48.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CPOOL-EUR +38.35% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- T-EUR +21.41% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FIL-EUR +18.23% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- REZ-EUR +16.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- QKC-EUR +16.08% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CNPY-EUR +15.65% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- NPC-EUR +12.36% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- RON-EUR +10.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- RED-EUR +9.61% — NO_CONFIRMED_SHORT_TERM_EVENT — couche NOT_APPLICABLE — action NOT_APPLICABLE

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
