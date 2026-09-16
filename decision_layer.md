# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-16T14:39:44.333969+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : aucun candidat matériel
- **MEILLEURE_LIMITE_PASSIVE** : aucun candidat matériel
- **MEILLEUR_LATENT_ACCELERATOR** : aucun candidat matériel
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 7.696 | entrée 6.050 | trend 8.550 | rang 7.584
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.584
2. NEAR-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.515
3. USELESS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 6.390

## Accélération indépendante

- LSK-EUR — CONFIRMED_ACCELERATION — score 7.475/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VTHO-EUR — ACTIVE_NOW — score mémoire 7.926/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ETHFI-EUR — ACTIVE_NOW — score mémoire 7.843/10 — sources V4 — WATCH_ONLY
- ZORA-EUR — MEMORY_24H — score mémoire 7.801/10 — sources V4 — MEMORY_ONLY
- LDO-EUR — ACTIVE_NOW — score mémoire 7.777/10 — sources V4 — WATCH_ONLY
- ICP-EUR — ACTIVE_NOW — score mémoire 7.658/10 — sources V4 — WATCH_ONLY
- SOMI-EUR — ACTIVE_NOW — score mémoire 7.630/10 — sources V4 — WATCH_ONLY
- UNI-EUR — MEMORY_24H — score mémoire 7.629/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- ALGO-EUR — MEMORY_24H — score mémoire 7.613/10 — sources V4 — MEMORY_ONLY
- AVAX-EUR — MEMORY_24H — score mémoire 7.587/10 — sources V4 — MEMORY_ONLY
- ZEN-EUR — MEMORY_24H — score mémoire 7.586/10 — sources V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- SYN-EUR +118.95% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- LSK-EUR +55.10% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- HEI-EUR +19.04% — INSUFFICIENT_HISTORY — couche HISTORY — action NOT_APPLICABLE
- FOLD-EUR +18.19% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- USELESS-EUR +17.76% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- ARB-EUR +15.27% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- TAI-EUR +14.43% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- IOST-EUR +10.49% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- CNPY-EUR +9.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZKJ-EUR +8.55% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
