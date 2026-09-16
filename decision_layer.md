# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T09:35:20.619124+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : USELESS-EUR | action LATENT_ACCELERATOR | opportunité 7.421 | entrée 5.750 | trend 8.100 | rang 6.071
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : NEAR-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 9.201 | entrée 7.600 | trend 8.100 | rang 7.824
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.824
2. USELESS-EUR — MEILLEUR_LATENT_ACCELERATOR — LATENT_ACCELERATOR — rank 6.071

## Accélération indépendante

Aucune accélération indépendante confirmée ou en construction.

## Watchlist persistante 24–72 h

- AIOZ-EUR — ACTIVE_NOW — score mémoire 8.259/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 8.020/10 — sources V4 — WATCH_ONLY
- PUMP-EUR — ACTIVE_NOW — score mémoire 7.894/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- NEAR-EUR — ACTIVE_NOW — score mémoire 7.824/10 — sources ACCELERATION, DECISION_LAYER, V4 — DETECTED_BUT_TOO_LATE
- VTHO-EUR — ACTIVE_NOW — score mémoire 7.811/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- S-EUR — ACTIVE_NOW — score mémoire 7.753/10 — sources V4 — WATCH_ONLY
- COTI-EUR — ACTIVE_NOW — score mémoire 7.736/10 — sources V4 — DETECTED_BUT_TOO_LATE
- CVC-EUR — MEMORY_24H — score mémoire 7.734/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- XPL-EUR — ACTIVE_NOW — score mémoire 7.734/10 — sources V4 — WATCH_ONLY
- YGG-EUR — ACTIVE_NOW — score mémoire 7.714/10 — sources V4 — WATCH_ONLY

## Audit des plus fortes hausses

- SYN-EUR +120.44% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +30.22% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- USELESS-EUR +22.97% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +16.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +14.64% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ALIGN-EUR +10.90% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LMWR-EUR +10.90% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- FOLD-EUR +7.55% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- CROSS-EUR +7.28% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- ZIL-EUR +7.17% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
