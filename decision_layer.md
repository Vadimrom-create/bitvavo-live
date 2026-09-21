# Decision Layer V1 + boucle de contrôle — shadow

Scan : 2026-09-21T15:15:05.209507+00:00
Policy : DECISION_LAYER_V1_SHADOW au-dessus de V4_FROZEN_20260908

Cette couche ne modifie aucun score V4 et ne peut envoyer aucun ordre.
Entry est un indicateur de timing, pas un veto structurel.

## Quatre lectures obligatoires

- **MEILLEUR_ACHAT_IMMEDIAT** : STX-EUR | action ACHETE_MAINTENANT | opportunité 8.262 | entrée 7.200 | trend 8.600 | rang 7.916
  - V4 buy-ready with acceptable current entry; no structural veto.
- **MEILLEURE_LIMITE_PASSIVE** : COW-EUR | action PLACE_LIMITE_PASSIVE | opportunité 7.815 | entrée 5.850 | trend 8.900 | rang 7.691
  - Strong structure but imperfect current entry; prefer passive execution.
- **MEILLEUR_LATENT_ACCELERATOR** : CELO-EUR | action LATENT_ACCELERATOR | opportunité 7.887 | entrée 5.250 | trend 8.700 | rang 7.556
  - Strong structural opportunity retained despite weak instantaneous entry.
- **MEILLEUR_PULLBACK_REENTRY** : KAS-EUR | action ATTENDS_REPRISE_OU_REENTREE | opportunité 8.337 | entrée 7.300 | trend 8.700 | rang 8.027
  - Strong trend/opportunity retained through pullback; timing does not erase setup.

## Top cross-sectionnel

1. KAS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.027
2. GRASS-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 8.000
3. MERL-EUR — MEILLEUR_PULLBACK_REENTRY — ATTENDS_REPRISE_OU_REENTREE — rank 7.940

## Accélération indépendante

- ZRC-EUR — CONFIRMED_ACCELERATION — score 10.000/10 — DETECTED_BUT_TOO_LATE
- RON-EUR — CONFIRMED_ACCELERATION — score 9.938/10 — DETECTED_BUT_TOO_LATE
- ACE-EUR — CONFIRMED_ACCELERATION — score 9.570/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- THQ-EUR — CONFIRMED_ACCELERATION — score 9.062/10 — DETECTED_BUT_TOO_LATE
- CHILLGUY-EUR — CONFIRMED_ACCELERATION — score 8.954/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- MEW-EUR — CONFIRMED_ACCELERATION — score 8.311/10 — DETECTED_BUT_TOO_LATE
- BAND-EUR — CONFIRMED_ACCELERATION — score 8.250/10 — DETECTED_BUT_TOO_LATE
- MOG-EUR — CONFIRMED_ACCELERATION — score 8.008/10 — DETECTED_BUT_TOO_LATE
- ARX-EUR — CONFIRMED_ACCELERATION — score 7.615/10 — REQUIRES_FINAL_EXECUTION_VALIDATION
- PUFFER-EUR — CONFIRMED_ACCELERATION — score 7.462/10 — DETECTED_BUT_TOO_LATE

## Watchlist persistante 24–72 h

- VET-EUR — ACTIVE_NOW — score mémoire 7.768/10 — sources ACCELERATION, DECISION_LAYER, V4 — BUYABLE_NOW
- ZRC-EUR — ACTIVE_NOW — score mémoire 10.000/10 — sources ACCELERATION — DETECTED_BUT_TOO_LATE
- RON-EUR — ACTIVE_NOW — score mémoire 9.938/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ACE-EUR — ACTIVE_NOW — score mémoire 9.570/10 — sources ACCELERATION, V4 — WATCH_ONLY
- TAI-EUR — MEMORY_24H — score mémoire 9.488/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- THQ-EUR — ACTIVE_NOW — score mémoire 9.062/10 — sources ACCELERATION, V4 — DETECTED_BUT_TOO_LATE
- ACU-EUR — MEMORY_24H — score mémoire 9.053/10 — sources ACCELERATION, V4 — MEMORY_ONLY
- CHILLGUY-EUR — ACTIVE_NOW — score mémoire 8.954/10 — sources ACCELERATION, DECISION_LAYER, V4 — WATCH_ONLY
- ARB-EUR — MEMORY_24H — score mémoire 8.746/10 — sources ACCELERATION, DECISION_LAYER, V4 — MEMORY_ONLY
- FTT-EUR — MEMORY_24H — score mémoire 8.500/10 — sources ACCELERATION, V4 — MEMORY_ONLY

## Audit des plus fortes hausses

- ZETA-EUR +63.93% — NOT_DETECTED — couche SCANNER_COVERAGE — action NOT_APPLICABLE
- PHA-EUR +41.88% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- AIOZ-EUR +34.28% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- NIL-EUR +32.96% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- FTT-EUR +29.73% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- PTB-EUR +28.91% — NOT_DETECTED — couche DATA — action NOT_APPLICABLE
- ZRC-EUR +26.50% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- KMNO-EUR +26.38% — DETECTED_EARLY — couche NONE — action INTERPRETATION
- WIF-EUR +26.35% — DETECTED_EARLY — couche NONE — action ENTRY_TIMING_OR_EXECUTION
- SEI-EUR +24.80% — DETECTED_EARLY — couche NONE — action INTERPRETATION

## Garde-fous

- Veto uniquement pour défauts structurels de données/exécution.
- Les diagnostics de chase/mèche réduisent le rang mais n'effacent pas seuls une opportunité forte.
- Les décisions sont archivées par scan pour mesurer a posteriori chaque rejet et chaque promotion.
- La mémoire et l'accélération restent en shadow : elles ne peuvent pas déclencher un email d'achat.
- Aucune probabilité +10/+20/+30/+40 % n'est produite tant qu'elle n'est pas calibrée.
