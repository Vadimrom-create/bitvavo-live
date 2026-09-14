# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-14T05:37:55.199382+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : VTHO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.436 | entrée 6.800 | trend 9.200 | rang 8.097
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. VTHO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.097

## Accélération indépendante

- CVC-EUR — CONFIRMED_ACCELERATION — score 7.973/10 — DETECTED_BUT_TOO_LATE
- LSK-EUR — CONFIRMED_ACCELERATION — score 7.041/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- ICP-EUR — ACTIVE_NOW — score mémoire 8.379/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.125/10 — sources V4 — WATCH_ONLY
- VTHO-EUR — ACTIVE_NOW — score mémoire 8.097/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 8.046/10 — sources V4 — WATCH_ONLY
- LAPTOP-EUR — MEMORY_24H — score mémoire 8.013/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- ATOM-EUR — ACTIVE_NOW — score mémoire 7.979/10 — sources V4 — DETECTED_BUT_TOO_LATE
- CVC-EUR — ACTIVE_NOW — score mémoire 7.973/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- SYRUP-EUR — ACTIVE_NOW — score mémoire 7.941/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources V4 — WATCH_ONLY
- KAVA-EUR — ACTIVE_NOW — score mémoire 7.759/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- REZ-EUR +31.28% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CVC-EUR +26.18% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- CPOOL-EUR +23.68% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- MTL-EUR +22.58% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FIL-EUR +19.08% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +18.26% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +17.80% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +15.38% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- IQ-EUR +12.72% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- BABY-EUR +8.92% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
