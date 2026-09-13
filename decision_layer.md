# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-13T15:48:21.254630+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : VTHO-EUR | action LATENT_ACCELERATOR | opportunité 7.683 | entrée 4.950 | trend 9.200 | rang 6.752
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : TAO-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.529 | entrée 7.000 | trend 7.650 | rang 7.297
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. TAO-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.297
2. INJ-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.193
3. VTHO-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.752

## Accélération indépendante

- REZ-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- REZ-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- WLD-EUR — ACTIVE_NOW — score mémoire 8.191/10 — sources V4 — WATCH_ONLY
- VET-EUR — ACTIVE_NOW — score mémoire 7.996/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.914/10 — sources V4 — WATCH_ONLY
- KAS-EUR — ACTIVE_NOW — score mémoire 7.830/10 — sources V4 — WATCH_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.783/10 — sources V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.775/10 — sources V4 — WATCH_ONLY
- AVAX-EUR — MEMORY_24H — score mémoire 7.656/10 — sources V4 — MEMORY_ONLY
- XVG-EUR — ACTIVE_NOW — score mémoire 7.602/10 — sources V4 — WATCH_ONLY
- QKC-EUR — MEMORY_24H — score mémoire 7.588/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- LSK-EUR +285.60% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- CVC-EUR +70.84% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- REZ-EUR +22.94% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ARK-EUR +19.18% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- VTHO-EUR +18.81% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- FIL-EUR +16.34% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- BAT-EUR +11.99% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- XTZ-EUR +10.07% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- PUNDIX-EUR +9.76% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- POWR-EUR +9.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
