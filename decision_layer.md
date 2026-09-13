# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T14:17:51.159337+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.831 | entrée 5.400 | trend 9.200 | rang 6.993
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.415 | entrée 7.200 | trend 7.650 | rang 7.616
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.616
2. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.993

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- WLD-EUR — ACTIVE_NOW — score mémoire 8.332/10 — sources V4 — WATCH_ONLY
- MEGA-EUR — ACTIVE_NOW — score mémoire 8.021/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 8.012/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.956/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- AIOZ-EUR — ACTIVE_NOW — score mémoire 7.878/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.812/10 — sources V4 — WATCH_ONLY
- YB-EUR — ACTIVE_NOW — score mémoire 7.705/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.684/10 — sources V4 — WATCH_ONLY
- DOT-EUR — ACTIVE_NOW — score mémoire 7.665/10 — sources V4 — DETECTED_BUT_TOO_LATE
- YGG-EUR — ACTIVE_NOW — score mémoire 7.654/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- LSK-EUR +278.41% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +92.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ARK-EUR +36.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUNDIX-EUR +29.69% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- POWR-EUR +22.30% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +16.91% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- GLM-EUR +16.01% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZETA-EUR +14.94% — DETECTED_TOO_LATE — couche NONE — action INTERPRETATION
- STRAX-EUR +14.86% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +12.32% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
