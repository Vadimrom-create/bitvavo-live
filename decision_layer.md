# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T21:52:56.841821+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.598 | entrée 5.950 | trend 9.200 | rang 6.960
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.960

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.348/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 8.060/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.925/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.892/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.786/10 — sources V4 — WATCH_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.716/10 — sources V4 — WATCH_ONLY
- APT-EUR — MEMORY_24H — score mémoire 7.715/10 — sources V4 — MEMORY_ONLY
- CATI-EUR — ACTIVE_NOW — score mémoire 7.701/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.662/10 — sources V4 — WATCH_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.650/10 — sources V4 — WATCH_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 7.588/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +324.23% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- CVC-EUR +58.21% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +24.22% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +24.14% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- REZ-EUR +18.28% — NOT_DETECTED — couche SCANNER_SCORING — action NOT_APPLICABLE
- ZKJ-EUR +18.15% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- SOLV-EUR +14.84% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +12.86% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- POWR-EUR +11.31% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +11.00% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
